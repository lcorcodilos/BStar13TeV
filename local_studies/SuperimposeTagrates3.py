import ROOT
from ROOT import *

import array
from array import array

import math
from math import sqrt


import Bstar_Functions_local
from Bstar_Functions_local import TTR_Init, LoadConstants

Constants = LoadConstants()
Lumi = str(int(Constants["lumi"]))+'pb'



tagrates_main = ROOT.TFile("../plots/TWrate_Maker_QCD_35851pb_PSET_rate_default.root")
tagrates_cheat = ROOT.TFile("../plots/TWrate_Maker_QCD_35851pb_PSET_sideband1.root")

c4 = TCanvas('c4', 'Pt fitted tagrate in 0.0 < Eta <0.8', 800, 500)

cuts = { 	"rate_default": {
				"graphBP": [],
				"graphBPerrh": [],
				"graphBPerrl": []
			},
			"sideband1": {
				"graphBP": [],
				"graphBPerrh": [],
				"graphBPerrl": []
			}
		}

# Make two sets of fits
for cut in cuts.keys():
	TTR = TTR_Init('Bifpoly',cut,'QCD','tpt','../','')
	TTR_err = TTR_Init('Bifpoly_err',cut,'QCD','tpt','../','')
	x = array( 'd' )
	BPy = []
	BPerryh = []
	BPerryl = []

	# Initilize lists with empty arrays
	for eta in range(0,2):
		BPy.append(array( 'd' ))
		BPerryh.append(array( 'd' ))
		BPerryl.append(array( 'd' ))

	# For each x (pt) increment store the y values for each non-BP fit and then the BP fit and errors
	for j in range(0,2000):
		x.append(j)
		for eta in range(0,2):
			BPy[eta].append(TTR[eta].Eval(x[j]))
			BPerryh[eta].append(TTR[eta].Eval(x[j])+sqrt(TTR_err[eta].Eval(x[j])))
			BPerryl[eta].append(TTR[eta].Eval(x[j])-sqrt(TTR_err[eta].Eval(x[j])))

	graphBP = []
	graphBPerrh = []
	graphBPerrl = []

	for eta in range(0,2):
		graphBP.append(TGraph(len(x),x,BPy[eta]))
		if cut == "rate_default":
			graphBP[eta].SetLineColor(kBlue)
		if cut == "sideband1":
			graphBP[eta].SetLineColor(kRed)

		graphBPerrh.append(TGraph(len(x),x,BPerryh[eta]))
		graphBPerrl.append(TGraph(len(x),x,BPerryl[eta]))
		if cut == "rate_default":
			graphBPerrh[eta].SetLineColor(kBlue)
			graphBPerrl[eta].SetLineColor(kBlue)
		elif cut == "sideband1":
			graphBPerrh[eta].SetLineColor(kRed)
			graphBPerrl[eta].SetLineColor(kRed)
		graphBP[eta].SetLineWidth(2)
		graphBPerrh[eta].SetLineWidth(2)
		graphBPerrl[eta].SetLineWidth(2)
		graphBPerrh[eta].SetLineStyle(2)
		graphBPerrl[eta].SetLineStyle(2)

	cuts[cut]["graphBP"] = graphBP
	cuts[cut]["graphBPerrh"] = graphBPerrh
	cuts[cut]["graphBPerrl"] = graphBPerrl


trsLow = [None]*2
trsHigh = [None]*2

trsList = [trsLow, trsHigh]

trsLow[0]= tagrates_main.Get("tagrateeta1")
trsLow[1]= tagrates_main.Get("tagrateeta2")

trsHigh[0]= tagrates_cheat.Get("tagrateeta1")
trsHigh[1]= tagrates_cheat.Get("tagrateeta2")

c4.cd()
c4.SetLeftMargin(0.16)

etastring = [
'0.00 < |#eta| < 0.80',
'0.80 < |#eta| < 2.40'
]

for eta in range(0,2):
	first = True
	for trs in trsList: 
		trs[eta].SetTitle(';p_{T} (GeV);R_{P/F}')
		trs[eta].GetYaxis().SetTitleOffset(0.8)
		trs[eta].SetMaximum(0.20)
		trs[eta].SetMinimum(0.0)
		trs[eta].GetXaxis().SetRangeUser(400,1200)
		trs[eta].SetStats(0)
	#c4.cd()
		if first == True:
			trs[eta].SetLineColor(kBlue)
			trs[eta].Draw("histe")
			first = False
		elif first == False:
			trs[eta].SetLineColor(kRed)
			trs[eta].Draw("samehiste")

	cuts["rate_default"]["graphBP"][eta].Draw("same")
	cuts["rate_default"]["graphBPerrh"][eta].Draw("same")
	cuts["rate_default"]["graphBPerrl"][eta].Draw("same")

	cuts["sideband1"]["graphBP"][eta].Draw("same")
	cuts["sideband1"]["graphBPerrh"][eta].Draw("same")
	cuts["sideband1"]["graphBPerrl"][eta].Draw("same")

	c4.RedrawAxis()
	c4.Print('plots/tagrateeta'+str(eta+1)+'QCDfitBP_cheat.pdf', 'pdf')
	c4.Print('plots/tagrateeta'+str(eta+1)+'QCDfitBP_cheat.png', 'png')

	

tagrates_main.Close()
tagrates_cheat.Close()