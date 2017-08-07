

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
from optparse import OptionParser
#gROOT.Macro("rootlogon.C")
#gROOT.LoadMacro("insertlogo.C+")
parser = OptionParser()


parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-l', '--lumi', metavar='F', type='string', action='store',
                  default	=	'35851pb',
                  dest		=	'lumi',
                  help		=	'Lumi folder to look in')
parser.add_option('-y', '--modmass', metavar='F', type='string', action='store',
                  default	=	'nominal',
                  dest		=	'modmass',
                  help		=	'nominal up or down')
(options, args) = parser.parse_args()

cuts = options.cuts


#import Bstar_Functions	
#from Bstar_Functions import *

#Consts = LoadConstants()
#lumi = Consts['lumi']
#Lumi = str(int(lumi/1000))+'fb'
Lumi = options.lumi

pie = TMath.Pi()

kinVar = ['Tau_21',  	'Mt', 		'Tau_32', 	'MaxSJCSV', 	'dyfull', 	'dysemi', 	'Mw',	'MwStack'	]
kinBin = [10, 		 20, 		  10, 		  20,		  12,		   12,		 30,	    30		]
kinLow = [0, 		   0, 		   0, 		   0,		   0,		    0,		  0,	     0		]
kinHigh= [1.0, 		 500, 		 1.0, 		   1,		   5,		    5,		 300,	    300		]
rebin =  [1,		   1, 		   1,		   1,		   1,		    1,		 1,	     1		]
xTitle = ['#tau_{21}',	'M_{t}',	'#tau_{32}',	'Max SJCSV',	'|#Delta y|',	'|#Delta y|',	'M_{W}','M_{t}'		]
st1_label= [";Tau_21;Counts", ";Mass_{t} (GeV);Counts", ";Tau_32;Counts", ";Max subjet CSV;Counts", ";|\Delta y| between top and W candidates;Counts", ";|\Delta y| between top and W candidates;Counts", "Mass_{W} (GeV);Counts",";Mass_{t} (GeV);Counts"]
#pull_label= [";Nsubjets;(Data-Bkg)/#sigma", ";MinPairMass (GeV);(Data-Bkg)/#sigma", ";Mass_{t} (GeV);(Data-Bkg)/#sigma", ";Nsubjetiness;(Data-Bkg)/#sigma", ";Max subjet CSV;(Data-Bkg)/#sigma", ";|\Delta y| between top and W candidates;(Data-Bkg)/#sigma", ";Phi_{t} (rad)", ";|\Delta y| between top and W candidates;(Data-Bkg)/#sigma"]

iterations = len(kinVar)
kin = ''

mmstr = ""
if options.modmass!="nominal":
	print "using modm uncertainty"
	mmstr = "_modm_"+options.modmass

SR1200 = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesweightedsignalRH1200_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")
SR2800 = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesweightedsignalRH2800_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")
SR2000 = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesweightedsignalRH2000_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")

Data = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesdata_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")
QCDmc = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesQCD_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")
TTmc = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesweightedttbar_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")

ST = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesweightedsingletop_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")

#---------For ttbar closure test, using MwStack-----------------------------------
# Commented out since I wasn't using it - LC 5/30/17
# st2 = ROOT.THStack('st2','st2')
# MwStackData = Data.Get('MwStack')
# MwStackBE = Data.Get('QCDbkgMwStack')
# MwStackTTmc = TTmc.Get('MwStack')
# MwStackTTmcBE = TTmc.Get('QCDbkgMwStack')

# MwStackData.Rebin(5)
# MwStackBE.Rebin(5)
# MwStackTTmc.Rebin(5)
# MwStackTTmcBE.Rebin(5)


# MwStackData.GetXaxis().SetTitle("Mass candidate W jet")
# MwStackBE.GetXaxis().SetTitle("Mass candidate W jet")
# MwStackTTmc.GetXaxis().SetTitle("Mass candidate W jet")

# cMwStack = TCanvas('MwStack', 'W mass with Full selection', 700, 700)
# legend = TLegend(0.7, 0.6, 0.93, 0.9)

# cMwStack.SetLeftMargin(0.16)
# cMwStack.SetRightMargin(0.05)
# cMwStack.SetTopMargin(0.13)
# cMwStack.SetBottomMargin(0.15)


# MwStackBE.Add(MwStackTTmcBE,-1)

