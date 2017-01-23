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
                   default	=	'HLT_PFHT800_v3',
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

(options, args) = parser.parse_args()
if options.set == 'QCD':
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


#----Trigger Naming------
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
 		

#------Basics-----------
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
mod = "ttbsmAna"
if options.modulesuffix != "none" :
	mod = mod + options.modulesuffix


pstr = ""
if options.pdfweights!="nominal":
	print "using pdf uncertainty"
	pstr = "_pdf_"+options.pdfset+"_"+options.pdfweights

pustr = ""
if options.pileup=='off':
	pustr = "_pileup_unweighted"


#Based on what set we want to analyze, we find all Ntuple root files 

files = Load_Ntuples(options.set,options.bx)

if (options.set.find('ttbar') != -1) or (options.set.find('singletop') != -1):
	settype = 'ttbar'
elif (options.set.find('QCD') != -1):
	settype ='QCD'
	run_b_SF = False
else :
	
	settype = options.set.replace('right','').replace('left','')

print 'The type of set is ' + settype


if options.set != 'data':
	#Load up scale factors (to be used for MC only)

	TrigFile = TFile(di+"Triggerweight_data80X.root")
	TrigPlot = TrigFile.Get("TriggerWeight_"+tnamestr+"_pre_HLT_PFHT475_v3")

	#PileFile = TFile(di+"PileUp_Ratio_"+settype+".root")
	#PilePlot = PileFile.Get("Pileup_Ratio")

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
AK4HL 		= 	Initlv("jetsAK4")
BDiscAK4Handle 	= 	Handle (  "vector<float> "  )
BDiscAK4Label  	= 	( "jetsAK4" , "jetAK4CSV")
FlavourHandle	=	Handle (  "vector<float> "  )
FlavourLabel	=	( "jetsAK4" , "jetAK4PartonFlavour") 


#Here we load up handles and labels.
#These are used to grab entries from the Ntuples.
#To see all the current types in an Ntuple use edmDumpEventContent /PathtoNtuple/Ntuple.root
AK8HL = Initlv("jetsAK8")

GeneratorHandle 	= 	Handle (  "GenEventInfoProduct")
GeneratorLabel  	= 	( "generator" , "")

puHandle    	= 	Handle("int")
puLabel     	= 	( "eventUserData", "puNtrueInt" )

#minmassHandle 	= 	Handle (  "vector<float> "  )
#minmassLabel  	= 	( "jetsAK8" , "jetAK8minmass")

#nSubjetsHandle 	= 	Handle (  "vector<float> "  )
#nSubjetsLabel  	= 	( "jetsAK8" , "jetAK8nSubJets")

# not used
softDropMassHandle 	= 	Handle (  "vector<float> "  )
softDropMassLabel  	= 	( "jetsAK8" , "jetAK8softDropMass")

# for top mass
softDropMassuncorrHandle 	= 	Handle (  "vector<float> "  )
softDropMassuncorrLabel  	= 	( "jetsAK8" , "jetAK8softDropMassuncorr")

# for W mass
PrunedMassHandle 	= 	Handle (  "vector<float> "  )
PrunedMassLabel  	= 	( "jetsAK8" , "jetAK8prunedMass")

vsubjets0indexHandle 	= 	Handle (  "vector<float> "  )
vsubjets0indexLabel  	= 	( "jetsAK8" , "jetAK8vSubjetIndex0")

vsubjets1indexHandle 	= 	Handle (  "vector<float> "  )
vsubjets1indexLabel  	= 	( "jetsAK8" , "jetAK8vSubjetIndex1")

subjetsAK8CSVHandle 	= 	Handle (  "vector<float> "  )
subjetsAK8CSVLabel  	= 	( "subjetsAK8CHS" , "subjetAK8CHSCSVv2")

tau1Handle 	= 	Handle (  "vector<float> "  )
tau1Label  	= 	( "jetsAK8" , "jetAK8tau1")

