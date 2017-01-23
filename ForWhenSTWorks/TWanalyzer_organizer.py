import os
import array
import glob
import math
import ROOT
import sys
from ROOT import *
from array import *
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-s', '--set', metavar='F', type='string', action='store',
                  default	=	'data',
                  dest		=	'set',
                  help		=	'data or QCD')
parser.add_option('-l', '--lumi', metavar='F', type='string', action='store',
                  default	=	'27203pb',
                  dest		=	'lumi',
                  help		=	'Lumi folder to look in')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
(options, args) = parser.parse_args()

cuts=options.cuts
import Bstar_Functions	
from Bstar_Functions import *

gROOT.Macro("rootlogon.C")

#tMCentries = 6909048
#tSigma = 225.0

Lumi = options.lumi

rebin=2

def Zero(hist):
	for ibin in range(0,hist.GetXaxis().GetNbins()+1):
		hist.SetBinContent(ibin,max(0.0,hist.GetBinContent(ibin)))

LabelsU=['__jes__','__trig__','__ptsmear__']
mass = [1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]

for hand in ["LH"]: #,"left","vector"]:
	if hand == "RH":
		coup = "right"
	elif hand == "LH":
		coup = "left"
	
	output = ROOT.TFile( "limitsetting/theta/BStarCombination/allhadronic"+coup+Lumi+"_mtw.root", "recreate" )
	output.cd()

	Data = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzer"+options.set+"_Trigger_nominal_none_PSET_"+options.cuts+".root")
	Datamodmdown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzer"+options.set+"_Trigger_nominal_none_modm_down_PSET_"+options.cuts+".root")
	Datamodmup = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzer"+options.set+"_Trigger_nominal_none_modm_up_PSET_"+options.cuts+".root")


	TTmc 	= ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_"+options.cuts+".root")
	STmc = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsingletop_Trigger_nominal_none_PSET_"+options.cuts+".root")

	TTmcPtScaleUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_JES_up_PSET_"+options.cuts+".root")
	TTmcPtScaleDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_JES_down_PSET_"+options.cuts+".root")


	TTmcPtSmearUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_JER_up_PSET_"+options.cuts+".root")
	TTmcPtSmearDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_JER_down_PSET_"+options.cuts+".root")


	TTmcQ2ScaleUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbarscaleup_Trigger_nominal_none_PSET_"+options.cuts+".root")
	TTmcQ2ScaleDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbarscaledown_Trigger_nominal_none_PSET_"+options.cuts+".root")

	TTmcPileUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_pileup_up_PSET_"+options.cuts+".root")
	TTmcPileDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_pileup_down_PSET_"+options.cuts+".root")

	#TTmcPDFUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerttbar_none_pdf__up_PSET_"+options.cuts+".root")
	#TTmcPDFDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerttbar_none_pdf__down_PSET_"+options.cuts+".root")

	TTmcFS = TTmc.Get("Mtw")
	STmcFS = STmc.Get("Mtw")

	TTmcQCD = TTmc.Get("QCDbkg")
	TTmcQCD2d = TTmc.Get("QCDbkg2D")

	STmcQCD = STmc.Get("QCDbkg")
	STmcQCD2d = STmc.Get("QCDbkg2D")


	TTmcFSPtScaleUp = TTmcPtScaleUp.Get("Mtw")
	TTmcFSPtScaleDown = TTmcPtScaleDown.Get("Mtw")

	TTmcFSQ2ScaleUp = TTmcQ2ScaleUp.Get("Mtw")
	TTmcFSQ2ScaleDown = TTmcQ2ScaleDown.Get("Mtw")

	TTmcFSPtSmearUp = TTmcPtSmearUp.Get("Mtw")
	TTmcFSPtSmearDown = TTmcPtSmearDown.Get("Mtw")

	TTmcFSPileUp = TTmcPileUp.Get("Mtw")
	TTmcFSPileDown = TTmcPileDown.Get("Mtw")

