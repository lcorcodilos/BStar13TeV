#! /usr/bin/env python



###################################################################
##								 ##
## Name: TWrate.py						 ##
## Author: Kevin Nash 						 ##
## Date: 6/5/2012						 ##
## Purpose: This program creates eta binned tags and probes 	 ##
##          as a function of Pt for data and MC for use with 	 ##
##          TWrate_Maker.py.					 ##
##								 ##
###################################################################

import os
import glob
import math
from math import sqrt,exp
import ROOT
from ROOT import *

import sys
#from DataFormats.FWLite import Events, Handle
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
parser.add_option('-y', '--modmass', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'modmass',
				  help		=	'nominal up or down')
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
		
pie = math.pi 

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

#Based on what set we want to analyze, we find all Ntuple root files -----------------
if options.grid == "on":
	mainDir = "/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/BStar13TeV/TTrees/"
else:
	mainDir='TTrees/'

file = TFile(mainDir + "TWtreefile_"+options.set+"_Trigger_nominal_none.root")
tree = file.Get("Tree")
nevHisto = file.Get("nev")
B2Gnev = nevHisto.Integral()/jobs

settype = 'ttbar'

# if (options.set.find('ttbar') != -1) or (options.set.find('singletop') != -1):
# 	settype = 'ttbar'
# elif (options.set.find('QCD') != -1):
# 	settype ='ttbar'
# 	run_b_SF = False
# else :	
# 	settype = options.set

print 'The type of set is ' + settype

#--------------------------------------------------------------------------------------

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



if jobs!=1:
	f = TFile( "TWratefiletoy"+options.set+"_job"+options.num+"of"+options.jobs+"_PSET_"+options.cuts+".root", "recreate" )
else:
	f = TFile( "TWratefiletoy"+options.set+"_PSET_"+options.cuts+".root", "recreate" )

print "Creating histograms"

#Define Histograms
f.cd()
#---------------------------------------------------------------------------------------------------------------------#
Mtw_cut1    = TH1F("Mtw_cut1",  "mass of tw after wpt cut", 140, 500, 4000)
Mtw_cut2    = TH1F("Mtw_cut2",  "mass of tw after tpt cut", 140, 500, 4000)
Mtw_cut3    = TH1F("Mtw_cut3",  "mass of tw after dy cut", 140, 500, 4000)
Mtw_cut4    = TH1F("Mtw_cut4",  "mass of tw after tmass cut", 140, 500, 4000)
Mtw_cut5    = TH1F("Mtw_cut5",  "mass of tw after wmass cut", 140, 500, 4000)
Mtw_cut6    = TH1F("Mtw_cut6",  "mass of tw after tau21 cut", 140, 500, 4000)
Mtw_cut7    = TH1F("Mtw_cut7",  "mass of tw after sjbtag cut", 140, 500, 4000)
Mtw_cut8    = TH1F("Mtw_cut8", "mass of tw after tau32 cut", 140, 500, 4000)

Mtw_cut1.Sumw2()
Mtw_cut2.Sumw2()
Mtw_cut3.Sumw2()
Mtw_cut4.Sumw2()
Mtw_cut5.Sumw2()
Mtw_cut6.Sumw2()
Mtw_cut7.Sumw2()
Mtw_cut8.Sumw2()

nev = TH1F("nev",	"nev",		1, 0, 1 )

#---------------------------------------------------------------------------------------------------------------------#

# loop over events
#---------------------------------------------------------------------------------------------------------------------#

count = 0
jobiter = 0
print "Start looping"
#initialize the ttree variables
tree_vars = {	"wpt":array('d',[0.]),
				"wmass":array('d',[0.]),
				"tpt":array('d',[0.]),
				"tmass":array('d',[0.]),
				"tau32":array('d',[0.]),
				"tau21":array('d',[0.]),
				"sjbtag":array('d',[0.]),
				"weight":array('d',[0.])}#,"nsubjets":array('d',[0.])


NewTree = Make_Trees(tree_vars)
treeEntries = tree.GetEntries()
nev.SetBinContent(1,B2Gnev)

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


		# Initialize weight
		weight = 1.0

		dy_val = abs(tjet.Rapidity()-wjet.Rapidity())

		MtopW = (tjet+wjet).M()


		Mtw_cut1.Fill(MtopW,weight)
		wpt_cut = wpt[0]<wjet.Perp()<wpt[1]
		tpt_cut = tpt[0]<tjet.Perp()<tpt[1]
		dy_cut = dy[0]<=dy_val<dy[1]

		#We first perform the top and w candidate pt cuts and the deltaY cut
		if wpt_cut and tpt_cut:
			Mtw_cut2.Fill(MtopW,weight) 
			if dy_cut:
				Mtw_cut3.Fill(MtopW,weight) 
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
					
					if options.cuts=="default" and options.set.find("QCD") == -1:
						weightSFt = ttagsf

				tmass_cut = tmass[0]<tVals["SDmass"]<tmass[1]

				#Now we start top-tagging.  In this file, we use a sideband based on inverting some top-tagging requirements
				if tmass_cut:
					Mtw_cut4.Fill(MtopW,weight)

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
						PTW = tree.pt_reweight
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

					FullTop = sjbtag_cut and tau32_cut
					if wmass_cut:
						Mtw_cut5.Fill(MtopW,weight)
						if tau21_cut:
							Mtw_cut6.Fill(MtopW,weight)
							
							if sjbtag_cut:
								Mtw_cut7.Fill(MtopW,weight)
								# Grab the pass/fail ratio at the last second for efficiency
								if tau32_cut:
									Mtw_cut8.Fill(MtopW,weight)


									doneAlready = True


f.cd()
f.Write()
f.Close()

print "number of events: " + str(count)