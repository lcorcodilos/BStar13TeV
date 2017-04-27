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
parser.add_option('-S', '--split', metavar='F', type='string', action='store',
				  default	=	'file',
				  dest		=	'split',
				  help		=	'split by event of file')
parser.add_option('-A', '--Alphabet', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'Alphabet',
				  help		=	'turn alphabet on or off')


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

if options.set == "data":
	file = TFile(di+"TTrees/TWtreefile_"+options.set+"_Trigger_"+tnameformat+"_"+mod+pstr+mmstr+".root")
else:
	file = TFile(di+"TTrees/TWtreefile_"+options.set+"_Trigger_"+tnameformat+"_"+mod+pstr+mmstr+"_weighted.root")

tree = file.Get("Tree")

if (options.set.find('ttbar') != -1) or (options.set.find('singletop') != -1):
	settype = 'ttbar'
elif (options.set.find('QCD') != -1):
	settype ='ttbar'
	run_b_SF = False
else :
	settype = options.set

print 'The type of set is ' + settype

#CHANGE BACK
if options.Alphabet != "on"
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

#---------------------------------------------------------------------------------------------------------------------#
var = ""
if options.var == "kinematics":
	var = "_kin"

f = TFile( "TWanalyzer"+options.set+"_Trigger_"+tnameformat+"_"+mod+pstr+mmstr+"_PSET_"+options.cuts+var+".root", "recreate" )

#Load up the average t-tagging rates -- Takes parameters from text file and makes a function
#CHANGE BACK
if options.Alphabet == "on":
	TTR = TTR_Init('QUAD',options.cuts,setstr,di)
	TTR_errUp = TTR_Init('QUAD_errUp',options.cuts,setstr,di)
	TTR_errDown = TTR_Init('QUAD_errDown',options.cuts,setstr,di)
	fittitles = ["QUAD"]
	fits = []
	for fittitle in fittitles:
		fits.append(TTR_Init(fittitle,options.cuts,setstr,di))

elif options.Alphabet == "off":
	TTR = TTR_Init('Bifpoly','rate_'+options.cuts,setstr,di)
	TTR_err = TTR_Init('Bifpoly_err','rate_'+options.cuts,setstr,di)
	fittitles = ["pol0","pol2","pol3","FIT","Bifpoly","expofit"]
	fits = []
	for fittitle in fittitles:
		fits.append(TTR_Init(fittitle,'rate_'+options.cuts,setstr,di))
	TagFile1 = TFile(di+"Tagrate"+setstr+"2D_rate_"+options.cuts+".root")
	TagFile1 = TFile(di+"Tagrate"+setstr+"2D_"+options.cuts+".root")
	TagPlot2de1= TagFile1.Get("tagrateeta1")
	TagPlot2de2= TagFile1.Get("tagrateeta2")

print "Creating histograms"


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
if options.Alphabet == "off":
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

TopMass		= TH1F("TopMass",	"Top mass",				10,0,500)
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


TopMass.Sumw2()
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
	
	
QCDbkg_ARR = []
	
kinVars = 	['', 	'ET', 	'EW', 	'PT', 	'PW', 	'PTW', 	'PhT', 	'PhW', 	'dPhi'	]
kinBin = 	[140, 	12, 	12, 	50, 	50,	35,	12,	12,	12	]
kinLow = 	[500, 	-2.4, 	-2.4, 	450, 	370,	0,	-pie,	-pie,	2.2	]
kinHigh = 	[4000, 	2.4, 	2.4, 	1500, 	1430,	700,	pie,	pie,	pie	]

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
				"weight":array('d',[0.])}

NewTree = Make_Trees(tree_vars)

goodEvents = []
totevents = tree.GetEntries()


nev.SetBinContent(1,totevents)

