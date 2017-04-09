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
from ROOT import std,ROOT,TFile,TLorentzVector,TMath,gROOT, TF1,TH1F,TH1D,TH2F,TH2D
from ROOT import TVector
from ROOT import TFormula

import sys
from DataFormats.FWLite import Events, Handle
from optparse import OptionParser
from array import *

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
                  default	=	'data',
                  dest		=	'set',
                  help		=	'dataset (ie data,ttbar etc)')
parser.add_option('-u', '--ptreweight', metavar='F', type='string', action='store',
                  default	=	'none',
                  dest		=	'ptreweight',
                  help		=	'on or off')

parser.add_option('-t', '--tname', metavar='F', type='string', action='store',
                   default	=	'HLT_PFHT800_v3',
                   dest		=	'tname',
                   help		=	'trigger name')
parser.add_option('-S', '--split', metavar='F', type='string', action='store',
                  default	=	'file',
                  dest		=	'split',
                  help		=	'split by event of file')
parser.add_option('-b', '--bx', metavar='F', type='string', action='store',
                   default	=	'25ns',
                   dest		=	'bx',
                   help		=	'bunch crossing 50ns or 25ns')

parser.add_option('-n', '--num', metavar='F', type='string', action='store',
                  default	=	'all',
                  dest		=	'num',
                  help		=	'job number')
parser.add_option('-j', '--jobs', metavar='F', type='string', action='store',
                  default	=	'1',
                  dest		=	'jobs',
                  help		=	'number of jobs')
parser.add_option('-g', '--grid', metavar='F', type='string', action='store',
                  default	=	'off',
                  dest		=	'grid',
                  help		=	'running on grid off or on')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'rate_default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-x', '--pileup', metavar='F', type='string', action='store',
                  default	=	'on',
                  dest		=	'pileup',
                  help		=	'If not data do pileup reweighting?')



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
 		
trig='none'
if options.set!= 'data' and options.tname!='none': 
 	if options.tname=='HLT_PFHT800_v3':
 		trig = 'nominal'
 	elif options.tname!= []:
 		trig = 'tnamestr'
 		
if tnamestr=='HLT_PFHT800_v3':
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

#Load up cut values based on what selection we want to run 
Cons = LoadConstants()
lumi = Cons['lumi']
Lumi = str(lumi/1000)+"fb"

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


#For large datasets we need to parallelize the processing
jobs=int(options.jobs)
if jobs != 1:
	num=int(options.num)
	jobs=int(options.jobs)
	print "Running over " +str(jobs)+ " jobs"
	print "This will process job " +str(num)
else:
	print "Running over all events"


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

TstrHandle 	= 	Handle (  "vector<string>"  )
TstrLabel  	= 	( "TriggerUserData" , "triggerNameTree")

TbitHandle 	= 	Handle (  "vector<float>"  )
TbitLabel  	= 	( "TriggerUserData" , "triggerBitTree")


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

#topMassHandle 	= 	Handle (  "vector<float> "  )
#topMassLabel  	= 	( "jetsAK8" , "jetAK8topMass")

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

#Create the output file
if jobs != 1:
	f = TFile( "TWratefile"+options.set+"_job"+options.num+"of"+options.jobs+"_PSET_"+options.cuts+".root", "recreate" )
else:
	f = TFile( "TWratefile"+options.set+"_PSET_"+options.cuts+".root", "recreate" )




print "Creating histograms"

#Define Histograms
f.cd()
#---------------------------------------------------------------------------------------------------------------------#
pteta1pretag          = TH1D("pteta1pretag",           "t Probe pt in 0<Eta<0.8",             400,  0,  2000 )
pteta2pretag          = TH1D("pteta2pretag",           "t Probe pt in 0.8<Eta<2.4",             400,  0,  2000 )

pteta1          = TH1D("pteta1",           "t pt in 0<Eta<0.8",             400,  0,  2000 )
pteta2          = TH1D("pteta2",           "t pt in 0.8<Eta<2.4",             400,  0,  2000 )

Mpre          = TH1D("Mpre",           "top mass",             400,  110,  210 )
Mpre.Sumw2()

MpostFull          = TH1D("MpostFull",           "t pt in 0<Eta<0.8",             400,  110,  210 )
MpostFull.Sumw2()


MpostPartial          = TH1D("MpostPartial",           "t pt in 0<Eta<0.8",             400,  110,  210 )
MpostPartial.Sumw2()


pteta1pretag.Sumw2()
pteta2pretag.Sumw2()


pteta1.Sumw2()
pteta2.Sumw2()


MtwtptcomparepreSB1e1    = TH2F("MtwtptcomparepreSB1e1",  "Comparison wpt and Mtw",   		400,0,2000,  140,  500,  4000 )
MtwtptcomparepostSB1e1    = TH2F("MtwtptcomparepostSB1e1",  "Comparison wpt and Mtw",   		400,0,2000,  140,  500,  4000 )