tau2Handle 	= 	Handle (  "vector<float> "  )
tau2Label  	= 	( "jetsAK8" , "jetAK8tau2")

tau3Handle 	= 	Handle (  "vector<float> "  )
tau3Label  	= 	( "jetsAK8" , "jetAK8tau3")

topMassHandle 	= 	Handle (  "vector<float> "  )
topMassLabel  	= 	( "jetsAK8" , "jetAK8topMass")

subjetsCSVHandle 	= 	Handle (  "vector<float> "  )
subjetsCSVLabel  	= 	( "subjetsCmsTopTag" , "subjetCmsTopTagCSV")

subjets0indexHandle 	= 	Handle (  "vector<float> "  )
subjets0indexLabel  	= 	( "jetsAK8" , "jetAK8topSubjetIndex0")

subjets1indexHandle 	= 	Handle (  "vector<float> "  )
subjets1indexLabel  	= 	( "jetsAK8" , "jetAK8topSubjetIndex1")

subjets2indexHandle 	= 	Handle (  "vector<float> "  )
subjets2indexLabel  	= 	( "jetsAK8" , "jetAK8topSubjetIndex2")

subjets3indexHandle 	= 	Handle (  "vector<float> "  )
subjets3indexLabel  	= 	( "jetsAK8" , "jetAK8topSubjetIndex3")

HT800Handle     =       Handle ( "vector<bool>" )
HT800Label      =       ( "Filter" , "HT800bit" )

#---------------------------------------------------------------------------------------------------------------------#
var = ""

if jobs != 1:
	f = TFile( "TWvariables"+options.set+"_Trigger_"+tnameformat+"_"+options.modulesuffix +pustr+pstr+"_job"+options.num+"of"+options.jobs+"_PSET_"+options.cuts+var+".root", "recreate" )
else:
	f = TFile( "TWvariables"+options.set+"_Trigger_"+tnameformat+"_"+options.modulesuffix +pustr+pstr+"_PSET_"+options.cuts+var+".root", "recreate" )


print "Creating histograms"

TTR = TTR_Init('Bifpoly','rate_'+options.cuts,setstr,di)

#Define Histograms


f.cd()
#---------------------------------------------------------------------------------------------------------------------#
Tau_21		= TH1F("Tau_21",	"tau_21",				15,   0, 1.5 )
Mt		= TH1F("Mt",		"top candidate mass",			20,   0, 500 )
Tau_32		= TH1F("Tau_32",  	"Tau_32",     	  	      		15,   0, 1.5 )
MaxSJCSV	= TH1F("MaxSJCSV",	"Maximum subjet CSV",			20,   0, 1   )
dyfull		= TH1F("dyfull",     	"delta y between top and b candidates", 12,   0, 5   )
dysemi		= TH1F("dysemi",     	"delta y between top and b candidates", 12,   0, 5   )
Mw		= TH1F("Mw",		"W candidate mass",     	  	30,   0, 300 )

MtStack		= TH1F("MtStack",	"top candidate mass for stack",		100,   0, 500 )
QCDbkgMtStack	= TH1F("QCDbkgMtStack", "QCD background for top mass",		100, 0, 500 )

nev = TH1F("nev",	"nev",		1, 0, 1 )

Mt.Sumw2()
Mw.Sumw2()
Tau_21.Sumw2()
Tau_32.Sumw2()
MaxSJCSV.Sumw2()
dyfull.Sumw2()
dysemi.Sumw2()	

MtStack.Sumw2()
QCDbkgMtStack.Sumw2()
	
#---------------------------------------------------------------------------------------------------------------------#

# loop over events
#---------------------------------------------------------------------------------------------------------------------#

count = 0
jobiter = 0
print "Start looping"
#initialize the ttree variables
tree_vars = {"wpt":array('d',[0.]),"wmass":array('d',[0.]),"tpt":array('d',[0.]),"tmass":array('d',[0.]),"tau32":array('d',[0.]),"tau21":array('d',[0.]),"nsubjets":array('d',[0.]),"sjbtag":array('d',[0.]),"weight":array('d',[0.])}
Tree = Make_Trees(tree_vars)


