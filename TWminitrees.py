#! /usr/bin/env python



###################################################################
##								 								 ##
## Name: TWministrees.py						 						 ##
## Author: Lucas Corcodilos 						 			 ##
## Date: 10/10/17						 						 ##
## Purpose: This program analyzes a possible third jet in the b* ##
##          candidate event in QCD MC.						 	 ##
##          									 				 ##
###################################################################

import os
import glob
import math
from math import sqrt,exp
import ROOT
from ROOT import *

import sys
from optparse import OptionParser
from array import *

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
				  default	=	'data',
				  dest		=	'set',
				  help		=	'dataset (ie data,ttbar etc)')
parser.add_option('-g', '--grid', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'grid',
				  help		=	'running on grid off or on')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
				  default	=	'rate_default',
				  dest		=	'cuts',
				  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-t', '--tname', metavar='F', type='string', action='store',
				   default	=	'HLT_PFHT900,HLT_PFHT800,HLT_JET450',
				   dest		=	'tname',
				   help		=	'trigger name')
parser.add_option('-p', '--pdfweights', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'pdfweights',
				  help		=	'nominal, up, or down')
parser.add_option('-x', '--pileup', metavar='F', type='string', action='store',
				  default	=	'on',
				  dest		=	'pileup',
				  help		=	'If not data do pileup reweighting?')
parser.add_option('-S', '--split', metavar='F', type='string', action='store',
				  default   =   'event',
				  dest      =   'split',
				  help      =   'split by event of file') #File splitting not used with ttrees!
parser.add_option('-n', '--num', metavar='F', type='string', action='store',
				  default   =   'all',
				  dest      =   'num',
				  help      =   'job number')
parser.add_option('-j', '--jobs', metavar='F', type='string', action='store',
				  default   =   '1',
				  dest      =   'jobs',
				  help      =   'number of jobs')
parser.add_option('-u', '--ptreweight', metavar='F', type='string', action='store',
				  default	=	'on',
				  dest		=	'ptreweight',
				  help		=	'on or off')
parser.add_option('--noExtraPtCorrection', metavar='F', action='store_false',
				  default=True,
				  dest='extraPtCorrection',
				  help='Call to turn off extraPtCorrection')

(options, args) = parser.parse_args()


print "Options summary"
print "=================="
for  opt,value in options.__dict__.items():
	#print str(option)+ ": " + str(options[option]) 
	print str(opt) +': '+ str(value)
print "=================="
print ""

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

#If running on the grid we access the script within a tarred directory
di = ""
if options.grid == 'on':
	di = "tardir/"
	sys.path.insert(0, 'tardir/')

gROOT.Macro(di+"rootlogon.C")
import Bstar_Functions	
from Bstar_Functions import *

#For large datasets we need to parallelize the processing
jobs=int(options.jobs)
if jobs != 1:
	num=int(options.num)
	jobs=int(options.jobs)
	print "Running over " +str(jobs)+ " jobs"
	print "This will process job " +str(num)
else:
	print "Running over all events"


#Load up cut values based on what selection we want to run 
Cons = LoadConstants()
lumi = Cons['lumi']
Lumi = str(lumi/1000)+"fb"
ttagsf = Cons['ttagsf']

if options.cuts.find('rate') != -1:
	Wpurity = 'LP'
	wtagsf = Cons['wtagsf_LP']
	wtagsfsig = Cons['wtagsfsig_LP']
else:
	Wpurity = 'HP'
	wtagsf = Cons['wtagsf_HP']
	wtagsfsig = Cons['wtagsfsig_HP']

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

#Based on what set we want to analyze, we find all ttree root files -----------------
if options.grid=='on':
	mainDir = 'root://cmsxrootd.fnal.gov//store/user/lcorcodi/TTrees/'
else:
	mainDir = 'TTrees/'

file = TFile.Open(mainDir + "TWtreefile_"+options.set+"_Trigger_nominal_none.root")

tree = file.Get("Tree")

settype = 'ttbar'

print 'The type of set is ' + settype

#--------------------------------------Trigger reweight----------------------------------

if options.set != 'data':
	#Load up scale factors (to be used for MC only)
	TrigFile = TFile(di+"Triggerweight_2jethack_data.root")
	TrigPlot = TrigFile.Get("TriggerWeight_"+tnamestr+"_pre_HLT_PFHT475")

	print "TriggerWeight_"+tnamestr+"_pre_HLT_PFHT475"
	
	PileFile = TFile(di+"PileUp_Ratio_"+settype+".root")
	if options.pileup=='up':
		PilePlot = PileFile.Get("Pileup_Ratio_up")
	elif options.pileup=='down':
		PilePlot = PileFile.Get("Pileup_Ratio_down")
	else:   
		PilePlot = PileFile.Get("Pileup_Ratio")

