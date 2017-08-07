

###################################################################
##								 ##
## Name: Tagrate_Maker_B.py				         ##
## Author: Kevin Nash 						 ##
## Date: 5/28/2015						 ##
## Purpose: This program takes the root files created by  	 ##
##          TBTrigger.py and divides the histograms to create	 ##
##	    trigger turn on curves 				 ##
##								 ##
###################################################################

import os
import array
import glob
import math
import ROOT
import sys
from array import *
from ROOT import *
from optparse import OptionParser

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
                  default	=	'signalright2000',
                  dest		=	'set',
                  help		=	'dataset (ie data,ttbar etc)')

parser.add_option('-d', '--disc', metavar='F', type='string', action='store',
                  default	=	'',
                  dest		=	'disc',
                  help		=	'empty, untrig, or ttags')

parser.add_option('-b', '--bx', metavar='F', type='string', action='store',
                  default	=	'25ns',
                  dest		=	'bx',
                  help		=	'bunch crossing 50ns or 25ns')

(options, args) = parser.parse_args()

gROOT.Macro("rootlogon.C")
# Create the outfiles that will store fit and sigma data for use later
c1 = TCanvas('c1', 'Data Full selection vs b pt tagging background', 700, 500)

leg = TLegend(0.0, 0.0, 1.0, 1.0)
leg.SetFillColor(0)
leg.SetBorderSize(0)

trigs = [
#"HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p41_v1ORHLT_PFHT900_v1"
#"HLT_PFHT800_v2",
'HLT_PFHT900ORHLT_AK8PFJet450_pre_HLT_PFHT475_v3'
]
fvec = []
TR = []

Trigfile = ROOT.TFile( "Triggerweight_"+options.set+options.disc+".root", "recreate" )
for ifile in range(0,len(trigs)) :

	fvec.append(ROOT.TFile("triggerstudies/TWTrigger"+options.set+trigs[ifile]+".root"))
	HT = fvec[ifile].Get('Ht'+options.disc)
	HTpre = fvec[ifile].Get('Htpre'+options.disc)
	HT.Rebin(5)
	HTpre.Rebin(5)
	
	print trigs[ifile]
	print 'Full integral: ' + str(HT.Integral()/HTpre.Integral())
	print 'Partial integral: ' + str(HT.Integral(HT.FindBin(550),HT.FindBin(2000))/HTpre.Integral(HT.FindBin(550),HT.FindBin(2000)))
	TR.append(HT.Clone())
	TR[ifile].Divide(TR[ifile],HTpre,1.0,1.0,'B')

	TR[ifile].SetLineColor(ifile+1)
	TR[ifile].SetMarkerColor(ifile+1)
	if ifile >= 4:
		TR[ifile].SetLineColor(ifile+2)
		TR[ifile].SetMarkerColor(ifile+2)
		
	leg.AddEntry(TR[ifile] , trigs[ifile].replace('OR',' OR '), 'p')

	Tline = TLine(600.0, 0.5, 820.0, 1.01)
	Tline.SetLineColor(kRed)
	Tline.SetLineStyle(2)
	c1.cd()

		
	TR[ifile].SetMaximum(1.01)
	TR[ifile].SetMinimum(0.2)
	TR[ifile].GetXaxis().SetRangeUser(300,2000)
	TR[ifile].SetStats(0)
	TR[ifile].SetTitle(';p_{T_{jet1}} + p_{T_{jet2}} (GeV);Efficiency')
	if ifile ==0:
		TR[ifile].SetMarkerStyle(8)
		TR[ifile].Draw("p")
	else:
		TR[ifile].Draw("psame")
	gPad.SetLeftMargin(.15)
	gPad.SetBottomMargin(.17) 
	TR[ifile].GetYaxis().SetTitleOffset(0.8)

        Trigfile.cd()
	TR[ifile].Write("TriggerWeight_"+trigs[ifile])
	c3 = TCanvas('c3', 'Data Full selection vs t pt tagging background', 700, 500)
	TR[ifile].Draw("")
	c3.Print('plots/Trigger_'+trigs[ifile]+options.disc+'.root', 'root')
	c3.Print('plots/Trigger_'+trigs[ifile]+options.disc+'.pdf', 'pdf')
#Tline.Draw()
c1.Print('plots/Trigger_TEMP'+options.disc+'.root', 'root')
c1.Print('plots/Trigger_TEMP'+options.disc+'.pdf', 'pdf')

c2 = TCanvas('c2', 'Data Full selection vs t pt tagging background', 700, 200)
leg.Draw()
c2.Print('plots/Trigger_TEMP_legend.pdf'+options.disc, 'pdf')







