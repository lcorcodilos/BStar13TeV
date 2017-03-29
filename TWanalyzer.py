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
parser.add_option('-y', '--modmass', metavar='F', type='string', action='store',
                  default	=	'nominal',
                  dest		=	'modmass',
                  help		=	'nominal up or down')
parser.add_option('-j', '--jobs', metavar='F', type='string', action='store',
                  default	=	'1',
                  dest		=	'jobs',
                  help		=	'number of jobs')
parser.add_option('-t', '--tname', metavar='F', type='string', action='store',
                   default	=	'HLT_PFHT800_v3',
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
parser.add_option('--printEvents', metavar='F', action='store_true',
                  default=False,
                  dest='printEvents',
                  help='Print events that pass selection (run:lumi:event)')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-v', '--var', metavar='F', type='string', action='store',
                  default       =       'analyzer',
                  dest          =       'var',
                  help          =       'anaylzer or kinematics')
parser.add_option('-b', '--bx', metavar='F', type='string', action='store',
                   default	=	'25ns',
                   dest		=	'bx',
                   help		=	'bunch crossing 50ns or 25ns')
parser.add_option('-a', '--bprime', metavar='F', action='store_true',
		  default	=	True,
                  dest		=	'bprime',
                  help		=	'True if running bprime. False if running bstar.')
parser.add_option('-S', '--split', metavar='F', type='string', action='store',
                  default	=	'file',
                  dest		=	'split',
                  help		=	'split by event of file')
         


(options, args) = parser.parse_args()

if (options.set.find('QCD') != -1):
	setstr = 'QCD'
else:
	setstr = 'Data'

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
#trig='none'
#if options.set!= 'data' and options.tname!='none': 
# 	if options.tname=='HLT_PFHT800_v2ORHLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p45_v3':
# 		trig = 'nominal'
# 	elif options.tname!= []:
# 		trig = 'tnamestr'
 		
if tnamestr=='HLT_PFHT800_v3':
	tnameformat='nominal'
elif tnamestr=='':
	tnameformat='none'
else:
	tnameformat=tnamestr
 		
pie = math.pi 

#Load up cut values based on what selection we want to run 
Cuts = LoadCuts(options.cuts)
wpt = Cuts['wpt']
tpt = Cuts['tpt']
dy = Cuts['dy']
tmass = Cuts['tmass']
nsubjets = Cuts['nsubjets']
tau32 = Cuts['tau32']
tau21 = Cuts['tau21']
minmass = Cuts['minmass']
sjbtag = Cuts['sjbtag']
wmass = Cuts['wmass']
eta1 = Cuts['eta1']
eta2 = Cuts['eta2']

Cons = LoadConstants()
lumi = Cons['lumi']
Lumi = str(lumi/1000)+'fb'


#For large datasets we need to parallelize the processing
jobs=int(options.jobs)
if jobs != 1:
	num=int(options.num)
	jobs=int(options.jobs)
	print "Running over " +str(jobs)+ " jobs"
	print "This will process job " +str(num)
else:
	print "Running over all events"

#This section defines some strings that are used in naming the optput files
mod = ''
post = ''
if options.JES!='nominal':
	mod = mod + 'JES_' + options.JES
	post='jes'+options.JES
if options.JER!='nominal':
	mod = mod + 'JER_' + options.JER
	post='jer'+options.JER


pstr = ""
if options.pdfweights!="nominal":
	print "using pdf uncertainty"
	pstr = "_pdf_"+options.pdfset+"_"+options.pdfweights

pustr = ""
if options.pileup=='off':
	pustr = "pileup_unweighted"
if options.pileup=='up':
	pustr = "pileup_up"
if options.pileup=='down':
	pustr = "pileup_down"
mod = mod+pustr
if mod == '':
	mod = options.modulesuffix

print "mod = " + mod

mmstr = ""
if options.modmass!="nominal":
	print "using modm uncertainty"
	mmstr = "_modm_"+options.modmass



#Based on what set we want to analyze, we find all Ntuple root files 

files = Load_Ntuples(options.set,di)

if (options.set.find('ttbar') != -1) or (options.set.find('singletop') != -1):
	settype = 'ttbar'
elif (options.set.find('QCD') != -1):
	settype ='ttbar'
	run_b_SF = False
else :
	
	settype = options.set

print 'The type of set is ' + settype

#CHANGE BACK
ModFile = ROOT.TFile(di+"ModMassFile_rate_"+options.cuts+".root")
ModPlot = ModFile.Get("rtmass")

#ModFile = ROOT.TFile(di+"ModMassFile_"+options.cuts+".root")
#ModPlot = ModFile.Get("rtmass")


if options.set != 'data':
	#Load up scale factors (to be used for MC only)

	TrigFile = TFile(di+"Triggerweight_data80X.root")
	TrigPlot = TrigFile.Get("TriggerWeight_"+tnamestr+"_pre_HLT_PFHT475_v3")



	PileFile = TFile(di+"PileUp_Ratio_"+settype+".root")
	if options.pileup=='up':
		PilePlot = PileFile.Get("Pileup_Ratio_up")
	elif options.pileup=='down':
		PilePlot = PileFile.Get("Pileup_Ratio_down")
	else:	
		PilePlot = PileFile.Get("Pileup_Ratio")

# We select all the events:    
events = Events (files)


#For event counting
jobiter = 0
splitfiles = []