#----------------------------------- Pt Reweight string -----------------------------
ptString = ''
if options.set == 'ttbar':
	if not options.extraPtCorrection:
		ptString = '_noExtraPtCorrection'
	if options.ptreweight == 'off':
		ptString = '_ptreweight_off'
		

#----------------------------------------------------------------------------

nevHisto = file.Get("nev")
B2Gnev = nevHisto.Integral()/jobs

if jobs!=1:
	f = TFile( "TWminitree_"+options.set+"_job"+options.num+"of"+options.jobs+"_PSET_"+options.cuts+ptString+".root", "recreate" )
else:
	f = TFile( "TWminitree_"+options.set+"_PSET_"+options.cuts+ptString+".root", "recreate" )

print "Creating histograms"

#Define new miniTree
f.cd()

# Get and store the number of B2Gevents for one job
nev = TH1F("nev",	"nev",		1, 0, 1 )
nevHisto = file.Get("nev")
B2Gnev = nevHisto.Integral()/jobs
nev.SetBinContent(1,B2Gnev)

# Define some extra counting histograms
candidateCount = TH1I("candidateCount", "candidateCount",1,0,1)
ThirdJetCount = TH1I("3rdJetCount","3rdJetCount",1,0,1)

miniTreeVars = {
	'pt_top':array('d',[0]),
	'mass_top':array('d',[0]),
	'SDmass_top':array('d',[0]),
	'eta_top':array('d',[0]),
	'phi_top':array('d',[0]),
	'flavor_top':array('d',[0]),
	'tau32':array('d',[0]),
	'sjbtag':array('d',[0]),
	
	'pt_w':array('d',[0]),
	'mass_w':array('d',[0]),
	'SDmass_w':array('d',[0]),
	'eta_w':array('d',[0]),
	'phi_w':array('d',[0]),
	'flavor_w':array('d',[0]),
	'tau21':array('d',[0]),

	'pt_3':array('d',[0]),
	'mass_3':array('d',[0]),
	'topSDmass_3':array('d',[0]),
	'wSDmass_3':array('d',[0]),
	'eta_3':array('d',[0]),
	'phi_3':array('d',[0]),
	'flavor_3':array('d',[0]),
	'tau21':array('d',[0]),
	'tau32':array('d',[0]),

	'weight':array('d',[0])}

miniTree = Make_Trees(miniTreeVars)
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

print "Range of events: (" + str(lowBinEdge) + ", " + str(highBinEdge) + ")"