goodEvents = []
totevents = events.size()
print str(totevents)  +  ' Events total'
nev.SetBinContent(1,totnev)
infoArray=[]
for event in events:
    count	= 	count + 1
    m = 0
    t = 0
    if count % 100000 == 0 :
      print  '--------- Processing Event ' + str(count) +'   -- percent complete ' + str(100*count/totevents) + '% -- '

    if options.set == 'data':
	event.getByLabel (HT800Label, HT800Handle)
	trigBit = HT800Handle.product()
	if not trigBit:
		continue

    #Here we split up event processing based on number of jobs 
    #This is set up to have jobs range from 1 to the total number of jobs (ie dont start at job 0)
    if jobs != 1:
    	if (count - 1) % jobs == 0:
		jobiter+=1
	count_index = count - (jobiter-1)*jobs
	if count_index!=num:
		continue 
#Define different cuts
    # Need to separate into Hemispheres to get indexes
    AK8LV = Makelv(AK8HL,event)
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
    #Require 1 pt>150 jet in each hemisphere (top jets already have the 150GeV requirement) 
    for wjet in wJetsh0:
	if wjet.Perp() > 200.0:
		wjh0+=1
    for wjet in wJetsh1:
	if wjet.Perp() > 200.0:
		wjh1+=1

    njets11w0 	= 	((len(topJetsh1) == 1) and (wjh0 == 1))
    njets11w1 	= 	((len(topJetsh0) == 1) and (wjh1 == 1))
    tag = 0

    doneAlready = False
    #Need to pass basic requirements of hemisphere ocation and Eta
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
	#Finally look at cuts
    	wpt_cut = wpt[0]<wjet.Perp()<wpt[1]
    	tpt_cut = tpt[0]<tjet.Perp()<tpt[1]
    	dy_cut = dy[0]<=abs(tjet.Rapidity()-wjet.Rapidity())<dy[1]

	event.getByLabel (softDropMassLabel, softDropMassHandle)
	topJetMass 	= 	softDropMassHandle.product()

	# For W mass
        event.getByLabel (PrunedMassLabel, PrunedMassHandle)
        prunedJetMass 	= 	PrunedMassHandle.product()

	# For top mass
        event.getByLabel (softDropMassuncorrLabel, softDropMassuncorrHandle)
        topJetMassuncorr 	= 	softDropMassuncorrHandle.product()

	tmass_cut = tmass[0]<topJetMassuncorr[tindexval]<tmass[1]
	wmass_cut = wmass[0]<=prunedJetMass[windexval]<wmass[1]

	#event.getByLabel ( nSubjetsLabel , nSubjetsHandle )
	#nSubjets 		= 	nSubjetsHandle.product()
	#event.getByLabel (minmassLabel, minmassHandle)
	#topJetminmass 	= 	minmassHandle.product()	
	#minmass_cut = minmass[0]<=topJetminmass[tindexval]<minmass[1]
	#nsubjets_cut = nsubjets[0]<=nSubjets[tindexval]<nsubjets[1]
	
	
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
	#	 	SJ_csvvals.append(subjetsCSV[int(SJ_csvs[icsv][tindexval])])
	#	else:
	#	 	SJ_csvvals.append(0.)
	
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
	
	
	event.getByLabel (tau3Label, tau3Handle)
	Tau3		= 	tau3Handle.product() 
 	event.getByLabel (tau2Label, tau2Handle)
	Tau2		= 	tau2Handle.product() 		
	event.getByLabel (tau1Label, tau1Handle)
	Tau1		= 	tau1Handle.product() 
	if Tau1[windexval] != 0:
		tau21val=Tau2[windexval]/Tau1[windexval]
	if Tau2[tindexval] != 0:
		tau32val =  Tau3[tindexval]/Tau2[tindexval]
	
	tau21_cut =  tau21[0]<=tau21val<tau21[1]
	tau32_cut =  tau32[0]<=tau32val<tau32[1]
	
	mtw_cut = 1800<((tjet+wjet).M())


	eta_regions = [eta1,eta2]
	TTRweight = bkg_weight(tjet,TTR,eta_regions)

	ModFile = ROOT.TFile(di+"ModMassFile_rate_"+options.cuts+".root")
	ModPlot = ModFile.Get("rtmass")
	modm = topJetMassuncorr[tindexval]
	if options.modmass=='nominal':
		massw = ModPlot.Interpolate(modm)
	if options.modmass=='up':
		massw = 1 + 0.5*(ModPlot.Interpolate(modm)-1)
	if options.modmass=='down':
		massw = max(0.0,1 + 1.5*(ModPlot.Interpolate(modm)-1))
	if options.modmass=='none':
		massw = 1

