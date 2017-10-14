#! /usr/bin/env python

###################################################################
##								 ##
## Name: TWkinematics.py	   			         ##
## Author: Kevin Nash 						 ##
## Date: 6/5/2012						 ##
## Purpose: This program performs the main analysis.  		 ##
##	    It takes the tagrates created by  	 		 ##
##          TWrate_Maker.py stored in fitdata, and uses 	 ##
##          them to weigh pre b tagged samples to create a 	 ##
##	    QCD background estimate along with the full event    ##
##	    selection to product Mtw inputs to Theta		 ##
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
#from DataFormats.FWLite import Events, Handle
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
parser.add_option('-y', '--modmass', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'modmass',
				  help		=	'nominal up or down')
parser.add_option('-j', '--jobs', metavar='F', type='string', action='store',
				  default	=	'1',
				  dest		=	'jobs',
				  help		=	'number of jobs')
parser.add_option('-t', '--tname', metavar='F', type='string', action='store',
				   default	=	'HLT_PFHT900,HLT_PFHT800,HLT_JET450',
				   dest		=	'tname',
				   help		=	'trigger name')
parser.add_option('-J', '--JES', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'JES',
				  help		=	'nominal, up, or down')
parser.add_option('-R', '--JER', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'JER',
				  help		=	'nominal, up, or down')
parser.add_option('-a', '--JMS', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'JMS',
				  help		=	'nominal, up, or down')
parser.add_option('-b', '--JMR', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'JMR',
				  help		=	'nominal, up, or down')
parser.add_option('-m', '--modulesuffix', metavar='F', type='string', action='store',
				  default	=	'none',
				  dest		=	'modulesuffix',
				  help		=	'ex. PtSmearUp')
parser.add_option('-g', '--grid', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'grid',
				  help		=	'running on grid off or on')
parser.add_option('-u', '--ptreweight', metavar='F', type='string', action='store',
				  default	=	'on',
				  dest		=	'ptreweight',
				  help		=	'on or off')
parser.add_option('-T', '--ttsub', metavar='F', type='string', action='store',
				  default	=	'on',
				  dest		=	'ttsub',
				  help		=	'on, off, or double')
parser.add_option('-p', '--pdfweights', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'pdfweights',
				  help		=	'nominal, up, or down')
parser.add_option('-z', '--pdfset', metavar='F', type='string', action='store',
				  default	=	'cteq66',
				  dest		=	'pdfset',
				  help		=	'pdf set')
parser.add_option('--printEvents', metavar='F', action='store_true',
				  default=False,
				  dest='printEvents',
				  help='Print events that pass selection (run:lumi:event)')
parser.add_option('--noExtraPtCorrection', metavar='F', action='store_false',
				  default=True,
				  dest='extraPtCorrection',
				  help='Call to turn off extraPtCorrection')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
				  default	=	'default',
				  dest		=	'cuts',
				  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-v', '--var', metavar='F', type='string', action='store',
				  default       =       'analyzer',
				  dest          =       'var',
				  help          =       'anaylzer or kinematics')
parser.add_option('-S', '--split', metavar='F', type='string', action='store',
				  default	=	'event',
				  dest		=	'split',
				  help		=	'split by event of file') # file splitting doesn't work with ttrees
parser.add_option('-A', '--Alphabet', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'Alphabet',
				  help		=	'turn alphabet on or off')
parser.add_option('-r', '--rate', metavar='F', type='string', action='store',
				  default	=	'tpt',
				  dest		=	'rate',
				  help		=	'tpt, Mt, Mtw')
parser.add_option('-C', '--cheat', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'cheat',
				  help		=	'on or off')
parser.add_option('-i', '--iteration', metavar='F', type='int', action='store',
				  default	=	-1,
				  dest		=	'iteration',
				  help		=	'Scale factor iteration. Default 0')

(options, args) = parser.parse_args()

if (options.set.find('QCD') != -1):
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
		
pie = math.pi 

#Load up cut values based on what selection we want to run 
if options.cuts == 'lowWmass' or options.cuts == 'highWmass':
	Cuts = LoadCuts('default')
elif options.cuts == 'lowWmass1' or options.cuts == 'highWmass1':
	Cuts = LoadCuts('sideband')
else:
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
eta = Cuts['eta']

Cons = LoadConstants()
lumi = Cons['lumi']
Lumi = str(lumi/1000)+'fb'
Lumi2 = str(int(lumi)) + 'pb'
ttagsf = Cons['ttagsf']

if options.cuts.find('rate') != -1:
	Wpurity = 'LP'
	wtagsf = Cons['wtagsf_LP']
	wtagsfsig = Cons['wtagsfsig_LP']
else:
	Wpurity = 'HP'
	wtagsf = Cons['wtagsf_HP']
	wtagsfsig = Cons['wtagsfsig_HP']



#For large datasets we need to parallelize the processing
jobs=int(options.jobs)
if jobs != 1:
	num=int(options.num)
	jobs=int(options.jobs)
	print "Running over " +str(jobs)+ " jobs"
	print "This will process job " +str(num)
else:
	print "Running over all events"

#This section defines some strings that are used in naming the output files

#-- Postuncorr is used for softdrop mass, post is used for LV
mod = ''
post = ''
post2 = ''
if options.JES!='nominal':
	mod = mod + 'JES' + '_' + options.JES
	post='jes'+options.JES
if options.JER!='nominal':
	mod = mod + 'JER' + '_' + options.JER
	post='jer'+options.JER
if options.JMS!='nominal':
	mod = mod + 'JMS' + '_' + options.JMS
	post2='jes'+options.JMS
if options.JMR!='nominal':
	mod = mod + 'JMR' + '_' + options.JMR
	post2='jer'+options.JMR

#----------------Need to grab extra top pt reweight factor-------------------
# Naming syntax
# - ptItString: only non-empty for doing the iterations study, assigned to all files
# - ptTTString: always empty for non-ttbar, empty for ttbar when doing iterations

ptItString = ''
ptTTString = ''
# # If we're not running the study
# if options.iteration == -1:
# 	# And we want the extra correction turned on
# 	if options.extraPtCorrection:
# 		# Grab the latest SF and don't do any renaming
# 		ptTTString = ''
# 		TopPtReweightFile = TFile(di+'TWTopPtSF_9.root')
# 		TopPtReweightPlot = TopPtReweightFile.Get('TWTopPtSF_9')
# 	# And we don't want the extra correction turned on
# 	elif not options.extraPtCorrection:
# 		ptTTString = '_noExtraPtCorrection'
# 		TopPtReweightFile = TFile(di+'TWTopPtSF_0.root')
# 		TopPtReweightPlot = TopPtReweightFile.Get('TWTopPtSF_0')
# 	# And we don't want any pt correction
# 	elif options.ptreweight == 'off':
# 		ptTTString = '_ptreweight_off'
# # If we are running the pt study
# elif options.iteration >=0:
# 	ptTTString = '_ptSF' + str(options.iteration)
# 	TopPtReweightFile = TFile(di+'TWTopPtSF_'+str(options.iteration)+'.root')
# 	TopPtReweightPlot = TopPtReweightFile.Get('TWTopPtSF_'+str(options.iteration))

ptTTString = ''
if options.set == 'ttbar':
	if not options.extraPtCorrection:
		ptTTString = '_noExtraPtCorrection'
	if options.ptreweight == 'off':
		ptTTString = '_ptreweight_off'