if jobs != 1 and options.split=="file":
    for ifile in range(1,len(files)+1):
    	if (ifile-1) % jobs == 0:
		jobiter+=1
	count_index = ifile  - (jobiter-1)*jobs
	if count_index==num:
		splitfiles.append(files[ifile-1])

    events = Events(splitfiles)
    runs = Runs(splitfiles)

if options.split=="event" or jobs == 1:	  
	events = Events(files)
    	runs = Runs(files)

totnev = 0

nevHandle 	= 	Handle (  "vector<int> "  )
nevLabel  	= 	( "counter" , "nevr")

for run in runs:

		run.getByLabel (nevLabel,nevHandle )
    		nev 		= 	nevHandle.product() 
		
		totnev+=nev[0]
print "Total unfiltered events in selection: ",totnev

#Load up AK4 handles and labels for b-tagging later
AK4HL = Initlv("jetsAK4",post)
BDiscAK4Handle 	= 	Handle (  "vector<float> "  )
BDiscAK4Label  	= 	( "jetsAK4" , "jetAK4CSV")
FlavourHandle	=	Handle (  "vector<float> "  )
FlavourLabel	=	( "jetsAK4" , "jetAK4PartonFlavour") 


#Here we load up handles and labels.
#These are used to grab entries from the Ntuples.
#To see all the current types in an Ntuple use edmDumpEventContent /PathtoNtuple/Ntuple.root
AK8HL = Initlv("jetsAK8",post)

GeneratorHandle 	= 	Handle (  "GenEventInfoProduct")
GeneratorLabel  	= 	( "generator" , "")

puHandle    	= 	Handle("int")
puLabel     	= 	( "eventUserData", "puNtrueInt" )

#minmassHandle 	= 	Handle (  "vector<float> "  )
#minmassLabel  	= 	( "jetsAK8" , "jetAK8minmass")

#nSubjetsHandle 	= 	Handle (  "vector<float> "  )
#nSubjetsLabel  	= 	( "jetsAK8" , "jetAK8nSubJets")

# for top mass
softDropPuppiMassHandle		=	Handle (  "vector<float> "  )
softDropPuppiMassLabel		=	( "jetsAK8" , "jetAK8PuppiCorrectedsoftDropMass")

vsubjets0indexHandle 	= 	Handle (  "vector<float> "  )
vsubjets0indexLabel  	= 	( "jetsAK8" , "jetAK8PuppivSubjetIndex0")

vsubjets1indexHandle 	= 	Handle (  "vector<float> "  )
vsubjets1indexLabel  	= 	( "jetsAK8" , "jetAK8PuppivSubjetIndex1")

subjetsAK8CSVHandle 	= 	Handle (  "vector<float> "  )
subjetsAK8CSVLabel  	= 	( "subjetsAK8Puppi" , "subjetAK8PuppiCSVv2")

tau1Handle 	= 	Handle (  "vector<float> "  )
tau1Label  	= 	( "jetsAK8" , "jetAK8Puppitau1")

tau2Handle 	= 	Handle (  "vector<float> "  )
tau2Label  	= 	( "jetsAK8" , "jetAK8Puppitau2")

tau3Handle 	= 	Handle (  "vector<float> "  )
tau3Label  	= 	( "jetsAK8" , "jetAK8Puppitau3")

#subjetsCSVHandle 	= 	Handle (  "vector<float> "  )
#subjetsCSVLabel  	= 	( "subjetsCmsTopTag" , "subjetCmsTopTagCSV")

#subjets0indexHandle 	= 	Handle (  "vector<float> "  )
#subjets0indexLabel  	= 	( "jetsAK8" , "jetAK8topSubjetIndex0")

#subjets1indexHandle 	= 	Handle (  "vector<float> "  )
#subjets1indexLabel  	= 	( "jetsAK8" , "jetAK8topSubjetIndex1")

#subjets2indexHandle 	= 	Handle (  "vector<float> "  )
#subjets2indexLabel  	= 	( "jetsAK8" , "jetAK8topSubjetIndex2")

#subjets3indexHandle 	= 	Handle (  "vector<float> "  )
#subjets3indexLabel  	= 	( "jetsAK8" , "jetAK8topSubjetIndex3")

HT800Handle	=	Handle ( "vector<bool>" )
HT800Label	=	( "Filter" , "HT800bit" )

#---------------------------------------------------------------------------------------------------------------------#
var = ""
if options.var == "kinematics":
	var = "_kin"



if jobs != 1:
	f = TFile( "TWanalyzer"+options.set+"_Trigger_"+tnameformat+"_"+mod+pstr+mmstr+"_job"+options.num+"of"+options.jobs+"_PSET_"+options.cuts+var+".root", "recreate" )
else:
	f = TFile( "TWanalyzer"+options.set+"_Trigger_"+tnameformat+"_"+mod+pstr+mmstr+"_PSET_"+options.cuts+var+".root", "recreate" )

#Load up the average b-tagging rates -- Takes parameters from text file and makes a function
#CHANGE BACK
TTR = TTR_Init('Bifpoly','rate_'+options.cuts,setstr,di)
TTR_err = TTR_Init('Bifpoly_err','rate_'+options.cuts,setstr,di)
fittitles = ["pol0","pol2","pol3","FIT","Bifpoly","expofit"]
fits = []
for fittitle in fittitles:
	fits.append(TTR_Init(fittitle,'rate_'+options.cuts,setstr,di))