#SFTtag
	weightSFt = 1.0	
	if tmass_cut and tau32_cut and sjbtag_cut: 
		if options.set!="data" and options.cuts=="default" and options.set!="QCD":
			#top scale factor reweighting done here
			SFT = SFT_Lookup( tjet.Perp() )
			weightSFt = SFT[0]
			weight*=weightSFt

	ht = tjet.Perp() + wjet.Perp()
	if wpt_cut and tpt_cut and dy_cut and tmass_cut:
		if tname != 'none' and options.set!='data' :
			#Trigger reweighting done here
			TRW = Trigger_Lookup( ht , TrigPlot )[0]
			weight*=TRW

#Define selections
	fullsel =  wpt_cut and tpt_cut and dy_cut and tmass_cut and tau21_cut and  tau32_cut and sjbtag_cut and wmass_cut
    	dyfullsel =  wpt_cut and tpt_cut  and tmass_cut and wmass_cut
    	dysemisel = wpt_cut and tpt_cut  and tmass_cut and wmass_cut and mtw_cut
    	tmasssel =  wpt_cut and tpt_cut and dy_cut  and  tau32_cut and sjbtag_cut
	tmassStackSel = wpt_cut and tpt_cut and dy_cut  and tau21_cut and tau32_cut and sjbtag_cut and wmass_cut
	tmassBEStackSel = wpt_cut and tpt_cut and dy_cut and tau21_cut and wmass_cut
    	tau21sel =  wpt_cut and tpt_cut and dy_cut  and wmass_cut
    	tau32sel =  wpt_cut and tpt_cut and dy_cut and tmass_cut  and sjbtag_cut
    	wmasssel =  wpt_cut and tpt_cut and dy_cut  and tau21_cut
	sjbtagsel =  wpt_cut and tpt_cut and dy_cut and tmass_cut and tau32_cut

#Fill histograms-------
	weight = weightSFt
	if fullsel:
		doneAlready = True
	if tau21sel:
		Tau_21.Fill(tau21val,weight)
	if tau32sel:
		Tau_32.Fill(tau32val,weight)
	if tmasssel:
		Mt.Fill(topJetMassuncorr[tindexval],weight)
	if wmasssel:
		Mw.Fill(topJetMassuncorr[windexval],weight)
	if sjbtagsel:
		MaxSJCSV.Fill(SJ_csvmax,weight)
	if dyfullsel:
		dyfull.Fill(abs(tjet.Rapidity()-wjet.Rapidity()),weight)
	if dysemisel:
		dysemi.Fill(abs(tjet.Rapidity()-wjet.Rapidity()),weight)
	if tmassBEStackSel:
		QCDbkgMtStack.Fill(topJetMassuncorr[tindexval],TTRweight*weight*massw)
	if tmassStackSel:
		MtStack.Fill(topJetMassuncorr[tindexval],weight)
		
				
		
	
#ONLY USED FOR DEBUGGING	
#for i in infoArray:
#	print i
f.cd()
f.Write()
f.Close()