# MwStackBE.SetFillColor(kYellow)
# MwStackTTmc.SetFillColor(kRed)

# st2.Add(MwStackBE)
# st2.Add(MwStackTTmc)

# legend.AddEntry( MwStackData, 'Data', 'P')
# legend.AddEntry( MwStackBE, 'QCD background prediction', 'F')	
# legend.AddEntry( MwStackTTmc, 't#bar{t} MC prediction', 'F')

# st2.SetMaximum(MwStackData.GetMaximum() * 1.3)
# st2.SetMinimum(0.1)
# st2.SetTitle(";Mass candidate W jet (GeV);Counts")
# st2.Draw("hist")

# MwStackData.SetMaximum(MwStackData.GetMaximum() * 1.3)
# MwStackData.Draw("same")

# cMwStack.cd()

# legend.Draw()

# cMwStack.Print('MwStack_'+Lumi+'_'+options.cuts+'.root')
# cMwStack.Print('MwStack_'+Lumi+'_'+options.cuts+'.pdf')

#-----------------Now plot 2D distributions---------------------------------------

cTaus = TCanvas("Taus","Taus", 1700, 1000)
cTausPfx = TCanvas("TausPfx","TausPfx", 1700, 1000)
cTausPfy = TCanvas("TausPfy","TausPfy", 1700, 1000)
cWspace = TCanvas("Wspace", "Wspace", 1700, 1000)

cTaus.Divide(3,2, 0.005, 0.005)
cTausPfx.Divide(3,2, 0.005, 0.005)
cTausPfy.Divide(3,2, 0.005, 0.005)
cWspace.Divide(3,2, 0.005, 0.005)

TTmcTaus = TTmc.Get("Tau32vsTau21")
QCDmcTaus = QCDmc.Get("Tau32vsTau21")
SR1200Taus = SR1200.Get("Tau32vsTau21")
SR2800Taus = SR2800.Get("Tau32vsTau21")
SR2000Taus = SR2000.Get("Tau32vsTau21")
STTaus = ST.Get("Tau32vsTau21")

TTmcWspace = TTmc.Get("Tau21vWmass")
QCDmcWspace = QCDmc.Get("Tau21vWmass")
SR1200Wspace = SR1200.Get("Tau21vWmass")
SR2800Wspace = SR2800.Get("Tau21vWmass")
SR2000Wspace = SR2000.Get("Tau21vWmass")
STWspace = ST.Get("Tau21vWmass")

histList = [	[QCDmcTaus,QCDmcWspace],
			[TTmcTaus,TTmcWspace],
			[STTaus,STWspace],
			[SR1200Taus,SR1200Wspace],
			[SR2000Taus,SR2000Wspace],
			[SR2800Taus,SR2800Wspace]	]
titleList = ["QCD MC","TTbar MC","Single top MC","b*_{R} 1200 GeV","b*_{R} 2000 GeV","b*_{R} 2800 GeV"]
title2List = ["QCD", "TT", "ST", "SR1200", "SR2000", "SR28000"]

gStyle.SetOptStat(0)

for i in range(len(titleList)):
	cTaus.cd(i+1)
	cTaus.GetPad(i+1).SetRightMargin(0.15)
	histList[i][0].SetTitle(titleList[i])
	histList[i][0].GetXaxis().SetTitle("#tau_{21}")
	histList[i][0].GetYaxis().SetTitle("#tau_{32}")
	histList[i][0].GetYaxis().SetTitleOffset(0.7)
	histList[i][0].Draw("COLZ")
	# palette = histList[i][0].GetListOfFunctions().FindObject("palette")
	# palette.SetX1NDC(0.85)
	# palette.SetX2NDC(0.89)
	cTausPfx.cd(i+1)
	profilex = histList[i][0].ProfileX(titleList[i]+"_pfx",1,-1,"o")
	#profilex.SetMinimum(0)
	#profilex.SetMaximum(1)
	profilex.Draw()
	cTausPfy.cd(i+1)
	profiley = histList[i][0].ProfileY(titleList[i]+"_pfy",1,-1,"o")
	#profiley.SetMinimum(0)
	#profiley.SetMaximum(1)
	profiley.Draw()

	
cTausPfx.Print("Tau32vsTau21_pfx.png","png")
cTausPfy.Print("Tau32vsTau21_pfy.png","png")
cTaus.Print("Tau32vsTau21.png","png")

