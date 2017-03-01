
import os
import array
import glob
import math
import ROOT
import sys
from array import *
from ROOT import *

leg = TLegend(0.5, 0.5, 0.84, 0.84)
leg.SetFillColor(0)
leg.SetBorderSize(0)

ROOT.gROOT.Macro("rootlogon.C")

fdata = ROOT.TFile("DataPU69000.root")
fdataup = ROOT.TFile("DataPU72450.root")
fdatadown = ROOT.TFile("DataPU65550.root")

fttbar  = ROOT.TFile("TWPileupttbar.root")


output = ROOT.TFile( "PileUp_Ratio_ttbar.root", "recreate" )

output.cd()

# Get numerators and denominators for each eta region

ndata = fdata.Get("pileup")
ndataup = fdataup.Get("pileup")
ndatadown = fdatadown.Get("pileup")

ndata.Sumw2()
ndataup.Sumw2()
ndatadown.Sumw2()

ndata.Scale(1./ndata.Integral())
ndataup.Scale(1./ndataup.Integral())
ndatadown.Scale(1./ndatadown.Integral())

dttbar = fttbar.Get("npvtruehistUW")
dttbar.Scale(1./dttbar.Integral())

ttbar_pileup_reweight = ndata.Clone("Pileup_Ratio")
ttbar_pileup_reweight.Divide(dttbar)

ttbar_pileup_reweight.Write()
ttbar_pileup_reweight_up = ndataup.Clone("Pileup_Ratio_up")
ttbar_pileup_reweight_up.Divide(dttbar)
ttbar_pileup_reweight_up.Write()

ttbar_pileup_reweight_down = ndatadown.Clone("Pileup_Ratio_down")
ttbar_pileup_reweight_down.Divide(dttbar)
ttbar_pileup_reweight_down.Write()


files = [
ROOT.TFile("TWPileupsignalLH1200.root"),
ROOT.TFile("TWPileupsignalRH1200.root"),
ROOT.TFile("TWPileupsignalLH1400.root"),
ROOT.TFile("TWPileupsignalRH1400.root"),
ROOT.TFile("TWPileupsignalLH1600.root"),
ROOT.TFile("TWPileupsignalRH1600.root"),
ROOT.TFile("TWPileupsignalLH1800.root"),
ROOT.TFile("TWPileupsignalRH1800.root"),
ROOT.TFile("TWPileupsignalLH2000.root"),
ROOT.TFile("TWPileupsignalRH2000.root"),
ROOT.TFile("TWPileupsignalLH2200.root"),
ROOT.TFile("TWPileupsignalRH2200.root"),
ROOT.TFile("TWPileupsignalLH2400.root"),
ROOT.TFile("TWPileupsignalRH2400.root"),
ROOT.TFile("TWPileupsignalLH2600.root"),
ROOT.TFile("TWPileupsignalRH2600.root"),
ROOT.TFile("TWPileupsignalLH2800.root"),
ROOT.TFile("TWPileupsignalRH2800.root"),
ROOT.TFile("TWPileupsignalLH3000.root"),
ROOT.TFile("TWPileupsignalRH3000.root")
#ROOT.TFile("TWPileupBprimeBToTW1200.root"),
#ROOT.TFile("TWPileupBprimeBToTW1400.root"),
#ROOT.TFile("TWPileupBprimeBToTW1600.root"),
#ROOT.TFile("TWPileupBprimeBToTW1800.root"),
#ROOT.TFile("TWPileupBprimeTToTW1200.root"),
#ROOT.TFile("TWPileupBprimeTToTW1400.root"),
#ROOT.TFile("TWPileupBprimeTToTW1600.root"),
#ROOT.TFile("TWPileupBprimeTToTW1800.root")

]

names = [
"PileUp_Ratio_signalLH1200.root",
"PileUp_Ratio_signalRH1200.root",
"PileUp_Ratio_signalLH1400.root",
"PileUp_Ratio_signalRH1400.root",
"PileUp_Ratio_signalLH1600.root",
"PileUp_Ratio_signalRH1600.root",
"PileUp_Ratio_signalLH1800.root",
"PileUp_Ratio_signalRH1800.root",
"PileUp_Ratio_signalLH2000.root",
"PileUp_Ratio_signalRH2000.root",
"PileUp_Ratio_signalLH2200.root",
"PileUp_Ratio_signalRH2200.root",
"PileUp_Ratio_signalLH2400.root",
"PileUp_Ratio_signalRH2400.root",
"PileUp_Ratio_signalLH2600.root",
"PileUp_Ratio_signalRH2600.root",
"PileUp_Ratio_signalLH2800.root",
"PileUp_Ratio_signalRH2800.root",
"PileUp_Ratio_signalLH3000.root",
"PileUp_Ratio_signalRH3000.root"
#"PileUp_Ratio_BprimeBToTW1200.root",
#"PileUp_Ratio_BprimeBToTW1400.root",
#"PileUp_Ratio_BprimeBToTW1600.root",
#"PileUp_Ratio_BprimeBToTW1800.root",
#"PileUp_Ratio_BprimeTToTW1200.root",
#"PileUp_Ratio_BprimeTToTW1400.root",
#"PileUp_Ratio_BprimeTToTW1600.root",
#"PileUp_Ratio_BprimeTToTW1800.root",
]

dhists = []
dhistsalt = []
for ifile in range(0,len(files)):
	outputsig = ROOT.TFile(names[ifile] , "recreate" )
	outputsig.cd()



	dhists.append(files[ifile].Get("npvtruehistUW"))
	dhists[ifile].Scale(1./dhists[ifile].Integral())

	Pileup_Ratio = ndata.Clone("Pileup_Ratio")
	Pileup_Ratio_up = ndataup.Clone("Pileup_Ratio_up")
	Pileup_Ratio_down = ndatadown.Clone("Pileup_Ratio_down")

	Pileup_Ratio.Divide(dhists[ifile])
	Pileup_Ratio_up.Divide(dhists[ifile])
	Pileup_Ratio_down.Divide(dhists[ifile])

	Pileup_Ratio.Write()
	Pileup_Ratio_up.Write()
	Pileup_Ratio_down.Write()

	#outputsig.Write()
	outputsig.Close()

