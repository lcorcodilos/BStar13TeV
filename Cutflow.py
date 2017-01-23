#!/usr/bin/env python

import os
import array
import glob
import math
import ROOT
import sys
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True
from ROOT import *
from array import *
gROOT.Macro("rootlogon.C")

Data = {}
QCD = {}
ttbar = {}
SR1200 = {}
SR1400 = {}
SR1600 = {}
SR1800 = {}
SR2000 = {}
SR2200 = {}
SR2400 = {}
SR2600 = {}
SR2800 = {}
SR3000 = {}
singletop = {}


#Data['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerdata_Trigger_nominal_none_PSET_default_kin.root')
QCD['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerQCD_Trigger_nominal_none_PSET_default_kin.root')
ttbar['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_default_kin.root')
SR1200['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerweightedsignalLH1200_Trigger_nominal_none_PSET_default_kin.root')
SR1400['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerweightedsignalLH1400_Trigger_nominal_none_PSET_default_kin.root')
SR1600['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerweightedsignalLH1600_Trigger_nominal_none_PSET_default_kin.root')
SR1800['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerweightedsignalLH1800_Trigger_nominal_none_PSET_default_kin.root')
SR2000['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerweightedsignalLH2000_Trigger_nominal_none_PSET_default_kin.root')
SR2200['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerweightedsignalLH2200_Trigger_nominal_none_PSET_default_kin.root')
SR2400['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerweightedsignalLH2400_Trigger_nominal_none_PSET_default_kin.root')
SR2600['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerweightedsignalLH2600_Trigger_nominal_none_PSET_default_kin.root')
SR2800['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerweightedsignalLH2800_Trigger_nominal_none_PSET_default_kin.root')
SR3000['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerweightedsignalLH3000_Trigger_nominal_none_PSET_default_kin.root')
#singletop['file'] = ROOT.TFile('rootfiles/27203pb/TWanalyzerweightedsingletop_Trigger_nominal_none_PSET_default_kin.root')

#Blinded so doesn't currently have data
mainDict = {'QCD':QCD,'ttbar':ttbar,'SR1200':SR1200,'SR1400':SR1400,'SR1600':SR1600,'SR1800':SR1800,'SR2000':SR2000,'SR2200':SR2200,'SR2400':SR2400,'SR2600':SR2600,'SR2800':SR2800,'SR3000':SR3000}#, 'singletop':singletop}
keys = mainDict.keys()

cuts = ['Mtw_cut1','Mtw_cut2','Mtw_cut3','Mtw_cut4','Mtw_cut5','Mtw_cut6','Mtw_cut9','Mtw_cut10']

#mainDict['Data']['Mtw_cut1'] = mainDict['Data']['file'].Get('Mtw_cut1')
#testing = mainDict['Data']['Mtw_cut1']
#c = TCanvas()
#testing.Draw()
#c.Print("testerBrah.root",'root')

#test = mainDict['Data']['Mtw_cut1_Int'] = mainDict['Data']['Mtw_cut1'].Integral()

print 'x-----------------------------------------------------------------------------------------------------------------------------x'
print 'x							Cutflow								      x'
print 'x-----------------------------------------------------------------------------------------------------------------------------x'

print '| Sample \t | 2jet \t | pT \t | deltaY \t | Mtop \t | Mw \t | t2/t1 \t | SJCSVMax \t | t3/t2 \t |'

for k in keys:
	mainDict[k]['name'] = k

	for c in cuts:

		mainDict[k][c] = mainDict[k]['file'].Get(c)		#get the cut histogram 
									# - ex. mainDict['Data']['Mtw_cut1'] = mainDict['Data']['file'].Get('Mtw_cut1')
		mainDict[k][c+'_Int'] = mainDict[k][c].Integral()	#get the integral of the cut - ex. mainDict['Data']['Mtw_cut1'] = mainDict['Data']['file'].Get('Mtw_cut1')
									# - ex. mainDict['Data']['Mtw_cut1_Int'] = mainDict['Data']['Mtw_cut1'].Integral()
for k in keys:
	print '|-----------------------------------------------------------------------------------------------------------------------------|'
	print '| ' + mainDict[k]['name'] + ' \t \t | ',
	for c in cuts:
		print "{0:d}".format(int(mainDict[k][c+'_Int']))+ ' \t | ',
	print ''				#prints new line

print 'x------------------------------------------------------------------------------------------------------------------------x' 