#CHANGE BACK
#TTR = TTR_Init('Bifpoly',options.cuts,setstr,di)
#TTR_err = TTR_Init('Bifpoly_err',options.cuts,setstr,di)
#fittitles = ["pol0","pol2","pol3","FIT","Bifpoly","expofit"]
#fits = []
#for fittitle in fittitles:
#	fits.append(TTR_Init(fittitle,options.cuts,setstr,di))

print "Creating histograms"

#Define Histograms
#CHANGE BACK
TagFile1 = TFile(di+"Tagrate"+setstr+"2D_rate_"+options.cuts+".root")
#TagFile1 = TFile(di+"Tagrate"+setstr+"2D_"+options.cuts+".root")
TagPlot2de1= TagFile1.Get("tagrateeta1")
TagPlot2de2= TagFile1.Get("tagrateeta2")


f.cd()
#---------------------------------------------------------------------------------------------------------------------#
Mtw	    = TH1F("Mtw",     "mass of tw",     	  	      140, 500, 4000 )

nev = TH1F("nev",	"nev",		1, 0, 1 )

Mtwtrigup	= TH1F("Mtwtrigup",	"mass of tw trig up",     	  	140, 500, 4000 )
Mtwtrigdown	= TH1F("Mtwtrigdown",	"mass of tw trig up",     	  	140, 500, 4000 )

MtwTup		= TH1F("MtwTup",	"mass of tw top tag SF up",     	  	140, 500, 4000 )
MtwTdown	= TH1F("MtwTdown",	"mass of tw top tag SF down",     	  	140, 500, 4000 )

Nevents	    = TH1F("Nevents",     	  "mass of tb",     	  	         5, 0., 5. )
QCDbkg= TH1F("QCDbkg",     "QCD background estimate",     	  	      140, 500, 4000 )
QCDbkgh= TH1F("QCDbkgh",     "QCD background estimate up error",     	  	      140, 500, 4000 )
QCDbkgl= TH1F("QCDbkgl",     "QCD background estimate down error",     	  	      140, 500, 4000 )
QCDbkg2D= TH1F("QCDbkg2D",     "QCD background estimate 2d error",     	  	      140, 500, 4000 )
QCDbkg2Dup= TH1F("QCDbkg2Dup",     "QCD background estimate 2d error",     	  	      140, 500, 4000 )
QCDbkg2Ddown= TH1F("QCDbkg2Ddown",     "QCD background estimate 2d error",     	  	      140, 500, 4000 )

MtStack		= TH1F("MtStack",	"top candidate mass for stack",		100,   0, 500 )
QCDbkgMtStack	= TH1F("QCDbkgMtStack", "QCD background for top mass",		100, 0, 500 )

masswHist = TH1F("Massw", "Massw", 25,  0, 5 )
masswHist.Sumw2()

Mtw.Sumw2()

Mtwtrigup.Sumw2()
Mtwtrigdown.Sumw2()

MtwTup.Sumw2()
MtwTdown.Sumw2()

QCDbkg.Sumw2()
QCDbkgh.Sumw2()
QCDbkgl.Sumw2()

MtStack.Sumw2()
QCDbkgMtStack.Sumw2()