#----------------------------------------------------------------------------

#TTbar subtraction string is set here for non-qcd
ttsubString = ''
if setstr == 'data':
	if options.ttsub == 'on':
		ttsubString = ''
	elif options.ttsub == 'off':
		ttsubString = '_nottsub'
	elif options.ttsub == 'double':
		ttsubString = '_doublettsub'

pstr = ""
if options.pdfweights!="nominal":
	print "using pdf uncertainty"
	pstr = "_pdf_"+options.pdfweights

pustr = ""
if options.pileup=='off':
	pustr = "_pileup_unweighted"
if options.pileup=='up':
	pustr = "_pileup_up"
if options.pileup=='down':
	pustr = "_pileup_down"

if mod == '':
	mod = options.modulesuffix

print "mod = " + mod

mmstr = ""
if options.modmass!="nominal":
	print "using modm uncertainty"
	mmstr = "_modm_"+options.modmass

#------------------------------------------------------------------------

#Based on what set we want to analyze, we find all Ntuple root files 
if options.grid == "on":
	mainDir = "root://cmsxrootd.fnal.gov//store/user/lcorcodi/TTrees/"
else:
	mainDir='TTrees/'

file = TFile.Open(mainDir + "TWtreefile_"+options.set+"_Trigger_"+tnameformat+"_"+mod+".root")
tree = file.Get("Tree")

settype = 'ttbar'

#CHANGE BACK if we get signal pileup
# if (options.set.find('ttbar') != -1) or (options.set.find('signal') != -1):
# 	settype = 'ttbar'
# else :
# 	settype = options.set

# print 'The type of set is ' + settype

#---------------Modmass file if you dont want alphabet-----------------------
if options.cheat == 'off':
	rateCuts = 'rate_'+options.cuts
elif options.cheat == 'on':
	rateCuts = options.cuts

# if rateCuts == 'rate_sideband1':
# 	rateCuts = 'rate_default'


if options.Alphabet != "on":
	ModFile = ROOT.TFile(di+"ModMassFile_"+rateCuts+ptTTString+".root")
	ModPlot = ModFile.Get("rtmass")

	# if options.rate == 'tpt':
	# 	ModFitParams = open(di+'fitdata/ModMass_pol3_PSET_rate_'+options.cuts+'.txt')
	# else:
	# 	ModFitParams = open(di+'fitdata/'+options.rate+'/ModMass_pol3_PSET_rate_'+options.cuts+'.txt')

	# ModFitParams.seek(0)
	# ModFit = TF1("ModFit",'pol3',tmass[0],tmass[1])

	# ModFitParams2 = ModFitParams.read()

	# for i in range(0,4):
	# 	ModFit.SetParameter(i,float(ModFitParams2.split('\n')[i]) )

	# ModFile = ROOT.TFile(di+"ModMassFile_"+options.cuts+".root")
	# ModPlot = ModFile.Get("rtmass")


if options.set != 'data':
	#Load up scale factors (to be used for MC only)

	TrigFile = TFile(di+"Triggerweight_2jethack_data.root")
	TrigPlot = TrigFile.Get("TriggerWeight_"+tnamestr+"_pre_HLT_PFHT475")


	if settype == 'ttbar':
		PileFile = TFile(di+"PileUp_Ratio_"+settype+".root")
		if options.pileup=='up':
			PilePlot = PileFile.Get("Pileup_Ratio_up")
		elif options.pileup=='down':
			PilePlot = PileFile.Get("Pileup_Ratio_down")
		else:	
			PilePlot = PileFile.Get("Pileup_Ratio")


nevHisto = file.Get("nev")
B2Gnev = nevHisto.Integral()/jobs
# For some reason, the above line makes python forget what `tpt` is so redifining
tpt = Cuts['tpt']

#---------------------------------------------------------------------------------------------------------------------#
# var = ""
# if options.var == "kinematics":
# 	var = "_kin"

if jobs != 1:
	f = TFile( "TWanalyzer"+options.set+"_Trigger_"+tnameformat+"_"+mod+pustr+pstr+mmstr+"_job"+options.num+"of"+options.jobs+"_PSET_"+options.cuts+ttsubString+ptTTString+".root", "recreate" )
else:
	f = TFile( "TWanalyzer"+options.set+"_Trigger_"+tnameformat+"_"+mod+pustr+pstr+mmstr+"_PSET_"+options.cuts+ttsubString+ptTTString+".root", "recreate" )

#Load up the average t-tagging rates -- Takes parameters from text file and makes a function
#CHANGE BACK
if options.Alphabet == "on":
	TTR = TTR_Init('QUAD',rateCuts,setstr,options.rate,di,ttsubString+ptTTString)
	TTR_errUp = TTR_Init('QUAD_errUp',rateCuts,setstr,options.rate,di,ttsubString+ptTTString)
	TTR_errDown = TTR_Init('QUAD_errDown',rateCuts,setstr,options.rate,di,ttsubString+ptTTString)
	fittitles = ["QUAD"]
	fits = []
	for fittitle in fittitles:
		fits.append(TTR_Init(fittitle,rateCuts,setstr,options.rate,di,ttsubString+ptTTString))

elif options.Alphabet == "off":
	TagFile = TFile(di+"plots/TWrate_Maker_"+setstr+"_"+Lumi2+"_PSET_"+rateCuts+ttsubString+ptTTString+".root")
	print "Opening rate file " + "plots/TWrate_Maker_"+setstr+"_"+Lumi2+"_PSET_"+rateCuts+ttsubString+ptTTString+".root"
	TagPlote1 = TagFile.Get("tagrateeta1")
	TagPlote2 = TagFile.Get("tagrateeta2") 


	TTR = TTR_Init('Bifpoly',rateCuts,setstr,options.rate,di,ttsubString+ptTTString)
	TTR_err = TTR_Init('Bifpoly_err',rateCuts,setstr,options.rate,di,ttsubString+ptTTString)

	fittitles = ["pol0","pol2","pol3","FIT","Bifpoly","expofit"]
	fits = []
	for fittitle in fittitles:
		fits.append(TTR_Init(fittitle,rateCuts,setstr,options.rate,di,ttsubString+ptTTString))

	TagFile1 = TFile(di+"Tagrate"+setstr+"2D_"+rateCuts+ttsubString+ptTTString+".root")
	TagPlot2de1= TagFile1.Get("tagrateeta1")
	TagPlot2de2= TagFile1.Get("tagrateeta2")

print "Creating histograms"


f.cd()
#---------------------------------------------------------------------------------------------------------------------#
Mtw	    = TH1F("Mtw",     "mass of tw",     	  	      140, 500, 4000 )

nev = TH1F("nev",	"nev",		1, 0, 1 )

hEta1Count = TH1I("eta1Count", "number of events in low eta region", 1, 0, 1)
hEta2Count = TH1I("eta2Count", "number of events in high eta region", 1, 0, 1)

hmatchingFailed = TH1F("matchingFailed", "fraction of events that failed w jet matching requirement", 1, 0, 1)

Mtwtrigup	= TH1F("Mtwtrigup",	"mass of tw trig up",     	  	140, 500, 4000 )
Mtwtrigdown	= TH1F("Mtwtrigdown",	"mass of tw trig up",     	  	140, 500, 4000 )