MtwtptcomparepreSB1e1.Sumw2()
MtwtptcomparepostSB1e1.Sumw2()

MtwtptcomparepreSB1e2    = TH2F("MtwtptcomparepreSB1e2",  "Comparison wpt and Mtw",   		400,0,2000,  140,  500,  4000 )
MtwtptcomparepostSB1e2    = TH2F("MtwtptcomparepostSB1e2",  "Comparison wpt and Mtw",   		400,0,2000,  140,  500,  4000 )

MtwtptcomparepreSB1e2.Sumw2()
MtwtptcomparepostSB1e2.Sumw2()

nev = TH1F("nev",	"nev",		1, 0, 1 )


#---------------------------------------------------------------------------------------------------------------------#

# loop over events
#---------------------------------------------------------------------------------------------------------------------#

count = 0
jobiter = 0
print "Start looping"
#initialize the ttree variables
tree_vars = {"wpt":array('d',[0.]),"wmass":array('d',[0.]),"tpt":array('d',[0.]),"tmass":array('d',[0.]),"tau32":array('d',[0.]),"tau21":array('d',[0.]),"sjbtag":array('d',[0.]),"weight":array('d',[0.])}#,"nsubjets":array('d',[0.])


Tree = Make_Trees(tree_vars)
totevents = events.size()

usegenweight = False
#if options.set == "QCDFLAT7000":
#	usegenweight = True
#	print "Using gen weight"
#print str(totevents)  +  ' Events total'

