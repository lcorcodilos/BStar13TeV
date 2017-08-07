#! /usr/bin/env python

###################################################################
##								 ##
## Name: TWkinematics.py	   			         ##
## Author: Kevin Nash and Lucas Corcodilos			 ##
## Date: 1/13/2016						 ##
## Purpose: This program produces graphs of each variable	 ##
##	    before any cuts are made				 ##
##								 ##
###################################################################

import os
import glob
import math
from math import sqrt
#import quickroot
#from quickroot import *
import ROOT 
from ROOT import *
import sys
from DataFormats.FWLite import Events, Handle
from optparse import OptionParser

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
				  default	=	'data',
				  dest		=	'set',
				  help		=	'data or ttbar')
parser.add_option('-x', '--pileup', metavar='F', type='string', action='store',
				  default	=	'on',
				  dest		=	'pileup',
				  help		=	'If not data do pileup reweighting?')
parser.add_option('-n', '--num', metavar='F', type='string', action='store',
				  default	=	'all',
				  dest		=	'num',
				  help		=	'job number')
parser.add_option('-j', '--jobs', metavar='F', type='string', action='store',
				  default	=	'1',
				  dest		=	'jobs',
				  help		=	'number of jobs')
parser.add_option('-t', '--tname', metavar='F', type='string', action='store',
				   default	=	'HLT_PFHT900,HLT_PFHT800,HLT_JET450',
				   dest		=	'tname',
				   help		=	'trigger name')

parser.add_option('-m', '--modulesuffix', metavar='F', type='string', action='store',
				  default	=	'none',
				  dest		=	'modulesuffix',
				  help		=	'ex. PtSmearUp')

parser.add_option('-g', '--grid', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'grid',
				  help		=	'running on grid off or on')
parser.add_option('-u', '--ptreweight', metavar='F', type='string', action='store',
				  default	=	'none',
				  dest		=	'ptreweight',
				  help		=	'on or off')

parser.add_option('-p', '--pdfweights', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'pdfweights',
				  help		=	'nominal, up, or down')
parser.add_option('-z', '--pdfset', metavar='F', type='string', action='store',
				  default	=	'cteq66',
				  dest		=	'pdfset',
				  help		=	'pdf set')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
				  default	=	'default',
				  dest		=	'cuts',
				  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-b', '--bx', metavar='F', type='string', action='store',
				   default	=	'25ns',
				   dest		=	'bx',
				   help		=	'bunch crossing 50ns or 25ns')            
parser.add_option('-y', '--modmass', metavar='F', type='string', action='store',
				   default	=	'nominal',
				   dest		=	'modmass',
				   help		=	'nominal, up, down')
parser.add_option('-S', '--split', metavar='F', type='string', action='store',
				  default	=	'file',
				  dest		=	'split',
				  help		=	'split by event of file')
parser.add_option('-r', '--rate', metavar='F', type='string', action='store',
				  default	=	'tpt',
				  dest		=	'rate',
				  help		=	'tpt, Mt, Mtw')

(options, args) = parser.parse_args()
if options.set == 'QCD':
	setstr = 'QCD'
else:
	setstr = 'data'

print "Options summary"
print "=================="
for  opt,value in options.__dict__.items():
	#print str(option)+ ": " + str(options[option]) 
	print str(opt) +': '+ str(value)
print "=================="
print ""
di = ""
if options.grid == 'on':
	di = "tardir/"
	sys.path.insert(0, 'tardir/')

gROOT.Macro(di+"rootlogon.C")

import Bstar_Functions	
from Bstar_Functions import *


#----Trigger Naming------
tname = options.tname.split(',')
tnamestr = ''
for iname in range(0,len(tname)):
	tnamestr+=tname[iname]
	if iname!=len(tname)-1:
		tnamestr+='OR'
		
if tnamestr=='HLT_PFHT900ORHLT_PFHT800ORHLT_JET450':
	tnameformat='nominal'
elif tnamestr=='':
	tnameformat='none'
else:
	tnameformat=tnamestr
		

#------Basics-----------
pie = math.pi 

