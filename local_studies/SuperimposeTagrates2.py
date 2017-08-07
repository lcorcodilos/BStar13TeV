import ROOT
from ROOT import *

import array
from array import array

import math
from math import sqrt

from optparse import OptionParser

parser = OptionParser()

parser.add_option('-r', '--rate', metavar='F', type='string', action='store',
                  default	=	'tpt',
                  dest		=	'rate',
                  help		=	'tpt or Mtw')
parser.add_option('-t', '--tau', metavar='F', type='string', action='store',
                  default	=	'low',
                  dest		=	'tau',
                  help		=	'low or high')

(options, args) = parser.parse_args()

import Bstar_Functions_local
from Bstar_Functions_local import TTR_Init, LoadConstants

Constants = LoadConstants()
Lumi = str(int(Constants["lumi"]))+'pb'

folder = ''
if options.rate == "Mtw":
	folder = 'Mtw/'

if options.tau == 'low':
	tagrates_cheat = ROOT.TFile("../plots/"+folder+"TWrate_Maker_QCD_"+Lumi+"_PSET_default.root")
	tagrates_lowWmass = ROOT.TFile("../plots/"+folder+"TWrate_Maker_QCD_"+Lumi+"_PSET_rate_lowWmass.root")
	tagrates_highWmass = ROOT.TFile("../plots/"+folder+"TWrate_Maker_QCD_"+Lumi+"_PSET_rate_highWmass.root")
	tagrates_avg = ROOT.TFile("../plots/"+folder+"TWrate_Maker_QCD_"+Lumi+"_PSET_rate_default.root")
	sigRegion = "default"
	coeffic = ''
elif options.tau == 'high':
	tagrates_cheat = ROOT.TFile("../plots/"+folder+"TWrate_Maker_QCD_"+Lumi+"_PSET_sideband.root")
	tagrates_lowWmass = ROOT.TFile("../plots/"+folder+"TWrate_Maker_QCD_"+Lumi+"_PSET_rate_lowWmass1.root")
	tagrates_highWmass = ROOT.TFile("../plots/"+folder+"TWrate_Maker_QCD_"+Lumi+"_PSET_rate_highWmass1.root")
	tagrates_avg = ROOT.TFile("../plots/"+folder+"TWrate_Maker_QCD_"+Lumi+"_PSET_rate_sideband.root")
	sigRegion = "sideband"
	coeffic = '1'

c4 = TCanvas('c4', 'Pt fitted tagrate in 0.0 < Eta <0.8', 800, 500)

rates = { 	"rate_lowWmass"+coeffic: {
				"graphBP": [],
				"graphBPerrh": [],
				"graphBPerrl": []
			},
			"rate_highWmass"+coeffic: {
				"graphBP": [],
				"graphBPerrh": [],
				"graphBPerrl": []
			},
			"rate_"+sigRegion: {
				"graphBP": [],
				"graphBPerrh": [],
				"graphBPerrl": []
			},
			sigRegion: {
				"graphBP": [],
				"graphBPerrh": [],
				"graphBPerrl": []
			}
			
		}

# Make two sets of fits
for cut in rates.keys():
	TTR = TTR_Init('Bifpoly',cut,'QCD',options.rate,'../')
	TTR_err = TTR_Init('Bifpoly_err',cut,'QCD',options.rate,'../')
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
	for j in range(0,4000):
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
		graphBPerrh.append(TGraph(len(x),x,BPerryh[eta]))
		graphBPerrl.append(TGraph(len(x),x,BPerryl[eta]))
		if cut == "rate_lowWmass"+coeffic:
			graphBP[eta].SetLineColor(kBlue)
			graphBPerrh[eta].SetLineColor(kBlue)
			graphBPerrl[eta].SetLineColor(kBlue)
		if cut == "rate_highWmass"+coeffic:
			graphBP[eta].SetLineColor(kRed)
			graphBPerrh[eta].SetLineColor(kRed)
			graphBPerrl[eta].SetLineColor(kRed)
		if cut == "rate_"+sigRegion:
			graphBP[eta].SetLineColor(kBlack)
			graphBPerrh[eta].SetLineColor(kBlack)
			graphBPerrl[eta].SetLineColor(kBlack)
		if cut == sigRegion:
			graphBP[eta].SetLineColor(6)
			graphBPerrh[eta].SetLineColor(6)
			graphBPerrl[eta].SetLineColor(6)

		graphBP[eta].SetLineWidth(2)
		graphBPerrh[eta].SetLineWidth(2)
		graphBPerrl[eta].SetLineWidth(2)
		graphBPerrh[eta].SetLineStyle(2)
		graphBPerrl[eta].SetLineStyle(2)

	rates[cut]["graphBP"] = graphBP
	rates[cut]["graphBPerrh"] = graphBPerrh
	rates[cut]["graphBPerrl"] = graphBPerrl