for i in range(len(titleList)):
	cWspace.cd(i+1)
	cWspace.GetPad(i+1).SetRightMargin(0.15)
	histList[i][1].SetTitle(titleList[i])
	histList[i][1].GetXaxis().SetTitle("M_{W}")
	histList[i][1].GetYaxis().SetTitle("#tau_{21}")
	histList[i][1].GetYaxis().SetTitleOffset(0.7)
	histList[i][1].Draw("COLZ")
	# palette = histList[i][0].GetListOfFunctions().FindObject("palette")
	# palette.SetX1NDC(0.85)
	# palette.SetX2NDC(0.89)

cWspace.Print("Tau21vsWmass.png","png")


#------------------Resume---------------------------------------------------------

for i in range(0, iterations-1):
	print "kinVar = " + "'" + kinVar[i] + "'"

	QCDmc = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesQCD_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")


	c1 = TCanvas(kinVar[i], 'TBD', 700, 700)
	main = ROOT.TPad("main", "main", 0, 0, 1, 1)
	#out = ROOT.TH1F(kinVar[i], kinVar[i], kinBin[i], kinLow[i], kinHigh[i])

	main.SetLeftMargin(0.16)
	main.SetRightMargin(0.05)
	main.SetTopMargin(0.05)
	main.SetBottomMargin(0.15)

	main.Draw()

	main.cd()

	leg = TLegend(0.0, 0.0, 1.0, 1.0)
	leg.SetNColumns(2)
	leg.SetFillColor(0)
	leg.SetBorderSize(0)


	Mult = 1.0

	DataFS = Data.Get(kinVar[i])
	TTmcFS = TTmc.Get(kinVar[i])
	QCDmcFS = QCDmc.Get(kinVar[i])
	SR1200FS = SR1200.Get(kinVar[i])
	SR2800FS = SR2800.Get(kinVar[i])
	SR2000FS = SR2000.Get(kinVar[i])
	STFS = ST.Get(kinVar[i])

	print "Selections grabbed"

	#DataFS = DataFS.Rebin(rebin[i])
	#TTmcFS = TTmcFS.Rebin(rebin[i])
	#QCDmcFS = QCDmcFS.Rebin(rebin[i])
	#SR1200FS = SR1200FS.Rebin(rebin[i])
	#SR2800FS = SR2800FS.Rebin(rebin[i])	
	#SR2000FS = SR2000FS.Rebin(rebin[i])
	#STFS = STFS.Rebin(rebin[i])
	
	print "Data integral: " + str(DataFS.Integral())
	
	DataFS.Scale(1/DataFS.Integral())
	TTmcFS.Scale(1/TTmcFS.Integral())
	QCDmcFS.Scale(1/QCDmcFS.Integral())
	SR1200FS.Scale(1/SR1200FS.Integral())
	SR2800FS.Scale(1/SR2800FS.Integral())
	SR2000FS.Scale(1/SR2000FS.Integral())
	STFS.Scale(1/STFS.Integral())

#	out.Add(singletop)
	DataFS.SetStats(0)
	TTmcFS.SetStats(0)
	QCDmcFS.SetStats(0)
	SR1200FS.SetStats(0)
	SR2800FS.SetStats(0)
	SR2000FS.SetStats(0)
	STFS.SetStats(0)

	DataFS.SetLineColor(kBlack)
	DataFS.SetLineWidth(0)
	TTmcFS.SetLineColor(kRed)
	TTmcFS.SetLineWidth(2)
	QCDmcFS.SetLineColor(kBlack)
	QCDmcFS.SetFillColor(5)
	QCDmcFS.SetLineWidth(2)
	SR1200FS.SetLineColor(kBlue)
	SR1200FS.SetLineWidth(2)
	SR1200FS.SetLineStyle(5)
	SR2800FS.SetLineColor(kBlue-3)
	SR2800FS.SetLineWidth(2)
	SR2800FS.SetLineStyle(5)
	SR2000FS.SetLineColor(kBlue+3)
	SR2000FS.SetLineWidth(2)
	SR2000FS.SetLineStyle(5)
	STFS.SetLineColor(kGreen-3)
	STFS.SetLineWidth(2)



	histList = [TTmcFS, QCDmcFS, SR1200FS, SR2800FS, SR2000FS, STFS, DataFS]

	yMax = histList[0].GetMaximum()
	maxHist = histList[0]
	for h in range(1,len(histList)):
		if histList[h].GetMaximum() > yMax:
			yMax = histList[h].GetMaximum()
			maxHist = histList[h]
	for h in histList:
		h.SetMaximum(yMax*1.3)
		h.SetTitle("")
		axis = h.GetXaxis()

		if kinVar[i] == 'Mw' or kinVar[i] == 'Mt':
			axis.SetTitle(xTitle[i]+'(GeV)')
		else:
			axis.SetTitle(xTitle[i])

		if kinVar[i] == "Mt" or kinVar[i] == 'Mw':
			axis.SetNdivisions(-1005)
		if kinVar[i] == "Tau_21" or kinVar[i] == "Tau_32":
			axis.SetRangeUser(0,1)