#	TTmcFSPDFUp = TTmcPDFUp.Get("Mtw")
#	TTmcFSPDFDown = TTmcPDFDown.Get("Mtw")

	TTmcFSTriggerUp = TTmc.Get("Mtwtrigup")
	TTmcFSTriggerDown = TTmc.Get("Mtwtrigdown")

	TTmcFSTup =  TTmc.Get("MtwTup")
	TTmcFSTdown =  TTmc.Get("MtwTdown")

	DataFS = Data.Get("Mtw")
	DataQCD = Data.Get("QCDbkg")
	DataQCD2d = Data.Get("QCDbkg2D")
	DataQCDUp = Data.Get("QCDbkgh")
	DataQCDDown = Data.Get("QCDbkgl")
	DataQCDmodmup = Datamodmup.Get("QCDbkg")
	DataQCDmodmdown = Datamodmdown.Get("QCDbkg")
	#TTmcQCD2d = TTmc.Get("QCDbkg2D")
	#DataFS.Add(TTmc.Get("Mtw"))

	DataQCD.Add(TTmcQCD,-1)
	DataQCDUp.Add(TTmcQCD,-1)
	DataQCDDown.Add(TTmcQCD,-1)
	DataQCD2d.Add(TTmcQCD2d,-1)
	DataQCDmodmup.Add(TTmcQCD,-1)
	DataQCDmodmdown.Add(TTmcQCD,-1)


	DataQCD.Add(STmcQCD,-1)
	DataQCDUp.Add(STmcQCD,-1)
	DataQCDDown.Add(STmcQCD,-1)
	DataQCD2d.Add(STmcQCD2d,-1)
	DataQCDmodmup.Add(STmcQCD,-1)
	DataQCDmodmdown.Add(STmcQCD,-1)

	Zero(DataQCD)
	Zero(DataQCDUp)
	Zero(DataQCDDown)
	Zero(DataQCD2d)
	Zero(DataQCDmodmup)
	Zero(DataQCDmodmdown)

	fittitles = ["pol0","pol2","pol3","FIT","Bifpoly","expofit"]
	QCDbkg_ARR = []
	for ihist in range(0,len(fittitles)):
		QCDbkg_ARR.append(Data.Get("QCDbkg"+str(fittitles[ihist])).Rebin(rebin))

	BEfiterrh = Fit_Uncertainty(QCDbkg_ARR)


	DataQCD2d.Rebin(rebin)
	DataFS.Rebin(rebin)
	DataQCD.Rebin(rebin)
	DataQCDmodmup.Rebin(rebin)
	DataQCDmodmdown.Rebin(rebin)


	DataQCDUp.Rebin(rebin)
	DataQCDDown.Rebin(rebin)
	#DataBEtptl.Rebin(rebin)
	#DataBEtpth.Rebin(rebin)
	TTmcFS.Rebin(rebin)
	STmcFS.Rebin(rebin)



	TTmcFSQ2ScaleUp.Rebin(rebin)
	TTmcFSQ2ScaleDown.Rebin(rebin)

	TTmcFSPtScaleUp.Rebin(rebin)
	TTmcFSPtScaleDown.Rebin(rebin)

	TTmcFSPtSmearUp.Rebin(rebin)
	TTmcFSPtSmearDown.Rebin(rebin)

	TTmcFSPileUp.Rebin(rebin)
	TTmcFSPileDown.Rebin(rebin)