if options.var == "kinematics":
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
	#Mtw_cut11   = TH1F("Mtw_cut11", "mass of tw after nsubjets cut", 140, 500, 4000)
	#Mtw_cut12   = TH1F("Mtw_cut12", "mass of tw after minmass cut", 140, 500, 4000)

	EtaTop      = TH1F("EtaTop",        "Top Candidate eta",     	  	      12, -2.4, 2.4 )
	EtaW   = TH1F("EtaW",     "W Candidate eta",     	      12, -2.4, 2.4 )

	PtTop       = TH1F("PtTop",       	"Top Candidate pt (GeV)",     	      50, 450, 1500 )
	PtW    	    = TH1F("PtW",     		"W Candidate pt (GeV)",     	      50, 370, 1430 )
	PtTopW      = TH1F("PtTopW",  		"pt of tw system",     	  	      35,   0, 700 )

	PhiTop    = TH1F("PhiTop",      "Top Candidate Phi (rad)",     	  	             12, -pie, pie )
	PhiW 	  = TH1F("PhiW",   	"Top Candidate Phi (rad)",     	  	             12, -pie, pie )
	dPhi      = TH1F("dPhi",        "delta theat between Top and W Candidates",    	     12, 2.2, pie )

	#NSubJets 	= TH1F("NSubJets",	"Number of Subjets",			6,0,6)
	#MinMass 	= TH1F("MinPairMass",	"Minimum pairwise mass",		6,0,120)
	TopMass		= TH1F("TopMass",	"Top mass",				10,0,500)
	Nsubjetiness	= TH1F("Nsubjetiness",	"Nsubjetiness",				8,0,1.6)
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
	QCDbkgET2D= TH1F("QCDbkgET2D",     "QCD background estimate 2d error",     	  	      12, -2.4, 2.4 )
	QCDbkgET2Dup= TH1F("QCDbkgET2Dup",     "QCD background estimate 2d error",     	  	      12, -2.4, 2.4 )
	QCDbkgET2Ddown= TH1F("QCDbkgET2Ddown",     "QCD background estimate 2d error",     	  	      12, -2.4, 2.4 )
	
	QCDbkgEW	= TH1F("QCDbkgEW",       "QCD background estimate eta w",       	     12, -2.4, 2.4 )
	QCDbkgEWh= TH1F("QCDbkgEWh",     "QCD background estimate up error",     	  	      12, -2.4, 2.4 )
	QCDbkgEWl= TH1F("QCDbkgEWl",     "QCD background estimate down error",     	  	      12, -2.4, 2.4 )
	QCDbkgEW2D= TH1F("QCDbkgEW2D",     "QCD background estimate 2d error",     	  	      12, -2.4, 2.4 )
	QCDbkgEW2Dup= TH1F("QCDbkgEW2Dup",     "QCD background estimate 2d error",     	  	      12, -2.4, 2.4 )
	QCDbkgEW2Ddown= TH1F("QCDbkgEW2Ddown",     "QCD background estimate 2d error",     	  	      12, -2.4, 2.4 )
	
	QCDbkgPT	= TH1F("QCDbkgPT",       "QCD background estimate pt top",     	  	     50, 450, 1500 )
	QCDbkgPTh= TH1F("QCDbkgPTh",     "QCD background estimate up error",     	  	      50, 450, 1500 )
	QCDbkgPTl= TH1F("QCDbkgPTl",     "QCD background estimate down error",     	  	      50, 450, 1500 )
	QCDbkgPT2D= TH1F("QCDbkgPT2D",     "QCD background estimate 2d error",     	  	      50, 450, 1500 )
	QCDbkgPT2Dup= TH1F("QCDbkgPT2Dup",     "QCD background estimate 2d error",     	  	      50, 450, 1500 )
	QCDbkgPT2Ddown= TH1F("QCDbkgPT2Ddown",     "QCD background estimate 2d error",     	  	      50, 450, 1500 )
	
	QCDbkgPW	= TH1F("QCDbkgPW",       "QCD background estimate pt W",       	 	     50, 370, 1430 )
	QCDbkgPWh= TH1F("QCDbkgPWh",     "QCD background estimate up error",     	  	      50, 370, 1430 )
	QCDbkgPWl= TH1F("QCDbkgPWl",     "QCD background estimate down error",     	  	      50, 370, 1430 )
	QCDbkgPW2D= TH1F("QCDbkgPW2D",     "QCD background estimate 2d error",     	  	      50, 370, 1430 )
	QCDbkgPW2Dup= TH1F("QCDbkgPW2Dup",     "QCD background estimate 2d error",     	  	      50, 370, 1430 )
	QCDbkgPW2Ddown= TH1F("QCDbkgPW2Ddown",     "QCD background estimate 2d error",     	  	      50, 370, 1430 )
	
	QCDbkgPTW	= TH1F("QCDbkgPTW",      "QCD background estimate pt top+w",     	     35,   0, 700  )
	QCDbkgPTWh= TH1F("QCDbkgPTWh",     "QCD background estimate up error",     	  	      35,   0, 700 )
	QCDbkgPTWl= TH1F("QCDbkgPTWl",     "QCD background estimate down error",     	  	      35,   0, 700 )
	QCDbkgPTW2D= TH1F("QCDbkgPTW2D",     "QCD background estimate 2d error",     	  	      35,   0, 700 )
	QCDbkgPTW2Dup= TH1F("QCDbkgPTW2Dup",     "QCD background estimate 2d error",     	  	      35,   0, 700 )
	QCDbkgPTW2Ddown= TH1F("QCDbkgPTW2Ddown",     "QCD background estimate 2d error",     	  	      35,   0, 700 )
	
	QCDbkgPhT	= TH1F("QCDbkgPhT",      "QCD background estimate phi top",       	     12, -pie, pie )
	QCDbkgPhTh= TH1F("QCDbkgPhTh",     "QCD background estimate up error",     	  	      12, -pie, pie )
	QCDbkgPhTl= TH1F("QCDbkgPhTl",     "QCD background estimate down error",     	  	      12, -pie, pie )
	QCDbkgPhT2D= TH1F("QCDbkgPhT2D",     "QCD background estimate 2d error",     	  	      12, -pie, pie )
	QCDbkgPhT2Dup= TH1F("QCDbkgPhT2Dup",     "QCD background estimate 2d error",     	  	      12, -pie, pie )
	QCDbkgPhT2Ddown= TH1F("QCDbkgPhT2Ddown",     "QCD background estimate 2d error",     	  	      12, -pie, pie )
	
	QCDbkgPhW	= TH1F("QCDbkgPhW",      "QCD background estimate phi w",     	  	     12, -pie, pie )
	QCDbkgPhWh= TH1F("QCDbkgPhWh",     "QCD background estimate up error",     	  	      12, -pie, pie )
	QCDbkgPhWl= TH1F("QCDbkgPhWl",     "QCD background estimate down error",     	  	      12, -pie, pie )
	QCDbkgPhW2D= TH1F("QCDbkgPhW2D",     "QCD background estimate 2d error",     	  	      12, -pie, pie )
	QCDbkgPhW2Dup= TH1F("QCDbkgPhW2Dup",     "QCD background estimate 2d error",     	  	      12, -pie, pie )
	QCDbkgPhW2Ddown= TH1F("QCDbkgPhW2Ddown",     "QCD background estimate 2d error",     	  	      12, -pie, pie )
	
	QCDbkgdPhi	= TH1F("QCDbkgdPhi",     "QCD background estimate delta phi",       	     12,  2.2, pie )
	QCDbkgdPhih= TH1F("QCDbkgdPhih",     "QCD background estimate up error",     	  	      12, 2.2, pie )
	QCDbkgdPhil= TH1F("QCDbkgdPhil",     "QCD background estimate down error",     	  	      12, 2.2, pie )
	QCDbkgdPhi2D= TH1F("QCDbkgdPhi2D",     "QCD background estimate 2d error",     	  	      12, 2.2, pie )
	QCDbkgdPhi2Dup= TH1F("QCDbkgdPhi2Dup",     "QCD background estimate 2d error",     	  	      12, 2.2, pie )
	QCDbkgdPhi2Ddown= TH1F("QCDbkgdPhi2Ddown",     "QCD background estimate 2d error",     	  	      12, 2.2, pie )
	


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
	#Mtw_cut11.Sumw2()
	#Mtw_cut12.Sumw2()
	
	EtaTop.Sumw2()
	EtaW.Sumw2()
	
	PtTop.Sumw2()
	PtW.Sumw2()
	PtTopW.Sumw2()
	
	PhiTop.Sumw2()
	PhiW.Sumw2()
	dPhi.Sumw2()
	
	#NSubJets.Sumw2()
	#MinPairMass.Sumw2()
	TopMass.Sumw2()
	Nsubjetiness.Sumw2()
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
	
	
QCDbkg_ARR = []
	