MtwWup		= TH1F("MtwWup",	"mass of tw w tag SF up",     	  	140, 500, 4000 )
MtwWdown	= TH1F("MtwWdown",	"mass of tw w tag SF down",     	  	140, 500, 4000 )

MtwTptup	= TH1F("MtwTptup",	"mass of tw top pt reweight up",     	  	140, 500, 4000 )
MtwTptdown 	= TH1F("MtwTptdown",	"mass of tw top pt reweight down",     	  	140, 500, 4000 )

MtwExtrapUp = TH1F("MtwExtrapUp", "mass of top extrapolation uncertainty up", 140, 500, 4000)
MtwExtrapDown = TH1F("MtwExtrapDown", "mass of top extrapolation uncertainty down", 140, 500, 4000)

Nevents	    = TH1F("Nevents",     	  "mass of tb",     	  	         5, 0., 5. )
QCDbkg= TH1F("QCDbkg",     "QCD background estimate",     	  	      140, 500, 4000 )
QCDbkgh= TH1F("QCDbkgh",     "QCD background estimate up error",     	  	     140, 500, 4000 )
QCDbkgl= TH1F("QCDbkgl",     "QCD background estimate down error",     	  	      140, 500, 4000 )
if options.Alphabet == "off":
	QCDbkg2D= TH1F("QCDbkg2D",     "QCD background estimate 2d error",     	  	      140, 500, 4000 )
	QCDbkg2Dup= TH1F("QCDbkg2Dup",     "QCD background estimate 2d error",     	  	      140, 500, 4000 )
	QCDbkg2Ddown= TH1F("QCDbkg2Ddown",     "QCD background estimate 2d error",     	  	      140, 500, 4000 )

preAntiTag = TH1F("preAntiTag",     "Antitag distribution before R p/f weighting",     	  	      140, 500, 4000 )
preAntiTag.Sumw2()

MwStack		= TH1F("MwStack",	"top candidate mass for stack",		100,   105, 210 )
QCDbkgMwStack	= TH1F("QCDbkgMwStack", "QCD background for top mass",		100, 105, 210 )

masswHist = TH1F("Massw", "Massw", 25,  0, 5 )
masswHist.Sumw2()

Mtw.Sumw2()

Mtwtrigup.Sumw2()
Mtwtrigdown.Sumw2()

MtwWup.Sumw2()
MtwWdown.Sumw2()

MtwTptup.Sumw2()
MtwTptdown.Sumw2()

MtwExtrapUp.Sumw2()
MtwExtrapDown.Sumw2()

QCDbkg.Sumw2()
QCDbkgh.Sumw2()
QCDbkgl.Sumw2()

MwStack.Sumw2()
QCDbkgMwStack.Sumw2()




Mtw_cut1    = TH1F("Mtw_cut1",  "mass of tw after wpt cut", 140, 500, 4000)
Mtw_cut2    = TH1F("Mtw_cut2",  "mass of tw after tpt cut", 140, 500, 4000)
Mtw_cut3    = TH1F("Mtw_cut3",  "mass of tw after dy cut", 140, 500, 4000)
Mtw_cut4    = TH1F("Mtw_cut4",  "mass of tw after tmass cut", 140, 500, 4000)
Mtw_cut5    = TH1F("Mtw_cut5",  "mass of tw after wmass cut", 140, 500, 4000)
Mtw_cut6    = TH1F("Mtw_cut6",  "mass of tw after tau21 cut", 140, 500, 4000)
Mtw_cut7    = TH1F("Mtw_cut7",  "mass of tw after eta1 cut", 140, 500, 4000)
Mtw_cut8    = TH1F("Mtw_cut8",  "mass of tw after eta2 cut", 140, 500, 4000)
Mtw_cut9    = TH1F("Mtw_cut9",  "mass of tw after sjbtag cut", 140, 500, 4000)
Mtw_cut10   = TH1F("Mtw_cut10", "mass of tw after tau32 cut", 140, 500, 4000)

EtaTop      = TH1F("EtaTop",        "Top Candidate eta",     	  	      12, -2.4, 2.4 )
EtaW   = TH1F("EtaW",     "W Candidate eta",     	      12, -2.4, 2.4 )

PtTop       = TH1F("PtTop",       	"Top Candidate pt (GeV)",     	      50, 450, 1500 )
PtW    	    = TH1F("PtW",     		"W Candidate pt (GeV)",     	      50, 370, 1430 )
PtTopW      = TH1F("PtTopW",  		"pt of tw system",     	  	      35,   0, 700 )

PhiTop    = TH1F("PhiTop",      "Top Candidate Phi (rad)",     	  	             12, -pie, pie )
PhiW 	  = TH1F("PhiW",   	"Top Candidate Phi (rad)",     	  	             12, -pie, pie )
dPhi      = TH1F("dPhi",        "delta theat between Top and W Candidates",    	     12, 2.2, pie )

Mt		= TH1F("Mt",	"Top mass",				25,105,210)
Nsubjetiness32	= TH1F("Nsubjetiness32",	"Nsubjetiness",				8,0,1.6)
Nsubjetiness21	= TH1F("Nsubjetiness21",	"Nsubjetiness",				8,0,1.6)
deltaY		= TH1F("deltaY",	"delta y between Top and b candidates",	10,0,5)
CSV		= TH1F("CSV",		"CSV",					10,0,1)
CSVMax		= TH1F("CSVMax",	"CSV maximum",				10,0,1)
Btag		= TH1F("Btag",		"Tagged bs",				4,0,4)
Btagmax		= TH1F("Btagmax",	"Max value of b disc",			30,0,1)
Btruth		= TH1F("Btruth",	"MC Truth for bs",			4,0,4)
JetsVsBtag	= TH2F("JetsVsBtag",	"Jets vs Btag",				4,0,4,	30,0,30)

QCDbkgET	= TH1F("QCDbkgET",       "QCD background estimate eta top",     	     12, -2.4, 2.4 )
QCDbkgETh= TH1F("QCDbkgETh",     "QCD background estimate up error",     	  	      12, -2.4, 2.4 )
QCDbkgETl= TH1F("QCDbkgETl",     "QCD background estimate down error",     	  	      12, -2.4, 2.4 )
if options.Alphabet == "off":
	QCDbkgET2D= TH1F("QCDbkgET2D",     "QCD background estimate 2d error",     	  	      12, -2.4, 2.4 )
	QCDbkgET2Dup= TH1F("QCDbkgET2Dup",     "QCD background estimate 2d error",     	  	      12, -2.4, 2.4 )
	QCDbkgET2Ddown= TH1F("QCDbkgET2Ddown",     "QCD background estimate 2d error",     	  	      12, -2.4, 2.4 )

QCDbkgEW	= TH1F("QCDbkgEW",       "QCD background estimate eta w",       	     12, -2.4, 2.4 )
QCDbkgEWh= TH1F("QCDbkgEWh",     "QCD background estimate up error",     	  	      12, -2.4, 2.4 )
QCDbkgEWl= TH1F("QCDbkgEWl",     "QCD background estimate down error",     	  	      12, -2.4, 2.4 )
if options.Alphabet == "off":
	QCDbkgEW2D= TH1F("QCDbkgEW2D",     "QCD background estimate 2d error",     	  	      12, -2.4, 2.4 )
	QCDbkgEW2Dup= TH1F("QCDbkgEW2Dup",     "QCD background estimate 2d error",     	  	      12, -2.4, 2.4 )
	QCDbkgEW2Ddown= TH1F("QCDbkgEW2Ddown",     "QCD background estimate 2d error",     	  	      12, -2.4, 2.4 )