nev.SetBinContent(1,totnev)
for event in events:
    count	= 	count + 1

   # Uncomment for a low count test run
    #if count > 5000:
	#break

    if count % 100000 == 0 :
      print  '--------- Processing Event ' + str(count) +'   -- percent complete ' + str(100*count/totevents) + '% -- '

    #Here we split up event processing based on number of jobs 
    #This is set up to have jobs range from 1 to the total number of jobs (ie dont start at job 0)
    if jobs != 1 and options.split=="event":
    	if (count - 1) % jobs == 0:
		jobiter+=1
	count_index = count - (jobiter-1)*jobs
	if count_index!=num:
		continue 
	
    #We load up the relevant handles and labels and create collections
  
    
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

    AK8LV = Makelv(AK8HL,event)

    if len(AK8LV)==0:
 	continue



    tindex,windex = Hemispherize(AK8LV,AK8LV)


    wJetsh1=[]
    wJetsh0=[]
    topJetsh1=[]
    topJetsh0=[]

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

    doneAlready = False

    #We consider both the case that the b is the leading (highest pt) jet (hemis0) and the case where the top is the leading jet (hemis1)
    for hemis in ['hemis0','hemis1']:
    	if hemis == 'hemis0'   :
		if not njets11w0:
			continue 
		#The Ntuple entries are ordered in pt, so [0] is the highest pt entry
		#We are calling a candidate b jet (highest pt jet in hemisphere0)  
		wjet = wJetsh0[0]
		tjet = topJetsh1[0]
     
 		tindexval = tindex[1][0]
 		windexval = windex[0][0]

    	if hemis == 'hemis1' and doneAlready == False  :
		if not njets11w1:
			continue 
		wjet = wJetsh1[0]
		tjet = topJetsh0[0]

  		tindexval = tindex[0][0]
 		windexval = windex[1][0]

	elif hemis == 'hemis1' and doneAlready == True:
		continue

	if abs(wjet.Eta())>2.40 or abs(tjet.Eta())>2.40:
		continue

    	weight=1.0
	#Cuts are loaded from the Bstar_Functions.py file
	#here wpt[0] is 370 and wpt[1] is inf, so we are making sure the b pt is at least 370 GeV
    	wpt_cut = wpt[0]<wjet.Perp()<wpt[1]
    	tpt_cut = tpt[0]<tjet.Perp()<tpt[1]
    	dy_cut = dy[0]<=abs(tjet.Rapidity()-wjet.Rapidity())<dy[1]
    	#We first perform the top and b candidate pt cuts and the deltaY cut
    	if wpt_cut and tpt_cut and dy_cut: 
		weightSFt = 1.0
		weightSFtdown = 1.0
		weightSFtup = 1.0		
		if options.set!="data":
			#Pileup reweighting is done here 

			event.getByLabel (puLabel, puHandle)
		    	PileUp 		= 	puHandle.product()
		     	bin1 = PilePlot.FindBin(PileUp[0]) 

			if options.pileup != 'off':
				weight *= PilePlot.GetBinContent(bin1)
			if options.cuts=="rate_default" and options.set.find("QCD") == -1:
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

         	#event.getByLabel ( nSubjetsLabel , nSubjetsHandle )
     		#nSubjets 		= 	nSubjetsHandle.product()
         	#event.getByLabel (minmassLabel, minmassHandle)
     		#topJetminmass 	= 	minmassHandle.product()

 		tmass_cut = tmass[0]<puppiJetMass[tindexval]<tmass[1]
		#nsubjets_cut = nsubjets[0]<=nSubjets[tindexval]<nsubjets[1]

		#Now we start top-tagging.  In this file, we use a sideband based on inverting some top-tagging requirements
		if tmass_cut:
			#minmass_cut = minmass[0]<=topJetminmass[tindexval]<minmass[1]
			ht = tjet.Perp() + wjet.Perp()
			weighttrigup=1.0
			weighttrigdown=1.0
			if tname != [] and options.set!='data' :
				#Trigger reweighting done here
				TRW = Trigger_Lookup( ht , TrigPlot )[0]
				TRWup = Trigger_Lookup( ht , TrigPlot )[1]
				TRWdown = Trigger_Lookup( ht , TrigPlot )[2]

				weighttrigup=weight*TRWup
				weighttrigdown=weight*TRWdown
				weight*=TRW

			if False:#options.ptreweight == "on":
				#ttbar pt reweighting done here
				event.getByLabel( GenLabel, GenHandle )
				GenParticles = GenHandle.product()
				PTW = PTW_Lookup( GenParticles )
				weight*=PTW

			
			weightSFtup=weight*weightSFtup
			weightSFtdown=weight*weightSFtdown
			weight*=weightSFt

			weighttrigup*=weightSFt
			weighttrigdown*=weightSFt

     			#event.getByLabel (Label, subjets0indexHandle)
     			#subjets0index 		= 	subjets0indexHandle.product() 

     			#event.getByLabel (subjets1indexLabel, subjets1indexHandle)
     			#subjets1index 		= 	subjets1indexHandle.product() 

     			#event.getByLabel (subjets2indexLabel, subjets2indexHandle)
     			#subjets2index 		= 	subjets2indexHandle.product() 

     			#event.getByLabel (subjets3indexLabel, subjets3indexHandle)
     			#subjets3index 		= 	subjets3indexHandle.product()


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
					if type(wmass[0]) is float:
						wmass_cut = wmass[0]<=puppiJetMass[windexval]<wmass[1]
					elif type(wmass[0]) is list:
				        	wmass_cut = wmass[0][0]<=puppiJetMass[windexval]<wmass[0][1] or wmass[1][0]<=puppiJetMass[windexval]<wmass[1][1] 
					else:
						print "wmass type error"				        
					FullTop = sjbtag_cut and tau32_cut
				        if wmass_cut:
					        if tau21_cut:
						        eta1_cut = eta1[0]<=abs(tjet.Eta())<eta1[1]
						        eta2_cut = eta2[0]<=abs(tjet.Eta())<eta2[1]
						        #Extract tags and probes for the average b tagging rate here 
						        #We use two eta regions 
						        if eta1_cut:
							        MtwtptcomparepreSB1e1.Fill(tjet.Perp(),(tjet+wjet).M(),weight)
                        					pteta1pretag.Fill( tjet.Perp(),weight)
							        Mpre.Fill(puppiJetMass[tindexval],weight)
                        					if FullTop :
								        MpostFull.Fill(puppiJetMass[tindexval],weight)
								        MtwtptcomparepostSB1e1.Fill(tjet.Perp(),(tjet+wjet).M(),weight)
                        						pteta1.Fill( tjet.Perp(),weight)
                 
						        if eta2_cut:
							        MtwtptcomparepreSB1e2.Fill(tjet.Perp(),(tjet+wjet).M(),weight)
                        					pteta2pretag.Fill( tjet.Perp(),weight)
							        Mpre.Fill(puppiJetMass[tindexval],weight)
                        					if FullTop :
								        MpostFull.Fill(puppiJetMass[tindexval],weight)
								        MtwtptcomparepostSB1e2.Fill(tjet.Perp(),(tjet+wjet).M(),weight)
                        						pteta2.Fill( tjet.Perp(),weight) 
					            
						        temp_variables = {"wpt":wjet.Perp(),"wmass":puppiJetMass[windexval],"tpt":tjet.Perp(),"tmass":puppiJetMass[tindexval],"tau32":tau32val,"tau21":tau21val,"sjbtag":SJ_csvmax,"weight":weight,}#"nsubjets":nSubjets[tindexval]}
						        for tv in tree_vars.keys():
							        tree_vars[tv][0] = temp_variables[tv]
						        Tree.Fill()
							doneAlready = True
	

f.cd()
f.Write()
f.Close()

print "number of events: " + str(count)