kinVars = 	['', 	'ET', 	'EW', 	'PT', 	'PW', 	'PTW', 	'PhT', 	'PhW', 	'dPhi'	]
kinBin = 	[140, 	12, 	12, 	50, 	50,	35,	12,	12,	12	]
kinLow = 	[500, 	-2.4, 	-2.4, 	450, 	370,	0,	-pie,	-pie,	2.2	]
kinHigh = 	[4000, 	2.4, 	2.4, 	1500, 	1430,	700,	pie,	pie,	pie	]

if options.var == 'analyzer':
	iterations = 1
elif options.var == 'kinematics':
	iterations = len(kinVars)
else:
	print "You messed up the var options bozo"
	quit()

arr_count = 0
for iVar in range(0,iterations):
	for ihist in fittitles:
		QCDbkg_ARR.append(TH1F("QCDbkg"+kinVars[iVar]+ihist,     str(kinVars[iVar]) + "in b+1 pt est etabin",    kinBin[iVar], kinLow[iVar], kinHigh[iVar]))
		QCDbkg_ARR[arr_count].Sumw2()
		arr_count += 1

#---------------------------------------------------------------------------------------------------------------------#

# loop over events
#---------------------------------------------------------------------------------------------------------------------#

count = 0
jobiter = 0
print "Start looping"
#initialize the ttree variables
tree_vars = {"wpt":array('d',[0.]),"wmass":array('d',[0.]),"tpt":array('d',[0.]),"tmass":array('d',[0.]),"tau32":array('d',[0.]),"tau21":array('d',[0.]),"sjbtag":array('d',[0.]),"weight":array('d',[0.])}#,"nsubjets":array('d',[0.])
Tree = Make_Trees(tree_vars)

usegenweight = False
#if options.set == "QCDFLAT7000":
#	usegenweight = True
#	print "Using gen weight"

goodEvents = []
totevents = events.size()
#print str(totevents)  +  ' Events total'

nev.SetBinContent(1,totnev)

infoArray=[]
for event in events:
    count	= 	count + 1
    m = 0
    t = 0
  #  if count > 100000:
#	break

    if count % 100000 == 0 :
      print  '--------- Processing Event ' + str(count) +'   -- percent complete ' + str(100*count/totevents) + '% -- '

    #Here we split up event processing based on number of jobs 
    #This is set up to have jobs range from 1 to the total number of jobs (ie dont start at job 0)
    if usegenweight:
		try:
			event.getByLabel (GeneratorLabel, GeneratorHandle)
    			gen 		= 	GeneratorHandle.product()
			Nevents.Fill(0.,gen.weightProduct())
		except:
			continue 
    
    if options.set == 'data':
	event.getByLabel (HT800Label, HT800Handle)
	trigBit = HT800Handle.product()
	if not trigBit:
		continue

    if jobs != 1 and options.split=="event":
    	if (count - 1) % jobs == 0:
		jobiter+=1
	count_index = count - (jobiter-1)*jobs
	if count_index!=num:
		continue 
    # We load up the relevant handles and labels and create collections
    AK8LV = Makelv(AK8HL,event)
