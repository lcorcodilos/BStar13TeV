#! /usr/bin/env python

###################################################################
##								 ##
## Name: TBanalyzer.py	   			                 ##
## Author: Kevin Nash 						 ##
## Date: 6/5/2012						 ##
## Purpose: This program performs the main analysis.  		 ##
##	    It takes the tagrates created by  	 		 ##
##          TBrate_Maker.py stored in fitdata, and uses 	 ##
##          them to weigh pre b tagged samples to create a 	 ##
##	    QCD background estimate along with the full event    ##
##	    selection to product Mtb inputs to Theta		 ##
##								 ##
###################################################################

import os
import glob
import math
import copy
import random
import time
from math import sqrt
#import quickroot
#from quickroot import *
import datetime
import ROOT 
from ROOT import TLorentzVector,TH1F,TH2F,TTree,TFile,gROOT

import sys
from DataFormats.FWLite import Events, Handle
from optparse import OptionParser

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
                  default	=	'THB',
                  dest		=	'set',
                  help		=	'data or ttbar')

parser.add_option('-g', '--grid', metavar='F', type='string', action='store',
                  default	=	'off',
                  dest		=	'grid',
                  help		=	'running on grid off or on')

parser.add_option('-J', '--JES', metavar='F', type='string', action='store',
                  default	=	'nominal',
                  dest		=	'JES',
                  help		=	'nominal, up, or down')
parser.add_option('-R', '--JER', metavar='F', type='string', action='store',
                  default	=	'nominal',
                  dest		=	'JER',
                  help		=	'nominal, up, or down')



(options, args) = parser.parse_args()

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


mod = ''
post = ''
if options.JES!='nominal':
	mod = mod + 'JES_' + options.JES
	post='jes'+options.JES
if options.JER!='nominal':
	mod = mod + 'JER_' + options.JER
	post='jer'+options.JER


#Load up cut values based on what selection we want to run 
# Cuts = LoadCuts(options.set)

#events = Events(files)
if options.set=='QCDHT500':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/QCDHT500/B2GEDMNtuple_1.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/QCDHT500/B2GEDMNtuple_2.root"
			]
if options.set=='QCDHT700':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/QCDHT700/B2GEDMNtuple_1.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/QCDHT700/B2GEDMNtuple_2.root"
			]
if options.set=='QCDHT1000':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/QCDHT1000/B2GEDMNtuple_1.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/QCDHT1000/B2GEDMNtuple_2.root"
			]
if options.set=='QCDHT1500':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/QCDHT1500/B2GEDMNtuple_1.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/QCDHT1500/B2GEDMNtuple_2.root"
			]
if options.set=='QCDHT2000':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/QCDHT2000/B2GEDMNtuple_3.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/QCDHT2000/B2GEDMNtuple_4.root"
			]




if options.set=='ttbar':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/ttbar/B2GEDMNtuple_1.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/ttbar/B2GEDMNtuple_2.root"
			]


if options.set=='dataB':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataB/B2GEDMNtuple_1.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataB/B2GEDMNtuple_2.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataB/B2GEDMNtuple_3.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataB/B2GEDMNtuple_4.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataB/B2GEDMNtuple_5.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataB/B2GEDMNtuple_6.root"
			]
if options.set=='dataC':
	b2ganafwf =		[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataC/B2GEDMNtuple_1.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataC/B2GEDMNtuple_2.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataC/B2GEDMNtuple_3.root"
			]
if options.set=='dataD':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataD/B2GEDMNtuple_1.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataD/B2GEDMNtuple_2.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataD/B2GEDMNtuple_3.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataD/B2GEDMNtuple_4.root"
			]
if options.set=='dataE':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataE/B2GEDMNtuple_1.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataE/B2GEDMNtuple_2.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataE/B2GEDMNtuple_3.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataE/B2GEDMNtuple_4.root"
			]
if options.set=='dataF':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataF/B2GEDMNtuple_1.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataF/B2GEDMNtuple_2.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataF/B2GEDMNtuple_3.root"
			]