QCDbkgPT	= TH1F("QCDbkgPT",       "QCD background estimate pt top",     	  	     50, 450, 1500 )
QCDbkgPTh= TH1F("QCDbkgPTh",     "QCD background estimate up error",     	  	      50, 450, 1500 )
QCDbkgPTl= TH1F("QCDbkgPTl",     "QCD background estimate down error",     	  	      50, 450, 1500 )
if options.Alphabet == "off":
	QCDbkgPT2D= TH1F("QCDbkgPT2D",     "QCD background estimate 2d error",     	  	      50, 450, 1500 )
	QCDbkgPT2Dup= TH1F("QCDbkgPT2Dup",     "QCD background estimate 2d error",     	  	      50, 450, 1500 )
	QCDbkgPT2Ddown= TH1F("QCDbkgPT2Ddown",     "QCD background estimate 2d error",     	  	      50, 450, 1500 )

QCDbkgPW	= TH1F("QCDbkgPW",       "QCD background estimate pt W",       	 	     50, 370, 1430 )
QCDbkgPWh= TH1F("QCDbkgPWh",     "QCD background estimate up error",     	  	      50, 370, 1430 )
QCDbkgPWl= TH1F("QCDbkgPWl",     "QCD background estimate down error",     	  	      50, 370, 1430 )
if options.Alphabet == "off":
	QCDbkgPW2D= TH1F("QCDbkgPW2D",     "QCD background estimate 2d error",     	  	      50, 370, 1430 )
	QCDbkgPW2Dup= TH1F("QCDbkgPW2Dup",     "QCD background estimate 2d error",     	  	      50, 370, 1430 )
	QCDbkgPW2Ddown= TH1F("QCDbkgPW2Ddown",     "QCD background estimate 2d error",     	  	      50, 370, 1430 )

QCDbkgPTW	= TH1F("QCDbkgPTW",      "QCD background estimate pt top+w",     	     35,   0, 700  )
QCDbkgPTWh= TH1F("QCDbkgPTWh",     "QCD background estimate up error",     	  	      35,   0, 700 )
QCDbkgPTWl= TH1F("QCDbkgPTWl",     "QCD background estimate down error",     	  	      35,   0, 700 )
if options.Alphabet == "off":
	QCDbkgPTW2D= TH1F("QCDbkgPTW2D",     "QCD background estimate 2d error",     	  	      35,   0, 700 )
	QCDbkgPTW2Dup= TH1F("QCDbkgPTW2Dup",     "QCD background estimate 2d error",     	  	      35,   0, 700 )
	QCDbkgPTW2Ddown= TH1F("QCDbkgPTW2Ddown",     "QCD background estimate 2d error",     	  	      35,   0, 700 )

QCDbkgPhT	= TH1F("QCDbkgPhT",      "QCD background estimate phi top",       	     12, -pie, pie )
QCDbkgPhTh= TH1F("QCDbkgPhTh",     "QCD background estimate up error",     	  	      12, -pie, pie )
QCDbkgPhTl= TH1F("QCDbkgPhTl",     "QCD background estimate down error",     	  	      12, -pie, pie )
if options.Alphabet == "off":
	QCDbkgPhT2D= TH1F("QCDbkgPhT2D",     "QCD background estimate 2d error",     	  	      12, -pie, pie )
	QCDbkgPhT2Dup= TH1F("QCDbkgPhT2Dup",     "QCD background estimate 2d error",     	  	      12, -pie, pie )
	QCDbkgPhT2Ddown= TH1F("QCDbkgPhT2Ddown",     "QCD background estimate 2d error",     	  	      12, -pie, pie )

QCDbkgPhW	= TH1F("QCDbkgPhW",      "QCD background estimate phi w",     	  	     12, -pie, pie )
QCDbkgPhWh= TH1F("QCDbkgPhWh",     "QCD background estimate up error",     	  	      12, -pie, pie )
QCDbkgPhWl= TH1F("QCDbkgPhWl",     "QCD background estimate down error",     	  	      12, -pie, pie )
if options.Alphabet == "off":
	QCDbkgPhW2D= TH1F("QCDbkgPhW2D",     "QCD background estimate 2d error",     	  	      12, -pie, pie )
	QCDbkgPhW2Dup= TH1F("QCDbkgPhW2Dup",     "QCD background estimate 2d error",     	  	      12, -pie, pie )
	QCDbkgPhW2Ddown= TH1F("QCDbkgPhW2Ddown",     "QCD background estimate 2d error",     	  	      12, -pie, pie )

QCDbkgdPhi	= TH1F("QCDbkgdPhi",     "QCD background estimate delta phi",       	     12,  2.2, pie )
QCDbkgdPhih= TH1F("QCDbkgdPhih",     "QCD background estimate up error",     	  	      12, 2.2, pie )
QCDbkgdPhil= TH1F("QCDbkgdPhil",     "QCD background estimate down error",     	  	      12, 2.2, pie )
if options.Alphabet == "off":
	QCDbkgdPhi2D= TH1F("QCDbkgdPhi2D",     "QCD background estimate 2d error",     	  	      12, 2.2, pie )
	QCDbkgdPhi2Dup= TH1F("QCDbkgdPhi2Dup",     "QCD background estimate 2d error",     	  	      12, 2.2, pie )
	QCDbkgdPhi2Ddown= TH1F("QCDbkgdPhi2Ddown",     "QCD background estimate 2d error",     	  	      12, 2.2, pie )

QCDbkgMt	= TH1F("QCDbkgMt",     "QCD background estimate top mass",       	     25,105,210 )
QCDbkgMth= TH1F("QCDbkgMth",     "QCD background estimate up error",     	  	      25,105,210 )
QCDbkgMtl= TH1F("QCDbkgMtl",     "QCD background estimate down error",     	  	      25,105,210 )
if options.Alphabet == "off":
	QCDbkgMt2D= TH1F("QCDbkgMt2D",     "QCD background estimate 2d error",     	  	      25,105,210 )
	QCDbkgMt2Dup= TH1F("QCDbkgMt2Dup",     "QCD background estimate 2d error",     	  	      25,105,210 )
	QCDbkgMt2Ddown= TH1F("QCDbkgMt2Ddown",     "QCD background estimate 2d error",     	  	      25,105,210 )


Mtw_cut1.Sumw2()
Mtw_cut2.Sumw2()
Mtw_cut3.Sumw2()
Mtw_cut4.Sumw2()
Mtw_cut5.Sumw2()
Mtw_cut6.Sumw2()
Mtw_cut7.Sumw2()
Mtw_cut8.Sumw2()
Mtw_cut9.Sumw2()
Mtw_cut10.Sumw2()


EtaTop.Sumw2()
EtaW.Sumw2()

PtTop.Sumw2()
PtW.Sumw2()
PtTopW.Sumw2()

PhiTop.Sumw2()
PhiW.Sumw2()
dPhi.Sumw2()


Mt.Sumw2()
Nsubjetiness32.Sumw2()
Nsubjetiness21.Sumw2()
deltaY.Sumw2()
CSV.Sumw2()
CSVMax.Sumw2()
Btag.Sumw2()
Btagmax.Sumw2()
Btruth.Sumw2()
JetsVsBtag.Sumw2()

