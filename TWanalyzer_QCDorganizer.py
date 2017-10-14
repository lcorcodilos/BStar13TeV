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
                  default	=	'sideband1',
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


rebin=1

def Zero(hist):
	for ibin in range(0,hist.GetXaxis().GetNbins()+1):
		hist.SetBinContent(ibin,max(0.0,hist.GetBinContent(ibin)))

#LabelsU=['__jes__','__trig__','__ptsmear__']
mass = [1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]

dataLumi = options.lumi

for ttbarSub in ["_nottsub","_doublettsub"]:
	if ttbarSub == '_nottsub':
		ttSubVal = 0
	elif ttbarSub == '_doublettsub':
		ttSubVal = -2

	for hand in ["RH","LH"]:#,"vector"]:
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

		
		output = ROOT.TFile( "limitsetting/theta/BStarCombination/allhadronic"+coup+dataLumi+ttbarSub+"_mt.root", "recreate" )
		output.cd()

	#------------Grab relevant files --------------------------------------
		# Grab nominal files
		Data = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzer"+options.set+"_Trigger_nominal_none_PSET_"+options.cuts+ttbarSub+".root")
		Datamodmdown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzer"+options.set+"_Trigger_nominal_none_modm_down_PSET_"+options.cuts+ttbarSub+".root")
		Datamodmup = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzer"+options.set+"_Trigger_nominal_none_modm_up_PSET_"+options.cuts+ttbarSub+".root")

		TTmc 	= ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_"+options.cuts+ttbarSub+".root")
		
		STmc = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsingletop_Trigger_nominal_none_PSET_"+options.cuts+ttbarSub+".root")

		STtmc = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsingletop_t_Trigger_nominal_none_PSET_"+options.cuts+ttbarSub+".root")
		STtBmc = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsingletop_tB_Trigger_nominal_none_PSET_"+options.cuts+ttbarSub+".root")
		STtWmc = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsingletop_tW_Trigger_nominal_none_PSET_"+options.cuts+ttbarSub+".root")
		STtWBmc = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsingletop_tWB_Trigger_nominal_none_PSET_"+options.cuts+ttbarSub+".root")

		# Grab ttbar JES, JER, Q2, PDF, Pileup
		TTmcPtScaleUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_JES_up_PSET_"+options.cuts+ttbarSub+".root")
		TTmcPtScaleDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_JES_down_PSET_"+options.cuts+ttbarSub+".root")

		TTmcPtSmearUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_JER_up_PSET_"+options.cuts+ttbarSub+".root")
		TTmcPtSmearDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_JER_down_PSET_"+options.cuts+ttbarSub+".root")

		TTmcMassScaleUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_JMS_up_PSET_"+options.cuts+ttbarSub+".root")
		TTmcMassScaleDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_JMS_down_PSET_"+options.cuts+ttbarSub+".root")

		TTmcMassSmearUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_JMR_up_PSET_"+options.cuts+ttbarSub+".root")
		TTmcMassSmearDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_JMR_down_PSET_"+options.cuts+ttbarSub+".root")

		# Now included in ttbar xsec uncertainty
		# TTmcQ2ScaleUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbarscaleup_Trigger_nominal_none_PSET_"+options.cuts+ttbarSub+".root")
		# TTmcQ2ScaleDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbarscaledown_Trigger_nominal_none_PSET_"+options.cuts+ttbarSub+".root")

		TTmcPileUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_none_pileup_up_PSET_"+options.cuts+ttbarSub+".root")
		TTmcPileDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_none_pileup_down_PSET_"+options.cuts+ttbarSub+".root")

		TTmcPDFUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_none_pdf_up_PSET_"+options.cuts+ttbarSub+".root")
		TTmcPDFDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedttbar_Trigger_nominal_none_pdf_down_PSET_"+options.cuts+ttbarSub+".root")

		
		# Grab singletop JES, JER, Pileup
		# t
		STtmcPtScaleUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_JES_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtmcPtScaleDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_JES_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtmcPtSmearUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_JER_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtmcPtSmearDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_JER_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtmcMassScaleUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_JMS_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtmcMassScaleDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_JMS_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtmcMassSmearUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_JMR_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtmcMassSmearDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_JMR_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtmcPileUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_none_pileup_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtmcPileDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_t_Trigger_nominal_none_pileup_down_PSET_'+options.cuts+ttbarSub+'.root')

		# tB
		STtBmcPtScaleUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_JES_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtBmcPtScaleDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_JES_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtBmcPtSmearUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_JER_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtBmcPtSmearDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_JER_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtBmcMassScaleUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_JMS_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtBmcMassScaleDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_JMS_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtBmcMassSmearUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_JMR_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtBmcMassSmearDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_JMR_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtBmcPileUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_none_pileup_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtBmcPileDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tB_Trigger_nominal_none_pileup_down_PSET_'+options.cuts+ttbarSub+'.root')
		# tW
		STtWmcPtScaleUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_JES_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtWmcPtScaleDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_JES_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtWmcPtSmearUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_JER_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtWmcPtSmearDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_JER_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtWmcMassScaleUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_JMS_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtWmcMassScaleDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_JMS_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtWmcMassSmearUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_JMR_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtWmcMassSmearDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_JMR_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtWmcPileUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_none_pileup_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtWmcPileDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tW_Trigger_nominal_none_pileup_down_PSET_'+options.cuts+ttbarSub+'.root')

		# tWB
		STtWBmcPtScaleUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_JES_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtWBmcPtScaleDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_JES_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtWBmcPtSmearUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_JER_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtWBmcPtSmearDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_JER_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtWBmcMassScaleUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_JMS_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtWBmcMassScaleDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_JMS_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtWBmcMassSmearUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_JMR_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtWBmcMassSmearDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_JMR_down_PSET_'+options.cuts+ttbarSub+'.root')

		STtWBmcPileUp = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_none_pileup_up_PSET_'+options.cuts+ttbarSub+'.root')
		STtWBmcPileDown = ROOT.TFile("rootfiles/"+dataLumi+'/TWanalyzerweightedsingletop_tWB_Trigger_nominal_none_pileup_down_PSET_'+options.cuts+ttbarSub+'.root')


	#------------Grab histos --------------------------------------
		# Nominal
		TTmcFS = TTmc.Get("Mt")
		STmcFS = STmc.Get("Mt")

		STtmcFS = STtmc.Get("Mt")
		STtBmcFS = STtBmc.Get("Mt")
		STtWmcFS = STtWmc.Get("Mt")
		STtWBmcFS = STtWBmc.Get("Mt")

		# QCD bkg
		TTmcQCD = TTmc.Get("QCDbkgMt")
		TTmcQCD2d = TTmc.Get("QCDbkgMt2D")

		STmcQCD = STmc.Get("QCDbkgMt")
		STmcQCD2d = STmc.Get("QCDbkgMt2D")

		# Grab top full selections of uncertainties
		TTmcFSPtScaleUp = TTmcPtScaleUp.Get("Mt")
		TTmcFSPtScaleDown = TTmcPtScaleDown.Get("Mt")

		TTmcFSPtSmearUp = TTmcPtSmearUp.Get("Mt")
		TTmcFSPtSmearDown = TTmcPtSmearDown.Get("Mt")

		TTmcFSMassScaleUp = TTmcMassScaleUp.Get("Mt")
		TTmcFSMassScaleDown = TTmcMassScaleDown.Get("Mt")

		TTmcFSMassSmearUp = TTmcMassSmearUp.Get("Mt")
		TTmcFSMassSmearDown = TTmcMassSmearDown.Get("Mt")

		# TTmcFSQ2ScaleUp = TTmcQ2ScaleUp.Get("Mt")
		# TTmcFSQ2ScaleDown = TTmcQ2ScaleDown.Get("Mt")

		TTmcFSPileUp = TTmcPileUp.Get("Mt")
		TTmcFSPileDown = TTmcPileDown.Get("Mt")

		TTmcFSPDFUp = TTmcPDFUp.Get("Mt")
		TTmcFSPDFDown = TTmcPDFDown.Get("Mt")

		# Grab single top full selections of uncertainties
		# t
		STtmcFSPtScaleUp = STtmcPtScaleUp.Get("Mt")
		STtmcFSPtScaleDown = STtmcPtScaleDown.Get("Mt")

		STtmcFSPtSmearUp = STtmcPtSmearUp.Get("Mt")
		STtmcFSPtSmearDown = STtmcPtSmearDown.Get("Mt")

		STtmcFSMassScaleUp = STtmcMassScaleUp.Get("Mt")
		STtmcFSMassScaleDown = STtmcMassScaleDown.Get("Mt")

		STtmcFSMassSmearUp = STtmcMassSmearUp.Get("Mt")
		STtmcFSMassSmearDown = STtmcMassSmearDown.Get("Mt")

		STtmcFSPileUp = STtmcPileUp.Get("Mt")
		STtmcFSPileDown = STtmcPileDown.Get("Mt")

		# tB
		STtBmcFSPtScaleUp = STtBmcPtScaleUp.Get("Mt")
		STtBmcFSPtScaleDown = STtBmcPtScaleDown.Get("Mt")

		STtBmcFSPtSmearUp = STtBmcPtSmearUp.Get("Mt")
		STtBmcFSPtSmearDown = STtBmcPtSmearDown.Get("Mt")

		STtBmcFSMassScaleUp = STtBmcMassScaleUp.Get("Mt")
		STtBmcFSMassScaleDown = STtBmcMassScaleDown.Get("Mt")

		STtBmcFSMassSmearUp = STtBmcMassSmearUp.Get("Mt")
		STtBmcFSMassSmearDown = STtBmcMassSmearDown.Get("Mt")

		STtBmcFSPileUp = STtBmcPileUp.Get("Mt")
		STtBmcFSPileDown = STtBmcPileDown.Get("Mt")

		# tW
		STtWmcFSPtScaleUp = STtWmcPtScaleUp.Get("Mt")
		STtWmcFSPtScaleDown = STtWmcPtScaleDown.Get("Mt")

		STtWmcFSPtSmearUp = STtWmcPtSmearUp.Get("Mt")
		STtWmcFSPtSmearDown = STtWmcPtSmearDown.Get("Mt")

		STtWmcFSMassScaleUp = STtWmcMassScaleUp.Get("Mt")
		STtWmcFSMassScaleDown = STtWmcMassScaleDown.Get("Mt")

		STtWmcFSMassSmearUp = STtWmcMassSmearUp.Get("Mt")
		STtWmcFSMassSmearDown = STtWmcMassSmearDown.Get("Mt")

		STtWmcFSPileUp = STtWmcPileUp.Get("Mt")
		STtWmcFSPileDown = STtWmcPileDown.Get("Mt")

		# tWB
		STtWBmcFSPtScaleUp = STtWBmcPtScaleUp.Get("Mt")
		STtWBmcFSPtScaleDown = STtWBmcPtScaleDown.Get("Mt")

		STtWBmcFSPtSmearUp = STtWBmcPtSmearUp.Get("Mt")
		STtWBmcFSPtSmearDown = STtWBmcPtSmearDown.Get("Mt")

		STtWBmcFSMassScaleUp = STtWBmcMassScaleUp.Get("Mt")
		STtWBmcFSMassScaleDown = STtWBmcMassScaleDown.Get("Mt")

		STtWBmcFSMassSmearUp = STtWBmcMassSmearUp.Get("Mt")
		STtWBmcFSMassSmearDown = STtWBmcMassSmearDown.Get("Mt")

		STtWBmcFSPileUp = STtWBmcPileUp.Get("Mt")
		STtWBmcFSPileDown = STtWBmcPileDown.Get("Mt")


		# Grab data stuff
		DataFS = Data.Get("Mt")
		DataQCD = Data.Get("QCDbkgMt")
		DataQCD2d = Data.Get("QCDbkgMt2D")
		DataQCDUp = Data.Get("QCDbkgMth")
		DataQCDDown = Data.Get("QCDbkgMtl")
		DataQCDmodmup = Datamodmup.Get("QCDbkgMt")
		DataQCDmodmdown = Datamodmdown.Get("QCDbkgMt")
		#DataFS.Add(TTmc.Get("Mt"))

		# Get rid of double counts
		DataQCD.Add(TTmcQCD,ttSubVal)
		DataQCDUp.Add(TTmcQCD,ttSubVal)
		DataQCDDown.Add(TTmcQCD,ttSubVal)
		DataQCD2d.Add(TTmcQCD2d,ttSubVal)
		DataQCDmodmup.Add(TTmcQCD,ttSubVal)
		DataQCDmodmdown.Add(TTmcQCD,ttSubVal)


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
			QCDbkg_ARR.append(Data.Get("QCDbkgMt"+str(fittitles[ihist])).Rebin(rebin))

		BEfiterrh = kinFit_Uncertainty(QCDbkg_ARR,'Mt')

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

		TTmcFSMassScaleUp.Rebin(rebin)
		TTmcFSMassScaleDown.Rebin(rebin)

		TTmcFSMassSmearUp.Rebin(rebin)
		TTmcFSMassSmearDown.Rebin(rebin)

		TTmcFSPileUp.Rebin(rebin)
		TTmcFSPileDown.Rebin(rebin)

		TTmcFSPDFUp.Rebin(rebin)
		TTmcFSPDFDown.Rebin(rebin)

		# Singletop
		# t
		STtmcFS.Rebin(rebin)

		STtmcFSPtScaleUp.Rebin(rebin)
		STtmcFSPtScaleDown.Rebin(rebin)

		STtmcFSPtSmearUp.Rebin(rebin)
		STtmcFSPtSmearDown.Rebin(rebin)

		STtmcFSMassScaleUp.Rebin(rebin)
		STtmcFSMassScaleDown.Rebin(rebin)

		STtmcFSMassSmearUp.Rebin(rebin)
		STtmcFSMassSmearDown.Rebin(rebin)

		STtmcFSPileUp.Rebin(rebin)
		STtmcFSPileDown.Rebin(rebin)

		# tB
		STtBmcFS.Rebin(rebin)

		STtBmcFSPtScaleUp.Rebin(rebin)
		STtBmcFSPtScaleDown.Rebin(rebin)

		STtBmcFSPtSmearUp.Rebin(rebin)
		STtBmcFSPtSmearDown.Rebin(rebin)

		STtBmcFSMassScaleUp.Rebin(rebin)
		STtBmcFSMassScaleDown.Rebin(rebin)

		STtBmcFSMassSmearUp.Rebin(rebin)
		STtBmcFSMassSmearDown.Rebin(rebin)

		STtBmcFSPileUp.Rebin(rebin)
		STtBmcFSPileDown.Rebin(rebin)

		# tW
		STtWmcFS.Rebin(rebin)

		STtWmcFSPtScaleUp.Rebin(rebin)
		STtWmcFSPtScaleDown.Rebin(rebin)

		STtWmcFSPtSmearUp.Rebin(rebin)
		STtWmcFSPtSmearDown.Rebin(rebin)

		STtWmcFSMassScaleUp.Rebin(rebin)
		STtWmcFSMassScaleDown.Rebin(rebin)

		STtWmcFSMassSmearUp.Rebin(rebin)
		STtWmcFSMassSmearDown.Rebin(rebin)

		STtWmcFSPileUp.Rebin(rebin)
		STtWmcFSPileDown.Rebin(rebin)


		# tWB
		STtWBmcFS.Rebin(rebin)

		STtWBmcFSPtScaleUp.Rebin(rebin)
		STtWBmcFSPtScaleDown.Rebin(rebin)

		STtWBmcFSPtSmearUp.Rebin(rebin)
		STtWBmcFSPtSmearDown.Rebin(rebin)

		STtWBmcFSMassScaleUp.Rebin(rebin)
		STtWBmcFSMassScaleDown.Rebin(rebin)

		STtWBmcFSMassSmearUp.Rebin(rebin)
		STtWBmcFSMassSmearDown.Rebin(rebin)

		STtWBmcFSPileUp.Rebin(rebin)
		STtWBmcFSPileDown.Rebin(rebin)


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
		DataFS.SetName("mt_allhad__DATA")
		DataQCD.SetName("mt_allhad__qcd")
		DataQCDUp.SetName("mt_allhad__qcd__Fit__plus")
		DataQCDDown.SetName("mt_allhad__qcd__Fit__minus")
		DataQCDmodmup.SetName("mt_allhad__qcd__modm__plus")
		DataQCDmodmdown.SetName("mt_allhad__qcd__modm__minus")
		# DataQCDE1Up.SetName("mt_allhad__qcd__TwoD__plus")
		# DataQCDE1Down.SetName("mt_allhad__qcd__TwoD__minus")
		DataQCDE2Up.SetName("mt_allhad__qcd__Alt__plus")
		DataQCDE2Down.SetName("mt_allhad__qcd__Alt__minus")

		TTmcFS.SetName("mt_allhad__ttbar")
		#STmcFS.SetName("mt_allhad__st")

		# ttbar stuff
		TTmcFSPtScaleUp.SetName("mt_allhad__ttbar__jes__plus")
		TTmcFSPtScaleDown.SetName("mt_allhad__ttbar__jes__minus")
		
		TTmcFSPtSmearUp.SetName("mt_allhad__ttbar__jer__plus")
		TTmcFSPtSmearDown.SetName("mt_allhad__ttbar__jer__minus")

		TTmcFSMassScaleUp.SetName("mt_allhad__ttbar__jms__plus")
		TTmcFSMassScaleDown.SetName("mt_allhad__ttbar__jms__minus")
		
		TTmcFSMassSmearUp.SetName("mt_allhad__ttbar__jmr__plus")
		TTmcFSMassSmearDown.SetName("mt_allhad__ttbar__jmr__minus")

		# TTmcFSQ2ScaleUp.SetName("mt_allhad__ttbar__q2__plus")
		# TTmcFSQ2ScaleDown.SetName("mt_allhad__ttbar__q2__minus")

		TTmcFSPileUp.SetName("mt_allhad__ttbar__pile__plus")
		TTmcFSPileDown.SetName("mt_allhad__ttbar__pile__minus")

		TTmcFSPDFUp.SetName('mt_allhad__ttbar__pdf__plus')
		TTmcFSPDFDown.SetName('mt_allhad__ttbar__pdf__minus')

		# TTmcFSTup.SetName("mt_allhad__ttbar__ttag__plus")
		# TTmcFSTdown.SetName("mt_allhad__ttbar__ttag__minus")


		# Single top
		# t
		STtmcFS.SetName("mt_allhad__stt")

		STtmcFSPtScaleUp.SetName('mt_allhad__stt__jes__plus')
		STtmcFSPtScaleDown.SetName('mt_allhad__stt__jes__minus')

		STtmcFSPtSmearUp.SetName('mt_allhad__stt__jer__plus')
		STtmcFSPtSmearDown.SetName('mt_allhad__stt__jer__minus')

		STtmcFSMassScaleUp.SetName('mt_allhad__stt__jms__plus')
		STtmcFSMassScaleDown.SetName('mt_allhad__stt__jms__minus')

		STtmcFSMassSmearUp.SetName('mt_allhad__stt__jmr__plus')
		STtmcFSMassSmearDown.SetName('mt_allhad__stt__jmr__minus')

		STtmcFSPileUp.SetName('mt_allhad__stt__pile__plus')
		STtmcFSPileDown.SetName('mt_allhad__stt__pile__minus')

		# tB
		STtBmcFS.SetName("mt_allhad__sttB")

		STtBmcFSPtScaleUp.SetName('mt_allhad__sttB__jes__plus')
		STtBmcFSPtScaleDown.SetName('mt_allhad__sttB__jes__minus')

		STtBmcFSPtSmearUp.SetName('mt_allhad__sttB__jer__plus')
		STtBmcFSPtSmearDown.SetName('mt_allhad__sttB__jer__minus')

		STtBmcFSMassScaleUp.SetName('mt_allhad__sttB__jms__plus')
		STtBmcFSMassScaleDown.SetName('mt_allhad__sttB__jms__minus')

		STtBmcFSMassSmearUp.SetName('mt_allhad__sttB__jmr__plus')
		STtBmcFSMassSmearDown.SetName('mt_allhad__sttB__jmr__minus')

		STtBmcFSPileUp.SetName('mt_allhad__sttB__pile__plus')
		STtBmcFSPileDown.SetName('mt_allhad__sttB__pile__minus')

		# tW
		STtWmcFS.SetName("mt_allhad__sttW")

		STtWmcFSPtScaleUp.SetName('mt_allhad__sttW__jes__plus')
		STtWmcFSPtScaleDown.SetName('mt_allhad__sttW__jes__minus')

		STtWmcFSPtSmearUp.SetName('mt_allhad__sttW__jer__plus')
		STtWmcFSPtSmearDown.SetName('mt_allhad__sttW__jer__minus')

		STtWmcFSMassScaleUp.SetName('mt_allhad__sttW__jms__plus')
		STtWmcFSMassScaleDown.SetName('mt_allhad__sttW__jms__minus')

		STtWmcFSMassSmearUp.SetName('mt_allhad__sttW__jmr__plus')
		STtWmcFSMassSmearDown.SetName('mt_allhad__sttW__jmr__minus')

		STtWmcFSPileUp.SetName('mt_allhad__sttW__pile__plus')
		STtWmcFSPileDown.SetName('mt_allhad__sttW__pile__minus')


		# tWB
		STtWBmcFS.SetName("mt_allhad__sttWB")

		STtWBmcFSPtScaleUp.SetName('mt_allhad__sttWB__jes__plus')
		STtWBmcFSPtScaleDown.SetName('mt_allhad__sttWB__jes__minus')

		STtWBmcFSPtSmearUp.SetName('mt_allhad__sttWB__jer__plus')
		STtWBmcFSPtSmearDown.SetName('mt_allhad__sttWB__jer__minus')

		STtWBmcFSMassScaleUp.SetName('mt_allhad__sttWB__jms__plus')
		STtWBmcFSMassScaleDown.SetName('mt_allhad__sttWB__jms__minus')

		STtWBmcFSMassSmearUp.SetName('mt_allhad__sttWB__jmr__plus')
		STtWBmcFSMassSmearDown.SetName('mt_allhad__sttWB__jmr__minus')

		STtWBmcFSPileUp.SetName('mt_allhad__sttWB__pile__plus')
		STtWBmcFSPileDown.SetName('mt_allhad__sttWB__pile__minus')


	#-------Set title------------------------------------
		# Data and QCD
		DataFS.SetTitle("mt_allhad__DATA")
		DataQCD.SetTitle("mt_allhad__qcd")
		DataQCDUp.SetTitle("mt_allhad__qcd__Fit__plus")
		DataQCDDown.SetTitle("mt_allhad__qcd__Fit__minus")
		# DataQCDE1Up.SetTitle("mt_allhad__qcd__TwoD__plus")
		# DataQCDE1Down.SetTitle("mt_allhad__qcd__TwoD__minus")
		DataQCDE2Up.SetTitle("mt_allhad__qcd__Alt__plus")
		DataQCDE2Down.SetTitle("mt_allhad__qcd__Alt__minus")
		DataQCDmodmup.SetTitle("mt_allhad__qcd__modm__plus")
		DataQCDmodmdown.SetTitle("mt_allhad__qcd__modm__minus")



		TTmcFS.SetTitle("mt_allhad__ttbar")
		# STmcFS.SetTitle("mt_allhad__st")

		# ttbar stuff
		TTmcFSPtScaleUp.SetTitle("mt_allhad__ttbar__jes__plus")
		TTmcFSPtScaleDown.SetTitle("mt_allhad__ttbar__jes__minus")
		
		TTmcFSPtSmearUp.SetTitle("mt_allhad__ttbar__jer__plus")
		TTmcFSPtSmearDown.SetTitle("mt_allhad__ttbar__jer__minus")

		TTmcFSMassScaleUp.SetTitle("mt_allhad__ttbar__jms__plus")
		TTmcFSMassScaleDown.SetTitle("mt_allhad__ttbar__jms__minus")
		
		TTmcFSMassSmearUp.SetTitle("mt_allhad__ttbar__jmr__plus")
		TTmcFSMassSmearDown.SetTitle("mt_allhad__ttbar__jmr__minus")

		# TTmcFSQ2ScaleUp.SetTitle("mt_allhad__ttbar__q2__plus")
		# TTmcFSQ2ScaleDown.SetTitle("mt_allhad__ttbar__q2__minus")

		TTmcFSPileUp.SetTitle("mt_allhad__ttbar__pile__plus")
		TTmcFSPileDown.SetTitle("mt_allhad__ttbar__pile__minus")

		TTmcFSPDFUp.SetTitle('mt_allhad__ttbar__pdf__plus')
		TTmcFSPDFDown.SetTitle('mt_allhad__ttbar__pdf__minus')

		# TTmcFSTup.SetTitle("mt_allhad__ttbar__ttag__plus")
		# TTmcFSTdown.SetTitle("mt_allhad__ttbar__ttag__minus")


		# Single top
		# t
		STtmcFS.SetTitle("mt_allhad__stt")

		STtmcFSPtScaleUp.SetTitle('mt_allhad__stt__jes__plus')
		STtmcFSPtScaleDown.SetTitle('mt_allhad__stt__jes__minus')

		STtmcFSPtSmearUp.SetTitle('mt_allhad__stt__jer__plus')
		STtmcFSPtSmearDown.SetTitle('mt_allhad__stt__jer__minus')

		STtmcFSMassScaleUp.SetTitle('mt_allhad__stt__jms__plus')
		STtmcFSMassScaleDown.SetTitle('mt_allhad__stt__jms__minus')

		STtmcFSMassSmearUp.SetTitle('mt_allhad__stt__jmr__plus')
		STtmcFSMassSmearDown.SetTitle('mt_allhad__stt__jmr__minus')

		STtmcFSPileUp.SetTitle('mt_allhad__stt__pile__plus')
		STtmcFSPileDown.SetTitle('mt_allhad__stt__pile__minus')

		# tB
		STtBmcFS.SetTitle("mt_allhad__sttB")

		STtBmcFSPtScaleUp.SetTitle('mt_allhad__sttB__jes__plus')
		STtBmcFSPtScaleDown.SetTitle('mt_allhad__sttB__jes__minus')

		STtBmcFSPtSmearUp.SetTitle('mt_allhad__sttB__jer__plus')
		STtBmcFSPtSmearDown.SetTitle('mt_allhad__sttB__jer__minus')

		STtBmcFSMassScaleUp.SetTitle('mt_allhad__sttB__jms__plus')
		STtBmcFSMassScaleDown.SetTitle('mt_allhad__sttB__jms__minus')

		STtBmcFSMassSmearUp.SetTitle('mt_allhad__sttB__jmr__plus')
		STtBmcFSMassSmearDown.SetTitle('mt_allhad__sttB__jmr__minus')

		STtBmcFSPileUp.SetTitle('mt_allhad__sttB__pile__plus')
		STtBmcFSPileDown.SetTitle('mt_allhad__sttB__pile__minus')

		# tW
		STtWmcFS.SetTitle("mt_allhad__sttW")

		STtWmcFSPtScaleUp.SetTitle('mt_allhad__sttW__jes__plus')
		STtWmcFSPtScaleDown.SetTitle('mt_allhad__sttW__jes__minus')

		STtWmcFSPtSmearUp.SetTitle('mt_allhad__sttW__jer__plus')
		STtWmcFSPtSmearDown.SetTitle('mt_allhad__sttW__jer__minus')

		STtWmcFSMassScaleUp.SetTitle('mt_allhad__sttW__jms__plus')
		STtWmcFSMassScaleDown.SetTitle('mt_allhad__sttW__jms__minus')

		STtWmcFSMassSmearUp.SetTitle('mt_allhad__sttW__jmr__plus')
		STtWmcFSMassSmearDown.SetTitle('mt_allhad__sttW__jmr__minus')

		STtWmcFSPileUp.SetTitle('mt_allhad__sttW__pile__plus')
		STtWmcFSPileDown.SetTitle('mt_allhad__sttW__pile__minus')

		# tWB
		STtWBmcFS.SetTitle("mt_allhad__sttWB")

		STtWBmcFSPtScaleUp.SetTitle('mt_allhad__sttWB__jes__plus')
		STtWBmcFSPtScaleDown.SetTitle('mt_allhad__sttWB__jes__minus')

		STtWBmcFSPtSmearUp.SetTitle('mt_allhad__sttWB__jer__plus')
		STtWBmcFSPtSmearDown.SetTitle('mt_allhad__sttWB__jer__minus')

		STtWBmcFSMassScaleUp.SetTitle('mt_allhad__sttWB__jms__plus')
		STtWBmcFSMassScaleDown.SetTitle('mt_allhad__sttWB__jms__minus')

		STtWBmcFSMassSmearUp.SetTitle('mt_allhad__sttWB__jmr__plus')
		STtWBmcFSMassSmearDown.SetTitle('mt_allhad__sttWB__jmr__minus')

		STtWBmcFSPileUp.SetTitle('mt_allhad__sttWB__pile__plus')
		STtWBmcFSPileDown.SetTitle('mt_allhad__sttWB__pile__minus')


	#--------Start writing out----------------
		output.cd()

		DataFS.Write("mt_allhad__DATA")
		DataQCD.Write("mt_allhad__qcd")
		DataQCDUp.Write("mt_allhad__qcd__Fit__plus")
		DataQCDDown.Write("mt_allhad__qcd__Fit__minus")
		# DataQCDE1Up.Write("mt_allhad__qcd__TwoD__plus")
		# DataQCDE1Down.Write("mt_allhad__qcd__TwoD__minus")
		DataQCDE2Up.Write("mt_allhad__qcd__Alt__plus")
		DataQCDE2Down.Write("mt_allhad__qcd__Alt__minus")
		DataQCDmodmup.Write("mt_allhad__qcd__modm__plus")
		DataQCDmodmdown.Write("mt_allhad__qcd__modm__minus")
		#DataQCDBEH.Write("mt_allhad__qcd__bkg__plus")
		#DataQCDBEL.Write("mt_allhad__qcd__bkg__minus")

		TTmcFS.Write("mt_allhad__ttbar")
		# STmcFS.Write("mt_allhad__st")

		# ttbar stuff
		TTmcFSPtScaleUp.Write("mt_allhad__ttbar__jes__plus")
		TTmcFSPtScaleDown.Write("mt_allhad__ttbar__jes__minus")
		
		TTmcFSPtSmearUp.Write("mt_allhad__ttbar__jer__plus")
		TTmcFSPtSmearDown.Write("mt_allhad__ttbar__jer__minus")

		TTmcFSMassScaleUp.Write("mt_allhad__ttbar__jms__plus")
		TTmcFSMassScaleDown.Write("mt_allhad__ttbar__jms__minus")
		
		TTmcFSMassSmearUp.Write("mt_allhad__ttbar__jmr__plus")
		TTmcFSMassSmearDown.Write("mt_allhad__ttbar__jmr__minus")

		# TTmcFSQ2ScaleUp.Write("mt_allhad__ttbar__q2__plus")
		# TTmcFSQ2ScaleDown.Write("mt_allhad__ttbar__q2__minus")

		TTmcFSPileUp.Write("mt_allhad__ttbar__pile__plus")
		TTmcFSPileDown.Write("mt_allhad__ttbar__pile__minus")

		TTmcFSPDFUp.Write('mt_allhad__ttbar__pdf__plus')
		TTmcFSPDFDown.Write('mt_allhad__ttbar__pdf__minus')

		# TTmcFSTup.Write("mt_allhad__ttbar__ttag__plus")
		# TTmcFSTdown.Write("mt_allhad__ttbar__ttag__minus")


		# Single top
		# t
		STtmcFS.Write("mt_allhad__stt")

		STtmcFSPtScaleUp.Write('mt_allhad__stt__jes__plus')
		STtmcFSPtScaleDown.Write('mt_allhad__stt__jes__minus')

		STtmcFSPtSmearUp.Write('mt_allhad__stt__jer__plus')
		STtmcFSPtSmearDown.Write('mt_allhad__stt__jer__minus')

		STtmcFSMassScaleUp.Write('mt_allhad__stt__jms__plus')
		STtmcFSMassScaleDown.Write('mt_allhad__stt__jms__minus')

		STtmcFSMassSmearUp.Write('mt_allhad__stt__jmr__plus')
		STtmcFSMassSmearDown.Write('mt_allhad__stt__jmr__minus')

		STtmcFSPileUp.Write('mt_allhad__stt__pile__plus')
		STtmcFSPileDown.Write('mt_allhad__stt__pile__minus')

		# tB
		STtBmcFS.Write("mt_allhad__sttB")

		STtBmcFSPtScaleUp.Write('mt_allhad__sttB__jes__plus')
		STtBmcFSPtScaleDown.Write('mt_allhad__sttB__jes__minus')

		STtBmcFSPtSmearUp.Write('mt_allhad__sttB__jer__plus')
		STtBmcFSPtSmearDown.Write('mt_allhad__sttB__jer__minus')

		STtBmcFSMassScaleUp.Write('mt_allhad__sttB__jms__plus')
		STtBmcFSMassScaleDown.Write('mt_allhad__sttB__jms__minus')

		STtBmcFSMassSmearUp.Write('mt_allhad__sttB__jmr__plus')
		STtBmcFSMassSmearDown.Write('mt_allhad__sttB__jmr__minus')

		STtBmcFSPileUp.Write('mt_allhad__sttB__pile__plus')
		STtBmcFSPileDown.Write('mt_allhad__sttB__pile__minus')

		# tW
		STtWmcFS.Write("mt_allhad__sttW")

		STtWmcFSPtScaleUp.Write('mt_allhad__sttW__jes__plus')
		STtWmcFSPtScaleDown.Write('mt_allhad__sttW__jes__minus')

		STtWmcFSPtSmearUp.Write('mt_allhad__sttW__jer__plus')
		STtWmcFSPtSmearDown.Write('mt_allhad__sttW__jer__minus')

		STtWmcFSMassScaleUp.Write('mt_allhad__sttW__jms__plus')
		STtWmcFSMassScaleDown.Write('mt_allhad__sttW__jms__minus')

		STtWmcFSMassSmearUp.Write('mt_allhad__sttW__jmr__plus')
		STtWmcFSMassSmearDown.Write('mt_allhad__sttW__jmr__minus')

		STtWmcFSPileUp.Write('mt_allhad__sttW__pile__plus')
		STtWmcFSPileDown.Write('mt_allhad__sttW__pile__minus')

		# tWB
		STtWBmcFS.Write("mt_allhad__sttWB")

		STtWBmcFSPtScaleUp.Write('mt_allhad__sttWB__jes__plus')
		STtWBmcFSPtScaleDown.Write('mt_allhad__sttWB__jes__minus')

		STtWBmcFSPtSmearUp.Write('mt_allhad__sttWB__jer__plus')
		STtWBmcFSPtSmearDown.Write('mt_allhad__sttWB__jer__minus')

		STtWBmcFSMassScaleUp.Write('mt_allhad__sttWB__jms__plus')
		STtWBmcFSMassScaleDown.Write('mt_allhad__sttWB__jms__minus')

		STtWBmcFSMassSmearUp.Write('mt_allhad__sttWB__jmr__plus')
		STtWBmcFSMassSmearDown.Write('mt_allhad__sttWB__jmr__minus')

		STtWBmcFSPileUp.Write('mt_allhad__sttWB__pile__plus')
		STtWBmcFSPileDown.Write('mt_allhad__sttWB__pile__minus')


		xsecDict = {}
		for RA in range(0,len(mass)):
			SignalB11 = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_none_PSET_"+cuts+".root")

			SignalB11PtScaleUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JES_up_PSET_"+options.cuts+ttbarSub+".root")
			SignalB11PtScaleDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JES_down_PSET_"+options.cuts+ttbarSub+".root")


			SignalB11PtSmearUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JER_up_PSET_"+options.cuts+ttbarSub+".root")
			SignalB11PtSmearDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JER_down_PSET_"+options.cuts+ttbarSub+".root")


			SignalB11MassScaleUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JMS_up_PSET_"+options.cuts+ttbarSub+".root")
			SignalB11MassScaleDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JMS_down_PSET_"+options.cuts+ttbarSub+".root")


			SignalB11MassSmearUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JMR_up_PSET_"+options.cuts+ttbarSub+".root")
			SignalB11MassSmearDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_JMR_down_PSET_"+options.cuts+ttbarSub+".root")


			SignalB11PileUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_none_pileup_up_PSET_"+options.cuts+ttbarSub+".root")
			SignalB11PileDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_none_pileup_down_PSET_"+options.cuts+ttbarSub+".root")


			SignalB11PDFUp = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_none_pdf_up_PSET_"+options.cuts+ttbarSub+".root")
			SignalB11PDFDown = ROOT.TFile("rootfiles/"+dataLumi+"/TWanalyzerweightedsignal"+hand+str(mass[RA])+"_Trigger_nominal_none_pdf_down_PSET_"+options.cuts+ttbarSub+".root")



			SignalFS = SignalB11.Get("Mt")
			# SignalTup = SignalB11.Get("MtTup")
			# SignalTdown = SignalB11.Get("MtTdown")

			SignalPDFUp = SignalB11PDFUp.Get("Mt")
			SignalPDFDown = SignalB11PDFDown.Get("Mt")

			SignalPtScaleup = SignalB11PtScaleUp.Get("Mt")
			SignalPtScaledown = SignalB11PtScaleDown.Get("Mt")

			SignalPtSmearup = SignalB11PtSmearUp.Get("Mt")
			SignalPtSmeardown = SignalB11PtSmearDown.Get("Mt")

			SignalMassScaleup = SignalB11MassScaleUp.Get("Mt")
			SignalMassScaledown = SignalB11MassScaleDown.Get("Mt")

			SignalMassSmearup = SignalB11MassSmearUp.Get("Mt")
			SignalMassSmeardown = SignalB11MassSmearDown.Get("Mt")

			SignalPileup = SignalB11PileUp.Get("Mt")
			SignalPiledown = SignalB11PileDown.Get("Mt")


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

			SignalPtScaleup.Rebin(rebin)
			SignalPtScaledown.Rebin(rebin)

			SignalPtSmearup.Rebin(rebin)
			SignalPtSmeardown.Rebin(rebin)

			SignalMassScaleup.Rebin(rebin)
			SignalMassScaledown.Rebin(rebin)

			SignalMassSmearup.Rebin(rebin)
			SignalMassSmeardown.Rebin(rebin)

			SignalPDFShapeUp.Rebin(rebin)
			SignalPDFShapeDown.Rebin(rebin)

			SignalPileup.Rebin(rebin)
			SignalPiledown.Rebin(rebin)


			SignalFS.SetTitle("mt_allhad__bs"+str(mass[RA]))
			SignalPtScaleup.SetTitle("mt_allhad__bs"+str(mass[RA])+"__jes__plus")
			SignalPtScaledown.SetTitle("mt_allhad__bs"+str(mass[RA])+"__jes__minus")
			SignalPtSmearup.SetTitle("mt_allhad__bs"+str(mass[RA])+"__jer__plus")
			SignalPtSmeardown.SetTitle("mt_allhad__bs"+str(mass[RA])+"__jer__minus")
			SignalMassScaleup.SetTitle("mt_allhad__bs"+str(mass[RA])+"__jms__plus")
			SignalMassScaledown.SetTitle("mt_allhad__bs"+str(mass[RA])+"__jms__minus")
			SignalMassSmearup.SetTitle("mt_allhad__bs"+str(mass[RA])+"__jmr__plus")
			SignalMassSmeardown.SetTitle("mt_allhad__bs"+str(mass[RA])+"__jmr__minus")
			SignalPileup.SetTitle("mt_allhad__bs"+str(mass[RA])+"__pile__plus")
			SignalPiledown.SetTitle("mt_allhad__bs"+str(mass[RA])+"__pile__minus")
			SignalPDFShapeUp.SetTitle('mt_allhad__bs'+str(mass[RA])+'__pdf__plus')
			SignalPDFShapeDown.SetTitle('mt_allhad__bs'+str(mass[RA])+'__pdf__minus')


			SignalFS.SetName("mt_allhad__bs"+str(mass[RA]))
			SignalPtScaleup.SetName("mt_allhad__bs"+str(mass[RA])+"__jes__plus")
			SignalPtScaledown.SetName("mt_allhad__bs"+str(mass[RA])+"__jes__minus")
			SignalPtSmearup.SetName("mt_allhad__bs"+str(mass[RA])+"__jer__plus")
			SignalPtSmeardown.SetName("mt_allhad__bs"+str(mass[RA])+"__jer__minus")
			SignalMassScaleup.SetName("mt_allhad__bs"+str(mass[RA])+"__jms__plus")
			SignalMassScaledown.SetName("mt_allhad__bs"+str(mass[RA])+"__jms__minus")
			SignalMassSmearup.SetName("mt_allhad__bs"+str(mass[RA])+"__jmr__plus")
			SignalMassSmeardown.SetName("mt_allhad__bs"+str(mass[RA])+"__jmr__minus")
			SignalPileup.SetName("mt_allhad__bs"+str(mass[RA])+"__pile__plus")
			SignalPiledown.SetName("mt_allhad__bs"+str(mass[RA])+"__pile__minus")
			SignalPDFShapeUp.SetName('mt_allhad__bs'+str(mass[RA])+'__pdf__plus')
			SignalPDFShapeDown.SetName('mt_allhad__bs'+str(mass[RA])+'__pdf__minus')


			SignalFS.Write("mt_allhad__bs"+str(mass[RA]))
			SignalPtScaleup.Write("mt_allhad__bs"+str(mass[RA])+"__jes__plus")
			SignalPtScaledown.Write("mt_allhad__bs"+str(mass[RA])+"__jes__minus")
			SignalPtSmearup.Write("mt_allhad__bs"+str(mass[RA])+"__jer__plus")
			SignalPtSmeardown.Write("mt_allhad__bs"+str(mass[RA])+"__jer__minus")
			SignalMassScaleup.Write("mt_allhad__bs"+str(mass[RA])+"__jms__plus")
			SignalMassScaledown.Write("mt_allhad__bs"+str(mass[RA])+"__jms__minus")
			SignalMassSmearup.Write("mt_allhad__bs"+str(mass[RA])+"__jmr__plus")
			SignalMassSmeardown.Write("mt_allhad__bs"+str(mass[RA])+"__jmr__minus")
			SignalPileup.Write("mt_allhad__bs"+str(mass[RA])+"__pile__plus")
			SignalPiledown.Write("mt_allhad__bs"+str(mass[RA])+"__pile__minus")
			SignalPDFShapeUp.Write('mt_allhad__bs'+str(mass[RA])+'__pdf__plus')
			SignalPDFShapeDown.Write('mt_allhad__bs'+str(mass[RA])+'__pdf__minus')


		xsecFile = open('results/xsec_dict_'+coup+'_had.pkl',"wb")
		pickle.dump(xsecDict,xsecFile)
		xsecFile.close()
		


	