preTopTagCount = 0
has3rdJetCount = 0
count = 0
# syntax to get a var(branch value) from the event is:tree.branchname
for entry in range(lowBinEdge,highBinEdge):
	# Have to grab tree entry first
	tree.GetEntry(entry)

	count	= 	count + 1

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
				"SDmass":tree.topSDmass_leading,
				"flavor":tree.flavor_leading
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
				"SDmass":tree.wSDmass_subleading,
				"flavor":tree.flavor_subleading
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
				"SDmass":tree.wSDmass_leading,
				"flavor":tree.flavor_leading
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
				"SDmass":tree.topSDmass_subleading,
				"flavor":tree.flavor_subleading
			}

		elif hemis == 'hemis1' and doneAlready == True:
			continue

		# Remake the lorentz vectors
		tjet = TLorentzVector()
		tjet.SetPtEtaPhiM(tVals["pt"],tVals["eta"],tVals["phi"],tVals["mass"])

		wjet = TLorentzVector()
		wjet.SetPtEtaPhiM(wVals["pt"],wVals["eta"],wVals["phi"],wVals["mass"])


		# Initialize weight
		weight = 1.0

		dy_val = abs(tjet.Rapidity()-wjet.Rapidity())

		wpt_cut = wpt[0]<wjet.Perp()<wpt[1]
		tpt_cut = tpt[0]<tjet.Perp()<tpt[1]
		dy_cut = dy[0]<=dy_val<dy[1]


		#We first perform the top and w candidate pt cuts and the deltaY cut
		if wpt_cut and tpt_cut and dy_cut: 

			# Apply the pdf weight
			if options.pdfweights != "nominal":
				if options.pdfweights == 'up':
					iweight = tree.pdf_weightUp
				elif options.pdfweights == 'down':
					iweight = tree.pdf_weightDown
				weight *= iweight


			weightSFt = 1.0
   
			if options.set!="data":
				#Pileup reweighting is done here 
				bin1 = tree.pileBin

				if options.pileup != 'off':
					weight *= PilePlot.GetBinContent(bin1)
				
				if options.set.find("QCD") == -1:
					weightSFt = ttagsf

			tmass_cut = tmass[0]<tVals["SDmass"]<tmass[1]

			#Now we start top-tagging.  In this file, we use a sideband based on inverting some top-tagging requirements
			if tmass_cut:
				ht = tjet.Perp() + wjet.Perp()

				weight*=weightSFt

				if tree.WJetMatchingRequirement == 1:
					if options.set.find('tW') != -1 or options.set.find('signal') != -1:
						weight*=wtagsf


				if tname != 'none' and options.set!='data' :
					#Trigger reweighting done here
					TRW = Trigger_Lookup( ht , TrigPlot )[0]

					weight*=TRW

				if options.ptreweight == "on" and options.set.find('ttbar') != -1:
					#ttbar pt reweighting done here
					# Need to grab extra correction from .txt
					if options.extraPtCorrection:
						FlatPtSFFile = open(di+'bstar_theta_PtSF_onTOPgroupCorrection.txt','r')
						FlatPtSFList = FlatPtSFFile.readlines()
						extraCorrection = float(FlatPtSFList[0])
						print 'Pt scale correction = ' + str(1+extraCorrection)
						FlatPtSFFile.close()
					else:
						extraCorrection = 0

					PTW = tree.pt_reweight*(1+extraCorrection)
					weight*=PTW


				try:
					tau32val		= 	tVals["tau3"]/tVals["tau2"] 
					tau21val		= 	wVals["tau2"]/wVals["tau1"]
				except:
					continue

				tau21_cut =  tau21[0]<=tau21val<tau21[1]
				tau32_cut =  tau32[0]<=tau32val<tau32[1]

				SJ_csvval = tVals["sjbtag"]

				sjbtag_cut = sjbtag[0]<SJ_csvval<=sjbtag[1]

				if type(wmass[0]) is float:
					wmass_cut = wmass[0]<=wVals["SDmass"]<wmass[1]
				elif type(wmass[0]) is list:
					wmass_cut = wmass[0][0]<=wVals["SDmass"]<wmass[0][1] or wmass[1][0]<=wVals["SDmass"]<wmass[1][1] 
				else:
					print "wmass type error"
					continue                        

				FullTop = tau32_cut and sjbtag_cut
				if wmass_cut:
					if tau21_cut:
						preTopTagCount += 1
						# check we have a 3rd jet and that we never divide by zero
						if tree.pt_subsubleading <= 0.0:
							continue
						if tree.tau2_subsubleading <= 0.0 or tree.tau1_subsubleading <= 0.0:
							continue

						has3rdJetCount += 1

						temp_variables = {
							'pt_top':tVals['pt'],
							'mass_top':tVals['mass'],
							'SDmass_top':tVals['SDmass'],
							'eta_top':tVals['eta'],
							'phi_top':tVals['phi'],
							'flavor_top':tVals['flavor'],
							'tau32':tau32val,
							'sjbtag':SJ_csvval,
							
							'pt_w':wVals['pt'],
							'mass_w':wVals['mass'],
							'SDmass_w':wVals['SDmass'],
							'eta_w':wVals['eta'],
							'phi_w':wVals['phi'],
							'flavor_w':wVals['flavor'],
							'tau21':tau21val,

							'pt_3':tree.pt_subsubleading,
							'mass_3':tree.mass_subsubleading,
							'topSDmass_3':tree.topSDmass_subsubleading,
							'wSDmass_3':tree.wSDmass_subsubleading,
							'eta_3':tree.eta_subsubleading,
							'phi_3':tree.phi_subsubleading,
							'flavor_3':tree.flavor_subsubleading,
							'tau21_3':tree.tau2_subsubleading/tree.tau1_subsubleading,
							'tau32_3':tree.tau3_subsubleading/tree.tau2_subsubleading,

							'weight':weight}

						for tv in miniTreeVars.keys():
							# try:
							miniTreeVars[tv][0] = temp_variables[tv]
							# except:
							# 	print "failed on "+tv
						miniTree.Fill()

						doneAlready = True

candidateCount.SetBinContent(1,preTopTagCount)
ThirdJetCount.SetBinContent(1,has3rdJetCount)

f.cd()
f.Write()
f.Close()