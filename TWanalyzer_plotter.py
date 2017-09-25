

import os
import array
import glob
import math
import ROOT
import sys
from ROOT import *
from array import *
from optparse import OptionParser
gROOT.Macro("rootlogon.C")
gROOT.LoadMacro("insertlogo.C+")
parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
                  default       =       'data',
                  dest          =       'set',
                  help          =       'data or QCD or ttbar')
parser.add_option('-v', '--var', metavar='F', type='string', action='store',
                  default       =       'analyzer',
                  dest          =       'var',
                  help          =       'anaylzer or kinematics')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-l', '--lumi', metavar='F', type='string', action='store',
                  default	=	'35851pb',
                  dest		=	'lumi',
                  help		=	'Lumi folder to look in')
parser.add_option('-x', '--pileup', metavar='F', type='string', action='store',
                  default	=	'on',
                  dest		=	'pileup',
                  help		=	'If not data do pileup reweighting?')
parser.add_option('-u', '--ptreweight', metavar='F', type='string', action='store',
				  default	=	'on',
				  dest		=	'ptreweight',
				  help		=	'on or off')
parser.add_option('--noExtraPtCorrection', metavar='F', action='store_false',
				  default=True,
				  dest='extraPtCorrection',
				  help='Call to turn off extraPtCorrection')
parser.add_option('-b', '--blinded', metavar='F', type='string', action='store',
                  default	=	'off',
                  dest		=	'blinded',
                  help		=	'Hides data if on')
parser.add_option('-m', '--mcsf', metavar='F', type='string', action='store',
                  default	=	'off',
                  dest		=	'mcsf',
                  help		=	'Turns QCD MC scale factor on and off')
#Not used
parser.add_option('-y', '--modmass', metavar='F', type='string', action='store',
                  default	=	'nominal',
                  dest		=	'modmass',
                  help		=	'nominal up or down')
parser.add_option('-p', '--bprime', metavar='F', action='store_true',
                  default       =       False,
                  dest          =       'bprime',
                  help          =       'True if running bprime. False if running bstar.')
parser.add_option('-C', '--printCanvas', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'printCanvas',
				  help		=	'on or off')
(options, args) = parser.parse_args()

if options.printCanvas == 'off':
	ROOT.gROOT.SetBatch(True)
	ROOT.PyConfig.IgnoreCommandLineOptions = True


cuts = options.cuts


import Bstar_Functions_local	
from Bstar_Functions_local import *

#Consts = LoadConstants()
#lumi = Consts['lumi']
#Lumi = str(int(lumi/1000))+'fb'
Lumi = options.lumi

pie = TMath.Pi()

kinVar = ['Mtw', 	'EtaTop', 	'EtaW', 	'PtTop', 	'PtW', 		'PtTopW', 	'PhiTop', 	'PhiW', 	'dPhi',		'Mt']
kinBkg = ['', 		'ET', 		'EW', 		'PT', 		'PW', 		'PTW', 		'PhT', 		'PhW', 		'dPhi',		'Mt']
kinBin = [140, 		12, 		12, 		50, 		50,			35,			12,			12,			12,			25    ]
kinLow = [500, 		-2.4, 		-2.4, 		450, 		370,		0,		   -pie,		-pie,		2.2,		105   ]
kinHigh= [4000, 	2.4, 		2.4, 		1500, 		1430,		700,		pie,		pie,		pie,		210   ]
rebin =  [4,		 1,		 	1, 		 	2,		 	2,		 	1,		 	1,			 1,		 	1,			1    ]
st1_label= [";M_{tw} (GeV);Counts", ";Eta_{t} (rad);Counts", ";Eta_{W} (rad);Counts", ";top p_{T} (GeV);Counts", ";W p_{T} (GeV);Counts", ";tW pair p_{T} (GeV);Counts", ";Phi_{t} (rad)", ";Phi_{W} (rad);Counts", ";Delta Phi (rad);Counts", ";M_{t} (Gev);Counts"]
pull_label= [";M_{tw} (GeV);(Data-Bkg)/#sigma", ";Eta_{t} (rad);(Data-Bkg)/#sigma", ";Eta_{W} (rad);(Data-Bkg)/#sigma", ";top p_{T} (GeV);(Data-Bkg)/#sigma", ";W p_{T} (GeV);(Data-Bkg)/#sigma", ";tW pair p_{T} (GeV);(Data-Bkg)/#sigma", ";Phi_{t} (rad)", ";Phi_{W} (rad);(Data-Bkg)/#sigma", ";Delta Phi (rad);(Data-Bkg)/#sigma", ";M_{t} (GeV);(Data-Bkg)/#sigma"]

if options.var == 'analyzer':
	iterations = 1
	kin = ''
elif options.var == 'kinematics':
	iterations = len(kinVar)
	kin = ''
else:
	print "Error in var option"
	quit()

pustr = 'none'
if options.pileup == 'off':
	pustr = 'pileup_unweighted'

ptString = ''
if options.ptreweight == 'off':
	ptString = '_ptreweight_off'
elif not options.extraPtCorrection:
	ptString = '_noExtraPtCorrection'

mmstr = ""
if options.modmass!="nominal":
	print "using modm uncertainty"
	mmstr = "_modm_"+options.modmass

if options.blinded == 'on':
	sBlind = '_blinded'
else:
	sBlind = ''

if options.cuts == 'default' and options.var == 'analyzer':
	mod = ['none','none_pileup_up','none_pileup_down','JES_up','JES_down','JER_up','JER_down','JMS_up','JMS_down','JMR_up','JMR_down','none_pdf_up','none_pdf_down']
	subtractPDF = -2
else:
	mod = ['none']
	subtractPDF = 0
