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



(options, args) = parser.parse_args()


print "Options summary"
print "=================="
for  opt,value in options.__dict__.items():
	#print str(option)+ ": " + str(options[option]) 
	print str(opt) +': '+ str(value)
print "=================="
print ""


if (options.set.find('ttbar') != -1) or (options.set.find('singletop') != -1):
	settype = 'ttbar'
elif (options.set.find('QCD') != -1):
	settype ='ttbar'
	run_b_SF = False
else :	
	settype = options.set

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
tau32 = Cuts['tau32']
tau21 = Cuts['tau21']
sjbtag = Cuts['sjbtag']
wmass = Cuts['wmass']
eta1 = Cuts['eta1']
eta2 = Cuts['eta2']


#Based on what set we want to analyze, we find all Ntuple root files 

if options.set == "data":
	file = TFile(di+"TTrees/TWtreefile_"+options.set+".root")
else:
	file = TFile(di+"TTrees/TWtreefile_"+options.set+"_weighted.root")

tree = file.Get("Tree")

print 'The type of set is ' + settype

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
tree_vars = {	"wpt":array('d',[0.]),
				"wmass":array('d',[0.]),
				"tpt":array('d',[0.]),
				"tmass":array('d',[0.]),
				"tau32":array('d',[0.]),
				"tau21":array('d',[0.]),
				"sjbtag":array('d',[0.]),
				"weight":array('d',[0.])}#,"nsubjets":array('d',[0.])


NewTree = Make_Trees(tree_vars)
totevents = tree.GetEntries()


nev.SetBinContent(1,totevents)
# syntax to get a var(branch value) from the event is event.branchname
for event in tree:
	count	= 	count + 1

	if count % 100000 == 0 :
	  print  '--------- Processing Event ' + str(count) +'   -- percent complete ' + str(100*count/totevents) + '% -- '
	
	wpt_cut = wpt[0]<event.wpt<wpt[1]
    tpt_cut = tpt[0]<event.tpt<tpt[1]
    dy_cut = dy[0]<=event.dy<dy[1]
    #We first perform the top and b candidate pt cuts and the deltaY cut
    if wpt_cut and tpt_cut and dy_cut: 
		tmass_cut = tmass[0]<event.t_SDmass<tmass[1]

		#Now we start top-tagging.  In this file, we use a sideband based on inverting some top-tagging requirements
		if tmass_cut:

			tau32val		= 	event.tau32 
			tau21val		= 	event.tau21 

			tau21_cut =  tau21[0]<=tau21val<tau21[1]
			tau32_cut =  tau32[0]<=tau32val<tau32[1]

			SJ_csvval = event.sjbtag

			sjbtag_cut = sjbtag[0]<SJ_csvval<=sjbtag[1]

			wmass_cut = wmass[0]<=event.wmass<wmass[1]
				        
			FullTop = sjbtag_cut and tau32_cut
			if wmass_cut:
				if tau21_cut:
					eta1_cut = eta1[0]<=abs(event.eta)<eta1[1]
					eta2_cut = eta2[0]<=abs(event.eta)<eta2[1]
					#Extract tags and probes for the average b tagging rate here 
					#We use two eta regions 
					if eta1_cut:
						MtwtptcomparepreSB1e1.Fill(event.tpt,(event.wmass+event.t_LVmass),event.weight)
						pteta1pretag.Fill(event.tpt,event.weight)
						Mpre.Fill(event.t_LVmass,event.weight)
						if FullTop :
							MpostFull.Fill(event.t_LVmass,event.weight)
							MtwtptcomparepostSB1e1.Fill(event.tpt,(event.wmass+event.t_LVmass),event.weight)
							pteta1.Fill( event.tpt,event.weight)
	 
					if eta2_cut:
						MtwtptcomparepreSB1e2.Fill(event.tpt,(event.wmass+event.t_LVmass),event.weight)
						pteta2pretag.Fill( event.tpt,event.weight)
						Mpre.Fill(event.t_LVmass,event.weight)
						if FullTop :
							MpostFull.Fill(event.t_LVmass,event.weight)
							MtwtptcomparepostSB1e2.Fill(event.tpt,(event.wmass+event.t_LVmass),event.weight)
							pteta2.Fill( event.tpt,event.weight) 
					
					temp_variables = {"wpt":event.wpt,"wmass":event.w_SDmass,"tpt":event.tpt,"tmass":event.t_SDmass,"tau32":tau32val,"tau21":tau21val,"sjbtag":SJ_csvval,"weight":event.weight}#"nsubjets":nSubjets[tindexval]}
					for tv in tree_vars.keys():
						tree_vars[tv][0] = temp_variables[tv]
					NewTree.Fill()
					doneAlready = True
	

f.cd()
f.Write()
f.Close()

print "number of events: " + str(count)