#    AK4LV = Makelv(AK4HL,event)
    if len(AK8LV)==0:
	continue
    tindex,windex = Hemispherize(AK8LV,AK8LV)

    wJetsh1 = []
    wJetsh0  =  []
    topJetsh1 = []
    topJetsh0  = []

    for i in range(0,len(windex[1])):
   	wJetsh1.append(AK8LV[windex[1][i]])
    for i in range(0,len(windex[0])):
    	wJetsh0.append(AK8LV[windex[0][i]])
    for i in range(0,len(tindex[1])):
    	topJetsh1.append(AK8LV[tindex[1][i]])
    for i in range(0,len(tindex[0])):
    	topJetsh0.append(AK8LV[tindex[0][i]])

    
    wjh0 = 0
    wjh1 = 0

    tjh0 = 0
    tjh1 = 0

    #Require 1 pt>150 jet in each hemisphere (top jets already have the 150GeV requirement) 
    for wjet in wJetsh0:
	if wjet.Perp() > 200.0:
		wjh0+=1
    for tjet in topJetsh0:
	if tjet.Perp() > 200.0:
		tjh0+=1

    for wjet in wJetsh1:
	if wjet.Perp() > 200.0:
		wjh1+=1

    for tjet in topJetsh1:
	if tjet.Perp() > 200.0:
		tjh1+=1


    njets11w0 	= 	((tjh1 >= 1) and (wjh0 >= 1))
    njets11w1 	= 	((tjh0 >= 1) and (wjh1 >= 1))

    tag = 0

    doneAlready = False
  
    for hemis in ['hemis0','hemis1']:
    	if hemis == 'hemis0'   :
		if not njets11w0:
			continue 
		#The Ntuple entries are ordered in pt, so [0] is the highest pt entry
		#We are calling a candidate b jet (highest pt jet in hemisphere0)  
 		tindexval = tindex[1][0]
 		windexval = windex[0][0]

		wjet = wJetsh0[0]
		tjet = topJetsh1[0]

    	if hemis == 'hemis1' and doneAlready == False :
		if not njets11w1:
			continue 


 		tindexval = tindex[0][0]
 		windexval = windex[1][0]

		wjet = wJetsh1[0]
		tjet = topJetsh0[0]
	
	elif hemis == 'hemis1' and doneAlready == True:
		continue

	if abs(wjet.Eta())>2.40 or abs(tjet.Eta())>2.40:
		continue

    	weight=1.0

	if options.var == "kinematics":
		Mtw_cut1.Fill((tjet+wjet).M(),weight)

    	wpt_cut = wpt[0]<wjet.Perp()<wpt[1]
    	tpt_cut = tpt[0]<tjet.Perp()<tpt[1]
    	dy_cut = dy[0]<=abs(tjet.Rapidity()-wjet.Rapidity())<dy[1]
 	if usegenweight:
 		try:
 			weight*=gen.weightProduct()
 		except:
 			continue 
		
	if wpt_cut:

		if tpt_cut:
			if options.var == "kinematics":
				Mtw_cut2.Fill((tjet+wjet).M(),weight)
				deltaY.Fill(abs(tjet.Rapidity()-wjet.Rapidity()),weight)

			if dy_cut:
				if options.var == "kinematics":
					Mtw_cut3.Fill((tjet+wjet).M(),weight)
		   		if options.pdfweights != "nominal" :
		            		event.getByLabel( pdfLabel, pdfHandle )
		            		pdfs = pdfHandle.product()
					iweight = PDF_Lookup( pdfs , options.pdfweights )
		            		weight *= iweight

				weightSFt = 1.0
				weightSFtdown = 1.0
				weightSFtup = 1.0

				if options.set!="data":

					event.getByLabel (puLabel, puHandle)
		    			PileUp 		= 	puHandle.product()
		               		bin1 = PilePlot.FindBin(PileUp[0]) 

					if options.pileup != 'off':
						weight *= PilePlot.GetBinContent(bin1)

					if options.cuts=="default" and options.set!="QCD":
						#top scale factor reweighting done here
						SFT = SFT_Lookup( tjet.Perp() )
						weightSFt = SFT[0]
						weightSFtdown = SFT[1]
						weightSFtup = SFT[2]

	
				# For W mass
         			#event.getByLabel (PrunedMassLabel, PrunedMassHandle)
         			#prunedJetMass 	= 	PrunedMassHandle.product()

				# For top mass
        			event.getByLabel (softDropPuppiMassLabel, softDropPuppiMassHandle)
		        	puppiJetMass 	= 	softDropPuppiMassHandle.product()


				tmass_cut = tmass[0]<puppiJetMass[tindexval]<tmass[1]
				if options.var == "kinematics":
					TopMass.Fill(puppiJetMass[tindexval],weight)

				if tmass_cut :
					if options.var == "kinematics":
	 					Mtw_cut4.Fill((tjet+wjet).M(),weight)
		         		#event.getByLabel ( nSubjetsLabel , nSubjetsHandle )
		     			#nSubjets 		= 	nSubjetsHandle.product()
		         		#event.getByLabel (minmassLabel, minmassHandle)
		     			#topJetminmass 	= 	minmassHandle.product()
		
					#minmass_cut = minmass[0]<=topJetminmass[tindexval]<minmass[1]

					#nsubjets_cut = nsubjets[0]<=nSubjets[tindexval]<nsubjets[1]

					#if options.var == "kinematics":
					#	NSubJets.Fill(nSubjets[tindexval],weight)
					#	MinMass.Fill(topJetminmass[tindexval],weight)

					ht = tjet.Perp() + wjet.Perp()

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
				
					if options.ptreweight == "on":
						#ttbar pt reweighting done here
						event.getByLabel( GenLabel, GenHandle )
						GenParticles = GenHandle.product()
						PTW = PTW_Lookup( GenParticles )
						weight*=PTW
	     					weightSFptup=max(0.0,weight*(2*PTW-1))
	     					weightSFptdown=weight


					weightSFtup=weight*weightSFtup
					weightSFtdown=weight*weightSFtdown
					weight*=weightSFt

					weighttrigup*=weightSFt
					weighttrigdown*=weightSFt

     					#event.getByLabel (subjets0indexLabel, subjets0indexHandle)
		     			#subjets0index 		= 	subjets0indexHandle.product() 

		     			#event.getByLabel (subjets1indexLabel, subjets1indexHandle)
		     			#subjets1index 		= 	subjets1indexHandle.product() 

		     			#event.getByLabel (subjets2indexLabel, subjets2indexHandle)
		     			#subjets2index 		= 	subjets2indexHandle.product() 

		     			#event.getByLabel (subjets3indexLabel, subjets3indexHandle)
		     			#subjets3index 		= 	subjets3indexHandle.product()
	
		    		
		     			#event.getByLabel (subjetsCSVLabel, subjetsCSVHandle)
		     			#subjetsCSV 		= 	subjetsCSVHandle.product()  

		 			#SJ_csvs = [subjets0index,subjets1index,subjets2index,subjets3index]
 			
		 			#SJ_csvvals = []
		 			#for icsv in range(0,int(nSubjets[tindexval])):
		 			#	if int(SJ_csvs[icsv][tindexval])!=-1:
		 			#		SJ_csvvals.append(subjetsCSV[int(SJ_csvs[icsv][tindexval])])
		 			#	else:
		 			#		SJ_csvvals.append(0.)

					event.getByLabel (vsubjets0indexLabel,vsubjets0indexHandle )
	    				vsubjets0index 		= 	vsubjets0indexHandle.product() 

	    				event.getByLabel (vsubjets1indexLabel,vsubjets1indexHandle )
	    				vsubjets1index 		= 	vsubjets1indexHandle.product() 

	    				event.getByLabel (subjetsAK8CSVLabel,subjetsAK8CSVHandle )
	    				subjetsAK8CSV		= 	subjetsAK8CSVHandle.product() 


					if len(subjetsAK8CSV)==0:
						continue
					if len(subjetsAK8CSV)<2:
						subjetsAK8CSV[int(vsubjets0index[tindexval])]
					else:
	    					SJ_csvvals = [subjetsAK8CSV[int(vsubjets0index[tindexval])],subjetsAK8CSV[int(vsubjets1index[tindexval])]]

		 			if SJ_csvvals != []: #added this because files with no SJ_csvvals would cause the entire thing to fail			
						SJ_csvmax = max(SJ_csvvals)
		 				sjbtag_cut = sjbtag[0]<SJ_csvmax<=sjbtag[1]
						if options.var == "kinematics":
							CSVMax.Fill(SJ_csvmax,weight)
							#CSV.Fill(SJ_csvvals,weight)
	

			     			event.getByLabel (tau3Label, tau3Handle)
			     			Tau3		= 	tau3Handle.product() 
 	
		 
			     			event.getByLabel (tau2Label, tau2Handle)
			     			Tau2		= 	tau2Handle.product() 
	 		
			     			event.getByLabel (tau1Label, tau1Handle)
			     			Tau1		= 	tau1Handle.product() 
						if Tau1[windexval] != 0 and Tau2[tindexval] != 0:
						
							tau21val=Tau2[windexval]/Tau1[windexval]
							tau21_cut =  tau21[0]<=tau21val<tau21[1]

							tau32val =  Tau3[tindexval]/Tau2[tindexval]
							tau32_cut =  tau32[0]<=tau32val<tau32[1]
							if options.var == "kinematics":
								Nsubjetiness.Fill(tau32val,weight)
								
								
							if type(wmass[0])== list:
								wmass_cut = wmass[0][0]<=puppiJetMass[windexval]<wmass[0][1] or wmass[1][0]<=puppiJetMass[windexval]<wmass[1][1] 
							elif type(wmass[0]) == float:
								wmass_cut = wmass[0]<=puppiJetMass[windexval]<wmass[1]
							else:
								print "issue with wmass cut"

							FullTop = sjbtag_cut and tau32_cut

							if wmass_cut:
								if options.var == "kinematics":
									Mtw_cut5.Fill((tjet+wjet).M(),weight)
								if tau21_cut:
									if options.var == "kinematics":
										Mtw_cut6.Fill((tjet+wjet).M(),weight)
									eta_regions = [eta1,eta2]
									TTRweight = bkg_weight(tjet,TTR,eta_regions)
									TTRweightsigsq = bkg_weight(tjet,TTR_err,eta_regions)
	
									TTRweighterrup = TTRweight+sqrt(TTRweightsigsq)
									TTRweighterrdown = TTRweight-sqrt(TTRweightsigsq)
	

									eta1_cut = eta1[0]<=abs(tjet.Eta())<eta1[1]
									eta2_cut = eta2[0]<=abs(tjet.Eta())<eta2[1]

									modm = puppiJetMass[tindexval]
									if options.modmass=='nominal':
		        							massw = ModPlot.Interpolate(modm)
									if options.modmass=='up':
		        							massw = 1 + 0.5*(ModPlot.Interpolate(modm)-1)
									if options.modmass=='down':
		        							massw = max(0.0,1 + 1.5*(ModPlot.Interpolate(modm)-1))
		        						if options.modmass=='none':
		        							massw = 1
	
									masswHist.Fill(massw)

									if (eta1_cut) :
										xbin = TagPlot2de1.GetXaxis().FindBin(tjet.Perp())
										ybin = TagPlot2de1.GetYaxis().FindBin((tjet+wjet).M())
										tagrate2d = TagPlot2de1.GetBinContent(xbin,ybin)
										tagrate2derr = TagPlot2de1.GetBinError(xbin,ybin)
										QCDbkg2D.Fill((tjet+wjet).M(),tagrate2d*weight*massw)
										QCDbkg2Dup.Fill((tjet+wjet).M(),(tagrate2d+tagrate2derr)*weight*massw)
										QCDbkg2Ddown.Fill((tjet+wjet).M(),(tagrate2d-tagrate2derr)*weight*massw)
	
										if options.var == "kinematics":
											Mtw_cut7.Fill((tjet+wjet).M(),weight)
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
				
									if (eta2_cut):
										xbin = TagPlot2de2.GetXaxis().FindBin(tjet.Perp())
										ybin = TagPlot2de2.GetYaxis().FindBin((tjet+wjet).M())
										tagrate2d = TagPlot2de2.GetBinContent(xbin,ybin)
										tagrate2derr = TagPlot2de2.GetBinError(xbin,ybin)
										QCDbkg2D.Fill((tjet+wjet).M(),tagrate2d*weight*massw)
										QCDbkg2Dup.Fill((tjet+wjet).M(),(tagrate2d+tagrate2derr)*weight*massw)
										QCDbkg2Ddown.Fill((tjet+wjet).M(),(tagrate2d-tagrate2derr)*weight*massw)	
				
										if options.var == "kinematics":
											Mtw_cut8.Fill((tjet+wjet).M(),weight)
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
								
									if options.var == 'analyzer':
										fillSpec = [(tjet+wjet).M()]
									elif options.var == 'kinematics':
										fillSpec = [(tjet+wjet).M(), tjet.Eta(), wjet.Eta(), tjet.Perp(), wjet.Perp(), (tjet+wjet).Perp(), tjet.Phi(), wjet.Phi(), abs(tjet.Phi()-wjet.Phi())]
	
									arr_count = 0
									for spec in fillSpec:
										for ifit in range(0,len(fittitles)):
											tempweight = bkg_weight(tjet,fits[ifit],eta_regions)
											QCDbkg_ARR[arr_count].Fill(spec,tempweight*weight*massw) 
											arr_count+=1
	
									QCDbkg.Fill((tjet+wjet).M(),TTRweight*weight*massw)
									QCDbkgh.Fill((tjet+wjet).M(),TTRweighterrup*weight*massw)
									QCDbkgl.Fill((tjet+wjet).M(),TTRweighterrdown*weight*massw)

									QCDbkgMtStack.Fill(puppiJetMass[tindexval],TTRweight*weight*massw)
	
									if options.var == "kinematics":
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
									if sjbtag_cut:
										if options.var == "kinematics":
											Mtw_cut9.Fill((tjet+wjet).M(),weight)
										if tau32_cut:
											if options.var == "kinematics":
												Mtw_cut10.Fill((tjet+wjet).M(),weight)
								  				        	
											if tag==0:
												if ((tjet+wjet).M()>2400):
													goodEvents.append( [ event.object().id().run(), event.object().id().luminosityBlock(), event.object().id().event(),  ] )
												Mtw.Fill((tjet+wjet).M(),weight) 

												MtStack.Fill(puppiJetMass[tindexval],weight)

												Mtwtrigup.Fill((tjet+wjet).M(),weighttrigup)
												Mtwtrigdown.Fill((tjet+wjet).M(),weighttrigdown)
												MtwTup.Fill((tjet+wjet).M(),weightSFtup) 
												MtwTdown.Fill((tjet+wjet).M(),weightSFtdown) 
	
												if options.var == "kinematics":
													b_count = 0
													bTruthCount = 0
														
							#							if len(AK4LV) != 0:
							#							btags = []
							#							for ijet in range(0,len(AK4LV)):													
							#								event.getByLabel (BDiscAK4Label, BDiscAK4Handle)
							#								event.getByLabel (FlavourLabel, FlavourHandle)
	    						#								bJetBDiscs 	= 	BDiscAK4Handle.product()
							#								flav = FlavourHandle.product()
														
							#								bJetBDisc = bJetBDiscs[ijet]

							#								if abs(tjet.Rapidity() - AK4LV[ijet].Rapidity()) > 1.5:
							#									btags.append(bJetBDiscs[ijet])											
	 						#									if bJetBDisc > 0.7:
							#										b_count+=1
							#								if abs(flav[ijet])==5:
							#									bTruthCount+=1
							#							Btag.Fill(b_count,weight)
							#							if btags != []:
							#								Btagmax.Fill(max(btags),weight)
							#							Btruth.Fill(bTruthCount,weight)
							#							JetsVsBtag.Fill(b_count,len(AK4LV),weight)
							#							infoArray.append(str(count)+'\t'+str(b_count) + '\t' + str(len(AK4LV)))
	
													EtaTop.Fill(tjet.Eta(),weight)
													EtaW.Fill(wjet.Eta(),weight)
												
													PtTop.Fill(tjet.Perp(),weight)
													PtW.Fill(wjet.Perp(),weight)
													PtTopW.Fill((tjet+wjet).Perp(),weight)
				
												
													PhiTop.Fill(tjet.Phi(),weight)
													PhiW.Fill(wjet.Phi(),weight)
													dPhi.Fill(abs(tjet.Phi()-wjet.Phi()),weight)
	
												tag=1
												temp_variables = {"wpt":wjet.Perp(),"wmass":puppiJetMass[windexval],"tpt":tjet.Perp(),"tmass":puppiJetMass[tindexval],"tau32":tau32val,"tau21":tau21val,"sjbtag":SJ_csvmax,"weight":weight}#,"nsubjets":nSubjets[tindexval]
	
												for tv in tree_vars.keys():
													tree_vars[tv][0] = temp_variables[tv]
												Tree.Fill()
												doneAlready = True

		
	
#ONLY USED FOR DEBUGGING	
#for i in infoArray:
#	print i
f.cd()
f.Write()
f.Close()

print "number of events: " + str(count)

if options.printEvents:
    Outf1   =   open("DataEvents"+options.num+".txt", "w")
    sys.stdout = Outf1
    for goodEvent in goodEvents :
        print '{0:12.0f}:{1:12.0f}:{2:12.0f}'.format(
            goodEvent[0], goodEvent[1], goodEvent[2]
        )
