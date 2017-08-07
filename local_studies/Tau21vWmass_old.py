import ROOT
from ROOT import *

QCDFile = TFile('TWtreefile_QCD_Trigger_nominal_none.root','open')
SR1200File = TFile('../TTrees/TWtreefile_signalRH1200_Trigger_nominal_none.root','open')
SR2000File = TFile('../TTrees/TWtreefile_signalRH2000_Trigger_nominal_none.root','open')
SR2800File = TFile('../TTrees/TWtreefile_signalRH2800_Trigger_nominal_none.root','open')
TTFile = TFile('../TTrees/TWtreefile_ttbar_Trigger_nominal_none.root','open')
STFile = TFile('TWtreefile_singletop_Trigger_nominal_none.root','open')

print "Files made"

QCDTree = QCDFile.Get('Tree')
SR1200Tree = SR1200File.Get('Tree')
SR2000Tree = SR2000File.Get('Tree')
SR2800Tree = SR2800File.Get('Tree')
TTTree = TTFile.Get('Tree')
STTree = STFile.Get('Tree')

treeList = [QCDTree, SR1200Tree, SR2000Tree, SR2800Tree, TTTree, STTree]

print "Trees grabbed"

cQCD = TCanvas("cQCD","cQCD",600,600)
cSR1200 = TCanvas("cSR1200","cSR1200",600,600)
cSR2000 = TCanvas("cSR2000","cSR2000",600,600)
cSR2800 = TCanvas("cSR2800","cSR2800",600,600)
cTT = TCanvas("cTT","cTT",600,600)
cST = TCanvas("cST","cST",600,600)

cList = [cQCD, cSR1200, cSR2000, cSR2800, cTT, cST]

QCDHist = TH2F('QCD MC', 'QCD MC', 20, 0, 500, 10, 0, 1)
SR1200Hist = TH2F('SR1200 MC', 'SR1200 MC', 20, 0, 500, 10, 0, 1)
SR2000Hist = TH2F('SR2000 MC', 'SR2000 MC', 20, 0, 500, 10, 0, 1)
SR2800Hist = TH2F('SR2800 MC', 'SR2800 MC', 20, 0, 500, 10, 0, 1)
TTHist = TH2F('TT MC', 'TT MC', 20, 0, 500, 10, 0, 1)
STHist = TH2F('ST MC', 'ST MC', 20, 0, 500, 10, 0, 1)

histList = [QCDHist, SR1200Hist, SR2000Hist, SR2800Hist, TTHist, STHist]

print "Hists made"

stringList = ['QCD', 'SR1200', 'SR2000', 'SR2800', 'TT', 'ST']

for i in range(len(histList)):
	print "Processing " + stringList[i] + "...",
	wmass_val = event.SDmass_subleading
	tau21_val = event.tau2_subleading/event.tau1_subleading
	treeList[i].Draw("SDmass_subleading:")

	# for event in treeList[i]:
	# 	if event.tau1_subleading <= 0:
	# 		continue
	# 	wmass_val = event.SDmass_subleading
	# 	tau21_val = event.tau2_subleading/event.tau1_subleading
	# 	histList[i].Fill(tau21_val,wmass_val)
	# cList[i].cd()
	# histList[i].Draw()
	cList[i].Print('Plot_Tau21vWmass_'+stringList[i]+'.pdf','pdf')
	print "done"