#Load up cut values based on what selection we want to run 
Cuts = LoadCuts(options.cuts)
wpt = Cuts['wpt']
tpt = Cuts['tpt']
dy = Cuts['dy']
tmass = Cuts['tmass']
tau32 = Cuts['tau32']
tau21 = Cuts['tau21']
sjbtag = Cuts['sjbtag']
wmass = Cuts['wmass']
eta1 = Cuts['eta1']
eta2 = Cuts['eta2']

Cons = LoadConstants()
lumi = Cons['lumi']
Lumi = str(lumi/1000)+'fb'
ttagsf = Cons['ttagsf']
ttagsf_errUp = Cons['ttagsf_errUp']
ttagsf_errDown = Cons['ttagsf_errDown']


#------For large datasets we need to parallelize the processing
jobs=int(options.jobs)
if jobs != 1:
	num=int(options.num)
	jobs=int(options.jobs)
	print "Running over " +str(jobs)+ " jobs"
	print "This will process job " +str(num)
else:
	print "Running over all events"

#This section defines some strings that are used in naming the optput files
mod = ""
if options.modulesuffix != "none" :
	mod = mod + options.modulesuffix


pstr = ""
if options.pdfweights!="nominal":
	print "using pdf uncertainty"
	pstr = "_pdf_"+options.pdfset+"_"+options.pdfweights

pustr = ""
if options.pileup=='off':
	pustr = "_pileup_unweighted"
if mod == '':
	mod = options.modulesuffix

mmstr = ""
if options.modmass!="nominal":
	print "using modm uncertainty"
	mmstr = "_modm_"+options.modmass

#Based on what set we want to analyze, we find all Ntuple root files 
if options.grid == "on":
	mainDir = "/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/BStar13TeV/TTrees/"
else:
	mainDir='TTrees/'

file = TFile(mainDir + "TWtreefile_"+options.set+"_Trigger_"+tnameformat+"_"+mod+pstr+".root")

print "opened file: " + mainDir + "TWtreefile_"+options.set+"_Trigger_"+tnameformat+"_"+mod+pstr+".root"

tree = file.Get("Tree")

if (options.set.find('ttbar') != -1) or (options.set.find('singletop') != -1):
	settype = 'ttbar'
elif (options.set.find('QCD') != -1):
	settype ='ttbar'
	run_b_SF = False
else :
	settype = options.set

print 'The type of set is ' + settype


# Load Up the trigger
if options.set != 'data':
	#Load up scale factors (to be used for MC only)

	TrigFile = TFile(di+"Triggerweight_2jethack_data.root")
	TrigPlot = TrigFile.Get("TriggerWeight_"+tnamestr+"_pre_HLT_PFHT475")

	PileFile = TFile(di+"PileUp_Ratio_"+settype+".root")
	if options.pileup=='up':
		PilePlot = PileFile.Get("Pileup_Ratio_up")
	elif options.pileup=='down':
		PilePlot = PileFile.Get("Pileup_Ratio_down")
	else:	
		PilePlot = PileFile.Get("Pileup_Ratio")

nevHisto = file.Get("nev")
B2Gnev = nevHisto.Integral()/jobs

rateCuts = 'rate_'+options.cuts
if options.cuts == 'sideband1':
	rateCuts = 'rate_default'

# #For event counting
# jobiter = 0
# splitfiles = []

# if jobs != 1 and options.split=="file":
#     for ifile in range(1,len(files)+1):
#     	if (ifile-1) % jobs == 0:
# 		jobiter+=1
# 	count_index = ifile  - (jobiter-1)*jobs
# 	if count_index==num:
# 		splitfiles.append(files[ifile-1])

#     events = Events(splitfiles)
#     runs = Runs(splitfiles)

# if options.split=="event" or jobs == 1:	  
# 	events = Events(files)
#     	runs = Runs(files)

# totnev = 0

# nevHandle 	= 	Handle (  "vector<int> "  )
# nevLabel  	= 	( "counter" , "nevr")

# for run in runs:

# 		run.getByLabel (nevLabel,nevHandle )
#     		nev 		= 	nevHandle.product() 
		
# 		totnev+=nev[0]
# print "Total unfiltered events in selection: ",totnev


#---------------------------------------------------------------------------------------------------------------------#
var = ""