#string lists for naming
SR1200sList = []
SR2800sList = []
SR2000sList = []
TTmcsList = []
for m in mod:
	SR1200sList.append("rootfiles/"+Lumi+"/TWanalyzerweightedsignalRH1200_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+kin+".root")
	SR2800sList.append("rootfiles/"+Lumi+"/TWanalyzerweightedsignalRH2800_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+kin+".root")
	SR2000sList.append("rootfiles/"+Lumi+"/TWanalyzerweightedsignalRH2000_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+kin+".root")
	#BPB1200sList.append("rootfiles/"+Lumi+"/TWanalyzerBprimeBToTW1200_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+kin+"weighted.root")
	#BPB1400sList.append("rootfiles/"+Lumi+"/TWanalyzerBprimeBToTW1400_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+kin+"weighted.root")
	#BPB1600sList.append("rootfiles/"+Lumi+"/TWanalyzerBprimeBToTW1600_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+kin+"weighted.root")
	#BPB1800sList.append("rootfiles/"+Lumi+"/TWanalyzerBprimeBToTW1800_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+kin+"weighted.root")
	#BPT1200sList.append("rootfiles/"+Lumi+"/TWanalyzerBprimeTToTW1200_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+kin+"weighted.root")
	#BPT1400sList.append("rootfiles/"+Lumi+"/TWanalyzerBprimeTToTW1400_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+kin+"weighted.root")
	#BPT1600sList.append("rootfiles/"+Lumi+"/TWanalyzerBprimeTToTW1600_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+kin+"weighted.root")
	#BPT1800sList.append("rootfiles/"+Lumi+"/TWanalyzerBprimeTToTW1800_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+kin+"weighted.root")
	if m == 'none':
		TTmcsList.append("rootfiles/"+Lumi+"/TWanalyzer"+"weightedttbar_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+ptString+kin+".root")
	else:
		TTmcsList.append("rootfiles/"+Lumi+"/TWanalyzer"+"weightedttbar_Trigger_nominal_"+m+mmstr+"_PSET_"+options.cuts+kin+".root")


#Make root file lists by pulling from string lists
# Subtract 2 from signals because we don't want full PDF uncertainties
SR1200fList = []
for i in range(len(SR1200sList)-subtractPDF):
	# print SR1200sList[i]
	SR1200fList.append(ROOT.TFile(SR1200sList[i]))

SR2800fList = []
for i in range(len(SR2800sList)-subtractPDF):
	SR2800fList.append(ROOT.TFile(SR2800sList[i]))

SR2000fList = []
for i in range(len(SR2000sList)-subtractPDF):
	SR2000fList.append(ROOT.TFile(SR2000sList[i]))

TTmcfList = []
for i in range(len(TTmcsList)):
	TTmcfList.append(ROOT.TFile(TTmcsList[i]))

#Have to also put the two extra ttbar files in TTmcfList
if options.cuts == 'default' and options.var == 'analyzer':
	TTmcfList.append(ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzer"+"weightedttbarscaleup_Trigger_nominal_"+pustr+mmstr+"_PSET_"+options.cuts+kin+".root"))
	TTmcfList.append(ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzer"+"weightedttbarscaledown_Trigger_nominal_"+pustr+mmstr+"_PSET_"+options.cuts+kin+".root"))


Data = ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzer"+options.set+"_Trigger_nominal_"+pustr+mmstr+"_PSET_"+options.cuts+kin+".root")
DataMmup = ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzer"+options.set+"_Trigger_nominal_"+pustr+"_modm_up_PSET_"+options.cuts+kin+".root")
DataMmdown = ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzer"+options.set+"_Trigger_nominal_"+pustr+"_modm_down_PSET_"+options.cuts+kin+".root")

print "Root file opened"

#---------For ttbar closure test, using MtStack-----------------------------------
# Outdated

# st2 = ROOT.THStack('st2','st2')
# MtStackData = Data.Get('Mt')
# MtStackBE = Data.Get('QCDbkgMt')
# MtStackTTmc = TTmcfList[0].Get('Mt')
# MtStackTTmcBE = TTmcfList[0].Get('QCDbkgMt')

# MtStackData.Rebin(1)
# MtStackBE.Rebin(1)
# MtStackTTmc.Rebin(1)
# MtStackTTmcBE.Rebin(1)

# cMtStack = TCanvas('MtStack', 'Top mass with Full selection', 700, 700)
# legend = TLegend(0.7, 0.7, 0.93, 0.9)

# cMtStack.SetLeftMargin(0.16)
# cMtStack.SetRightMargin(0.05)
# cMtStack.SetTopMargin(0.13)
# cMtStack.SetBottomMargin(0.15)

# MtStackBE.Add(MtStackTTmcBE,-1)

# MtStackBE.SetFillColor(kYellow)
# MtStackTTmc.SetFillColor(kRed)
# st2.Add(MtStackBE)
# st2.Add(MtStackTTmc)

# legend.AddEntry( MtStackData, 'Data', 'P')
# legend.AddEntry( MtStackBE, 'QCD background prediction', 'F')	
# legend.AddEntry( MtStackTTmc, 't#bar{t} MC prediction', 'F')

# st2.SetMaximum(MtStackData.GetMaximum() * 1.3)
# st2.SetMinimum(0.1)
# st2.SetTitle(";M_{t} (GeV);Counts")
# st2.Draw("hist")

# MtStackData.SetMaximum(MtStackData.GetMaximum() * 1.3)
# MtStackData.Draw("same")

# cMtStack.cd()

# legend.Draw()

# cMtStack.Print('rootfiles/'+Lumi+'/MtStack_'+Lumi+'_'+options.set+'_'+options.cuts+'.root')
# cMtStack.Print('rootfiles/'+Lumi+'/MtStack_'+Lumi+'_'+options.set+'_'+options.cuts+'.pdf')
# cMtStack.Print('rootfiles/'+Lumi+'/MtStack_'+Lumi+'_'+options.set+'_'+options.cuts+'.png')





#------------------Resume---------------------------------------------------------

for i in range(0, iterations):
	print "kinVar = " + "'" + kinVar[i] + "'"
	print "kinBkg = " + "'" + kinBkg[i] + "'"

	st1 = ROOT.THStack('st1', 'st1')

	if i == 0:
		leg = TLegend(0.6, 0.55, 0.93, 0.9)
	else:
		leg = TLegend(0.0, 0.0, 1.0, 1.0)
	leg.SetNColumns(1)
	leg.SetFillColor(0)
	leg.SetBorderSize(0)





#bins=[500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1200,1300,1400,1500,1700,1900,2300,2700,3100]
#bins.append(3000)
#bins2=array('d',bins)

	Mult = 1.0

#Kfac=1.2



	DataFS = Data.Get(kinVar[i])
	DataBE = Data.Get("QCDbkg" + kinBkg[i])

	DataBE2d = Data.Get("QCDbkg" + kinBkg[i]+"2D")
	DataBEMmup = DataMmup.Get("QCDbkg" + kinBkg[i])
	DataBEMmdown = DataMmdown.Get("QCDbkg" + kinBkg[i])
	DataBE2dup = Data.Get("QCDbkg" + kinBkg[i]+"2Dup")
	DataBE2ddown = Data.Get("QCDbkg" + kinBkg[i]+"2Ddown")

	#Selections in order (Selection, PUup, PUdown, JESup, JESdown, JERup, JERdown, Wup, Wdown, trigup, trig down)
	SR1200FS = []
	for j in range(len(SR1200fList)):
		SR1200FS.append(SR1200fList[j].Get(kinVar[i]))
	SR2800FS = []
	for j in range(len(SR2800fList)):
		SR2800FS.append(SR2800fList[j].Get(kinVar[i]))

	SR2000FS = []
	for j in range(len(SR2000fList)):
		SR2000FS.append(SR2000fList[j].Get(kinVar[i]))

	#BPT1200FS = []
	#for j in range(len(BPT1200fList)):
	#	BPT1200FS.append(BPT1200fList[j].Get(kinVar[i]))

	#BPT1400FS = []
	#for j in range(len(BPT1400fList)):
	#	BPT1400FS.append(BPT1400fList[j].Get(kinVar[i]))

	#BPT1600FS = []
	#for j in range(len(BPT1600fList)):
	#	BPT1600FS.append(BPT1600fList[j].Get(kinVar[i]))

	#BPT1800FS = []
	#for j in range(len(BPT1800fList)):
	#	BPT1800FS.append(BPT1800fList[j].Get(kinVar[i]))

	if options.var == 'analyzer':
		# Need to calculate the PDF shape uncertainty and then append it
		SR1200fPDFup = TFile(SR1200sList[-2])
		SR1200fPDFdown = TFile(SR1200sList[-1])
		SR1200PDFup, SR1200PDFdown = PDFShapeUncert(SR1200fList[0].Get('Mtw'),SR1200fPDFup.Get('Mtw'),SR1200fPDFdown.Get('Mtw'))
		SR1200FS.append(SR1200PDFup)
		SR1200FS.append(SR1200PDFdown)
		#[0] index is your regular full selection
		SR1200trigup = SR1200fList[0].Get("Mtwtrigup")
		SR1200trigdown = SR1200fList[0].Get("Mtwtrigdown")
		SR1200Wup = SR1200fList[0].Get("MtwWup")
		SR1200Wdown = SR1200fList[0].Get("MtwWdown")
		SR1200ExtrapUp = SR1200fList[0].Get("MtwExtrapUp")
		SR1200ExtrapDown = SR1200fList[0].Get("MtwExtrapDown")
		SR1200FS.append(SR1200trigup)
		SR1200FS.append(SR1200trigdown)
		SR1200FS.append(SR1200Wup)
		SR1200FS.append(SR1200Wdown)
		SR1200FS.append(SR1200ExtrapUp)
		SR1200FS.append(SR1200ExtrapDown)


		# Need to calculate the PDF shape uncertainty and then append it
		SR2800fPDFup = TFile(SR2800sList[-2])
		SR2800fPDFdown = TFile(SR2800sList[-1])
		SR2800PDFup, SR2800PDFdown = PDFShapeUncert(SR2800fList[0].Get('Mtw'),SR2800fPDFup.Get('Mtw'),SR2800fPDFdown.Get('Mtw'))
		SR2800FS.append(SR2800PDFup)
		SR2800FS.append(SR2800PDFdown)
		#[0] index is your regular full selection
		SR2800trigup = SR2800fList[0].Get("Mtwtrigup")
		SR2800trigdown = SR2800fList[0].Get("Mtwtrigdown")
		SR2800Wup = SR2800fList[0].Get("MtwWup")
		SR2800Wdown = SR2800fList[0].Get("MtwWdown")
		SR2800ExtrapUp = SR2800fList[0].Get("MtwExtrapUp")
		SR2800ExtrapDown = SR2800fList[0].Get("MtwExtrapDown")
		SR2800FS.append(SR2800trigup)
		SR2800FS.append(SR2800trigdown)
		SR2800FS.append(SR2800Wup)
		SR2800FS.append(SR2800Wdown)
		SR2800FS.append(SR2800ExtrapUp)
		SR2800FS.append(SR2800ExtrapDown)
	
		# Need to calculate the PDF shape uncertainty and then append it
		SR2000fPDFup = TFile(SR2000sList[-2])
		SR2000fPDFdown = TFile(SR2000sList[-1])
		SR2000PDFup, SR2000PDFdown = PDFShapeUncert(SR2000fList[0].Get('Mtw'),SR2000fPDFup.Get('Mtw'),SR2000fPDFdown.Get('Mtw'))
		SR2000FS.append(SR2000PDFup)
		SR2000FS.append(SR2000PDFdown)
		#[0] index is your regular full selection
		SR2000trigup = SR2000fList[0].Get("Mtwtrigup")
		SR2000trigdown = SR2000fList[0].Get("Mtwtrigdown")
		SR2000Wup = SR2000fList[0].Get("MtwWup")
		SR2000Wdown = SR2000fList[0].Get("MtwWdown")
		SR2000ExtrapUp = SR2000fList[0].Get("MtwExtrapUp")
		SR2000ExtrapDown = SR2000fList[0].Get("MtwExtrapDown")
		SR2000FS.append(SR2000trigup)
		SR2000FS.append(SR2000trigdown)
		SR2000FS.append(SR2000Wup)
		SR2000FS.append(SR2000Wdown)
		SR2000FS.append(SR2000ExtrapUp)
		SR2000FS.append(SR2000ExtrapDown)

	
		#BPB1200FS = []
		#for j in range(len(BPB1200fList)):
		#	BPB1200FS.append(BPB1200fList[j].Get(kinVar[i]))

		#[0] index is your regular full selection
		#BPB1200trigup = BPB1200fList[0].Get("Mtwtrigup")
		#BPB1200trigdown = BPB1200fList[0].Get("Mtwtrigdown")
		#BPB1200Wup = BPB1200fList[0].Get("MtwWup")
		#BPB1200Tdown = BPB1200fList[0].Get("MtwTdown")
		#BPB1200FS.append(BPB1200Wup)
		#BPB1200FS.append(BPB1200Tdown)
		#BPB1200FS.append(BPB1200trigup)
		#BPB1200FS.append(BPB1200trigdown)

		#BPB1400FS = []
		#for j in range(len(BPB1400fList)):
		#	BPB1400FS.append(BPB1400fList[j].Get(kinVar[i]))

		#[0] index is your regular full selection
		#BPB1400trigup = BPB1400fList[0].Get("Mtwtrigup")
		#BPB1400trigdown = BPB1400fList[0].Get("Mtwtrigdown")
		#BPB1400Wup = BPB1400fList[0].Get("MtwWup")
		#BPB1400Tdown = BPB1400fList[0].Get("MtwTdown")
		#BPB1400FS.append(BPB1400Wup)
		#BPB1400FS.append(BPB1400Tdown)
		#BPB1400FS.append(BPB1400trigup)
		#BPB1400FS.append(BPB1400trigdown)

		#BPB1600FS = []
		#for j in range(len(BPB1600fList)):
		#	BPB1600FS.append(BPB1600fList[j].Get(kinVar[i]))

		#[0] index is your regular full selection
		#BPB1600trigup = BPB1600fList[0].Get("Mtwtrigup")
		#BPB1600trigdown = BPB1600fList[0].Get("Mtwtrigdown")
		#BPB1600Wup = BPB1600fList[0].Get("MtwWup")
		#BPB1600Tdown = BPB1600fList[0].Get("MtwTdown")
		#BPB1600FS.append(BPB1600Wup)
		#BPB1600FS.append(BPB1600Tdown)
		#BPB1600FS.append(BPB1600trigup)
		#BPB1600FS.append(BPB1600trigdown)

		#BPB1800FS = []
		#for j in range(len(BPB1800fList)):
	#		BPB1800FS.append(BPB1800fList[j].Get(kinVar[i]))

		#[0] index is your regular full selection
		#BPB1800trigup = BPB1800fList[0].Get("Mtwtrigup")
		#BPB1800trigdown = BPB1800fList[0].Get("Mtwtrigdown")
		#BPB1800Wup = BPB1800fList[0].Get("MtwWup")
		#BPB1800Tdown = BPB1800fList[0].Get("MtwTdown")
		#BPB1800FS.append(BPB1800Wup)
		#BPB1800FS.append(BPB1800Tdown)
		#BPB1800FS.append(BPB1800trigup)
		#BPB1800FS.append(BPB1800trigdown)

		#[0] index is your regular full selection
		#BPT1200trigup = BPT1200fList[0].Get("Mtwtrigup")
		#BPT1200trigdown = BPT1200fList[0].Get("Mtwtrigdown")
		#BPT1200Wup = BPT1200fList[0].Get("MtwWup")
		#BPT1200Tdown = BPT1200fList[0].Get("MtwTdown")
		#BPT1200FS.append(BPT1200Wup)
		#BPT1200FS.append(BPT1200Tdown)
		#BPT1200FS.append(BPT1200trigup)
		#BPT1200FS.append(BPT1200trigdown)

	

		#[0] index is your regular full selection
		#BPT1400trigup = BPT1400fList[0].Get("Mtwtrigup")
		#BPT1400trigdown = BPT1400fList[0].Get("Mtwtrigdown")
		#BPT1400Wup = BPT1400fList[0].Get("MtwWup")
		#BPT1400Tdown = BPT1400fList[0].Get("MtwTdown")
		#BPT1400FS.append(BPT1400Wup)
		#BPT1400FS.append(BPT1400Tdown)
		#BPT1400FS.append(BPT1400trigup)
		#BPT1400FS.append(BPT1400trigdown)



		#[0] index is your regular full selection
		#BPT1600trigup = BPT1600fList[0].Get("Mtwtrigup")
		#BPT1600trigdown = BPT1600fList[0].Get("Mtwtrigdown")
		#BPT1600Wup = BPT1600fList[0].Get("MtwWup")
		#BPT1600Tdown = BPT1600fList[0].Get("MtwTdown")
		#BPT1600FS.append(BPT1600Wup)
		#BPT1600FS.append(BPT1600Tdown)
		#BPT1600FS.append(BPT1600trigup)
		#BPT1600FS.append(BPT1600trigdown)



		#[0] index is your regular full selection
		#BPT1800trigup = BPT1800fList[0].Get("Mtwtrigup")
		#BPT1800trigdown = BPT1800fList[0].Get("Mtwtrigdown")
		#BPT1800Wup = BPT1800fList[0].Get("MtwWup")
		#BPT1800Tdown = BPT1800fList[0].Get("MtwTdown")
		#BPT1800FS.append(BPT1800Wup)
		#BPT1800FS.append(BPT1800Tdown)
		#BPT1800FS.append(BPT1800trigup)
		#BPT1800FS.append(BPT1800trigdown)


	c1 = TCanvas(kinVar[i], 'Data Full selection vs b pt tagging background', 700, 700)

	if options.blinded == 'on':
		main = ROOT.TPad("main", "main", 0, 0, 1, 1)
		sub = ROOT.TPad("sub", "sub", 0, 0, 0, 0)
		main.SetBottomMargin(0.15)	
	else:	
		main = ROOT.TPad("main", "main", 0, 0.3, 1, 1)
		sub = ROOT.TPad("sub", "sub", 0, 0, 1, 0.3)
		main.SetBottomMargin(0.0)


	main.SetLeftMargin(0.16)
	main.SetRightMargin(0.05)
	main.SetTopMargin(0.1)

	sub.SetLeftMargin(0.16)
	sub.SetRightMargin(0.05)
	sub.SetTopMargin(0)
	sub.SetBottomMargin(0.3)

	main.Draw()
	sub.Draw()

	main.cd()



	#Selections in order (Selection, PUup, PUdown, JESup, JESdown, JERup, JERdown, JMSup, JMSdown, JMRup, JMRdown, PDFup, PDFdown, ScaleUp, ScaleDown, trigup, trig down)
	TTmcFS = []
	for j in range(len(TTmcfList)):
		TTmcFS.append(TTmcfList[j].Get(kinVar[i]))

	if options.var == 'analyzer':
		TTmctrigup = TTmcfList[0].Get("Mtwtrigup")
		TTmctrigdown = TTmcfList[0].Get("Mtwtrigdown")
		# TTmcTup = TTmcfList[0].Get("MtwTup")
		# TTmcTdown = TTmcfList[0].Get("MtwTdown")
		# TTmcFS.append(TTmcTup)
		# TTmcFS.append(TTmcTdown)
		TTmcFS.append(TTmctrigup)
		TTmcFS.append(TTmctrigdown)

		#To be consistent with the SRs, switch the 13th and 14th entries with the 15th and 16th entries
		#This puts scaleup and down at the end of the list

		if options.cuts == 'default':
			TTmcFS[13], TTmcFS[15] = TTmcFS[15], TTmcFS[13]
			TTmcFS[14], TTmcFS[16] = TTmcFS[16], TTmcFS[14]

	TTmcBE = TTmcfList[0].Get("QCDbkg" + kinBkg[i])

	TTmcBE2d = TTmcfList[0].Get("QCDbkg" + kinBkg[i]+"2D")


	TTmcBEh = TTmcfList[0].Get("QCDbkg" + kinBkg[i]+"h")
	TTmcBEl = TTmcfList[0].Get("QCDbkg" + kinBkg[i]+"l")

	DataBEh = Data.Get("QCDbkg"+kinBkg[i]+"h")
	DataBEl = Data.Get("QCDbkg"+kinBkg[i]+"l")


	DataBE = DataBE.Rebin(rebin[i])
	DataFS = DataFS.Rebin(rebin[i])
	TTmcBE = TTmcBE.Rebin(rebin[i])
	TTmcBE2d = TTmcBE2d.Rebin(rebin[i])
	print "DataFS.Integral() = " + str(DataFS.Integral())
	DataBEl = DataBEl.Rebin(rebin[i])
	DataBEh = DataBEh.Rebin(rebin[i])

	setList = [SR1200FS, SR2000FS, SR2800FS,  TTmcFS]#, BPT1200FS, BPT1400FS, BPT1600FS, BPT1800FS]# BPB1200FS, BPB1400FS, BPB1600FS, BPB1800FS,


	x =1
	for selection in setList:
		# print '\n'
		# print x,' : ',
		y=1
		x+=1
		for item in selection:
			item.Rebin(rebin[i])
			# print y,
			y+=1

	DataBEMmup = DataBEMmup.Rebin(rebin[i])
	DataBEMmdown = DataBEMmdown.Rebin(rebin[i])
	DataBE2d = DataBE2d.Rebin(rebin[i])
	DataBE2ddown = DataBE2ddown.Rebin(rebin[i])
	DataBE2dup = DataBE2dup.Rebin(rebin[i])


#subtract weighted TT pretags

	if options.set == 'data':
		DataBE.Add(TTmcBE,-1)
		DataBE2d.Add(TTmcBE2d,-1)
		DataBEl.Add(TTmcBE,-1)
		DataBEh.Add(TTmcBE,-1)
		DataBEMmup.Add(TTmcBE,-1)
		DataBEMmdown.Add(TTmcBE,-1)
		DataBE2dup.Add(TTmcBE2d,-1)
		DataBE2ddown.Add(TTmcBE2d,-1)
		
	print "begin singletop"
	main.cd()


	stop = ['singletop_tW','singletop_tWB','singletop_t','singletop_tB']
	sfiles = []
	shists = []
	ssubs = []
	ssubsh = []
	ssubsl =[]
	ssubs2d = []

	singletop = ROOT.TH1F("singletop",     "singletop",     	  	      kinBin[i], kinLow[i], kinHigh[i] )
	singletop = singletop.Rebin(rebin[i])
	singletop.SetFillColor(6)
	schanst = ROOT.TH1F("schanst",     "schanst",     	  	       kinBin[i], kinLow[i], kinHigh[i] )
	schanst = schanst.Rebin(rebin[i])


	for ifile in range(0,len(stop)):
		sfiles.append(ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzerweighted"+stop[ifile]+"_Trigger_nominal_"+pustr+mmstr+"_PSET_"+options.cuts+kin+".root"))
		shists.append(sfiles[ifile].Get(kinVar[i]))
		ssubs.append(sfiles[ifile].Get("QCDbkg"+kinBkg[i]))
		ssubsh.append(sfiles[ifile].Get("QCDbkg"+kinBkg[i]+"h"))
		ssubsl.append(sfiles[ifile].Get("QCDbkg"+kinBkg[i]+"l"))
		ssubs2d.append(sfiles[ifile].Get("QCDbkg"+kinBkg[i]+"2D"))
		shists[ifile] = shists[ifile].Rebin(rebin[i])
		ssubs[ifile] = ssubs[ifile].Rebin(rebin[i])
		ssubsh[ifile] = ssubsh[ifile].Rebin(rebin[i])
		ssubsl[ifile] = ssubsl[ifile].Rebin(rebin[i])
		ssubs2d[ifile] = ssubs2d[ifile].Rebin(rebin[i])

		print stop[ifile]

		if options.set == 'data':
			DataBE.Add(ssubs[ifile],-1)
			DataBEl.Add(ssubsl[ifile],-1)
			DataBEh.Add(ssubsh[ifile],-1)  
			DataBE2d.Add(ssubs2d[ifile],-1)
			DataBEMmup.Add(ssubs[ifile],-1)
			DataBEMmdown.Add(ssubs[ifile],-1)
		
		singletop.Add(shists[ifile])
		if ifile<=1:
			schanst.Add(shists[ifile])

	st1.Add(singletop)

	if options.set == "QCD":	
		DataFS.Add(TTmcFS[0])
		DataFS.Add(singletop)
#output.cd()

	fittitles = ["pol0","pol2","pol3","FIT","Bifpoly","expofit"]
	QCDbkg_ARR = []
	for ihist in range(0,len(fittitles)):
		print "Appending to QCDbkg_ARR - " + "QCDbkg"+kinBkg[i]+str(fittitles[ihist])
		QCDbkg_ARR.append(Data.Get("QCDbkg"+kinBkg[i]+str(fittitles[ihist])))
		QCDbkg_ARR[ihist] = QCDbkg_ARR[ihist].Rebin(rebin[i])

	BEfiterrh = kinFit_Uncertainty(QCDbkg_ARR, kinBkg[i])


	DataQCDBEH=DataBE.Clone("DataQCDBEH")
	DataQCDBEL=DataBE.Clone("DataQCDBEL")
	DataTOTALBEH=DataBE.Clone("DataTOTALBEH")
	DataTOTALBEL=DataBE.Clone("DataTOTALBEL")

	for ibin in range(1,DataBE.GetNbinsX()+1):

		TTstat=TTmcFS[0].GetBinError(ibin)
		if DataBE.GetBinContent(ibin)>0:
			QCDstat=DataBE.GetBinError(ibin)
		else:
			QCDstat=0.
		QCDfit=abs(BEfiterrh.GetBinContent(ibin))
		QCDfit1=abs((DataBEh.GetBinContent(ibin)-DataBEl.GetBinContent(ibin))/2)
		#QCDfit2=abs(DataBE2d.GetBinContent(ibin)-DataBE.GetBinContent(ibin))
#	QCDfit3=abs(extrasig.GetBinContent(ibin))
		QCDMm=abs((DataBEMmup.GetBinContent(ibin)-DataBEMmdown.GetBinContent(ibin))/2)


		QCDsys=sqrt(QCDMm*QCDMm+ QCDfit*QCDfit+ QCDfit1*QCDfit1) #+QCDfit2*QCDfit2)
		QCDerror= sqrt(QCDstat*QCDstat+QCDsys*QCDsys)
		TTerrorup=sqrt(TTstat*TTstat)
		TTerrordown=sqrt(TTstat*TTstat)
		Totalerrorup=sqrt(QCDerror*QCDerror+TTerrorup*TTerrorup)
		Totalerrordown=sqrt(QCDerror*QCDerror+TTerrordown*TTerrordown)
		DataQCDBEH.SetBinContent(ibin,DataQCDBEH.GetBinContent(ibin)+QCDerror)
		DataQCDBEL.SetBinContent(ibin,DataQCDBEL.GetBinContent(ibin)-QCDerror)
		DataTOTALBEH.SetBinContent(ibin,DataTOTALBEH.GetBinContent(ibin)+Totalerrorup)
		DataTOTALBEL.SetBinContent(ibin,DataTOTALBEL.GetBinContent(ibin)-Totalerrordown)
	print "QCDMm: " + str(QCDMm)
	print "QCDfit: " + str(QCDfit)
	print "QCDfit1: " + str(QCDfit1)
	#print "QCDfit2: " + str(QCDfit2)
	print "QCDerror: " + str(QCDerror)
	
	print "DataQCDBEH: " + str(DataQCDBEH.Integral())
	print "DataBE: " + str(DataBE.Integral())

	print "QCD total error"
	print (DataQCDBEH.Integral()-DataBE.Integral())/DataBE.Integral()
	print 


	DataTOTALBEL.Add(TTmcFS[0])
	DataTOTALBEH.Add(TTmcFS[0])
	DataTOTALBEL.Add(singletop)
	DataTOTALBEH.Add(singletop)

	#for ifile in range(0,len(stop)):
	#	DataTOTALBEL.Add(shists[ifile])
	#	DataTOTALBEH.Add(shists[ifile])		

# -------- Systematic uncertainties ----------------------------------------------

	#setList is a list of SR1200/2800/2000, TTmc
	#each of those is a list with the necessary histos
	#(Selection, PUup, PUdown, JESup, JESdown, JERup, JERdown, JMSup, JMSdown, JMRup, JMRdown, trig up, trig down, Wup, Wdown/ScaleUp, ScaleDown )
	#ScaleUp and ScaleDown are ttbar only
	
	# Indexes of relevant histos in *FS
	if options.cuts == 'default' and options.var == 'analyzer':
		myIndexes = {'Pileup':[0,1,2],'JES':[0,3,4],'JER':[0,5,6], 'JMS':[0,7,8], 'JMR':[0,9,10], 'PDF':[0,11,12], 'Trig':[0,13,14], 'WSF':[0,15,16], 'Scale':[0,15,16], 'Extrap':[0,17,18]}
		# orderedKeys = ['Pileup','JES','JER','JMS','JMR','PDF','Trig','WSF','Scale']
		strSetList = ['SR1200', 'SR2000', 'SR2800',  'TTmc']#, 'BPT1200', 'BPT1400', 'BPT1600', 'BPT1800','BPB1200', 'BPB1400', 'BPB1600', 'BPB1800', 'BPT1200', 'BPT1400', 'BPT1600', 'BPT1800']
		for selection in setList:
			if selection == TTmcFS:
				orderedKeys = ['Pileup','JES','JER','JMS','JMR','PDF','Trig','Scale']
			else:
				orderedKeys = ['Pileup','JES','JER','JMS','JMR','PDF','Trig','WSF','Extrap']
			indexRange = len(orderedKeys)

			for x in range(indexRange):
				sSet =  strSetList[setList.index(selection)]
				sUncertainty = orderedKeys[x]
				print sUncertainty
				c0 = TCanvas(sSet+sUncertainty, sSet+sUncertainty, 700, 700)
				pad = ROOT.TPad(sSet, sSet, 0,0,1,1)
				pad.SetLeftMargin(0.16)
				pad.SetRightMargin(0.05)
				pad.SetTopMargin(0.1)
				pad.SetBottomMargin(0.15)
				pad.Draw()
				pad.cd()

				leg0 = TLegend(0.7, 0.6, 0.93, 0.9)
				leg0.SetNColumns(1)
				leg0.SetFillColor(0)
				leg0.SetBorderSize(0)

				normal = selection[myIndexes[sUncertainty][0]]
				up = selection[myIndexes[sUncertainty][1]]
				down = selection[myIndexes[sUncertainty][2]]

				normal.SetLineColor(kRed)
				normal.SetLineWidth(2)
				normal.SetTitle(sSet+' - ' + sUncertainty)
				normal.GetXaxis().SetTitle('M_{tW} (GeV)')
				normal.GetYaxis().SetTitle('Counts')
				normal.GetXaxis().SetNdivisions(50504)
				up.SetLineColor(kBlue)
				up.SetLineWidth(2)
				down.SetLineColor(kGreen+1)
				down.SetLineWidth(2)
				up.SetLineStyle(2)
				down.SetLineStyle(2)

				normal.SetStats(0)
				up.SetStats(0)
				down.SetStats(0)

				leg0.AddEntry( normal, "nominal", 'L')
				leg0.AddEntry( up, "up", 'L')
				leg0.AddEntry( down, "down", 'L')


				histList = [normal, up, down]

				yMax = histList[0].GetMaximum()
				maxHist = histList[0]
				for h in range(1,len(histList)):
					if histList[h].GetMaximum() > yMax:
						yMax = histList[h].GetMaximum()
						maxHist = histList[h]
				for h in histList:
					h.SetMaximum(yMax*1.1)

				normal.Draw("samehist")
				up.Draw("samehist")
				down.Draw("samehist")

				c0.Print('plots/Uncertainty'+sSet+sUncertainty+Lumi+'.root')
				c0.Print('plots/Uncertainty'+sSet+sUncertainty+Lumi+'.png')
				c0.Print('plots/Uncertainty'+sSet+sUncertainty+Lumi+'.pdf')
			
		legUncert = TCanvas("Uncertainty legend", "Uncertainty legend")
		leg0.Draw()
		legUncert.Print("uncertLeg.pdf",'pdf')


		c2 = TCanvas("QCD tagrate uncertainty", "QCD tagrate uncertainty", 700, 700)
		QCDtagrate = ROOT.TPad("QCDtagrate", "QDCtagrate", 0, 0, 1, 1)
		QCDtagrate.SetLeftMargin(0.16)
		QCDtagrate.SetRightMargin(0.05)
		QCDtagrate.SetTopMargin(0.1)
		QCDtagrate.SetBottomMargin(0.15)
		QCDtagrate.Draw()
		QCDtagrate.cd()
	
		DataBE.SetLineColor(kRed)
		DataBEl.SetLineColor(kGreen+1)
		DataBEh.SetLineColor(kBlue)
		DataBEl.SetLineStyle(2)
		DataBEh.SetLineStyle(2)
		DataBE.SetLineWidth(2)
		DataBEl.SetLineWidth(2)
		DataBEh.SetLineWidth(2)

		DataBE.SetStats(0)
		DataBEl.SetStats(0)
		DataBEh.SetStats(0)

		c2Max = DataBEh.GetMaximum()
		DataBE.SetMaximum(c2Max*1.1)
		DataBEh.SetMaximum(c2Max*1.1)
		DataBEl.SetMaximum(c2Max*1.1)

		DataBE.SetTitle("QCD - Fit uncertainty")
		DataBE.GetXaxis().SetTitle('M_{tW} (GeV)')
		DataBE.GetYaxis().SetTitle('Counts')
		DataBE.GetXaxis().SetNdivisions(50504)

		DataBE.Draw("samehist")
		DataBEl.Draw("samehist")
		DataBEh.Draw("samehist")

		c2.Print('plots/UncertaintyQCDtagrate.root')
		c2.Print('plots/UncertaintyQCDtagrate.png')
		c2.Print('plots/UncertaintyQCDtagrate.pdf')



		c3 = TCanvas("QCD 2D uncertainty", "QCD uncertainty", 700, 700)
		QCD2D = ROOT.TPad("QCD2D", "QDC2D", 0, 0, 1, 1)
		QCD2D.SetLeftMargin(0.16)
		QCD2D.SetRightMargin(0.05)
		QCD2D.SetTopMargin(0.1)
		QCD2D.SetBottomMargin(0.15)
		QCD2D.Draw()
		QCD2D.cd()
	
		DataBE2d.SetLineColor(kRed)
		DataBE2ddown.SetLineColor(kGreen+1)
		DataBE2dup.SetLineColor(kBlue)
		DataBE2ddown.SetLineStyle(2)
		DataBE2dup.SetLineStyle(2)
		DataBE2d.SetLineWidth(2)
		DataBE2dup.SetLineWidth(2)
		DataBE2ddown.SetLineWidth(2)

		DataBE2d.SetStats(0)
		DataBE2ddown.SetStats(0)
		DataBE2dup.SetStats(0)

		c3Max = DataBE2dup.GetMaximum()
		DataBE2d.SetMaximum(c3Max*1.1)
		DataBE2dup.SetMaximum(c3Max*1.1)
		DataBE2ddown.SetMaximum(c3Max*1.1)

		DataBE2d.SetTitle("QCD - Parameterization")
		DataBE2d.GetXaxis().SetTitle('M_{tW} (GeV)')
		DataBE2d.GetYaxis().SetTitle('Counts')
		DataBE2d.GetXaxis().SetNdivisions(50504)

		DataBE2d.Draw("samehist")
		DataBE2ddown.Draw("samehist")
		DataBE2dup.Draw("samehist")

		c3.Print('plots/UncertaintyQCD2D.root')
		c3.Print('plots/UncertaintyQCD2D.png')
		c3.Print('plots/UncertaintyQCD2D.pdf')

		QCDup = DataBE.Clone()
		QCDdown = DataBE.Clone()
		for ibin in range(1,DataBE.GetNbinsX()+1):
			QCDfiterr=abs(BEfiterrh.GetBinContent(ibin))
			QCDnominal=abs(DataBE.GetBinContent(ibin))
			QCDup.SetBinContent(ibin,(QCDnominal + QCDfiterr))
			QCDdown.SetBinContent(ibin,(QCDnominal - QCDfiterr))
		
		
	

		c4 = TCanvas("QCD fit uncertainty", "QCD uncertainty", 700, 700)
		QCDfit = ROOT.TPad("QCDfit", "QDCfit", 0, 0, 1, 1)
		QCDfit.SetLeftMargin(0.16)
		QCDfit.SetRightMargin(0.05)
		QCDfit.SetTopMargin(0.1)
		QCDfit.SetBottomMargin(0.15)
		QCDfit.Draw()
		QCDfit.cd()
	
		DataBE.SetLineColor(kRed)
		QCDdown.SetLineColor(kGreen+1)
		QCDup.SetLineColor(kBlue)
		QCDdown.SetLineStyle(2)
		QCDup.SetLineStyle(2)
		QCDup.SetLineWidth(2)
		QCDdown.SetLineWidth(2)

		QCDup.SetStats(0)
		QCDdown.SetStats(0)

		c4Max = QCDup.GetMaximum()
		DataBE.SetMaximum(c4Max*1.1)
		QCDdown.SetMaximum(c4Max*1.1)
		QCDup.SetMaximum(c4Max*1.1)

		DataBE.SetTitle("QCD - Alternative fits")
		# DataBE.GetXaxis().SetTitle('M_{tW} (GeV)')
		# DataBE.GetYaxis().SetTitle('Counts')
		# DataBE.GetXaxis().SetNdivisions(50504)

		DataBE.Draw("samehist")
		QCDdown.Draw("samehist")
		QCDup.Draw("samehist")

		c4.Print('plots/UncertaintyQCDfit.root')
		c4.Print('plots/UncertaintyQCDfit.png')
		c4.Print('plots/UncertaintyQCDfit.pdf')


		c5 = TCanvas("QCD mod mass uncertainty", "QCD mod mass uncertainty", 700, 700)
		QCDModMass = ROOT.TPad("QCDMm", "QCDMm", 0, 0, 1, 1)
		QCDModMass.SetLeftMargin(0.16)
		QCDModMass.SetRightMargin(0.05)
		QCDModMass.SetTopMargin(0.1)
		QCDModMass.SetBottomMargin(0.15)
		QCDModMass.Draw()
		QCDModMass.cd()
	
		DataBE.SetLineColor(kRed)
		DataBEMmdown.SetLineColor(kGreen+1)
		DataBEMmup.SetLineColor(kBlue)
		DataBEMmdown.SetLineStyle(2)
		DataBEMmup.SetLineStyle(2)
		DataBEMmup.SetLineWidth(2)
		DataBEMmdown.SetLineWidth(2)

		DataBEMmup.SetStats(0)
		DataBEMmdown.SetStats(0)

		c5Max =DataBEMmup.GetMaximum()
		DataBE.SetMaximum(c5Max*1.1)
		DataBEMmdown.SetMaximum(c5Max*1.1)
		DataBEMmup.SetMaximum(c5Max*1.1)

		DataBE.SetTitle('QCD - Top mass shape correction')

		DataBE.Draw("samehist")
		DataBEMmdown.Draw("samehist")
		DataBEMmup.Draw("samehist")

		c5.Print('plots/UncertaintyQCDModMass.root')
		c5.Print('plots/UncertaintyQCDModMass.png')
		c5.Print('plots/UncertaintyQCDModMass.pdf')






#---------------------- Resume -----------------------------------------------------

	# How the error bars get plotted:
	# The st1 stack gets drawn first and then the sigst stack gets drawn on top
	# The sigst stack is the ttbar mc, the low QCD background estimate, and sigma (the error bars)
	# which is derived by taking the difference between the high and low estiamates.
	# In the generic applicaltion, this plotting method works because the ttbar mc looks
	# identical at the bottom of both the st1 and sigst stacks.

	# However, when ttbar is moved up a spot in the stacks, there's an issue because the 
	# QCD estimates in the two different stacks are different. Thus, when plotting the Mt
	# variable (whcih needs ttbar on top of the stack), the histograms added to the sigst
	# stack need to be transparent. This maintains the position of the error bars while
	# allowing the reader to see the nominal stack from st1.

	main.cd()

	DataBE.SetFillColor(kYellow)
	DataBE.SetLineColor(kBlack)
	DataBE.SetLineWidth(1)
	TTmcFS[0].SetFillColor(kRed)
	TTmcFS[0].SetLineColor(kBlack)
	TTmcFS[0].SetLineWidth(1)
	SR1200FS[0].SetLineColor(kBlue)
	SR1200FS[0].SetLineWidth(2)
	SR2800FS[0].SetLineColor(kBlue-1)
	SR2800FS[0].SetLineWidth(2)
	SR2000FS[0].SetLineColor(kBlue-2)
	SR2000FS[0].SetLineWidth(2)


	DataTOTALBEH.SetLineColor(kBlue)
	DataTOTALBEH.SetLineWidth(2)

	centerqcd = DataTOTALBEL.Clone("centerqcd")
	centerqcd.SetFillColor(kYellow)
	centerqcd.Add(TTmcFS[0],-1)
	centerqcd.Add(singletop,-1)

	DataTOTALBEL.SetLineColor(kBlue)
	DataTOTALBEL.SetLineWidth(2)

	sigst= ROOT.THStack("sigst", "sigst")
	sigma = DataTOTALBEH.Clone("sigma")
	sigma.SetFillStyle(3245)
	sigma.SetFillColor(1)
	sigma.SetLineColor(0)
	centerqcd.SetLineColor(kYellow)

	sigma.Add(DataTOTALBEL,-1)
	sigst.Add(singletop)


	# ONLY WORKS WHEN RUN LOCALLY - I HAVE NO IDEA WHY
	if kinVar[i] == 'Mt':
		testHist = DataBE.Clone('testHist')
		testHist.Add(TTmcFS[0])
		testHist.Add(singletop)
		for b in range(1,testHist.GetNbinsX()+1):
			thisBinError = sigma.GetBinContent(b)/2
			testHist.SetBinError(b, thisBinError)

		myGraph = TGraphErrors(testHist)
		print "bin width: " + str(testHist.GetBinWidth(1))
		myGraph.SetFillStyle(3004)
		myGraph.SetFillColor(1)


		st1.Add(DataBE)
		st1.Add(TTmcFS[0])
	else:
		st1.Add(TTmcFS[0])
		st1.Add(DataBE)

	sigst.Add(TTmcFS[0])
	
	sigst.Add(centerqcd)
	sigst.Add(sigma)


	
	
	#st1.Add(SR1200FS[0])
	print "TT: " + str(TTmcFS[0].Integral())
	print "Data: " + str(DataFS.Integral())
	print "QCD: " + str(DataBE.Integral())
	print "ST: " + str(singletop.Integral())



	bkgline=st1.GetStack().Last().Clone("bkgline")
	bkgline.SetFillColor(0)
	bkgline.SetFillStyle(0)

	if options.blinded == 'off':
		if options.set == 'data':
			leg.AddEntry( DataFS, 'Data', 'P')
		elif options.set == 'QCD':
			leg.AddEntry( DataFS, 'QCD MC', 'P')

	leg.AddEntry( DataBE, 'QCD background prediction', 'F')	
	leg.AddEntry( TTmcFS[0], 't#bar{t} MC prediction', 'F')
	leg.AddEntry( singletop, 'Single top quark MC prediction', 'F')
	leg.AddEntry( sigma, '1 #sigma background uncertainty', 'F')

#------------------Plot to show this is a 'bump hunt'---------------------------------------------------------
	# if i==0 :
	# 	cBump = TCanvas('Bump','Bump')
	# 	pBump = ROOT.TPad("Bump", "Bump", 0, 0, 1, 1)
	# 	pBump.SetLeftMargin(0.1)
	# 	pBump.SetRightMargin(0.1)
	# 	pBump.SetTopMargin(0.1)
	# 	pBump.SetBottomMargin(0.15)
	# 	pBump.Draw()
	# 	pBump.cd()

	# 	lBump = TLegend(0.6, 0.5, 0.95, 0.95)
	# 	lBump.AddEntry( DataBE, 'QCD background prediction', 'F')	
	# 	lBump.AddEntry( TTmcFS[0], 't#bar{t} MC prediction', 'F')
	# 	lBump.AddEntry( singletop, 'Single top quark MC prediction', 'F')
	# 	lBump.AddEntry( sigma, '1 #sigma background uncertainty', 'F')
	# 	lBump.AddEntry( SR1200FS[0], 'b*_{R} at 1200 GeV', 'L' )

	# 	sBump = st1.Clone()
	# 	sBump.Add(SR1200FS[0])

	# 	sBump.Draw("hist")
	# 	sBump.GetXaxis().SetTitle("M_{tW} GeV")
	# 	sBump.GetYaxis().SetTitle("Counts")
	# 	sBump.GetYaxis().SetTitleOffset(0.9)
	# 	lBump.Draw()


	# #pBump.SetLogy()

	# 	cBump.Print('BumpHunt.pdf','pdf')

	

#---------------------------------------------Resume----------------------------------------------------------
	main.cd()
	if options.bprime:
		leg.AddEntry( BPB1200FS[0], "b'_{R} w/ b at 1200 GeV", 'L')
		#leg.AddEntry( BPB1400FS[0], "b'_{R} w/ b at 1400 GeV", 'L')
		#leg.AddEntry( BPB1600FS[0], "b'_{R} w/ b at 1600 GeV", 'L')
		#leg.AddEntry( BPB1800FS[0], "b'_{R} w/ b at 1800 GeV", 'L')
		#leg.AddEntry( BPT1200FS[0], "b'_{R} w/ t at 1200 GeV", 'L')
		#leg.AddEntry( BPT1400FS[0], "b'_{R} w/ t at 1400 GeV", 'L')
		#leg.AddEntry( BPT1600FS[0], "b'_{R} w/ t at 1600 GeV", 'L')
		#leg.AddEntry( BPT1800FS[0], "b'_{R} w/ t at 1800 GeV", 'L')
	else:
		leg.AddEntry( SR1200FS[0], 'b*_{R} at 1200 GeV', 'L')
		leg.AddEntry( SR2000FS[0], 'b*_{R} at 2000 GeV', 'L')
		leg.AddEntry( SR2800FS[0], 'b*_{R} at 2800 GeV', 'L')



	st1.SetMaximum(DataTOTALBEH.GetMaximum() * 1.3)
	st1.SetMinimum(0.1)
	st1.SetTitle(st1_label[i])
	if kinVar[i] == 'Mtw':
		if options.set == 'data' and options.cuts == 'default':
			st1.SetTitle('Data - Full Selection'+st1_label[i])
		elif options.set == 'QCD' and options.cuts == 'default':
			st1.SetTitle('QCD MC - Full Selection'+st1_label[i])
		elif options.set == 'data' and options.cuts == 'sideband':
			st1.SetTitle('Data - Sideband Selection'+st1_label[i])
	st1.Draw("hist")
	gPad.SetLeftMargin(.16)
	st1.GetYaxis().SetTitleOffset(1)

	if kinVar[i] == 'Mt':
		#testHist.Draw("same e2")
		myGraph.Draw("Z2")
	else:
		sigst.Draw("samehist")
	bkgline.Draw("samehist")


	DataFS1	    = TH1D("DataFS1",     str(kinVar[i])+" in b+1",	kinBin[i], kinLow[i], kinHigh[i] )
	DataFS1 = DataFS1.Rebin(rebin[i])
	for ibin in range(1,DataFS.GetNbinsX()+1):
		DataFS1.SetBinContent(ibin,DataFS.GetBinContent(ibin))

	DataFS1.SetBinErrorOption(DataFS1.kPoisson)
	
	DataFS1.SetMarkerStyle(20)

	#Take out when using data
	totalH = st1.GetStack().Last().Clone("totalH")
	if options.set == "QCD":	
		DataFS1=DataFS
		DataFS1.SetMarkerStyle(kFullSquare)
		DataFS1.SetMarkerColor(9)

	if options.blinded == 'off':
		DataFS1.Draw("samepEX0")
	if options.bprime:
		BPB1200FS[0].Draw("samehist")
		#BPB1400FS[0].Draw("samehist")
		#BPB1600FS[0].Draw("samehist")
		#BPB1800FS[0].Draw("samehist")
	#	BPT1200FS[0].Draw("samehist")
	#	BPT1400FS[0].Draw("samehist")
	#	BPT1600FS[0].Draw("samehist")
	#	BPT1800FS[0].Draw("samehist")
	else:
		SR1200FS[0].Draw("samehist")
		SR2800FS[0].Draw("samehist")
		SR2000FS[0].Draw("samehist")

	prelim = TLatex()
	prelim.SetNDC()
	#4 is 5.0fb-1, 5 is 1.0fb-1, 6 is 10.0fb-1
	# if lumi == 1000:
	# 	insertlogo( main, 5, 11 )
	# elif lumi == 5000:
	# 	insertlogo( main, 4, 11)
	# elif lumi == 10000:
	# 	insertlogo( main, 6, 11)
	# elif lumi == 1221.951:
	# 	insertlogo( main, 8, 11)

	if i == 0:
		leg.Draw()
	else:
		kinLeg = TCanvas("Kinematics legend","Kinematics legend")
		leg.Draw()
		kinLeg.Print('kinleg.pdf','pdf')

	sub.cd()
	gPad.SetLeftMargin(.16)

	if options.blinded == 'off':
		pull = Make_Pull_plot( DataFS1,totalH,DataTOTALBEH,DataTOTALBEL )
		print "Integral totalH: " + str(totalH.Integral())
		print "Integral DataTOTALBEH: " + str(DataTOTALBEH.Integral())
		print "Integral DataTOTALBEL: " + str(DataTOTALBEL.Integral())


	
		#pull.GetXaxis().SetRangeUser(0,3000)
		pull.SetFillColor(kBlue)
		pull.SetTitle(pull_label[i])
		pull.SetStats(0)


		pull.GetYaxis().SetRangeUser(-2.9,2.9)
		pull.GetXaxis().SetLabelSize(0.05)
		pull.GetYaxis().SetLabelSize(0.13)


		LS = .13

		pull.GetYaxis().SetTitleOffset(0.4)
		pull.GetXaxis().SetTitleOffset(0.9)
		pull.SetStats(0)
	    
	    
		pull.GetYaxis().SetLabelSize(LS)
		pull.GetYaxis().SetTitleSize(LS)
		pull.GetYaxis().SetNdivisions(306)
		pull.GetXaxis().SetLabelSize(LS)
		pull.GetXaxis().SetTitleSize(LS)

		pull.Draw("hist")

	line2=ROOT.TLine(500.0,0.0,4000.0,0.0)
	line2.SetLineColor(0)
	line1=ROOT.TLine(500.0,0.0,4000.0,0.0)
	line1.SetLineStyle(2)

	line2.Draw()
	line1.Draw()
	gPad.Update()

	main.RedrawAxis()
	
	analysis = ''
	if options.bprime:
		analysis = '_bprime'
	if options.mcsf != '':
		mcscale = '_mcscale_'+options.mcsf
	else:
		mcscale = ''

	c1.Print('plots/' + kinVar[i] + 'vsBkg_BifPoly_fit_'  +Lumi+'_'+pustr+'_PSET_'+options.set+'_'+options.cuts+analysis+mcscale+sBlind+ptString+'.root', 'root')
	c1.Print('plots/' + kinVar[i] + 'vsBkg_BifPoly_fit_'  +Lumi+'_'+pustr+'_PSET_'+options.set+'_'+options.cuts+analysis+mcscale+sBlind+ptString+'.pdf', 'pdf')
	c1.Print('plots/' + kinVar[i] + 'vsBkg_BifPoly_fit_'  +Lumi+'_'+pustr+'_PSET_'+options.set+'_'+options.cuts+analysis+mcscale+sBlind+ptString+'.png', 'png')
	main.SetLogy()
	st1.SetMaximum( DataBEh.GetMaximum() * 5000 )
	st1.SetMinimum( 0.1)
	main.RedrawAxis()

	c1.Print('plots/' + kinVar[i] + 'vsBkgsemilog_BifPoly_fit_'  +Lumi+'_'+pustr+'_PSET_'+options.set+'_'+options.cuts+analysis+mcscale+sBlind+ptString+'.root', 'root')
	c1.Print('plots/' + kinVar[i] + 'vsBkgsemilog_BifPoly_fit_'  +Lumi+'_'+pustr+'_PSET_'+options.set+'_'+options.cuts+analysis+mcscale+sBlind+ptString+'.pdf', 'pdf')
	c1.Print('plots/' + kinVar[i] + 'vsBkgsemilog_BifPoly_fit_'  +Lumi+'_'+pustr+'_PSET_'+options.set+'_'+options.cuts+analysis+mcscale+sBlind+ptString+'.png', 'png')