if options.set=='dataG':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataG/B2GEDMNtuple_1.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataG/B2GEDMNtuple_2.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataG/B2GEDMNtuple_3.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataG/B2GEDMNtuple_4.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataG/B2GEDMNtuple_5.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataG/B2GEDMNtuple_6.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataG/B2GEDMNtuple_7.root"
			]
if options.set=='dataH':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataH/B2GEDMNtuple_1.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataH/B2GEDMNtuple_2.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataH/B2GEDMNtuple_3.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataH/B2GEDMNtuple_4.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataH/B2GEDMNtuple_5.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataH/B2GEDMNtuple_6.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataH/B2GEDMNtuple_7.root",
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataH/B2GEDMNtuple_8.root"
			]
if options.set=='dataH2':
	b2ganafwf = 	[
			"/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/tempB2Gntuples/dataH2/B2GEDMNtuple_1.root"
			]



events = Events(b2ganafwf)

PDFup = 0.0
PDFdown = 0.0
PDFnom = 0.0
count = 0




reconpvHandle 	= 	Handle (  "int"  )
reconpvLabel  	= 	( "vertexInfo" , "npv")


truenpvHandle 	= 	Handle (  "int"  )
truenpvLabel  	= 	( "eventUserData" , "puNtrueInt")

f = TFile( "THBnpvtester"+options.set+".root", "recreate" )



truenpvhistpre  = TH1F("truenpvhistpre",		"",     	  	      	100, 0, 100.0 )
truenpvhistpost  = TH1F("truenpvhistpost",		"",     	  	      	100, 0, 100.0 )
truenpvhistpostup  = TH1F("truenpvhistpostup",		"",     	  	      	100, 0, 100.0 )
truenpvhistpostdown  = TH1F("truenpvhistpostdown",		"",     	  	      	100, 0, 100.0 )

reconpvhistpre  = TH1F("reconpvhistpre",		"",     	  	      	100, 0, 100.0 )
reconpvhistpost  = TH1F("reconpvhistpost",		"",     	  	      	100, 0, 100.0 )
reconpvhistpostup  = TH1F("reconpvhistpostup",		"",     	  	      	100, 0, 100.0 )
reconpvhistpostdown  = TH1F("reconpvhistpostdown",		"",     	  	      	100, 0, 100.0 )



truenpvhistpre.Sumw2()
truenpvhistpost.Sumw2()
truenpvhistpostup.Sumw2()
truenpvhistpostdown.Sumw2()

reconpvhistpre.Sumw2()
reconpvhistpost.Sumw2()
reconpvhistpostup.Sumw2()
reconpvhistpostdown.Sumw2()





	

PUFile = TFile(di+"PileUp_Ratio_ttbar.root")
PUplotvec = [PUFile.Get("Pileup_Ratio"),PUFile.Get("Pileup_Ratio_up"),PUFile.Get("Pileup_Ratio_down")]
		

for event in events:
  	count+=1
    	if count % 1000 == 0 :
      		print  '--------- Processing Event ' + str(count) #+'   -- percent complete ' + str(100*count/totevents) + '% -- '

	event.getByLabel (reconpvLabel, reconpvHandle)
	reconpv 	= 	reconpvHandle.product()
			
	puweight = 1.0
	if (options.set).find('data')==-1:
		event.getByLabel (truenpvLabel, truenpvHandle)
		truenpv 	= 	truenpvHandle.product()
		#print truenpv[0]



		puweightvec = PU_Lookup(truenpv[0],PUplotvec)
			
		puweight = puweightvec[0]
		puweightup = puweightvec[1]
		puweightdown = puweightvec[2]

		reconpvhistpre.Fill(reconpv[0])
		reconpvhistpostup.Fill(reconpv[0],puweightup)
		reconpvhistpostdown.Fill(reconpv[0],puweightdown)

	
		truenpvhistpre.Fill(truenpv[0])
		truenpvhistpost.Fill(truenpv[0],puweight)
		truenpvhistpostup.Fill(truenpv[0],puweightup)
		truenpvhistpostdown.Fill(truenpv[0],puweightdown)



	reconpvhistpost.Fill(reconpv[0],puweight)

	#print reconpv[0]


f.cd()
f.Write()
f.Close()