if jobs != 1:
	f = TFile( "TWvariables"+options.set+"_Trigger_"+tnameformat+"_"+options.modulesuffix +pustr+pstr+"_job"+options.num+"of"+options.jobs+"_PSET_"+options.cuts+var+".root", "recreate" )
else:
	f = TFile( "TWvariables"+options.set+"_Trigger_"+tnameformat+"_"+options.modulesuffix +pustr+pstr+"_PSET_"+options.cuts+var+".root", "recreate" )


print "Creating histograms"

TTR = TTR_Init('Bifpoly',rateCuts,setstr,options.rate,di)

#Define Histograms


f.cd()
#---------------------------------------------------------------------------------------------------------------------#
Tau_21		= TH1F("Tau_21",	"tau_21",				15,   0, 1.5 )
Mt		= TH1F("Mt",		"top candidate mass",			20,   0, 500 )
Tau_32		= TH1F("Tau_32",  	"Tau_32",     	  	      		15,   0, 1 )
MaxSJCSV	= TH1F("MaxSJCSV",	"Maximum subjet CSV",			20,   0, 1   )
dyfull		= TH1F("dyfull",     	"delta y between top and b candidates", 12,   0, 5   )
dysemi		= TH1F("dysemi",     	"delta y between top and b candidates", 12,   0, 5   )
Mw		= TH1F("Mw",		"W candidate mass",     	  	30,   0, 500 )

MwStack		= TH1F("MwStack",	"W candidate mass for stack",		100,   0, 500 )
QCDbkgMwStack	= TH1F("QCDbkgMwStack", "QCD background for W mass",		100, 0, 500 )

nev = TH1F("nev",	"nev",		1, 0, 1 )

Tau21vsWmass = TH2F('Tau21vWmass', 'Tau21 vs Wmass', 20, 0, 300, 10, 0, 1)
Tau32vsTau21 = TH2F("Tau32vsTau21", "Tau32 vs Tau21", 
					20, 0.0, 1.0,
					20, 0.0, 1.0)

MtvPtvTau32 = TH3F('MtvPtvTau32', 'Event distribution for top variables', 
					20, 0, 500,
					50, 450, 1500,
					15, 0, 1)

Mt.Sumw2()
Mw.Sumw2()
Tau_21.Sumw2()
Tau_32.Sumw2()
MaxSJCSV.Sumw2()
dyfull.Sumw2()
dysemi.Sumw2()	

MwStack.Sumw2()
QCDbkgMwStack.Sumw2()
Tau21vWmass.Sumw2()
Tau32vsTau21.Sumw2()
	
#---------------------------------------------------------------------------------------------------------------------#

# loop over events
#---------------------------------------------------------------------------------------------------------------------#

count = 0
jobiter = 0
print "Start looping"
treeEntries = tree.GetEntries()

# Design the splitting if necessary
if jobs != 1:
	evInJob = int(treeEntries/jobs)
	
	lowBinEdge = evInJob*(num-1)
	highBinEdge = evInJob*num

	if num == jobs:
		highBinEdge = treeEntries

else:
	lowBinEdge = 0
	highBinEdge = treeEntries

nev.SetBinContent(1,B2Gnev)
print "Range of events: (" + str(lowBinEdge) + ", " + str(highBinEdge) + ")"

infoArray=[]