trsLow = [None]*2
trsHigh = [None]*2
trsAvg = [None]*2
trsCheat = [None]*2

trsList = [trsLow, trsHigh, trsAvg, trsCheat]

trsLow[0]= tagrates_lowWmass.Get("tagrateeta1")
trsLow[1]= tagrates_lowWmass.Get("tagrateeta2")

trsHigh[0]= tagrates_highWmass.Get("tagrateeta1")
trsHigh[1]= tagrates_highWmass.Get("tagrateeta2")

trsAvg[0]= tagrates_avg.Get("tagrateeta1")
trsAvg[1]= tagrates_avg.Get("tagrateeta2")

trsCheat[0] = tagrates_cheat.Get("tagrateeta1")
trsCheat[1] = tagrates_cheat.Get("tagrateeta2")


c4.cd()
c4.SetLeftMargin(0.16)
c4.SetBottomMargin(0.15)

etastring = [
'0.00 < |#eta| < 0.80',
'0.80 < |#eta| < 2.40'
]

for eta in range(0,2):
	for trs in trsList:
		if options.rate == 'tpt':
			trs[eta].SetTitle(';p_{T} (GeV);R_{P/F}')
		elif options.rate == 'Mtw':
			trs[eta].SetTitle(';M_{tW} (GeV);R_{P/F}')
		trs[eta].GetYaxis().SetTitleOffset(0.8)
		trs[eta].SetMaximum(0.20)
		trs[eta].SetMinimum(0.0)
		if options.rate == 'tpt':
			trs[eta].GetXaxis().SetRangeUser(400,1200)
		elif options.rate == 'Mtw':
			trs[eta].GetXaxis().SetRangeUser(1000,4000)

		trs[eta].SetStats(0)
	#c4.cd()
		if trs == trsLow:
			trs[eta].SetLineColor(kBlue)
			trs[eta].Draw("histe")
		elif trs == trsHigh:
			trs[eta].SetLineColor(kRed)
			trs[eta].Draw("samehiste")
		elif trs == trsAvg:
			trs[eta].SetLineColor(kBlack)
			trs[eta].Draw("samehiste")
		elif trs == trsCheat:
			trs[eta].SetLineColor(6)
			trs[eta].Draw("samehiste")

	rates["rate_lowWmass"+coeffic]["graphBP"][eta].Draw("same")
	#rates["rate_lowWmass"+coeffic]["graphBPerrh"][eta].Draw("same")
	#rates["rate_lowWmass"+coeffic]["graphBPerrl"][eta].Draw("same")

	rates["rate_highWmass"+coeffic]["graphBP"][eta].Draw("same")
	#rates["rate_highWmass"+coeffic]["graphBPerrh"][eta].Draw("same")
	#rates["rate_highWmass"+coeffic]["graphBPerrl"][eta].Draw("same")

	rates["rate_"+sigRegion]["graphBP"][eta].Draw("same")
	#rates["rate_"+sigRegion]["graphBPerrh"][eta].Draw("same")
	#rates["rate_"+sigRegion]["graphBPerrl"][eta].Draw("same")

	rates[sigRegion]["graphBP"][eta].Draw("same")


	c4.RedrawAxis()
	c4.Print('plots/tagrateeta'+str(eta+1)+'QCDfitBP_'+options.rate+'_tau21_'+options.tau+'.pdf', 'pdf')
	c4.Print('plots/tagrateeta'+str(eta+1)+'QCDfitBP_'+options.rate+'_tau21_'+options.tau+'.png', 'png')

	

tagrates_lowWmass.Close()
tagrates_highWmass.Close()
tagrates_avg.Close()
tagrates_cheat.Close()