#	TTmcFSPDFUp.Rebin(rebin)
#	TTmcFSPDFDown.Rebin(rebin)

	TTmcFSTriggerUp.Rebin(rebin)
	TTmcFSTriggerDown.Rebin(rebin)

	TTmcFSTup.Rebin(rebin)
	TTmcFSTdown.Rebin(rebin)


	#STsmcFS.Rebin(rebin)
	#STtmcFS.Rebin(rebin)
	#STtWmcFS.Rebin(rebin)

	DataQCDE1Up = DataQCD.Clone()	
	DataQCDE2Up = DataQCD.Clone()	
	DataQCDE1Down = DataQCD.Clone()	
	DataQCDE2Down = DataQCD.Clone()
	for ibin in range(0,DataQCD.GetNbinsX()+1):
		QCDfit3=abs(DataQCD2d.GetBinContent(ibin)-DataQCD.GetBinContent(ibin))
		QCDfit2=abs(BEfiterrh.GetBinContent(ibin))
		DataQCDE1Up.SetBinContent(ibin,max(0.0,DataQCD.GetBinContent(ibin)+QCDfit3))
		DataQCDE1Down.SetBinContent(ibin,max(0.0,DataQCD.GetBinContent(ibin)-QCDfit3))
		DataQCDE2Up.SetBinContent(ibin,max(0.0,DataQCD.GetBinContent(ibin)+QCDfit2))
		DataQCDE2Down.SetBinContent(ibin,max(0.0,DataQCD.GetBinContent(ibin)-QCDfit2))
	



	DataFS.SetName("mtw_allhad__DATA")
	DataQCD.SetName("mtw_allhad__qcd")
	DataQCDUp.SetName("mtw_allhad__qcd__Fit__plus")
	DataQCDDown.SetName("mtw_allhad__qcd__Fit__minus")
	DataQCDmodmup.SetName("mtw_allhad__qcd__modm__plus")
	DataQCDmodmdown.SetName("mtw_allhad__qcd__modm__minus")
	DataQCDE1Up.SetName("mtw_allhad__qcd__TwoD__plus")
	DataQCDE1Down.SetName("mtw_allhad__qcd__TwoD__minus")
	DataQCDE2Up.SetName("mtw_allhad__qcd__Alt__plus")
	DataQCDE2Down.SetName("mtw_allhad__qcd__Alt__minus")

	TTmcFS.SetName("mtw_allhad__ttbar")
	STmcFS.SetName("mtw_allhad__st")

	TTmcFSPtScaleUp.SetName("mtw_allhad__ttbar__jes__plus")
	TTmcFSPtScaleDown.SetName("mtw_allhad__ttbar__jes__minus")

	TTmcFSQ2ScaleUp.SetName("mtw_allhad__ttbar__q2__plus")
	TTmcFSQ2ScaleDown.SetName("mtw_allhad__ttbar__q2__minus")


	TTmcFSTup.SetName("mtw_allhad__ttbar__ttag__plus")
	TTmcFSTdown.SetName("mtw_allhad__ttbar__ttag__minus")



	TTmcFSPtSmearUp.SetName("mtw_allhad__ttbar__jer__plus")
	TTmcFSPtSmearDown.SetName("mtw_allhad__ttbar__jer__minus")



	TTmcFSPileUp.SetName("mtw_allhad__ttbar__pile__plus")
	TTmcFSPileDown.SetName("mtw_allhad__ttbar__pile__minus")



	TTmcFSTriggerUp.SetName("mtw_allhad__ttbar__trig__plus")
	TTmcFSTriggerDown.SetName("mtw_allhad__ttbar__trig__minus")

	#STsmcFS.SetName("mtw_allhad__sts")
	#STtmcFS.SetName("mtw_allhad__stt")
	#STtWmcFS.SetName("mtw_allhad__sttw")

	DataFS.SetTitle("mtw_allhad__DATA")
	DataQCD.SetTitle("mtw_allhad__qcd")
	DataQCDUp.SetTitle("mtw_allhad__qcd__Fit__plus")
	DataQCDDown.SetTitle("mtw_allhad__qcd__Fit__minus")
	DataQCDE1Up.SetTitle("mtw_allhad__qcd__TwoD__plus")
	DataQCDE1Down.SetTitle("mtw_allhad__qcd__TwoD__minus")
	DataQCDE2Up.SetTitle("mtw_allhad__qcd__Alt__plus")
	DataQCDE2Down.SetTitle("mtw_allhad__qcd__Alt__minus")
	DataQCDmodmup.SetTitle("mtw_allhad__qcd__modm__plus")
	DataQCDmodmdown.SetTitle("mtw_allhad__qcd__modm__minus")



	TTmcFS.SetTitle("mtw_allhad__ttbar")
	STmcFS.SetTitle("mtw_allhad__st")
	TTmcFSPtScaleUp.SetTitle("mtw_allhad__ttbar__jes__plus")
	TTmcFSPtScaleDown.SetTitle("mtw_allhad__ttbar__jes__minus")
	
	TTmcFSQ2ScaleUp.SetTitle("mtw_allhad__ttbar__q2__plus")
	TTmcFSQ2ScaleDown.SetTitle("mtw_allhad__ttbar__q2__minus")


	TTmcFSTup.SetTitle("mtw_allhad__ttbar__ttag__plus")
	TTmcFSTdown.SetTitle("mtw_allhad__ttbar__ttag__minus")


	TTmcFSPtSmearUp.SetTitle("mtw_allhad__ttbar__jer__plus")
	TTmcFSPtSmearDown.SetTitle("mtw_allhad__ttbar__jer__minus")


	TTmcFSPileUp.SetTitle("mtw_allhad__ttbar__pile__plus")
	TTmcFSPileDown.SetTitle("mtw_allhad__ttbar__pile__minus")



	TTmcFSTriggerUp.SetTitle("mtw_allhad__ttbar__trig__plus")
	TTmcFSTriggerDown.SetTitle("mtw_allhad__ttbar__trig__minus")


        output.cd()

	DataFS.Write("mtw_allhad__DATA")
	DataQCD.Write("mtw_allhad__qcd")
	DataQCDUp.Write("mtw_allhad__qcd__Fit__plus")
	DataQCDDown.Write("mtw_allhad__qcd__Fit__minus")
	DataQCDE1Up.Write("mtw_allhad__qcd__TwoD__plus")
	DataQCDE1Down.Write("mtw_allhad__qcd__TwoD__minus")
	DataQCDE2Up.Write("mtw_allhad__qcd__Alt__plus")
	DataQCDE2Down.Write("mtw_allhad__qcd__Alt__minus")
	DataQCDmodmup.Write("mtw_allhad__qcd__modm__plus")
	DataQCDmodmdown.Write("mtw_allhad__qcd__modm__minus")
	#DataQCDBEH.Write("mtw_allhad__qcd__bkg__plus")
	#DataQCDBEL.Write("mtw_allhad__qcd__bkg__minus")

	TTmcFS.Write("mtw_allhad__ttbar")
	STmcFS.Write("mtw_allhad__st")

	TTmcFSPtScaleUp.Write("mtw_allhad__ttbar__jes__plus")
	TTmcFSPtScaleDown.Write("mtw_allhad__ttbar__jes__minus")

	TTmcFSQ2ScaleUp.Write("mtw_allhad__ttbar__q2__plus")
	TTmcFSQ2ScaleDown.Write("mtw_allhad__ttbar__q2__minus")


	TTmcFSTup.Write("mtw_allhad__ttbar__ttag__plus")
	TTmcFSTdown.Write("mtw_allhad__ttbar__ttag__minus")


	TTmcFSPtSmearUp.Write("mtw_allhad__ttbar__jer__plus")
	TTmcFSPtSmearDown.Write("mtw_allhad__ttbar__jer__minus")

	TTmcFSPileUp.Write("mtw_allhad__ttbar__pile__plus")
	TTmcFSPileDown.Write("mtw_allhad__ttbar__pile__minus")


	TTmcFSTriggerUp.Write("mtw_allhad__ttbar__trig__plus")
	TTmcFSTriggerDown.Write("mtw_allhad__ttbar__trig__minus")

	
	for RA in range(0,len(mass)):
		SignalB11 = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_none_PSET_"+cuts+".root")

		SignalB11PtScaleUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JES_up_PSET_"+options.cuts+".root")
		SignalB11PtScaleDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JES_down_PSET_"+options.cuts+".root")


		SignalB11PtSmearUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JER_up_PSET_"+options.cuts+".root")
		SignalB11PtSmearDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JER_down_PSET_"+options.cuts+".root")


		SignalB11PileUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_pileup_up_PSET_"+options.cuts+".root")
		SignalB11PileDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_pileup_down_PSET_"+options.cuts+".root")



		SignalFS = SignalB11.Get("Mtw")
		SignalTup = SignalB11.Get("MtwTup")
		SignalTdown = SignalB11.Get("MtwTdown")

		SignalTriggerup = SignalB11.Get("Mtwtrigup")
		SignalTriggerdown = SignalB11.Get("Mtwtrigdown")

		SignalPtScaleup = SignalB11PtScaleUp.Get("Mtw")
		SignalPtScaledown = SignalB11PtScaleDown.Get("Mtw")

		SignalPtSmearup = SignalB11PtSmearUp.Get("Mtw")
		SignalPtSmeardown = SignalB11PtSmearDown.Get("Mtw")

		SignalPileup = SignalB11PileUp.Get("Mtw")
		SignalPiledown = SignalB11PileDown.Get("Mtw")


		output.cd()

		SignalFS.Rebin(rebin)
		SignalTup.Rebin(rebin)
		SignalTdown.Rebin(rebin)
		SignalTriggerup.Rebin(rebin)
		SignalTriggerdown.Rebin(rebin)
		SignalPtScaleup.Rebin(rebin)
		SignalPtScaledown.Rebin(rebin)

		SignalPtSmearup.Rebin(rebin)
		SignalPtSmeardown.Rebin(rebin)


		SignalPileup.Rebin(rebin)
		SignalPiledown.Rebin(rebin)


		SignalFS.SetTitle("mtw_allhad__bs"+str(mass[RA]))
		SignalTup.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__ttag__plus")
		SignalTdown.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__ttag__minus")
		SignalTriggerup.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__trig__plus")
		SignalTriggerdown.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__trig__minus")
		SignalPtScaleup.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__jes__plus")
		SignalPtScaledown.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__jes__minus")
		SignalPtSmearup.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__jer__plus")
		SignalPtSmeardown.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__jer__minus")
		SignalPileup.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__pile__plus")
		SignalPiledown.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__pile__minus")


		SignalFS.SetName("mtw_allhad__bs"+str(mass[RA]))
		SignalTup.SetName("mtw_allhad__bs"+str(mass[RA])+"__ttag__plus")
		SignalTdown.SetName("mtw_allhad__bs"+str(mass[RA])+"__ttag__minus")
		SignalTriggerup.SetName("mtw_allhad__bs"+str(mass[RA])+"__trig__plus")
		SignalTriggerdown.SetName("mtw_allhad__bs"+str(mass[RA])+"__trig__minus")
		SignalPtScaleup.SetName("mtw_allhad__bs"+str(mass[RA])+"__jes__plus")
		SignalPtScaledown.SetName("mtw_allhad__bs"+str(mass[RA])+"__jes__minus")
		SignalPtSmearup.SetName("mtw_allhad__bs"+str(mass[RA])+"__jer__plus")
		SignalPtSmeardown.SetName("mtw_allhad__bs"+str(mass[RA])+"__jer__minus")
		SignalPileup.SetName("mtw_allhad__bs"+str(mass[RA])+"__pile__plus")
		SignalPiledown.SetName("mtw_allhad__bs"+str(mass[RA])+"__pile__minus")


		SignalFS.Write("mtw_allhad__bs"+str(mass[RA]))
		SignalTup.Write("mtw_allhad__bs"+str(mass[RA])+"__ttag__plus")
		SignalTdown.Write("mtw_allhad__bs"+str(mass[RA])+"__ttag__minus")
		SignalTriggerup.Write("mtw_allhad__bs"+str(mass[RA])+"__trig__plus")
		SignalTriggerdown.Write("mtw_allhad__bs"+str(mass[RA])+"__trig__minus")
		SignalPtScaleup.Write("mtw_allhad__bs"+str(mass[RA])+"__jes__plus")
		SignalPtScaledown.Write("mtw_allhad__bs"+str(mass[RA])+"__jes__minus")
		SignalPtSmearup.Write("mtw_allhad__bs"+str(mass[RA])+"__jer__plus")
		SignalPtSmeardown.Write("mtw_allhad__bs"+str(mass[RA])+"__jer__minus")
		SignalPileup.Write("mtw_allhad__bs"+str(mass[RA])+"__pile__plus")
		SignalPiledown.Write("mtw_allhad__bs"+str(mass[RA])+"__pile__minus")


		


	