for entry in range(lowBinEdge,highBinEdge):
	tree.GetEntry(entry)
	count	= 	count + 1
	m = 0
	t = 0
	if count % 100000 == 0 :
	  print  '--------- Processing Event ' + str(count) +'   -- percent complete ' + str(100*count/(highBinEdge-lowBinEdge)) + '% -- '

	doneAlready = False

	for hemis in ['hemis0','hemis1']:
		if hemis == 'hemis0':
			# Load up the ttree values
			tVals = {
				"tau1":tree.tau1_leading,
				"tau2":tree.tau2_leading,
				"tau3":tree.tau3_leading,
				"phi":tree.phi_leading,
				"mass":tree.mass_leading,
				"pt":tree.pt_leading,
				"eta":tree.eta_leading,
				"sjbtag":tree.sjbtag_leading,
				"SDmass":tree.topSDmass_leading
			}

			wVals = {
				"tau1":tree.tau1_subleading,
				"tau2":tree.tau2_subleading,
				"tau3":tree.tau3_subleading,
				"phi":tree.phi_subleading,
				"mass":tree.mass_subleading,
				"pt":tree.pt_subleading,
				"eta":tree.eta_subleading,
				"sjbtag":tree.sjbtag_subleading,
				"SDmass":tree.wSDmass_subleading
			}

		if hemis == 'hemis1' and doneAlready == False  :
			wVals = {
				"tau1":tree.tau1_leading,
				"tau2":tree.tau2_leading,
				"tau3":tree.tau3_leading,
				"phi":tree.phi_leading,
				"mass":tree.mass_leading,
				"pt":tree.pt_leading,
				"eta":tree.eta_leading,
				"sjbtag":tree.sjbtag_leading,
				"SDmass":tree.wSDmass_leading
			}

			tVals = {
				"tau1":tree.tau1_subleading,
				"tau2":tree.tau2_subleading,
				"tau3":tree.tau3_subleading,
				"phi":tree.phi_subleading,
				"mass":tree.mass_subleading,
				"pt":tree.pt_subleading,
				"eta":tree.eta_subleading,
				"sjbtag":tree.sjbtag_subleading,
				"SDmass":tree.topSDmass_subleading
			}

		elif hemis == 'hemis1' and doneAlready == True:
			continue

		# Remake the lorentz vectors
		tjet = TLorentzVector()
		tjet.SetPtEtaPhiM(tVals["pt"],tVals["eta"],tVals["phi"],tVals["mass"])

		wjet = TLorentzVector()
		wjet.SetPtEtaPhiM(wVals["pt"],wVals["eta"],wVals["phi"],wVals["mass"])

		ht = tjet.Perp() + wjet.Perp()

		if ht < 1100.0:
			continue

		weight = 1.0

		#Finally look at cuts
		wpt_cut = wpt[0]<wjet.Perp()<wpt[1]
		tpt_cut = tpt[0]<tjet.Perp()<tpt[1]
		dy_cut = dy[0]<=abs(tjet.Rapidity()-wjet.Rapidity())<dy[1]

		tmass_cut = tmass[0]<tVals["SDmass"]<tmass[1]
		if type(wmass[0]) is float:
			wmass_cut = wmass[0]<=wVals["SDmass"]<wmass[1]
		elif type(wmass[0]) is list:
			wmass_cut = wmass[0][0]<=wVals["SDmass"]<wmass[0][1] or wmass[1][0]<=wVals["SDmass"]<wmass[1][1] 
		else:
			print "wmass type error" 
			continue

		sjbtag_cut = sjbtag[0]<tVals["sjbtag"]<=sjbtag[1]
		
		try:
			tau32val		= 	tVals["tau3"]/tVals["tau2"] 
			tau21val		= 	wVals["tau2"]/wVals["tau1"]
		except:
			continue

		tau21_cut =  tau21[0]<=tau21val<tau21[1]
		tau32_cut =  tau32[0]<=tau32val<tau32[1]
		
		mtw_cut = 1800<((tjet+wjet).M())

		eta_regions = [eta1,eta2]
		TTRweight = bkg_weight_pt(tjet,TTR,eta_regions)

		# Load Up Mod Mass
		ModFile = TFile(di+"ModMassFile_"+rateCuts+".root")
		ModPlot = ModFile.Get("rtmass")

		ModFitParams = open(di+'fitdata/ModMass_pol3_PSET_'+rateCuts+'.txt')
		ModFitParams.seek(0)
		ModFit = TF1("ModFit",'pol3',tmass[0],tmass[1])

		ModFitParams2 = ModFitParams.read()

		for i in range(0,4):
			ModFit.SetParameter(i,float(ModFitParams2.split('\n')[i]) )

		# Apply Mod Mass
		massw = 1
		modm = tVals["SDmass"]
		if options.modmass=='nominal':
			massw = ModPlot.Interpolate(modm)
		if options.modmass=='up':
			massw = 1 + 0.5*(ModFit.Eval(modm) -1)
		if options.modmass=='down':
			massw = max(0.0,1 + 1.5*(ModFit.Eval(modm) -1))
		if options.modmass=='none':
			massw = 1

		#print massw
		# weightSFt = 1.0	
		if tmass_cut and tau32_cut and sjbtag_cut: 
			if options.set!="data":
				bin1 = tree.pileBin

				if options.pileup != 'off':
					weight *= PilePlot.GetBinContent(bin1)
			 	if options.cuts=="default" and options.set.find("QCD") == -1:
					weight *= ttagsf
					

		if options.ptreweight == "on" and options.set.find('ttbar') != -1:
			#ttbar pt reweighting done here
			PTW = tree.pt_reweight
			weight*=PTW
			

		# if options.pdfweights != "nominal" :
		# 	if options.pdfweights == 'up':
		# 		iweight = tree.pdf_weightUp
		# 	elif options.pdfweights == 'down':
		# 		iweight = tree.pdf_weightDown
		# 	weight *= iweight

		if wpt_cut and tpt_cut and dy_cut and tmass_cut:
			if tname != 'none' and options.set!='data' :
				#Trigger reweighting done here
				TRW = Trigger_Lookup( ht , TrigPlot )[0]
				weight*=TRW

	#Define selections
		fullsel =  wpt_cut and tpt_cut and dy_cut and tmass_cut and tau21_cut and  tau32_cut and sjbtag_cut and wmass_cut
		dyfullsel =  wpt_cut and tpt_cut  and tmass_cut and wmass_cut
		dysemisel = wpt_cut and tpt_cut  and tmass_cut and wmass_cut and mtw_cut
		tmasssel =  wpt_cut and tpt_cut and dy_cut  and  tau32_cut and sjbtag_cut and wmass_cut
		tmassStackSel = wpt_cut and tpt_cut and dy_cut  and tau21_cut and tau32_cut and sjbtag_cut and tmass_cut
		tmassBEStackSel = wpt_cut and tpt_cut and dy_cut and tau21_cut and tmass_cut and not (tau32_cut and sjbtag_cut)
		tau21sel =  wpt_cut and tpt_cut and dy_cut  and wmass_cut
		tau32sel =  wpt_cut and tpt_cut and dy_cut and tmass_cut  and sjbtag_cut and wmass_cut
		wmasssel =  wpt_cut and tpt_cut and dy_cut  and tau21_cut
		wmasssel2 =  wpt_cut and tpt_cut and dy_cut  and tau21_cut and tau32_cut and tmass_cut and sjbtag_cut
		sjbtagsel =  wpt_cut and tpt_cut and dy_cut and tmass_cut and tau32_cut and wmass_cut

	#Fill histograms-------
		# weight = weightSFt
		if fullsel:
			doneAlready = True
		if tau21sel:
			Tau_21.Fill(tau21val,weight)
		if tau32sel:
			Tau_32.Fill(tau32val,weight)
		if tmasssel:
			Mt.Fill(tjet.M(),weight)
		if wmasssel2:
			Mw.Fill(wjet.M(),weight)
		if sjbtagsel:
			MaxSJCSV.Fill(tVals["sjbtag"],weight)
		if dyfullsel:
			dyfull.Fill(abs(tjet.Rapidity()-wjet.Rapidity()),weight)
		if dysemisel:
			dysemi.Fill(abs(tjet.Rapidity()-wjet.Rapidity()),weight)
		if tmassBEStackSel:
			QCDbkgMwStack.Fill(wjet.M(),TTRweight*weight*massw)
		if tmassStackSel:
			MwStack.Fill(wjet.M(),weight)
		if tpt_cut and wpt_cut and dy_cut:
			Tau21vsWmass.Fill(wjet.M(),tau21val,weight)
			Tau32vsTau21.Fill(tau21val,tau32val,weight)
		if tpt_cut and wpt_cut and dy_cut and wmass_cut and tau21_cut:
			MtvPtvTau32.Fill(tjet.M(),tjet.Perp(),tau32val,weight)
	
#ONLY USED FOR DEBUGGING	
#for i in infoArray:
#	print i
f.cd()
f.Write()
f.Close()


