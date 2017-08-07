
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

parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'rate_default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-r', '--rate', metavar='F', type='string', action='store',
                  default	=	'Mtw',
                  dest		=	'rate',
                  help		=	'1D Rate parameterization (tpt, Mtw, Mt)')

(options, args) = parser.parse_args()

rootdir="rootfiles/"
import Bstar_Functions_local	
from Bstar_Functions_local import *

Cons = LoadConstants()

#Uncomment for the single lumi from BstarFunctions
cLumi = Cons['lumi']
lumiList = [cLumi]
Lumi = str(int(cLumi))+'pb'

setstr = ""
if options.set=='QCD':
	setstr = 'QCD'
elif options.set=='data':
	setstr = 'data'

gROOT.Macro("rootlogon.C")
#gROOT.LoadMacro("insertlogo.C+")

TTR = TTR_Init('Bifpoly',options.cuts,options.set,options.rate,'')
TTR_err = TTR_Init('Bifpoly_err',options.cuts,options.set,options.rate,'')

fittitles = ["pol0","pol2","pol3","FIT","expofit"]
fits = []
for fittitle in fittitles:
	fits.append(TTR_Init(fittitle,options.cuts,options.set,options.rate,''))

leg1 = TLegend(0.45,0.57,.84,.78)
leg1.SetFillColor(0)
leg1.SetBorderSize(0)

leg2 = TLegend(0.,0.,1.,1.)
leg2.SetFillColor(0)
leg2.SetBorderSize(0)


c4 = TCanvas('c4', 'Pt fitted tagrate in 0.0 < Eta <0.8', 800, 500)

cleg = TCanvas('cleg', 'tagged vs signal', 400, 600)

param1D = options.rate + '/'

tagrates = ROOT.TFile("plots/"+param1D+"TWrate_Maker_"+setstr+"_"+Lumi+"_PSET_"+options.cuts+".root")


x = array( 'd' )
y = []
BPy = []
BPerryh = []
BPerryl = []

# Initilize lists with empty arrays
for eta in range(0,2):
	y.append([])
	for fittitle in fittitles:
		y[eta].append(array( 'd' ))
	BPy.append(array( 'd' ))
	BPerryh.append(array( 'd' ))
	BPerryl.append(array( 'd' ))

# For each x (pt) increment store the y values for each non-BP fit and then the BP fit and errors
for j in range(0,4000):

	x.append(j)
	for eta in range(0,2):
		for ifit in range(0,len(fits)):
			y[eta][ifit].append(fits[ifit][eta].Eval(x[j]))
		BPy[eta].append(TTR[eta].Eval(x[j]))
		BPerryh[eta].append(TTR[eta].Eval(x[j])+sqrt(TTR_err[eta].Eval(x[j])))
		BPerryl[eta].append(TTR[eta].Eval(x[j])-sqrt(TTR_err[eta].Eval(x[j])))

# Create graphs of errors and ffor fittitle in fittitles:its

graphs = [] 
graphBP = []
graphBPerrh = []
graphBPerrl = []

for eta in range(0,2):
	graphs.append([])

	for ifit in range(0,len(fits)):
		graphs[eta].append(TGraph(len(x),x,y[eta][ifit]))
		graphs[eta][ifit].SetLineColor(kBlue)
		graphs[eta][ifit].SetLineWidth(2)
	graphBP.append(TGraph(len(x),x,BPy[eta]))
	graphBP[eta].SetLineColor(kBlue)

	graphBPerrh.append(TGraph(len(x),x,BPerryh[eta]))
	graphBPerrl.append(TGraph(len(x),x,BPerryl[eta]))
	graphBPerrh[eta].SetLineColor(kBlue)
	graphBPerrl[eta].SetLineColor(kBlue)
	graphBP[eta].SetLineWidth(2)
	graphBPerrh[eta].SetLineWidth(2)
	graphBPerrl[eta].SetLineWidth(2)
	graphBPerrh[eta].SetLineStyle(2)
	graphBPerrl[eta].SetLineStyle(2)




#leg1.AddEntry(treta3,"Data Points","p")
leg1.AddEntry(graphBP[0],"Bifurcated polynomial fit","l")
leg1.AddEntry(graphBPerrh[0],"Fit uncertainty","l")

trs = [None]*2

trs[0]= tagrates.Get("tagrateeta1")
trs[1]= tagrates.Get("tagrateeta2")

c4.cd()
c4.SetLeftMargin(0.16)

etastring = [
'0.00 < |#eta| < 0.80',
'0.80 < |#eta| < 2.40'
]

for eta in range(0,2):
	print eta
	trs[eta].SetTitle(';M_{tW} (GeV);R_{P/F}')
	trs[eta].GetYaxis().SetTitleOffset(0.8)
	trs[eta].SetMaximum(0.2)
	trs[eta].SetMinimum(0.0)
	trs[eta].GetXaxis().SetRangeUser(1000,4000)
	trs[eta].SetStats(0)
	c4.cd()

	trs[eta].Draw("histe")

	graphBP[eta].Draw("same")
	graphBPerrh[eta].Draw("same")
	graphBPerrl[eta].Draw("same")

	c4.RedrawAxis()
	c4.Print('plots/'+options.cuts+'/tagrateeta'+str(eta+1)+options.set+'fitBP'+options.rate+'.root', 'root')
	c4.Print('plots/'+options.cuts+'/tagrateeta'+str(eta+1)+options.set+'fitBP'+options.rate+'.pdf', 'pdf')
	c4.Print('plots/'+options.cuts+'/tagrateeta'+str(eta+1)+options.set+'fitBP'+options.rate+'.png', 'png')

	for ifit in range(0,len(fits)):
		trs[eta].SetTitle(';M_{tW} (GeV);R_{P/F}')
		trs[eta].GetYaxis().SetTitleOffset(0.8)
		trs[eta].SetMaximum(0.2)
		trs[eta].SetMinimum(0.0)
		trs[eta].GetXaxis().SetRangeUser(1000,4000)
		trs[eta].SetStats(0)
		trs[eta].Draw("histe")
		graphs[eta][ifit].Draw('same')

		c4.RedrawAxis()
		c4.Print('plots/tagrateeta'+str(eta+1)+fittitles[ifit]+options.set+'PSET_'+options.cuts+options.rate+'.root', 'root')
		c4.Print('plots/tagrateeta'+str(eta+1)+fittitles[ifit]+options.set+'PSET_'+options.cuts+options.rate+'.pdf', 'pdf')

	

tagrates.Close()

