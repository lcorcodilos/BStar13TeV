

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
gROOT.Macro("rootlogon.C")
gROOT.LoadMacro("insertlogo.C+")
parser = OptionParser()


parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-l', '--lumi', metavar='F', type='string', action='store',
                  default	=	'27203pb',
                  dest		=	'lumi',
                  help		=	'Lumi folder to look in')
parser.add_option('-y', '--modmass', metavar='F', type='string', action='store',
                  default	=	'nominal',
                  dest		=	'modmass',
                  help		=	'nominal up or down')
(options, args) = parser.parse_args()

cuts = options.cuts


import Bstar_Functions	
from Bstar_Functions import *

#Consts = LoadConstants()
#lumi = Consts['lumi']
#Lumi = str(int(lumi/1000))+'fb'
Lumi = options.lumi

pie = TMath.Pi()

kinVar = ['Tau_21',  	'Mt', 		'Tau_32', 	'MaxSJCSV', 	'dyfull', 	'dysemi', 	'Mw',	'MtStack'	]
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

SR1200 = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesweightedsignalLH1200_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")
SR2800 = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesweightedsignalLH2800_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")
SR2000 = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesweightedsignalLH2000_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")

Data = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesdata_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")
QCDmc = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesQCD_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")
TTmc = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesweightedttbar_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")

#ST = ROOT.TFile("rootfiles/"+Lumi+"/TWvariablesweightedsingletop_Trigger_nominal_none"+mmstr+"_PSET_"+options.cuts+kin+".root")

#---------For ttbar closure test, using MtStack-----------------------------------

st2 = ROOT.THStack('st2','st2')
MtStackData = Data.Get('MtStack')
MtStackBE = Data.Get('QCDbkgMtStack')
MtStackTTmc = TTmc.Get('MtStack')
MtStackTTmcBE = TTmc.Get('QCDbkgMtStack')

#MtStackData.GetXaxis().SetTitle("M_{t}")
#MtStackBE.GetXaxis().SetTitle("M_{t}")
#MtStackTTmc.GetXaxis().SetTitle("M_{t}")

cMtStack = TCanvas('MtStack', 'Top mass with Full selection', 700, 700)
legend = TLegend(0.7, 0.6, 0.93, 0.9)

cMtStack.SetLeftMargin(0.16)
cMtStack.SetRightMargin(0.05)
cMtStack.SetTopMargin(0.13)
cMtStack.SetBottomMargin(0.15)


MtStackBE.Add(MtStackTTmcBE,-1)

MtStackBE.SetFillColor(kYellow)
MtStackTTmc.SetFillColor(kRed)

st2.Add(MtStackBE)
st2.Add(MtStackTTmc)

legend.AddEntry( MtStackData, 'Data', 'P')
legend.AddEntry( MtStackBE, 'QCD background prediction', 'F')	
legend.AddEntry( MtStackTTmc, 't#bar{t} MC prediction', 'F')

st2.SetMaximum(MtStackData.GetMaximum() * 1.3)
st2.SetMinimum(0.1)
st2.SetTitle(";M_{t} (GeV);Counts")
st2.Draw("hist")

MtStackData.SetMaximum(MtStackData.GetMaximum() * 1.3)
MtStackData.Draw("same")

cMtStack.cd()

legend.Draw()

cMtStack.Print('MtStack_'+Lumi+'_'+options.cuts+'.root')
cMtStack.Print('MtStack_'+Lumi+'_'+options.cuts+'.pdf')

#------------------Resume---------------------------------------------------------

for i in range(0, iterations-1):
	print "kinVar = " + "'" + kinVar[i] + "'"



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




	print "Root files opened"

	DataFS = Data.Get(kinVar[i])
	TTmcFS = TTmc.Get(kinVar[i])
	QCDmcFS = QCDmc.Get(kinVar[i])
	SR1200FS = SR1200.Get(kinVar[i])
	SR2800FS = SR2800.Get(kinVar[i])
	SR2000FS = SR2000.Get(kinVar[i])
	#STFS = ST.Get(kinVar[i])

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
	#STFS.Scale(1/STFS.Integral())

#	out.Add(singletop)
	DataFS.SetStats(0)
	TTmcFS.SetStats(0)
	QCDmcFS.SetStats(0)
	SR1200FS.SetStats(0)
	SR2800FS.SetStats(0)
	SR2000FS.SetStats(0)
	#STFS.SetStats(0)

	DataFS.SetLineColor(kBlack)
	DataFS.SetLineWidth(0)
	TTmcFS.SetLineColor(kRed)
	TTmcFS.SetLineWidth(2)
	QCDmcFS.SetLineColor(kBlack)
	QCDmcFS.SetLineWidth(2)
	SR1200FS.SetLineColor(kBlue)
	SR1200FS.SetLineWidth(1)
	SR2800FS.SetLineColor(kBlue+1)
	SR2800FS.SetLineWidth(1)
	SR2000FS.SetLineColor(kBlue+2)
	SR2000FS.SetLineWidth(1)
	#STFS.SetLineColor(kBlue)
	#STFS.SetLineWidth(1)



	histList = [DataFS, TTmcFS, QCDmcFS, SR1200FS, SR2800FS, SR2000FS]#, STFS]

	yMax = histList[0].GetMaximum()
	maxHist = histList[0]
	for h in range(1,len(histList)):
		if histList[h].GetMaximum() > yMax:
			yMax = histList[h].GetMaximum()
			maxHist = histList[h]
	for h in histList:
		h.SetMaximum(yMax*1.3)
		h.SetTitle("")
		if kinVar[i] == 'Mw' or kinVar[i] == 'Mt':
			h.GetXaxis().SetTitle(xTitle[i]+'(GeV)')
		else:
			h.GetXaxis().SetTitle(xTitle[i])

	#leg.AddEntry( DataFS, 'Data', 'P')
	leg.AddEntry( QCDmcFS, 'QCD MC', 'L')	
	leg.AddEntry( TTmcFS, 't#bar{t} MC prediction', 'L')
	#leg.AddEntry( STFS, 'Single top quark MC prediction', 'L')
	leg.AddEntry( SR1200FS, 'b*_{L} at 1200 GeV', 'L')
	leg.AddEntry( SR2800FS, 'b*_{L} at 2800 GeV', 'L')
	leg.AddEntry( SR2000FS, 'b*_{L} at 2000 GeV', 'L')

	#DataFS.Draw("same")
	TTmcFS.Draw("samehist")
	QCDmcFS.Draw("samehist")
	SR1200FS.Draw("samehist")
	SR2800FS.Draw("samehist")
	SR2000FS.Draw("samehist")
	#STFS.Draw("samehist")

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
	if lumi == 1000:
		insertlogo( main, 5, 11 )
	elif lumi == 5000:
		insertlogo( main, 4, 11)
	elif lumi == 10000:
		insertlogo( main, 6, 11)
	elif lumi == 2553.0:
		insertlogo( main, 8, 11)



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

# Just for MtStack
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