QCDbkgET.Sumw2()
QCDbkgETh.Sumw2()
QCDbkgETl.Sumw2()

QCDbkgEW.Sumw2()
QCDbkgEWh.Sumw2()
QCDbkgEWl.Sumw2()

QCDbkgPT.Sumw2()
QCDbkgPTh.Sumw2()
QCDbkgPTl.Sumw2()

QCDbkgPW.Sumw2()
QCDbkgPWh.Sumw2()
QCDbkgPWl.Sumw2()

QCDbkgPTW.Sumw2()
QCDbkgPTWh.Sumw2()
QCDbkgPTWl.Sumw2()

QCDbkgPhT.Sumw2()
QCDbkgPhTh.Sumw2()
QCDbkgPhTl.Sumw2()

QCDbkgPhW.Sumw2()
QCDbkgPhWh.Sumw2()
QCDbkgPhWl.Sumw2()

QCDbkgdPhi.Sumw2()
QCDbkgdPhih.Sumw2()
QCDbkgdPhil.Sumw2()
	
QCDbkgMt.Sumw2()
QCDbkgMth.Sumw2()	
QCDbkgMtl.Sumw2()
	
QCDbkg_ARR = []
	
kinVars = 	['', 	'ET', 	'EW', 	'PT', 	'PW', 	'PTW', 	'PhT', 	'PhW', 	'dPhi', 'Mt'	]
kinBin = 	[140, 	12, 	12, 	50, 	50,	35,	12,	12,	12, 25	]
kinLow = 	[500, 	-2.4, 	-2.4, 	450, 	370,	0,	-pie,	-pie,	2.2, 105	]
kinHigh = 	[4000, 	2.4, 	2.4, 	1500, 	1430,	700,	pie,	pie,	pie, 210	]

# if options.var == 'analyzer':
# 	iterations = 1
# elif options.var == 'kinematics':
# 	iterations = len(kinVars)
# else:
# 	print "You messed up the var options bozo"
# 	quit()

iterations = len(kinVars)

arr_count = 0
for iVar in range(0,iterations):
	for ihist in fittitles:
		QCDbkg_ARR.append(TH1F("QCDbkg"+kinVars[iVar]+ihist,     str(kinVars[iVar]) + "in b+1 pt est etabin",    kinBin[iVar], kinLow[iVar], kinHigh[iVar]))
		QCDbkg_ARR[arr_count].Sumw2()
		arr_count += 1

#---------------------------------------------------------------------------------------------------------------------#

# loop over events
#---------------------------------------------------------------------------------------------------------------------#
eta1Count = 0
eta2Count = 0

matchingFailed = 0

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
				"flavor":array('d',[0.]),
				"weight":array('d',[0.])}

NewTree = Make_Trees(tree_vars)
treeEntries = tree.GetEntries()

goodEvents = []

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


		weight = 1.0

		dy_val = abs(tjet.Rapidity()-wjet.Rapidity())

		MtopW = (tjet+wjet).M()

		Mtw_cut1.Fill(MtopW,weight)
		wpt_cut = wpt[0]<wjet.Perp()<wpt[1]
		tpt_cut = tpt[0]<tjet.Perp()<tpt[1]
		dy_cut = dy[0]<=dy_val<dy[1]
			
		if wpt_cut and tpt_cut:
			Mtw_cut2.Fill(MtopW,weight)
			deltaY.Fill(dy_val,weight)

			if dy_cut:
				Mtw_cut3.Fill(MtopW,weight)
				if options.pdfweights != "nominal" :
					if options.pdfweights == 'up':
						iweight = tree.pdf_weightUp
					elif options.pdfweights == 'down':
						iweight = tree.pdf_weightDown
					weight *= iweight


# Apply top scale factor and pileup correction to all MC
# Got rid of uncertainties since they are flat and applied in theta
				weightSFt = 1.0
				if options.set!="data":
					bin1 = tree.pileBin

					if options.pileup != 'off':
						weight *= PilePlot.GetBinContent(bin1)

					if options.set.find("QCD") == -1:
						weightSFt = ttagsf # Error done in theta
						

				tmass_cut = tmass[0]<tVals["SDmass"]<tmass[1]

				if tmass_cut :
					Mtw_cut4.Fill(MtopW,weight)

					ht = tjet.Perp() + wjet.Perp()

					weight*=weightSFt

	# Apply w tagging scale factor for anything that passes w jet matching requirement and is ST_tW or signal
					weightSFwup = 1.0
					weightSFwdown = 1.0
					if tree.WJetMatchingRequirement == 1:
						if options.set.find('tW') != -1 or options.set.find('signal') != -1:
							weightSFwup = (wtagsf + wtagsfsig)*weight
							weightSFwdown = (wtagsf - wtagsfsig)*weight
							weight*=wtagsf
					elif tree.WJetMatchingRequirement == 0:
						matchingFailed += 1

					weighttrigup=1.0
					weighttrigdown=1.0
					if tname != 'none' and options.set!='data' :
						#Trigger reweighting done here
						TRW = Trigger_Lookup( ht , TrigPlot )[0]
						TRWup = Trigger_Lookup( ht , TrigPlot )[1]
						TRWdown = Trigger_Lookup( ht , TrigPlot )[2]

						weighttrigup=weight*TRWup
						weighttrigdown=weight*TRWdown
						weight*=TRW

						weightSFwup*=TRW
						weightSFwdown*=TRW
				

					weightSFptup=1.0
					weightSFptdown=1.0
					if options.ptreweight == "on" and options.set.find('ttbar') != -1:
					# 	ttbar pt reweighting done here
						# extraCorrection = TopPtReweightPlot.GetBinContent(1) # Will be zero with iteration 0
						if options.extraPtCorrection:
							FlatPtSFFile = open(di+'bstar_theta_PtSF_onTOPgroupCorrection.txt','r')
							FlatPtSFList = FlatPtSFFile.readlines()
							extraCorrection = float(FlatPtSFList[0])
							extraCorrectionUp = float(FlatPtSFList[1])
							extraCorrectionDown = float(FlatPtSFList[2])
							# print 'Pt scale correction = ' + str(1+extraCorrection)
							FlatPtSFFile.close()
						else:
							extraCorrection = 0
							extraCorrectionUp = 0
							extraCorrectionDown = 0


						PTW = tree.pt_reweight*(1+extraCorrection)
						PTWup = tree.pt_reweight*(1+extraCorrection+extraCorrectionUp)
						PTWdown = tree.pt_reweight*(1+extraCorrection-extraCorrectionDown)

						# weightSFptSig = abs(weight - weight*PTW)

						weightSFptup=weight*PTWup#PTW+weightSFptSig
						weightSFptdown=weight*PTWdown#max(0.0,weight*PTW-weightSFptSig)
						weight*=PTW

						weightSFwup*=PTW
						weightSFwdown*=PTW

						weighttrigup*=PTW
						weighttrigdown*=PTW
			
					try:
						tau32val		= 	tVals["tau3"]/tVals["tau2"] 
						tau21val		= 	wVals["tau2"]/wVals["tau1"]
					except:
						continue

					tau21_cut =  tau21[0]<=tau21val<tau21[1]
					tau32_cut =  tau32[0]<=tau32val<tau32[1]

					SJ_csvval = tVals["sjbtag"]

					sjbtag_cut = sjbtag[0]<SJ_csvval<=sjbtag[1]

					CSVMax.Fill(SJ_csvval,weight)

					Nsubjetiness32.Fill(tau32val,weight)
					Nsubjetiness21.Fill(tau21val,weight)
						
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

					# Get the extrapolation uncertainty
							extrap = ExtrapUncert_Lookup(wjet.Perp(),Wpurity)
							extrapUp = weight*(1+extrap)
							extrapDown = weight*(1-extrap)