for event in tree:
	count	= 	count + 1
	m = 0
	t = 0

	if count % 100000 == 0 :
		print  '--------- Processing Event ' + str(count) +'   -- percent complete ' + str(100*count/totevents) + '% -- '

	weight = 1.0

	MtopW = event.t_LVmass + event.w_LVmass

	Mtw_cut1.Fill(MtopW,weight)
	wpt_cut = wpt[0]<event.wpt<wpt[1]
	tpt_cut = tpt[0]<event.tpt<tpt[1]
	dy_cut = dy[0]<=event.dy<dy[1]
		
	if wpt_cut and tpt_cut:
		Mtw_cut2.Fill(MtopW,weight)
		deltaY.Fill(abs(event.dy),weight)

		if dy_cut:
			Mtw_cut3.Fill(MtopW,weight)
			# Have never used this so ignoring for now (pdfLabel/Handle also not defined)
			# if options.pdfweights != "nominal" :
			# 	event.getByLabel( pdfLabel, pdfHandle )
			# 	pdfs = pdfHandle.product()
			# 	iweight = PDF_Lookup( pdfs , options.pdfweights )
			# 	weight *= iweight

			weightSFt = 1.0
			weightSFtdown = 1.0
			weightSFtup = 1.0

			if options.set!="data":
				# event.getByLabel (puLabel, puHandle)
				# PileUp 		= 	puHandle.product()
				# bin1 = PilePlot.FindBin(PileUp[0]) 

				# Bin value was stored in the tree for this weight reconstruction
				# Value was initialized at -1 so if there's an issue, you should see it
				bin1 = event.pileBin

				if options.pileup != 'off':
					weight *= PilePlot.GetBinContent(bin1)

				if options.cuts=="default" and options.set!="QCD":
					#top scale factor reweighting done here
					SFT = SFT_Lookup( event.tpt )
					weightSFt = SFT[0]
					weightSFtdown = SFT[1]
					weightSFtup = SFT[2]


			# For top mass

			tmass_cut = tmass[0]<event.tmass<tmass[1]
			TopMass.Fill(event.tmass,weight)

			if tmass_cut :
				Mtw_cut4.Fill(MtopW,weight)

				ht = event.tpt + event.wpt

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
			
			# Like pdfweights, have never turned this on and GenLabel/Handle don't exist so ignoring for now
				# if options.ptreweight == "on":
				# 	#ttbar pt reweighting done here
				# 	event.getByLabel( GenLabel, GenHandle )
				# 	GenParticles = GenHandle.product()
				# 	PTW = PTW_Lookup( GenParticles )
				# 	weight*=PTW
				# 	weightSFptup=max(0.0,weight*(2*PTW-1))
				# 	weightSFptdown=weight


				weightSFtup=weight*weightSFtup
				weightSFtdown=weight*weightSFtdown
				weight*=weightSFt

				weighttrigup*=weightSFt
				weighttrigdown*=weightSFt
		
				SJ_csvmax = event.sjbtag
				sjbtag_cut = sjbtag[0]<SJ_csvmax<=sjbtag[1]

				CSVMax.Fill(SJ_csvmax,weight)
			
				tau21val=event.tau21
				tau21_cut =  tau21[0]<=tau21val<tau21[1]

				tau32val =  event.tau32
				tau32_cut =  tau32[0]<=tau32val<tau32[1]

				Nsubjetiness32.Fill(tau32val,weight)
				Nsubjetiness21.Fill(tau21val,weight)
					
				if type(wmass[0])== list:
					wmass_cut = wmass[0][0]<=event.wmass<wmass[0][1] or wmass[1][0]<=event.wmass<wmass[1][1] 
				elif type(wmass[0]) == float:
					wmass_cut = wmass[0]<=event.wmass<wmass[1]
				else:
					print "issue with wmass cut"
					continue

				FullTop = sjbtag_cut and tau32_cut

				if wmass_cut:
					Mtw_cut5.Fill(MtopW,weight)
					if tau21_cut:
						Mtw_cut6.Fill(MtopW,weight)

