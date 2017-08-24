import os
import pickle
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
                  default	=	'35851pb',
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

Cons = LoadConstants()


rebin=2

def Zero(hist):
	for ibin in range(0,hist.GetXaxis().GetNbins()+1):
		hist.SetBinContent(ibin,max(0.0,hist.GetBinContent(ibin)))

#LabelsU=['__jes__','__trig__','__ptsmear__']
mass = [1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]

for hand in ["RH","LH","vector"]:
	if hand == "RH":
		coup = "right"
		xsecs = Cons['xsec_bsr']
	elif hand == "LH":
		coup = "left"
		xsecs = Cons['xsec_bsl']
	elif hand == 'vector':
		coup = 'vector'
		for key in Cons['xsec_bsr']:
			xsecs[key] = Cons['xsec_bsr'][key]+Cons['xsec_bsl'][key]

	
	output = ROOT.TFile( "limitsetting/theta/BStarCombination/allhadronic"+coup+Lumi+"_mtw.root", "recreate" )
	output.cd()

#------------Grab relevant files --------------------------------------
	# Grab nominal files
	Data = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzer"+options.set+"_Trigger_nominal_none_PSET_"+options.cuts+".root")
	Datamodmdown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzer"+options.set+"_Trigger_nominal_none_modm_down_PSET_"+options.cuts+".root")
	Datamodmup = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzer"+options.set+"_Trigger_nominal_none_modm_up_PSET_"+options.cuts+".root")

	TTmc 	= ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_"+options.cuts+".root")
	
	STmc = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsingletop_Trigger_nominal_none_PSET_"+options.cuts+".root")

	STtmc = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsingletop_t_Trigger_nominal_none_PSET_"+options.cuts+".root")
	STtBmc = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsingletop_tB_Trigger_nominal_none_PSET_"+options.cuts+".root")
	STtWmc = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsingletop_tW_Trigger_nominal_none_PSET_"+options.cuts+".root")
	STtWBmc = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsingletop_tWB_Trigger_nominal_none_PSET_"+options.cuts+".root")

	# Grab ttbar JES, JER, Q2, PDF, Pileup
	TTmcPtScaleUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_JES_up_PSET_"+options.cuts+".root")
	TTmcPtScaleDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_JES_down_PSET_"+options.cuts+".root")

	TTmcPtSmearUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_JER_up_PSET_"+options.cuts+".root")
	TTmcPtSmearDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_JER_down_PSET_"+options.cuts+".root")

	# Now included in ttbar xsec uncertainty
	# TTmcQ2ScaleUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbarscaleup_Trigger_nominal_none_PSET_"+options.cuts+".root")
	# TTmcQ2ScaleDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbarscaledown_Trigger_nominal_none_PSET_"+options.cuts+".root")

	TTmcPileUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_none_pileup_up_PSET_"+options.cuts+".root")
	TTmcPileDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_none_pileup_down_PSET_"+options.cuts+".root")

	TTmcPDFUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_none_pdf_up_PSET_"+options.cuts+".root")
	TTmcPDFDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedttbar_Trigger_nominal_none_pdf_down_PSET_"+options.cuts+".root")

	
	# Grab singletop JES, JER, Pileup
	# t
	STtmcPtScaleUp = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_JES_up_PSET_'+options.cuts+'.root')
	STtmcPtScaleDown = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_JES_down_PSET_'+options.cuts+'.root')

	STtmcPtSmearUp = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_JER_up_PSET_'+options.cuts+'.root')
	STtmcPtSmearDown = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_JER_down_PSET_'+options.cuts+'.root')

	STtmcPileUp = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_none_pileup_up_PSET_'+options.cuts+'.root')
	STtmcPileDown = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_none_pileup_down_PSET_'+options.cuts+'.root')
	# tB
	STtBmcPtScaleUp = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_JES_up_PSET_'+options.cuts+'.root')
	STtBmcPtScaleDown = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_JES_down_PSET_'+options.cuts+'.root')

	STtBmcPtSmearUp = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_JER_up_PSET_'+options.cuts+'.root')
	STtBmcPtSmearDown = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_JER_down_PSET_'+options.cuts+'.root')

	STtBmcPileUp = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_none_pileup_up_PSET_'+options.cuts+'.root')
	STtBmcPileDown = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_none_pileup_down_PSET_'+options.cuts+'.root')
	# tW
	STtWmcPtScaleUp = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_JES_up_PSET_'+options.cuts+'.root')
	STtWmcPtScaleDown = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_JES_down_PSET_'+options.cuts+'.root')

	STtWmcPtSmearUp = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_JER_up_PSET_'+options.cuts+'.root')
	STtWmcPtSmearDown = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_JER_down_PSET_'+options.cuts+'.root')

	STtWmcPileUp = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_none_pileup_up_PSET_'+options.cuts+'.root')
	STtWmcPileDown = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_none_pileup_down_PSET_'+options.cuts+'.root')

	# tWB
	STtWBmcPtScaleUp = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_JES_up_PSET_'+options.cuts+'.root')
	STtWBmcPtScaleDown = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_JES_down_PSET_'+options.cuts+'.root')

	STtWBmcPtSmearUp = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_JER_up_PSET_'+options.cuts+'.root')
	STtWBmcPtSmearDown = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_JER_down_PSET_'+options.cuts+'.root')

	STtWBmcPileUp = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_none_pileup_up_PSET_'+options.cuts+'.root')
	STtWBmcPileDown = ROOT.TFile("rootfiles/"+options.lumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_none_pileup_down_PSET_'+options.cuts+'.root')


#------------Grab histos --------------------------------------
	# Nominal
	TTmcFS = TTmc.Get("Mtw")
	STmcFS = STmc.Get("Mtw")

	STtmcFS = STtmc.Get("Mtw")
	STtBmcFS = STtBmc.Get("Mtw")
	STtWmcFS = STtWmc.Get("Mtw")
	STtWBmcFS = STtWBmc.Get("Mtw")

	# QCD bkg
	TTmcQCD = TTmc.Get("QCDbkg")
	TTmcQCD2d = TTmc.Get("QCDbkg2D")

	STmcQCD = STmc.Get("QCDbkg")
	STmcQCD2d = STmc.Get("QCDbkg2D")

	# Grab top full selections of uncertainties
	TTmcFSPtScaleUp = TTmcPtScaleUp.Get("Mtw")
	TTmcFSPtScaleDown = TTmcPtScaleDown.Get("Mtw")

	TTmcFSPtSmearUp = TTmcPtSmearUp.Get("Mtw")
	TTmcFSPtSmearDown = TTmcPtSmearDown.Get("Mtw")

	# TTmcFSQ2ScaleUp = TTmcQ2ScaleUp.Get("Mtw")
	# TTmcFSQ2ScaleDown = TTmcQ2ScaleDown.Get("Mtw")

	TTmcFSPileUp = TTmcPileUp.Get("Mtw")
	TTmcFSPileDown = TTmcPileDown.Get("Mtw")

	TTmcFSPDFUp = TTmcPDFUp.Get("Mtw")
	TTmcFSPDFDown = TTmcPDFDown.Get("Mtw")

	TTmcFSTriggerUp = TTmc.Get("Mtwtrigup")
	TTmcFSTriggerDown = TTmc.Get("Mtwtrigdown")

	# Flat now so added as a lognormal uncertainty instead
	# TTmcFSTup =  TTmc.Get("MtwTup")
	# TTmcFSTdown =  TTmc.Get("MtwTdown")

	TTmcFSTptUp = TTmc.Get('MtwTptup')
	TTmcFSTptDown = TTmc.Get('MtwTptdown')

	# Grab single top full selections of uncertainties
	# t
	STtmcFSPtScaleUp = STtmcPtScaleUp.Get("Mtw")
	STtmcFSPtScaleDown = STtmcPtScaleDown.Get("Mtw")

	STtmcFSPtSmearUp = STtmcPtSmearUp.Get("Mtw")
	STtmcFSPtSmearDown = STtmcPtSmearDown.Get("Mtw")

	STtmcFSPileUp = STtmcPileUp.Get("Mtw")
	STtmcFSPileDown = STtmcPileDown.Get("Mtw")

	STtmcFSTriggerUp = STtmc.Get("Mtwtrigup")
	STtmcFSTriggerDown = STtmc.Get("Mtwtrigdown")

	# tB
	STtBmcFSPtScaleUp = STtBmcPtScaleUp.Get("Mtw")
	STtBmcFSPtScaleDown = STtBmcPtScaleDown.Get("Mtw")

	STtBmcFSPtSmearUp = STtBmcPtSmearUp.Get("Mtw")
	STtBmcFSPtSmearDown = STtBmcPtSmearDown.Get("Mtw")

	STtBmcFSPileUp = STtBmcPileUp.Get("Mtw")
	STtBmcFSPileDown = STtBmcPileDown.Get("Mtw")

	STtBmcFSTriggerUp = STtBmc.Get("Mtwtrigup")
	STtBmcFSTriggerDown = STtBmc.Get("Mtwtrigdown")

	# tW
	STtWmcFSPtScaleUp = STtWmcPtScaleUp.Get("Mtw")
	STtWmcFSPtScaleDown = STtWmcPtScaleDown.Get("Mtw")

	STtWmcFSPtSmearUp = STtWmcPtSmearUp.Get("Mtw")
	STtWmcFSPtSmearDown = STtWmcPtSmearDown.Get("Mtw")

	STtWmcFSPileUp = STtWmcPileUp.Get("Mtw")
	STtWmcFSPileDown = STtWmcPileDown.Get("Mtw")

	STtWmcFSTriggerUp = STtWmc.Get("Mtwtrigup")
	STtWmcFSTriggerDown = STtWmc.Get("Mtwtrigdown")

	STtWmcFSWSFup = STtWmc.Get('MtwWup')
	STtWmcFSWSFdown = STtWmc.Get('MtwWdown')

	STtWmcFSExtrapUp = STtWmc.Get('MtwExtrapUp')
	STtWmcFSExtrapDown = STtWmc.Get('MtwExtrapDown')

	# tWB
	STtWBmcFSPtScaleUp = STtWBmcPtScaleUp.Get("Mtw")
	STtWBmcFSPtScaleDown = STtWBmcPtScaleDown.Get("Mtw")

	STtWBmcFSPtSmearUp = STtWBmcPtSmearUp.Get("Mtw")
	STtWBmcFSPtSmearDown = STtWBmcPtSmearDown.Get("Mtw")

	STtWBmcFSPileUp = STtWBmcPileUp.Get("Mtw")
	STtWBmcFSPileDown = STtWBmcPileDown.Get("Mtw")

	STtWBmcFSTriggerUp = STtWBmc.Get("Mtwtrigup")
	STtWBmcFSTriggerDown = STtWBmc.Get("Mtwtrigdown")

	STtWBmcFSWSFup = STtWBmc.Get('MtwWup')
	STtWBmcFSWSFdown = STtWBmc.Get('MtwWdown')

	STtWBmcFSExtrapUp = STtWBmc.Get('MtwExtrapUp')
	STtWBmcFSExtrapDown = STtWBmc.Get('MtwExtrapDown')


	# Grab data stuff
	DataFS = Data.Get("Mtw")
	DataQCD = Data.Get("QCDbkg")
	DataQCD2d = Data.Get("QCDbkg2D")
	DataQCDUp = Data.Get("QCDbkgh")
	DataQCDDown = Data.Get("QCDbkgl")
	DataQCDmodmup = Datamodmup.Get("QCDbkg")
	DataQCDmodmdown = Datamodmdown.Get("QCDbkg")
	#DataFS.Add(TTmc.Get("Mtw"))

	# Get rid of double counts
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


	# Set empty bins to zero
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

	# Rebin everything
	DataQCD2d.Rebin(rebin)
	DataFS.Rebin(rebin)
	DataQCD.Rebin(rebin)
	DataQCDmodmup.Rebin(rebin)
	DataQCDmodmdown.Rebin(rebin)


	DataQCDUp.Rebin(rebin)
	DataQCDDown.Rebin(rebin)

	TTmcFS.Rebin(rebin)
	STmcFS.Rebin(rebin)

	# ttbar
	# TTmcFSQ2ScaleUp.Rebin(rebin)
	# TTmcFSQ2ScaleDown.Rebin(rebin)

	TTmcFSPtScaleUp.Rebin(rebin)
	TTmcFSPtScaleDown.Rebin(rebin)

	TTmcFSPtSmearUp.Rebin(rebin)
	TTmcFSPtSmearDown.Rebin(rebin)

	TTmcFSPileUp.Rebin(rebin)
	TTmcFSPileDown.Rebin(rebin)

	TTmcFSPDFUp.Rebin(rebin)
	TTmcFSPDFDown.Rebin(rebin)

	TTmcFSTriggerUp.Rebin(rebin)
	TTmcFSTriggerDown.Rebin(rebin)

	TTmcFSTptUp.Rebin(rebin)
	TTmcFSTptDown.Rebin(rebin)

	# Singletop
	# t
	STtmcFS.Rebin(rebin)

	STtmcFSPtScaleUp.Rebin(rebin)
	STtmcFSPtScaleDown.Rebin(rebin)

	STtmcFSPtSmearUp.Rebin(rebin)
	STtmcFSPtSmearDown.Rebin(rebin)

	STtmcFSPileUp.Rebin(rebin)
	STtmcFSPileDown.Rebin(rebin)

	STtmcFSTriggerUp.Rebin(rebin)
	STtmcFSTriggerDown.Rebin(rebin)

	# tB
	STtBmcFS.Rebin(rebin)

	STtBmcFSPtScaleUp.Rebin(rebin)
	STtBmcFSPtScaleDown.Rebin(rebin)

	STtBmcFSPtSmearUp.Rebin(rebin)
	STtBmcFSPtSmearDown.Rebin(rebin)

	STtBmcFSPileUp.Rebin(rebin)
	STtBmcFSPileDown.Rebin(rebin)

	STtBmcFSTriggerUp.Rebin(rebin)
	STtBmcFSTriggerDown.Rebin(rebin)

	# tW
	STtWmcFS.Rebin(rebin)

	STtWmcFSPtScaleUp.Rebin(rebin)
	STtWmcFSPtScaleDown.Rebin(rebin)

	STtWmcFSPtSmearUp.Rebin(rebin)
	STtWmcFSPtSmearDown.Rebin(rebin)

	STtWmcFSPileUp.Rebin(rebin)
	STtWmcFSPileDown.Rebin(rebin)

	STtWmcFSTriggerUp.Rebin(rebin)
	STtWmcFSTriggerDown.Rebin(rebin)

	STtWmcFSWSFup.Rebin(rebin)
	STtWmcFSWSFdown.Rebin(rebin)

	STtWmcFSExtrapUp.Rebin(rebin)
	STtWmcFSExtrapDown.Rebin(rebin)

	# tWB
	STtWBmcFS.Rebin(rebin)

	STtWBmcFSPtScaleUp.Rebin(rebin)
	STtWBmcFSPtScaleDown.Rebin(rebin)

	STtWBmcFSPtSmearUp.Rebin(rebin)
	STtWBmcFSPtSmearDown.Rebin(rebin)

	STtWBmcFSPileUp.Rebin(rebin)
	STtWBmcFSPileDown.Rebin(rebin)

	STtWBmcFSTriggerUp.Rebin(rebin)
	STtWBmcFSTriggerDown.Rebin(rebin)

	STtWBmcFSWSFup.Rebin(rebin)
	STtWBmcFSWSFdown.Rebin(rebin)

	STtWBmcFSExtrapUp.Rebin(rebin)
	STtWBmcFSExtrapDown.Rebin(rebin)

	# DataQCDE1Up = DataQCD.Clone()	
	DataQCDE2Up = DataQCD.Clone()	
	# DataQCDE1Down = DataQCD.Clone()	
	DataQCDE2Down = DataQCD.Clone()
	for ibin in range(0,DataQCD.GetNbinsX()+1):
		QCDfit3=abs(DataQCD2d.GetBinContent(ibin)-DataQCD.GetBinContent(ibin))
		QCDfit2=abs(BEfiterrh.GetBinContent(ibin))
		# DataQCDE1Up.SetBinContent(ibin,max(0.0,DataQCD.GetBinContent(ibin)+QCDfit3))
		# DataQCDE1Down.SetBinContent(ibin,max(0.0,DataQCD.GetBinContent(ibin)-QCDfit3))
		DataQCDE2Up.SetBinContent(ibin,max(0.0,DataQCD.GetBinContent(ibin)+QCDfit2))
		DataQCDE2Down.SetBinContent(ibin,max(0.0,DataQCD.GetBinContent(ibin)-QCDfit2))
	

#-----Set Name-------------------------------
	# Data and QCD
	DataFS.SetName("mtw_allhad__DATA")
	DataQCD.SetName("mtw_allhad__qcd")
	DataQCDUp.SetName("mtw_allhad__qcd__Fit__plus")
	DataQCDDown.SetName("mtw_allhad__qcd__Fit__minus")
	DataQCDmodmup.SetName("mtw_allhad__qcd__modm__plus")
	DataQCDmodmdown.SetName("mtw_allhad__qcd__modm__minus")
	# DataQCDE1Up.SetName("mtw_allhad__qcd__TwoD__plus")
	# DataQCDE1Down.SetName("mtw_allhad__qcd__TwoD__minus")
	DataQCDE2Up.SetName("mtw_allhad__qcd__Alt__plus")
	DataQCDE2Down.SetName("mtw_allhad__qcd__Alt__minus")

	TTmcFS.SetName("mtw_allhad__ttbar")
	#STmcFS.SetName("mtw_allhad__st")

	# ttbar stuff
	TTmcFSPtScaleUp.SetName("mtw_allhad__ttbar__jes__plus")
	TTmcFSPtScaleDown.SetName("mtw_allhad__ttbar__jes__minus")
	
	TTmcFSPtSmearUp.SetName("mtw_allhad__ttbar__jer__plus")
	TTmcFSPtSmearDown.SetName("mtw_allhad__ttbar__jer__minus")

	# TTmcFSQ2ScaleUp.SetName("mtw_allhad__ttbar__q2__plus")
	# TTmcFSQ2ScaleDown.SetName("mtw_allhad__ttbar__q2__minus")

	TTmcFSPileUp.SetName("mtw_allhad__ttbar__pile__plus")
	TTmcFSPileDown.SetName("mtw_allhad__ttbar__pile__minus")

	TTmcFSTriggerUp.SetName("mtw_allhad__ttbar__trig__plus")
	TTmcFSTriggerDown.SetName("mtw_allhad__ttbar__trig__minus")

	TTmcFSTptUp.SetName('mtw_allhad__ttbar__toppt__plus')
	TTmcFSTptDown.SetName('mtw_allhad__ttbar__toppt__minus')

	TTmcFSPDFUp.SetName('mtw_allhad__ttbar__pdf__plus')
	TTmcFSPDFDown.SetName('mtw_allhad__ttbar__pdf__minus')

	# TTmcFSTup.SetName("mtw_allhad__ttbar__ttag__plus")
	# TTmcFSTdown.SetName("mtw_allhad__ttbar__ttag__minus")


	# Single top
	# t
	STtmcFS.SetName("mtw_allhad__stt")

	STtmcFSPtScaleUp.SetName('mtw_allhad__stt__jes__plus')
	STtmcFSPtScaleDown.SetName('mtw_allhad__stt__jes__minus')

	STtmcFSPtSmearUp.SetName('mtw_allhad__stt__jer__plus')
	STtmcFSPtSmearDown.SetName('mtw_allhad__stt__jer__minus')

	STtmcFSPileUp.SetName('mtw_allhad__stt__pile__plus')
	STtmcFSPileDown.SetName('mtw_allhad__stt__pile__minus')

	STtmcFSTriggerUp.SetName('mtw_allhad__stt__trig__plus')
	STtmcFSTriggerDown.SetName('mtw_allhad__stt__trig__minus')
	# tB
	STtBmcFS.SetName("mtw_allhad__sttB")

	STtBmcFSPtScaleUp.SetName('mtw_allhad__sttB__jes__plus')
	STtBmcFSPtScaleDown.SetName('mtw_allhad__sttB__jes__minus')

	STtBmcFSPtSmearUp.SetName('mtw_allhad__sttB__jer__plus')
	STtBmcFSPtSmearDown.SetName('mtw_allhad__sttB__jer__minus')

	STtBmcFSPileUp.SetName('mtw_allhad__sttB__pile__plus')
	STtBmcFSPileDown.SetName('mtw_allhad__sttB__pile__minus')

	STtBmcFSTriggerUp.SetName('mtw_allhad__sttB__trig__plus')
	STtBmcFSTriggerDown.SetName('mtw_allhad__sttB__trig__minus')
	# tW
	STtWmcFS.SetName("mtw_allhad__sttW")

	STtWmcFSPtScaleUp.SetName('mtw_allhad__sttW__jes__plus')
	STtWmcFSPtScaleDown.SetName('mtw_allhad__sttW__jes__minus')

	STtWmcFSPtSmearUp.SetName('mtw_allhad__sttW__jer__plus')
	STtWmcFSPtSmearDown.SetName('mtw_allhad__sttW__jer__minus')

	STtWmcFSPileUp.SetName('mtw_allhad__sttW__pile__plus')
	STtWmcFSPileDown.SetName('mtw_allhad__sttW__pile__minus')

	STtWmcFSTriggerUp.SetName('mtw_allhad__sttW__trig__plus')
	STtWmcFSTriggerDown.SetName('mtw_allhad__sttW__trig__minus')

	STtWmcFSWSFup.SetName('mtw_allhad__sttW__wtag__plus')
	STtWmcFSWSFdown.SetName('mtw_allhad__sttW__wtag__minus')

	STtWmcFSExtrapUp.SetName('mtw_allhad__sttW__extrap__plus')
	STtWmcFSExtrapDown.SetName('mtw_allhad__sttW__extrap__minus')

	# tWB
	STtWBmcFS.SetName("mtw_allhad__sttWB")

	STtWBmcFSPtScaleUp.SetName('mtw_allhad__sttWB__jes__plus')
	STtWBmcFSPtScaleDown.SetName('mtw_allhad__sttWB__jes__minus')

	STtWBmcFSPtSmearUp.SetName('mtw_allhad__sttWB__jer__plus')
	STtWBmcFSPtSmearDown.SetName('mtw_allhad__sttWB__jer__minus')

	STtWBmcFSPileUp.SetName('mtw_allhad__sttWB__pile__plus')
	STtWBmcFSPileDown.SetName('mtw_allhad__sttWB__pile__minus')

	STtWBmcFSTriggerUp.SetName('mtw_allhad__sttWB__trig__plus')
	STtWBmcFSTriggerDown.SetName('mtw_allhad__sttWB__trig__minus')

	STtWBmcFSWSFup.SetName('mtw_allhad__sttWB__wtag__plus')
	STtWBmcFSWSFdown.SetName('mtw_allhad__sttWB__wtag__minus')

	STtWBmcFSExtrapUp.SetName('mtw_allhad__sttWB__extrap__plus')
	STtWBmcFSExtrapDown.SetName('mtw_allhad__sttWB__extrap__minus')

#-------Set title------------------------------------
	# Data and QCD
	DataFS.SetTitle("mtw_allhad__DATA")
	DataQCD.SetTitle("mtw_allhad__qcd")
	DataQCDUp.SetTitle("mtw_allhad__qcd__Fit__plus")
	DataQCDDown.SetTitle("mtw_allhad__qcd__Fit__minus")
	# DataQCDE1Up.SetTitle("mtw_allhad__qcd__TwoD__plus")
	# DataQCDE1Down.SetTitle("mtw_allhad__qcd__TwoD__minus")
	DataQCDE2Up.SetTitle("mtw_allhad__qcd__Alt__plus")
	DataQCDE2Down.SetTitle("mtw_allhad__qcd__Alt__minus")
	DataQCDmodmup.SetTitle("mtw_allhad__qcd__modm__plus")
	DataQCDmodmdown.SetTitle("mtw_allhad__qcd__modm__minus")



	TTmcFS.SetTitle("mtw_allhad__ttbar")
	# STmcFS.SetTitle("mtw_allhad__st")

	# ttbar stuff
	TTmcFSPtScaleUp.SetTitle("mtw_allhad__ttbar__jes__plus")
	TTmcFSPtScaleDown.SetTitle("mtw_allhad__ttbar__jes__minus")
	
	TTmcFSPtSmearUp.SetTitle("mtw_allhad__ttbar__jer__plus")
	TTmcFSPtSmearDown.SetTitle("mtw_allhad__ttbar__jer__minus")

	# TTmcFSQ2ScaleUp.SetTitle("mtw_allhad__ttbar__q2__plus")
	# TTmcFSQ2ScaleDown.SetTitle("mtw_allhad__ttbar__q2__minus")

	TTmcFSPileUp.SetTitle("mtw_allhad__ttbar__pile__plus")
	TTmcFSPileDown.SetTitle("mtw_allhad__ttbar__pile__minus")

	TTmcFSTriggerUp.SetTitle("mtw_allhad__ttbar__trig__plus")
	TTmcFSTriggerDown.SetTitle("mtw_allhad__ttbar__trig__minus")

	TTmcFSTptUp.SetTitle('mtw_allhad__ttbar__toppt__plus')
	TTmcFSTptDown.SetTitle('mtw_allhad__ttbar__toppt__minus')

	TTmcFSPDFUp.SetTitle('mtw_allhad__ttbar__pdf__plus')
	TTmcFSPDFDown.SetTitle('mtw_allhad__ttbar__pdf__minus')

	# TTmcFSTup.SetTitle("mtw_allhad__ttbar__ttag__plus")
	# TTmcFSTdown.SetTitle("mtw_allhad__ttbar__ttag__minus")


	# Single top
	# t
	STtmcFS.SetTitle("mtw_allhad__stt")

	STtmcFSPtScaleUp.SetTitle('mtw_allhad__stt__jes__plus')
	STtmcFSPtScaleDown.SetTitle('mtw_allhad__stt__jes__minus')

	STtmcFSPtSmearUp.SetTitle('mtw_allhad__stt__jer__plus')
	STtmcFSPtSmearDown.SetTitle('mtw_allhad__stt__jer__minus')

	STtmcFSPileUp.SetTitle('mtw_allhad__stt__pile__plus')
	STtmcFSPileDown.SetTitle('mtw_allhad__stt__pile__minus')

	STtmcFSTriggerUp.SetTitle('mtw_allhad__stt__trig__plus')
	STtmcFSTriggerDown.SetTitle('mtw_allhad__stt__trig__minus')
	# tB
	STtBmcFS.SetTitle("mtw_allhad__sttB")

	STtBmcFSPtScaleUp.SetTitle('mtw_allhad__sttB__jes__plus')
	STtBmcFSPtScaleDown.SetTitle('mtw_allhad__sttB__jes__minus')

	STtBmcFSPtSmearUp.SetTitle('mtw_allhad__sttB__jer__plus')
	STtBmcFSPtSmearDown.SetTitle('mtw_allhad__sttB__jer__minus')

	STtBmcFSPileUp.SetTitle('mtw_allhad__sttB__pile__plus')
	STtBmcFSPileDown.SetTitle('mtw_allhad__sttB__pile__minus')

	STtBmcFSTriggerUp.SetTitle('mtw_allhad__sttB__trig__plus')
	STtBmcFSTriggerDown.SetTitle('mtw_allhad__sttB__trig__minus')
	# tW
	STtWmcFS.SetTitle("mtw_allhad__sttW")

	STtWmcFSPtScaleUp.SetTitle('mtw_allhad__sttW__jes__plus')
	STtWmcFSPtScaleDown.SetTitle('mtw_allhad__sttW__jes__minus')

	STtWmcFSPtSmearUp.SetTitle('mtw_allhad__sttW__jer__plus')
	STtWmcFSPtSmearDown.SetTitle('mtw_allhad__sttW__jer__minus')

	STtWmcFSPileUp.SetTitle('mtw_allhad__sttW__pile__plus')
	STtWmcFSPileDown.SetTitle('mtw_allhad__sttW__pile__minus')

	STtWmcFSTriggerUp.SetTitle('mtw_allhad__sttW__trig__plus')
	STtWmcFSTriggerDown.SetTitle('mtw_allhad__sttW__trig__minus')

	STtWmcFSWSFup.SetTitle('mtw_allhad__sttW__wtag__plus')
	STtWmcFSWSFdown.SetTitle('mtw_allhad__sttW__wtag__minus')

	STtWmcFSExtrapUp.SetTitle('mtw_allhad__sttW__extrap__plus')
	STtWmcFSExtrapDown.SetTitle('mtw_allhad__sttW__extrap__minus')

	# tWB
	STtWBmcFS.SetTitle("mtw_allhad__sttWB")

	STtWBmcFSPtScaleUp.SetTitle('mtw_allhad__sttWB__jes__plus')
	STtWBmcFSPtScaleDown.SetTitle('mtw_allhad__sttWB__jes__minus')

	STtWBmcFSPtSmearUp.SetTitle('mtw_allhad__sttWB__jer__plus')
	STtWBmcFSPtSmearDown.SetTitle('mtw_allhad__sttWB__jer__minus')

	STtWBmcFSPileUp.SetTitle('mtw_allhad__sttWB__pile__plus')
	STtWBmcFSPileDown.SetTitle('mtw_allhad__sttWB__pile__minus')

	STtWBmcFSTriggerUp.SetTitle('mtw_allhad__sttWB__trig__plus')
	STtWBmcFSTriggerDown.SetTitle('mtw_allhad__sttWB__trig__minus')

	STtWBmcFSWSFup.SetTitle('mtw_allhad__sttWB__wtag__plus')
	STtWBmcFSWSFdown.SetTitle('mtw_allhad__sttWB__wtag__minus')

	STtWBmcFSExtrapUp.SetTitle('mtw_allhad__sttWB__extrap__plus')
	STtWBmcFSExtrapDown.SetTitle('mtw_allhad__sttWB__extrap__minus')

#--------Start writing out----------------
	output.cd()

	DataFS.Write("mtw_allhad__DATA")
	DataQCD.Write("mtw_allhad__qcd")
	DataQCDUp.Write("mtw_allhad__qcd__Fit__plus")
	DataQCDDown.Write("mtw_allhad__qcd__Fit__minus")
	# DataQCDE1Up.Write("mtw_allhad__qcd__TwoD__plus")
	# DataQCDE1Down.Write("mtw_allhad__qcd__TwoD__minus")
	DataQCDE2Up.Write("mtw_allhad__qcd__Alt__plus")
	DataQCDE2Down.Write("mtw_allhad__qcd__Alt__minus")
	DataQCDmodmup.Write("mtw_allhad__qcd__modm__plus")
	DataQCDmodmdown.Write("mtw_allhad__qcd__modm__minus")
	#DataQCDBEH.Write("mtw_allhad__qcd__bkg__plus")
	#DataQCDBEL.Write("mtw_allhad__qcd__bkg__minus")

	TTmcFS.Write("mtw_allhad__ttbar")
	# STmcFS.Write("mtw_allhad__st")

	# ttbar stuff
	TTmcFSPtScaleUp.Write("mtw_allhad__ttbar__jes__plus")
	TTmcFSPtScaleDown.Write("mtw_allhad__ttbar__jes__minus")
	
	TTmcFSPtSmearUp.Write("mtw_allhad__ttbar__jer__plus")
	TTmcFSPtSmearDown.Write("mtw_allhad__ttbar__jer__minus")

	# TTmcFSQ2ScaleUp.Write("mtw_allhad__ttbar__q2__plus")
	# TTmcFSQ2ScaleDown.Write("mtw_allhad__ttbar__q2__minus")

	TTmcFSPileUp.Write("mtw_allhad__ttbar__pile__plus")
	TTmcFSPileDown.Write("mtw_allhad__ttbar__pile__minus")

	TTmcFSTriggerUp.Write("mtw_allhad__ttbar__trig__plus")
	TTmcFSTriggerDown.Write("mtw_allhad__ttbar__trig__minus")

	TTmcFSTptUp.Write('mtw_allhad__ttbar__toppt__plus')
	TTmcFSTptDown.Write('mtw_allhad__ttbar__toppt__minus')

	TTmcFSPDFUp.Write('mtw_allhad__ttbar__pdf__plus')
	TTmcFSPDFDown.Write('mtw_allhad__ttbar__pdf__minus')

	# TTmcFSTup.Write("mtw_allhad__ttbar__ttag__plus")
	# TTmcFSTdown.Write("mtw_allhad__ttbar__ttag__minus")


	# Single top
	# t
	STtmcFS.Write("mtw_allhad__stt")

	STtmcFSPtScaleUp.Write('mtw_allhad__stt__jes__plus')
	STtmcFSPtScaleDown.Write('mtw_allhad__stt__jes__minus')

	STtmcFSPtSmearUp.Write('mtw_allhad__stt__jer__plus')
	STtmcFSPtSmearDown.Write('mtw_allhad__stt__jer__minus')

	STtmcFSPileUp.Write('mtw_allhad__stt__pile__plus')
	STtmcFSPileDown.Write('mtw_allhad__stt__pile__minus')

	STtmcFSTriggerUp.Write('mtw_allhad__stt__trig__plus')
	STtmcFSTriggerDown.Write('mtw_allhad__stt__trig__minus')
	# tB
	STtBmcFS.Write("mtw_allhad__sttB")

	STtBmcFSPtScaleUp.Write('mtw_allhad__sttB__jes__plus')
	STtBmcFSPtScaleDown.Write('mtw_allhad__sttB__jes__minus')

	STtBmcFSPtSmearUp.Write('mtw_allhad__sttB__jer__plus')
	STtBmcFSPtSmearDown.Write('mtw_allhad__sttB__jer__minus')

	STtBmcFSPileUp.Write('mtw_allhad__sttB__pile__plus')
	STtBmcFSPileDown.Write('mtw_allhad__sttB__pile__minus')

	STtBmcFSTriggerUp.Write('mtw_allhad__sttB__trig__plus')
	STtBmcFSTriggerDown.Write('mtw_allhad__sttB__trig__minus')
	# tW
	STtWmcFS.Write("mtw_allhad__sttW")

	STtWmcFSPtScaleUp.Write('mtw_allhad__sttW__jes__plus')
	STtWmcFSPtScaleDown.Write('mtw_allhad__sttW__jes__minus')

	STtWmcFSPtSmearUp.Write('mtw_allhad__sttW__jer__plus')
	STtWmcFSPtSmearDown.Write('mtw_allhad__sttW__jer__minus')

	STtWmcFSPileUp.Write('mtw_allhad__sttW__pile__plus')
	STtWmcFSPileDown.Write('mtw_allhad__sttW__pile__minus')

	STtWmcFSTriggerUp.Write('mtw_allhad__sttW__trig__plus')
	STtWmcFSTriggerDown.Write('mtw_allhad__sttW__trig__minus')

	STtWmcFSWSFup.Write('mtw_allhad__sttW__wtag__plus')
	STtWmcFSWSFdown.Write('mtw_allhad__sttW__wtag__minus')

	STtWmcFSExtrapUp.Write('mtw_allhad__sttW__extrap__plus')
	STtWmcFSExtrapDown.Write('mtw_allhad__sttW__extrap__minus')
	# tWB
	STtWBmcFS.Write("mtw_allhad__sttWB")

	STtWBmcFSPtScaleUp.Write('mtw_allhad__sttWB__jes__plus')
	STtWBmcFSPtScaleDown.Write('mtw_allhad__sttWB__jes__minus')

	STtWBmcFSPtSmearUp.Write('mtw_allhad__sttWB__jer__plus')
	STtWBmcFSPtSmearDown.Write('mtw_allhad__sttWB__jer__minus')

	STtWBmcFSPileUp.Write('mtw_allhad__sttWB__pile__plus')
	STtWBmcFSPileDown.Write('mtw_allhad__sttWB__pile__minus')

	STtWBmcFSTriggerUp.Write('mtw_allhad__sttWB__trig__plus')
	STtWBmcFSTriggerDown.Write('mtw_allhad__sttWB__trig__minus')

	STtWBmcFSWSFup.Write('mtw_allhad__sttWB__wtag__plus')
	STtWBmcFSWSFdown.Write('mtw_allhad__sttWB__wtag__minus')

	STtWBmcFSExtrapUp.Write('mtw_allhad__sttWB__extrap__plus')
	STtWBmcFSExtrapDown.Write('mtw_allhad__sttWB__extrap__minus')

	xsecDict = {}
	for RA in range(0,len(mass)):
		SignalB11 = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_none_PSET_"+cuts+".root")

		SignalB11PtScaleUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JES_up_PSET_"+options.cuts+".root")
		SignalB11PtScaleDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JES_down_PSET_"+options.cuts+".root")


		SignalB11PtSmearUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JER_up_PSET_"+options.cuts+".root")
		SignalB11PtSmearDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JER_down_PSET_"+options.cuts+".root")


		SignalB11PileUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_none_pileup_up_PSET_"+options.cuts+".root")
		SignalB11PileDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_none_pileup_down_PSET_"+options.cuts+".root")


		SignalB11PDFUp = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_none_pdf_up_PSET_"+options.cuts+".root")
		SignalB11PDFDown = ROOT.TFile("rootfiles/"+options.lumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_none_pdf_down_PSET_"+options.cuts+".root")



		SignalFS = SignalB11.Get("Mtw")
		# SignalTup = SignalB11.Get("MtwTup")
		# SignalTdown = SignalB11.Get("MtwTdown")

		SignalTriggerup = SignalB11.Get("Mtwtrigup")
		SignalTriggerdown = SignalB11.Get("Mtwtrigdown")

		SignalPDFUp = SignalB11PDFUp.Get("Mtw")
		SignalPDFDown = SignalB11PDFDown.Get("Mtw")

		SignalPtScaleup = SignalB11PtScaleUp.Get("Mtw")
		SignalPtScaledown = SignalB11PtScaleDown.Get("Mtw")

		SignalPtSmearup = SignalB11PtSmearUp.Get("Mtw")
		SignalPtSmeardown = SignalB11PtSmearDown.Get("Mtw")

		SignalPileup = SignalB11PileUp.Get("Mtw")
		SignalPiledown = SignalB11PileDown.Get("Mtw")

		SignalWSFup = SignalB11.Get("MtwWup")
		SignalWSFdown = SignalB11.Get("MtwWdown")

		SignalExtrapUp = SignalB11.Get('MtwExtrapUp')
		SignalExtrapDown = SignalB11.Get('MtwExtrapDown')


		# Need to separate the PDF shape and normalization uncertainties
		# Normalization will be applied later as a band on the theory limit line
		xsec_up, xsec_down = PDFNormUncert(SignalFS,SignalPDFUp,SignalPDFDown,xsecs[str(mass[RA])])
		# Store values in a dictionary - write out at the end
		xsecDict[str(mass[RA])] = [xsec_up,xsec_down]

		# We keep the shape uncertainty here
		SignalPDFShapeUp, SignalPDFShapeDown = PDFShapeUncert(SignalFS,SignalPDFUp,SignalPDFDown)


		output.cd()

		SignalFS.Rebin(rebin)
		# SignalTup.Rebin(rebin)
		# SignalTdown.Rebin(rebin)
		SignalTriggerup.Rebin(rebin)
		SignalTriggerdown.Rebin(rebin)

		SignalPtScaleup.Rebin(rebin)
		SignalPtScaledown.Rebin(rebin)

		SignalPtSmearup.Rebin(rebin)
		SignalPtSmeardown.Rebin(rebin)

		SignalPDFShapeUp.Rebin(rebin)
		SignalPDFShapeDown.Rebin(rebin)

		SignalPileup.Rebin(rebin)
		SignalPiledown.Rebin(rebin)

		SignalWSFup.Rebin(rebin)
		SignalWSFdown.Rebin(rebin)

		SignalExtrapUp.Rebin(rebin)
		SignalExtrapDown.Rebin(rebin)


		SignalFS.SetTitle("mtw_allhad__bs"+str(mass[RA]))
		SignalWSFup.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__wtag__plus")
		SignalWSFdown.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__wtag__minus")
		SignalTriggerup.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__trig__plus")
		SignalTriggerdown.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__trig__minus")
		SignalPtScaleup.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__jes__plus")
		SignalPtScaledown.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__jes__minus")
		SignalPtSmearup.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__jer__plus")
		SignalPtSmeardown.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__jer__minus")
		SignalPileup.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__pile__plus")
		SignalPiledown.SetTitle("mtw_allhad__bs"+str(mass[RA])+"__pile__minus")
		SignalPDFShapeUp.SetTitle('mtw_allhad__bs'+str(mass[RA])+'__pdf__plus')
		SignalPDFShapeDown.SetTitle('mtw_allhad__bs'+str(mass[RA])+'__pdf__minus')
		SignalExtrapUp.SetTitle('mtw_allhad__bs'+str(mass[RA])+'__extrap__plus')
		SignalExtrapDown.SetTitle('mtw_allhad__bs'+str(mass[RA])+'__extrap__minus')


		SignalFS.SetName("mtw_allhad__bs"+str(mass[RA]))
		SignalWSFup.SetName("mtw_allhad__bs"+str(mass[RA])+"__wtag__plus")
		SignalWSFdown.SetName("mtw_allhad__bs"+str(mass[RA])+"__wtag__minus")
		SignalTriggerup.SetName("mtw_allhad__bs"+str(mass[RA])+"__trig__plus")
		SignalTriggerdown.SetName("mtw_allhad__bs"+str(mass[RA])+"__trig__minus")
		SignalPtScaleup.SetName("mtw_allhad__bs"+str(mass[RA])+"__jes__plus")
		SignalPtScaledown.SetName("mtw_allhad__bs"+str(mass[RA])+"__jes__minus")
		SignalPtSmearup.SetName("mtw_allhad__bs"+str(mass[RA])+"__jer__plus")
		SignalPtSmeardown.SetName("mtw_allhad__bs"+str(mass[RA])+"__jer__minus")
		SignalPileup.SetName("mtw_allhad__bs"+str(mass[RA])+"__pile__plus")
		SignalPiledown.SetName("mtw_allhad__bs"+str(mass[RA])+"__pile__minus")
		SignalPDFShapeUp.SetName('mtw_allhad__bs'+str(mass[RA])+'__pdf__plus')
		SignalPDFShapeDown.SetName('mtw_allhad__bs'+str(mass[RA])+'__pdf__minus')
		SignalExtrapUp.SetName('mtw_allhad__bs'+str(mass[RA])+'__extrap__plus')
		SignalExtrapDown.SetName('mtw_allhad__bs'+str(mass[RA])+'__extrap__minus')


		SignalFS.Write("mtw_allhad__bs"+str(mass[RA]))
		SignalWSFup.Write("mtw_allhad__bs"+str(mass[RA])+"__wtag__plus")
		SignalWSFdown.Write("mtw_allhad__bs"+str(mass[RA])+"__wtag__minus")
		SignalTriggerup.Write("mtw_allhad__bs"+str(mass[RA])+"__trig__plus")
		SignalTriggerdown.Write("mtw_allhad__bs"+str(mass[RA])+"__trig__minus")
		SignalPtScaleup.Write("mtw_allhad__bs"+str(mass[RA])+"__jes__plus")
		SignalPtScaledown.Write("mtw_allhad__bs"+str(mass[RA])+"__jes__minus")
		SignalPtSmearup.Write("mtw_allhad__bs"+str(mass[RA])+"__jer__plus")
		SignalPtSmeardown.Write("mtw_allhad__bs"+str(mass[RA])+"__jer__minus")
		SignalPileup.Write("mtw_allhad__bs"+str(mass[RA])+"__pile__plus")
		SignalPiledown.Write("mtw_allhad__bs"+str(mass[RA])+"__pile__minus")
		SignalPDFShapeUp.Write('mtw_allhad__bs'+str(mass[RA])+'__pdf__plus')
		SignalPDFShapeDown.Write('mtw_allhad__bs'+str(mass[RA])+'__pdf__minus')
		SignalExtrapUp.Write('mtw_allhad__bs'+str(mass[RA])+'__extrap__plus')
		SignalExtrapDown.Write('mtw_allhad__bs'+str(mass[RA])+'__extrap__minus')

	xsecFile = open('results/xsec_dict_'+coup+'_had.pkl',"wb")
	pickle.dump(xsecDict,xsecFile)
	xsecFile.close()
		


	