#	leg.AddEntry( DataFS, 'Data', 'P')
	leg.AddEntry( QCDmcFS, 'QCD MC', 'F')	
	leg.AddEntry( TTmcFS, 't#bar{t} MC', 'L')
	leg.AddEntry( STFS, 'Single top quark MC', 'L')
	leg.AddEntry( SR1200FS, 'b*_{R} at 1200 GeV', 'L')
	leg.AddEntry( SR2800FS, 'b*_{R} at 2800 GeV', 'L')
	leg.AddEntry( SR2000FS, 'b*_{R} at 2000 GeV', 'L')

#	DataFS.Draw("same")
	QCDmcFS.Draw("samehist")
	STFS.Draw("samehist")
	TTmcFS.Draw("samehist")
	SR1200FS.Draw("samehist")
	SR2800FS.Draw("samehist")
	SR2000FS.Draw("samehist")
	

	#out.SetTitle(st1_label[i])
	gPad.SetLeftMargin(.16)
#	out.GetYaxis().SetTitleOffset(0.9)

	if i == 1:
		varLeg = TCanvas("Variables legend", "Variables legend")
		leg.Draw()
		varLeg.Print('varleg.pdf','pdf')
		c1.cd()

	prelim = TLatex()
	prelim.SetNDC()
	#4 is 5.0fb-1, 5 is 1.0fb-1, 6 is 10.0fb-1
	# if lumi == 1000:
	# 	insertlogo( main, 5, 11 )
	# elif lumi == 5000:
	# 	insertlogo( main, 4, 11)
	# elif lumi == 10000:
	# 	insertlogo( main, 6, 11)
	# elif lumi == 2553.0:
	# 	insertlogo( main, 8, 11)
	#insertlogo( main, 8, 11)



	gPad.SetLeftMargin(.16)



	line2=ROOT.TLine(500.0,0.0,4000.0,0.0)
	line2.SetLineColor(0)
	line1=ROOT.TLine(500.0,0.0,4000.0,0.0)
	line1.SetLineStyle(2)

	line2.Draw()
	line1.Draw()
	gPad.Update()

	main.RedrawAxis()

	c1.Print('plots/' + kinVar[i] + '_'+Lumi+'_PSET_'+options.cuts+'.root', 'root')
	c1.Print('plots/' + kinVar[i] + '_'+Lumi+'_PSET_'+options.cuts+'.pdf', 'pdf')
	c1.Print('plots/' + kinVar[i] + '_'+Lumi+'_PSET_'+options.cuts+'.png', 'png')

	c1.Close()
# Just for MwStack
'''c2 = TCanvas(kinVar[7], 'TBD', 700, 700)
main = ROOT.TPad("main", "main", 0, 0, 1, 1)
st1 = ROOT.THStack('st1', 'st1')

main.SetLeftMargin(0.16)
main.SetRightMargin(0.05)
main.SetTopMargin(0.1)
main.SetBottomMargin(0.1)

main.Draw()
main.cd()

leg = TLegend(0.0, 0.0, 1.0, 1.0)
leg.SetNColumns(2)
leg.SetFillColor(0)
leg.SetBorderSize(0)

print "Root files opened"

DataFSMt = Data.Get(kinVar[7])
TTmcFSMt = TTmc.Get(kinVar[7])
QCDmcFSMt = QCDmc.Get(kinVar[7])
STFSMt = ST.Get(kinVar[7])

print "Selections grabbed"

st1.Add(QCDmc)'''