# Now going to split into alphabet and tagrate parts
						if options.Alphabet == "off":
							eta_regions = [eta1,eta2]
							eta1_cut = eta1[0]<=abs(event.eta)<eta1[1]
							eta2_cut = eta2[0]<=abs(event.eta)<eta2[1]

							TTRweight = bkg_weight_pt(event,TTR,eta_regions)
							TTRweightsigsq = bkg_weight_pt(event,TTR_err,eta_regions)
							TTRweighterrup = TTRweight+sqrt(TTRweightsigsq)
							TTRweighterrdown = TTRweight-sqrt(TTRweightsigsq)

							modm = event.tmass
							if options.modmass=='nominal':
								massw = ModPlot.Interpolate(modm)
							if options.modmass=='up':
								massw = 1 + 0.5*(ModPlot.Interpolate(modm)-1)
							if options.modmass=='down':
								massw = max(0.0,1 + 1.5*(ModPlot.Interpolate(modm)-1))
							
							masswHist.Fill(massw)

							if (eta1_cut):
								xbin = TagPlot2de2.GetXaxis().FindBin(event.tpt)
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

							if (eta2_cut):
								xbin = TagPlot2de2.GetXaxis().FindBin(event.tpt)
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

							fillSpec = [MtopW, event.top_eta, event.w_eta, event.tpt, event.wpt, event.tpt+event.wpt, event.top_phi, event.w_phi, abs(event.top_phi-event.w_phi)]

							arr_count = 0
							for spec in fillSpec:
								for ifit in range(0,len(fittitles)):
									tempweight = bkg_weight_pt(event,fits[ifit],eta_regions)
									QCDbkg_ARR[arr_count].Fill(spec,tempweight*weight*massw) 
									arr_count+=1

							QCDbkg.Fill(MtopW,TTRweight*weight*massw)
							QCDbkgh.Fill(MtopW,TTRweighterrup*weight*massw)
							QCDbkgl.Fill(MtopW,TTRweighterrdown*weight*massw)

							QCDbkgMtStack.Fill(event.tmass,TTRweight*weight*massw)

							QCDbkgET.Fill(event.top_eta,TTRweight*weight*massw)
							QCDbkgETh.Fill(event.top_eta,TTRweighterrup*weight*massw)
							QCDbkgETl.Fill(event.top_eta,TTRweighterrdown*weight*massw)

							QCDbkgEW.Fill(event.w_eta,TTRweight*weight*massw)
							QCDbkgEWh.Fill(event.w_eta,TTRweighterrup*weight*massw)
							QCDbkgEWl.Fill(event.w_eta,TTRweighterrdown*weight*massw)

							QCDbkgPT.Fill(event.tpt,TTRweight*weight*massw)
							QCDbkgPTh.Fill(event.tpt,TTRweighterrup*weight*massw)
							QCDbkgPTl.Fill(event.tpt,TTRweighterrdown*weight*massw)

							QCDbkgPW.Fill(event.wpt,TTRweight*weight*massw)
							QCDbkgPWh.Fill(event.wpt,TTRweighterrup*weight*massw)
							QCDbkgPWl.Fill(event.wpt,TTRweighterrdown*weight*massw)

							QCDbkgPTW.Fill((event.tpt+event.wpt),TTRweight*weight*massw)
							QCDbkgPTWh.Fill((event.tpt+event.wpt),TTRweighterrup*weight*massw)
							QCDbkgPTWl.Fill((event.tpt+event.wpt),TTRweighterrdown*weight*massw)

							QCDbkgPhT.Fill(event.top_phi,TTRweight*weight*massw)
							QCDbkgPhTh.Fill(event.top_phi,TTRweighterrup*weight*massw)
							QCDbkgPhTl.Fill(event.top_phi,TTRweighterrdown*weight*massw)

							QCDbkgPhW.Fill(event.w_phi,TTRweight*weight*massw)
							QCDbkgPhWh.Fill(event.w_phi,TTRweighterrup*weight*massw)
							QCDbkgPhWl.Fill(event.w_phi,TTRweighterrdown*weight*massw)

							QCDbkgdPhi.Fill(abs(event.top_phi-event.w_phi),TTRweight*weight*massw)  
							QCDbkgdPhih.Fill(abs(event.top_phi-event.w_phi),TTRweighterrup*weight*massw)
							QCDbkgdPhil.Fill(abs(event.top_phi-event.w_phi),TTRweighterrdown*weight*massw)


							if sjbtag_cut:
								Mtw_cut9.Fill(MtopW,weight)
								# Grab the pass/fail ratio at the last second for efficiency
								if tau32_cut:
									Mtw_cut10.Fill((tjet+wjet).M(),weight)
						  				        	

									if ((MtopW)>2400):
										goodEvents.append( [ event.object().id().run(), event.object().id().luminosityBlock(), event.object().id().event(),  ] )
									Mtw.Fill(MtopW,weight) 

									MtStack.Fill(event.tmass,weight)

									Mtwtrigup.Fill(MtopW,weighttrigup)
									Mtwtrigdown.Fill(MtopW,weighttrigdown)
									MtwTup.Fill(MtopW,weightSFtup) 
									MtwTdown.Fill(MtopW,weightSFtdown) 

									if options.var == "kinematics":

									EtaTop.Fill(event.top_eta,weight)
									EtaW.Fill(event.w_eta,weight)
									
									PtTop.Fill(event.tpt,weight)
									PtW.Fill(event.wpt,weight)
									PtTopW.Fill((event.tpt+event.wpt),weight)
	
									
									PhiTop.Fill(event.top_phi,weight)
									PhiW.Fill(event.w_phi,weight)
									dPhi.Fill(abs(event.top_phi-event.w_phi),weight)


									temp_variables = {	"wpt":event.wpt,
														"wmass":event.wmass,
														"tpt":event.tpt,
														"tmass":event.tmass,
														"tau32":tau32val,
														"tau21":tau21val,
														"sjbtag":SJ_csvmax,
														"weight":weight}

									for tv in tree_vars.keys():
										tree_vars[tv][0] = temp_variables[tv]
									NewTree.Fill()



						elif options.Alphabet == "on":
							eta_cut = eta[0]<=abs(event.top_eta)<eta[1]
							massw = 1
							masswHist.Fill(massw)
							
							if sjbtag_cut:
								Mtw_cut9.Fill(MtopW,weight)
								# Grab the pass/fail ratio at the last second for efficiency
								TTRweight = bkg_weight_mass(event,TTR,eta)
								TTRweighterrup = bkg_weight_mass(event,TTR_errUp,eta)
								TTRweighterrdown = bkg_weight_mass(event,TTR_errDown,eta)

								if not tau32_cut:
								# Start generating the QCD estimate using the pass/fail ratio 
								# on events that fail the tau32 cut
									fillSpec = [MtopW, event.top_eta, event.w_eta, event.tpt, event.wpt, event.tpt+event.wpt, event.top_phi, event.w_phi, abs(event.top_phi-event.w_phi)]
	
									arr_count = 0
									for spec in fillSpec:
										for ifit in range(0,len(fittitles)):
											tempweight = bkg_weight_mass(event,fits[ifit],eta)
											QCDbkg_ARR[arr_count].Fill(spec,tempweight*weight*massw) 
											arr_count+=1
	
									QCDbkg.Fill(MtopW,TTRweight*weight*massw)
									QCDbkgh.Fill(MtopW,TTRweighterrup*weight*massw)
									QCDbkgl.Fill(MtopW,TTRweighterrdown*weight*massw)

									QCDbkgMtStack.Fill(event.tmass,TTRweight*weight*massw)

									QCDbkgET.Fill(event.top_eta,TTRweight*weight*massw)
									QCDbkgETh.Fill(event.top_eta,TTRweighterrup*weight*massw)
									QCDbkgETl.Fill(event.top_eta,TTRweighterrdown*weight*massw)

									QCDbkgEW.Fill(event.w_eta,TTRweight*weight*massw)
									QCDbkgEWh.Fill(event.w_eta,TTRweighterrup*weight*massw)
									QCDbkgEWl.Fill(event.w_eta,TTRweighterrdown*weight*massw)

									QCDbkgPT.Fill(event.tpt,TTRweight*weight*massw)
									QCDbkgPTh.Fill(event.tpt,TTRweighterrup*weight*massw)
									QCDbkgPTl.Fill(event.tpt,TTRweighterrdown*weight*massw)

									QCDbkgPW.Fill(event.wpt,TTRweight*weight*massw)
									QCDbkgPWh.Fill(event.wpt,TTRweighterrup*weight*massw)
									QCDbkgPWl.Fill(event.wpt,TTRweighterrdown*weight*massw)

									QCDbkgPTW.Fill((event.tpt+event.wpt),TTRweight*weight*massw)
									QCDbkgPTWh.Fill((event.tpt+event.wpt),TTRweighterrup*weight*massw)
									QCDbkgPTWl.Fill((event.tpt+event.wpt),TTRweighterrdown*weight*massw)

									QCDbkgPhT.Fill(event.top_phi,TTRweight*weight*massw)
									QCDbkgPhTh.Fill(event.top_phi,TTRweighterrup*weight*massw)
									QCDbkgPhTl.Fill(event.top_phi,TTRweighterrdown*weight*massw)

									QCDbkgPhW.Fill(event.w_phi,TTRweight*weight*massw)
									QCDbkgPhWh.Fill(event.w_phi,TTRweighterrup*weight*massw)
									QCDbkgPhWl.Fill(event.w_phi,TTRweighterrdown*weight*massw)

									QCDbkgdPhi.Fill(abs(event.top_phi-event.w_phi),TTRweight*weight*massw)  
									QCDbkgdPhih.Fill(abs(event.top_phi-event.w_phi),TTRweighterrup*weight*massw)
									QCDbkgdPhil.Fill(abs(event.top_phi-event.w_phi),TTRweighterrdown*weight*massw)

								if tau32_cut:
									Mtw_cut10.Fill(MtopW,weight)
													
									if (MtopW>2400):
										goodEvents.append( [ event.object().id().run(), event.object().id().luminosityBlock(), event.object().id().event(),  ] )
									Mtw.Fill(MtopW,weight) 

									MtStack.Fill(event.tmass,weight)

									Mtwtrigup.Fill(MtopW,weighttrigup)
									Mtwtrigdown.Fill(MtopW,weighttrigdown)
									MtwTup.Fill(MtopW,weightSFtup) 
									MtwTdown.Fill(MtopW,weightSFtdown) 

									EtaTop.Fill(tjet.Eta(),weight)
									EtaW.Fill(wjet.Eta(),weight)
								
									PtTop.Fill(tjet.Perp(),weight)
									PtW.Fill(wjet.Perp(),weight)
									PtTopW.Fill((tjet+wjet).Perp(),weight)

								
									PhiTop.Fill(tjet.Phi(),weight)
									PhiW.Fill(wjet.Phi(),weight)
									dPhi.Fill(abs(tjet.Phi()-wjet.Phi()),weight)

									temp_variables = {	"wpt":event.wpt,
														"wmass":event.wmass,
														"tpt":event.tpt,
														"tmass":event.tmass,
														"tau32":tau32val,
														"tau21":tau21val,
														"sjbtag":SJ_csvmax,
														"weight":weight}


									for tv in tree_vars.keys():
										tree_vars[tv][0] = temp_variables[tv]
									NewTree.Fill()


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