# ------------------- Now going to split into alphabet and tagrate parts -----------------
							if options.Alphabet == "off":
								eta_regions = [eta1,eta2]
								eta1_cut = eta1[0]<=abs(tjet.Eta())<eta1[1]
								eta2_cut = eta2[0]<=abs(tjet.Eta())<eta2[1]

								TTRweight = bkg_weight_pt(tjet,TTR,eta_regions)
								TTRweightsigsq = bkg_weight_pt(tjet,TTR_err,eta_regions)
								#TTRweight = bkg_weight_twmass(tjet,MtopW,TTR,eta_regions)
								#TTRweightsigsq = bkg_weight_twmass(tjet,MtopW,TTR_err,eta_regions)
								TTRweighterrup = TTRweight+sqrt(TTRweightsigsq)
								TTRweighterrdown = TTRweight-sqrt(TTRweightsigsq)

								modm = tVals["SDmass"]
								if options.modmass=='nominal':
									massw = ModPlot.Interpolate(modm) #ModFit.Eval(modm) 
								if options.modmass=='up':
									massw = 1 + 0.5*(ModPlot.Interpolate(modm) -1)
								if options.modmass=='down':
									massw = max(0.0,1 + 1.5*(ModPlot.Interpolate(modm) -1))
								if options.modmass=='none':
									massw = 1
								
								masswHist.Fill(massw)

								if (eta1_cut) and not FullTop:
									eta1Count += 1
									xbin = TagPlot2de2.GetXaxis().FindBin(tjet.Perp())
									ybin = TagPlot2de2.GetYaxis().FindBin(MtopW)
									tagrate2d = TagPlot2de2.GetBinContent(xbin,ybin)
									tagrate2derr = TagPlot2de2.GetBinError(xbin,ybin)
									QCDbkg2D.Fill(MtopW,tagrate2d*weight*massw)
									QCDbkg2Dup.Fill(MtopW,(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkg2Ddown.Fill(MtopW,(tagrate2d-tagrate2derr)*weight*massw)	
			
									Mtw_cut8.Fill(MtopW,weight)
									QCDbkgET2D.Fill(tjet.Eta(),tagrate2d*weight*massw)
									QCDbkgET2Dup.Fill(tjet.Eta(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgET2Ddown.Fill(tjet.Eta(),(tagrate2d-tagrate2derr)*weight*massw)

									QCDbkgEW2D.Fill(wjet.Eta(),tagrate2d*weight*massw)
									QCDbkgEW2Dup.Fill(wjet.Eta(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgEW2Ddown.Fill(wjet.Eta(),(tagrate2d-tagrate2derr)*weight*massw)

									QCDbkgPT2D.Fill(tjet.Perp(),tagrate2d*weight*massw)
									QCDbkgPT2Dup.Fill(tjet.Perp(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgPT2Ddown.Fill(tjet.Perp(),(tagrate2d-tagrate2derr)*weight*massw)

									QCDbkgPW2D.Fill(wjet.Perp(),tagrate2d*weight*massw)
									QCDbkgPW2Dup.Fill(wjet.Perp(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgPW2Ddown.Fill(wjet.Perp(),(tagrate2d-tagrate2derr)*weight*massw)

									QCDbkgPTW2D.Fill((tjet+wjet).Perp(),tagrate2d*weight*massw)
									QCDbkgPTW2Dup.Fill((tjet+wjet).Perp(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgPTW2Ddown.Fill((tjet+wjet).Perp(),(tagrate2d-tagrate2derr)*weight*massw)

									QCDbkgPhT2D.Fill(tjet.Phi(),tagrate2d*weight*massw)
									QCDbkgPhT2Dup.Fill(tjet.Phi(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgPT2Ddown.Fill(tjet.Phi(),(tagrate2d-tagrate2derr)*weight*massw)	

									QCDbkgPhW2D.Fill(wjet.Phi(),tagrate2d*weight*massw)
									QCDbkgPhW2Dup.Fill(wjet.Phi(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgPhW2Ddown.Fill(wjet.Phi(),(tagrate2d-tagrate2derr)*weight*massw)

									QCDbkgdPhi2D.Fill(abs(tjet.Phi()-wjet.Phi()),tagrate2d*weight*massw)
									QCDbkgdPhi2Dup.Fill(abs(tjet.Phi()-wjet.Phi()),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgdPhi2Ddown.Fill(abs(tjet.Phi()-wjet.Phi()),(tagrate2d-tagrate2derr)*weight*massw)

									if tjet.Perp() > 500:
										QCDbkgMt2D.Fill(tjet.M(),tagrate2d*weight*massw)
										QCDbkgMt2Dup.Fill(tjet.M(),(tagrate2d+tagrate2derr)*weight*massw)
										QCDbkgMt2Ddown.Fill(tjet.M(),(tagrate2d-tagrate2derr)*weight*massw)

								if (eta2_cut) and not FullTop:
									eta2Count += 1
									xbin = TagPlot2de2.GetXaxis().FindBin(tjet.Perp())
									ybin = TagPlot2de2.GetYaxis().FindBin(MtopW)
									tagrate2d = TagPlot2de2.GetBinContent(xbin,ybin)
									tagrate2derr = TagPlot2de2.GetBinError(xbin,ybin)
									QCDbkg2D.Fill(MtopW,tagrate2d*weight*massw)
									QCDbkg2Dup.Fill(MtopW,(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkg2Ddown.Fill(MtopW,(tagrate2d-tagrate2derr)*weight*massw)	
			
									Mtw_cut8.Fill(MtopW,weight)
									QCDbkgET2D.Fill(tjet.Eta(),tagrate2d*weight*massw)
									QCDbkgET2Dup.Fill(tjet.Eta(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgET2Ddown.Fill(tjet.Eta(),(tagrate2d-tagrate2derr)*weight*massw)

									QCDbkgEW2D.Fill(wjet.Eta(),tagrate2d*weight*massw)
									QCDbkgEW2Dup.Fill(wjet.Eta(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgEW2Ddown.Fill(wjet.Eta(),(tagrate2d-tagrate2derr)*weight*massw)

									QCDbkgPT2D.Fill(tjet.Perp(),tagrate2d*weight*massw)
									QCDbkgPT2Dup.Fill(tjet.Perp(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgPT2Ddown.Fill(tjet.Perp(),(tagrate2d-tagrate2derr)*weight*massw)

									QCDbkgPW2D.Fill(wjet.Perp(),tagrate2d*weight*massw)
									QCDbkgPW2Dup.Fill(wjet.Perp(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgPW2Ddown.Fill(wjet.Perp(),(tagrate2d-tagrate2derr)*weight*massw)

									QCDbkgPTW2D.Fill((tjet+wjet).Perp(),tagrate2d*weight*massw)
									QCDbkgPTW2Dup.Fill((tjet+wjet).Perp(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgPTW2Ddown.Fill((tjet+wjet).Perp(),(tagrate2d-tagrate2derr)*weight*massw)

									QCDbkgPhT2D.Fill(tjet.Phi(),tagrate2d*weight*massw)
									QCDbkgPhT2Dup.Fill(tjet.Phi(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgPT2Ddown.Fill(tjet.Phi(),(tagrate2d-tagrate2derr)*weight*massw)	

									QCDbkgPhW2D.Fill(wjet.Phi(),tagrate2d*weight*massw)
									QCDbkgPhW2Dup.Fill(wjet.Phi(),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgPhW2Ddown.Fill(wjet.Phi(),(tagrate2d-tagrate2derr)*weight*massw)

									QCDbkgdPhi2D.Fill(abs(tjet.Phi()-wjet.Phi()),tagrate2d*weight*massw)
									QCDbkgdPhi2Dup.Fill(abs(tjet.Phi()-wjet.Phi()),(tagrate2d+tagrate2derr)*weight*massw)
									QCDbkgdPhi2Ddown.Fill(abs(tjet.Phi()-wjet.Phi()),(tagrate2d-tagrate2derr)*weight*massw)

									if tjet.Perp():
										QCDbkgMt2D.Fill(wjet.M(),tagrate2d*weight*massw)
										QCDbkgMt2Dup.Fill(wjet.M(),(tagrate2d+tagrate2derr)*weight*massw)
										QCDbkgMt2Ddown.Fill(wjet.M(),(tagrate2d-tagrate2derr)*weight*massw)

								fillSpec = [MtopW, tjet.Eta(), wjet.Eta(), tjet.Perp(), wjet.Perp(), tjet.Perp()+wjet.Perp(), tjet.Phi(), wjet.Phi(), abs(tjet.Phi()-wjet.Phi()), wVals['SDmass']]

								arr_count = 0
								for spec in fillSpec:
									for ifit in range(0,len(fittitles)):
										tempweight = bkg_weight_pt(tjet,fits[ifit],eta_regions)
										QCDbkg_ARR[arr_count].Fill(spec,tempweight*weight*massw) 
										arr_count+=1

								preAntiTag.Fill(MtopW,weight*massw)
								if not FullTop:
									# if eta1_cut:
									# 	pt_bin = TagPlote1.GetXaxis().FindBin(tjet.Perp())
									# 	TTRweight = TagPlote1.GetBinContent(pt_bin)
									# 	TTRweightsigsq = TagPlote1.GetBinError(pt_bin)
					
									# elif eta2_cut:
									# 	pt_bin = TagPlote2.GetXaxis().FindBin(tjet.Perp())
									# 	TTRweight = TagPlote2.GetBinContent(pt_bin)
									# 	TTRweightsigsq = TagPlote2.GetBinError(pt_bin)
										
									# TTRweighterrup = TTRweight+sqrt(TTRweightsigsq)
									# TTRweighterrdown = TTRweight-sqrt(TTRweightsigsq)
									
									QCDbkg.Fill(MtopW,TTRweight*weight*massw)
									QCDbkgh.Fill(MtopW,TTRweighterrup*weight*massw)
									QCDbkgl.Fill(MtopW,TTRweighterrdown*weight*massw)

									QCDbkgMwStack.Fill(wjet.M(),TTRweight*weight*massw)

									QCDbkgET.Fill(tjet.Eta(),TTRweight*weight*massw)
									QCDbkgETh.Fill(tjet.Eta(),TTRweighterrup*weight*massw)
									QCDbkgETl.Fill(tjet.Eta(),TTRweighterrdown*weight*massw)

									QCDbkgEW.Fill(wjet.Eta(),TTRweight*weight*massw)
									QCDbkgEWh.Fill(wjet.Eta(),TTRweighterrup*weight*massw)
									QCDbkgEWl.Fill(wjet.Eta(),TTRweighterrdown*weight*massw)

									QCDbkgPT.Fill(tjet.Perp(),TTRweight*weight*massw)
									QCDbkgPTh.Fill(tjet.Perp(),TTRweighterrup*weight*massw)
									QCDbkgPTl.Fill(tjet.Perp(),TTRweighterrdown*weight*massw)

									QCDbkgPW.Fill(wjet.Perp(),TTRweight*weight*massw)
									QCDbkgPWh.Fill(wjet.Perp(),TTRweighterrup*weight*massw)
									QCDbkgPWl.Fill(wjet.Perp(),TTRweighterrdown*weight*massw)

									QCDbkgPTW.Fill((tjet+wjet).Perp(),TTRweight*weight*massw)
									QCDbkgPTWh.Fill((tjet+wjet).Perp(),TTRweighterrup*weight*massw)
									QCDbkgPTWl.Fill((tjet+wjet).Perp(),TTRweighterrdown*weight*massw)

									QCDbkgPhT.Fill(tjet.Phi(),TTRweight*weight*massw)
									QCDbkgPhTh.Fill(tjet.Phi(),TTRweighterrup*weight*massw)
									QCDbkgPhTl.Fill(tjet.Phi(),TTRweighterrdown*weight*massw)

									QCDbkgPhW.Fill(wjet.Phi(),TTRweight*weight*massw)
									QCDbkgPhWh.Fill(wjet.Phi(),TTRweighterrup*weight*massw)
									QCDbkgPhWl.Fill(wjet.Phi(),TTRweighterrdown*weight*massw)

									QCDbkgdPhi.Fill(abs(tjet.Phi()-wjet.Phi()),TTRweight*weight*massw)  
									QCDbkgdPhih.Fill(abs(tjet.Phi()-wjet.Phi()),TTRweighterrup*weight*massw)
									QCDbkgdPhil.Fill(abs(tjet.Phi()-wjet.Phi()),TTRweighterrdown*weight*massw)

									if tjet.Perp() > 500:
										QCDbkgMt.Fill(tjet.M(),TTRweight*weight*massw)
										QCDbkgMth.Fill(tjet.M(),TTRweighterrup*weight*massw)
										QCDbkgMtl.Fill(tjet.M(),TTRweighterrdown*weight*massw)

								if sjbtag_cut:
									Mtw_cut9.Fill(MtopW,weight)
									# Grab the pass/fail ratio at the last second for efficiency
									if tau32_cut:
										Mtw_cut10.Fill(MtopW,weight)
							  				        	
								if FullTop:
										#if ((MtopW)>2400):
										#	goodEvents.append( [ tree.object().id().run(), tree.object().id().luminosityBlock(), tree.object().id().event(),  ] )
										Mtw.Fill((wjet+tjet).M(),weight) 

										MwStack.Fill(wjet.M(),weight)

										Mtwtrigup.Fill(MtopW,weighttrigup)
										Mtwtrigdown.Fill(MtopW,weighttrigdown)
										MtwWup.Fill(MtopW,weightSFwup) 
										MtwWdown.Fill(MtopW,weightSFwdown)

										MtwTptup.Fill(MtopW,weightSFptup)
										MtwTptdown.Fill(MtopW,weightSFptdown) 

										MtwExtrapUp.Fill(MtopW,extrapUp)
										MtwExtrapDown.Fill(MtopW,extrapDown)

										EtaTop.Fill(tjet.Eta(),weight)
										EtaW.Fill(wjet.Eta(),weight)
										
										PtTop.Fill(tjet.Perp(),weight)
										PtW.Fill(wjet.Perp(),weight)
										PtTopW.Fill((tjet+wjet).Perp(),weight)
		
										
										PhiTop.Fill(tjet.Phi(),weight)
										PhiW.Fill(wjet.Phi(),weight)
										dPhi.Fill(abs(tjet.Phi()-wjet.Phi()),weight)

										if tjet.Perp() > 500:
											Mt.Fill(tjet.M(),weight)

										temp_variables = {	"wpt":wjet.Perp(),
															"wmass":wVals["SDmass"],
															"tpt":tjet.Perp(),
															"tmass":tVals["SDmass"],
															"tau32":tau32val,
															"tau21":tau21val,
															"sjbtag":SJ_csvval,
															"flavor":tVals["flavor"],
															"weight":weight}

										for tv in tree_vars.keys():
											tree_vars[tv][0] = temp_variables[tv]
										NewTree.Fill()
										
										doneAlready = True

# ---------------------- Now for Alphabet ----------------------------------------
							elif options.Alphabet == "on":
								eta_cut = eta[0]<=abs(tjet.Eta())<eta[1]
								massw = 1
								masswHist.Fill(massw)
								
								if sjbtag_cut:
									Mtw_cut9.Fill(MtopW,weight)
									# Grab the pass/fail ratio at the last second for efficiency
									TTRweight = bkg_weight_mass(tjetTTR,eta)
									TTRweighterrup = bkg_weight_mass(tjet,TTR_errUp,eta)
									TTRweighterrdown = bkg_weight_mass(tjet,TTR_errDown,eta)

									if not tau32_cut:
									# Start generating the QCD estimate using the pass/fail ratio 
									# on events that fail the tau32 cut
										fillSpec = [MtopW, tjet.Eta(), wjet.Eta(), tjet.Perp(), wjet.Perp(), tjet.Perp()+wjet.Perp(), tjet.Phi(), wjet.Phi(), abs(tjet.Phi()-wjet.Phi())]
		
										arr_count = 0
										for spec in fillSpec:
											for ifit in range(0,len(fittitles)):
												tempweight = bkg_weight_mass(tjet,fits[ifit],eta)
												QCDbkg_ARR[arr_count].Fill(spec,tempweight*weight*massw) 
												arr_count+=1
		
										QCDbkg.Fill(MtopW,TTRweight*weight*massw)
										QCDbkgh.Fill(MtopW,TTRweighterrup*weight*massw)
										QCDbkgl.Fill(MtopW,TTRweighterrdown*weight*massw)

										QCDbkgMwStack.Fill(wVals["SDmass"],TTRweight*weight*massw)

										QCDbkgET.Fill(tjet.Eta(),TTRweight*weight*massw)
										QCDbkgETh.Fill(tjet.Eta(),TTRweighterrup*weight*massw)
										QCDbkgETl.Fill(tjet.Eta(),TTRweighterrdown*weight*massw)

										QCDbkgEW.Fill(wjet.Eta(),TTRweight*weight*massw)
										QCDbkgEWh.Fill(wjet.Eta(),TTRweighterrup*weight*massw)
										QCDbkgEWl.Fill(wjet.Eta(),TTRweighterrdown*weight*massw)

										QCDbkgPT.Fill(tjet.Perp(),TTRweight*weight*massw)
										QCDbkgPTh.Fill(tjet.Perp(),TTRweighterrup*weight*massw)
										QCDbkgPTl.Fill(tjet.Perp(),TTRweighterrdown*weight*massw)

										QCDbkgPW.Fill(wjet.Perp(),TTRweight*weight*massw)
										QCDbkgPWh.Fill(wjet.Perp(),TTRweighterrup*weight*massw)
										QCDbkgPWl.Fill(wjet.Perp(),TTRweighterrdown*weight*massw)

										QCDbkgPTW.Fill((tjet.Perp()+wjet.Perp()),TTRweight*weight*massw)
										QCDbkgPTWh.Fill((tjet.Perp()+wjet.Perp()),TTRweighterrup*weight*massw)
										QCDbkgPTWl.Fill((tjet.Perp()+wjet.Perp()),TTRweighterrdown*weight*massw)

										QCDbkgPhT.Fill(tjet.Phi(),TTRweight*weight*massw)
										QCDbkgPhTh.Fill(tjet.Phi(),TTRweighterrup*weight*massw)
										QCDbkgPhTl.Fill(tjet.Phi(),TTRweighterrdown*weight*massw)

										QCDbkgPhW.Fill(wjet.Phi(),TTRweight*weight*massw)
										QCDbkgPhWh.Fill(wjet.Phi(),TTRweighterrup*weight*massw)
										QCDbkgPhWl.Fill(wjet.Phi(),TTRweighterrdown*weight*massw)

										QCDbkgdPhi.Fill(abs(tjet.Phi()-wjet.Phi()),TTRweight*weight*massw)  
										QCDbkgdPhih.Fill(abs(tjet.Phi()-wjet.Phi()),TTRweighterrup*weight*massw)
										QCDbkgdPhil.Fill(abs(tjet.Phi()-wjet.Phi()),TTRweighterrdown*weight*massw)

									if tau32_cut:
										Mtw_cut10.Fill(MtopW,weight)
														
										# if (MtopW>2400):
										#	goodEvents.append( [ tree.object().id().run(), tree.object().id().luminosityBlock(), tree.object().id().event(),  ] )
										Mtw.Fill(MtopW,weight) 

										MwStack.Fill(tjet.M(),weight)

										Mtwtrigup.Fill(MtopW,weighttrigup)
										Mtwtrigdown.Fill(MtopW,weighttrigdown)
										MtwWup.Fill(MtopW,weightSFwup) 
										MtwWdown.Fill(MtopW,weightSFwdown) 

										EtaTop.Fill(tjet.Eta(),weight)
										EtaW.Fill(wjet.Eta(),weight)
									
										PtTop.Fill(tjet.Perp(),weight)
										PtW.Fill(wjet.Perp(),weight)
										PtTopW.Fill((tjet+wjet).Perp(),weight)

									
										PhiTop.Fill(tjet.Phi(),weight)
										PhiW.Fill(wjet.Phi(),weight)
										dPhi.Fill(abs(tjet.Phi()-wjet.Phi()),weight)

										temp_variables = {"wpt":wjet.Perp(),
												"wmass":wVals["SDmass"],
												"tpt":tjet.Perp(),
												"tmass":tVals["SDmass"],
												"tau32":tau32val,
												"tau21":tau21val,
												"sjbtag":SJ_csvval,
												"flavor":tVals["flavor"],
												"weight":weight }


										for tv in tree_vars.keys():
											tree_vars[tv][0] = temp_variables[tv]
										NewTree.Fill()

hEta1Count.SetBinContent(1,eta1Count)
hEta2Count.SetBinContent(1,eta2Count)
hmatchingFailed.SetBinContent(1,float(matchingFailed/count))

print "fraction of events that failed matching: " + str(float(matchingFailed/count))

f.cd()
f.Write()
f.Close()

print "number of events: " + str(count)



# if options.printEvents:
# 	Outf1   =   open("DataEvents"+options.num+".txt", "w")
# 	sys.stdout = Outf1
# 	for goodEvent in goodEvents :
# 		print '{0:12.0f}:{1:12.0f}:{2:12.0f}'.format(
# 			goodEvent[0], goodEvent[1], goodEvent[2]
# 		)
