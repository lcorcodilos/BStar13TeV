
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
parser.add_option('-e', '--eta', metavar='F', type='string', action='store',
                  default	=	'full',
                  dest		=	'eta',
                  help		=	'full or split')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'rate_default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-p', '--printCanvas', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'printCanvas',
				  help		=	'on or off')
(options, args) = parser.parse_args()

if options.printCanvas == 'off':
	ROOT.gROOT.SetBatch(True)
	ROOT.PyConfig.IgnoreCommandLineOptions = True


rootdir="rootfiles/"
import Bstar_Functions	
from Bstar_Functions import *

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

Rpf = Alpha_Init(options.eta, options.cuts, options.set,'')
Rpf_errup = Alpha_Init(options.eta+'_errup', options.cuts, options.set,'')
Rpf_errdown = Alpha_Init(options.eta+'_errdown', options.cuts, options.set,'')


leg1 = TLegend(0.45,0.57,.84,.78)
leg1.SetFillColor(0)
leg1.SetBorderSize(0)

leg2 = TLegend(0.,0.,1.,1.)
leg2.SetFillColor(0)
leg2.SetBorderSize(0)

#output = ROOT.TFile( "fitting.root", "recreate" )
#output.cd()
c1 = TCanvas('c1', 'Tagrate numerator and deominator', 1500, 1000)
c4 = TCanvas('c4', 'Pt fitted tagrate in 0.0 < Eta <0.8', 800, 500)
c7 = TCanvas('c7', 'tagged vs signal', 800, 500)
c8 = TCanvas('c8', 'tagged vs signal', 800, 500)

cleg = TCanvas('cleg', 'tagged vs signal', 400, 600)

stack1 = THStack("typeb1probeseta1", "; Failed t-tagged Jet p_{T} (GeV); Events / 50(GeV)")
stack2 = THStack("typeb1probeseta2", "; Failed t-tagged Jet p_{T} (GeV); Events / 50(GeV)")

stack4 = THStack("typeb1tagseta1", "; Passed t-tagged Jet p_{T} (GeV); Events / 50(GeV)")
stack5 = THStack("typeb1tagseta2", "; Passed t-tagged Jet p_{T} (GeV); Events / 50(GeV)")

tagrates = ROOT.TFile("plots/TWrate_Maker_"+setstr+"_"+Lumi+"_PSET_"+options.cuts+".root")

ratedata = TFile(rootdir+Lumi+"/TWratefile"+options.set+"_PSET_"+options.cuts+".root")

ratettbar = TFile(rootdir+Lumi+"/TWratefileweightedttbar_PSET_"+options.cuts+".root")
ratest = TFile(rootdir+Lumi+"/TWratefilesingletop_PSET_"+options.cuts+".root")

probeeta1data=ratedata.Get("pteta1pretag")
probeeta2data=ratedata.Get("pteta2pretag")

tageta1data=ratedata.Get("pteta1")
tageta2data=ratedata.Get("pteta2")

probeeta1mc=ratettbar.Get("pteta1pretag")
probeeta2mc=ratettbar.Get("pteta2pretag")

tageta1mc=ratettbar.Get("pteta1")
tageta2mc=ratettbar.Get("pteta2")


probeeta1st=ratest.Get("pteta1pretag")
probeeta2st=ratest.Get("pteta2pretag")

tageta1st=ratest.Get("pteta1")
tageta2st=ratest.Get("pteta2")

ptrebin = 10

probeeta1data.Rebin(ptrebin)
probeeta2data.Rebin(ptrebin)

tageta1data.Rebin(ptrebin)
tageta2data.Rebin(ptrebin)

probeeta1mc.Rebin(ptrebin)
probeeta2mc.Rebin(ptrebin)

tageta1mc.Rebin(ptrebin)
tageta2mc.Rebin(ptrebin)



probeeta1st.Rebin(ptrebin)
probeeta2st.Rebin(ptrebin)

tageta1st.Rebin(ptrebin)
tageta2st.Rebin(ptrebin)



probeeta1data.SetFillColor( kYellow )
probeeta2data.SetFillColor( kYellow )

tageta1data.SetFillColor( kYellow )
tageta2data.SetFillColor( kYellow )

probeeta1mc.SetFillColor( kRed )
probeeta2mc.SetFillColor( kRed )

tageta1mc.SetFillColor( kRed )
tageta2mc.SetFillColor( kRed )

probeeta1st.SetFillColor( 4 )
probeeta2st.SetFillColor( 4 )

tageta1st.SetFillColor( 4 )
tageta2st.SetFillColor( 4 )

#treta1= tagrates.Get("tagrateeta1")
#treta2= tagrates.Get("tagrateeta2")
#treta3= tagrates.Get("tagrateeta3")

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
for j in range(0,2000):

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


c1.cd()
prelim = ROOT.TLatex()
prelim.SetTextFont(42)
prelim.SetNDC()

chis = ROOT.TLatex()
chis.SetTextFont(42)
chis.SetNDC()

OFF = 1.1

SigFiles = [
#ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalLH1200_PSET_"+options.cuts+".root"),
ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalRH1200_PSET_"+options.cuts+".root"),
#ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalLH1400_PSET_"+options.cuts+".root"),
ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalRH1400_PSET_"+options.cuts+".root"),
#ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalLH1600_PSET_"+options.cuts+".root"),
ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalRH1600_PSET_"+options.cuts+".root"),
#ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalLH1800_PSET_"+options.cuts+".root"),
ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalRH1800_PSET_"+options.cuts+".root"),
#ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalLH2000_PSET_"+options.cuts+".root"),
ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalRH2000_PSET_"+options.cuts+".root"),
#ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalLH2200_PSET_"+options.cuts+".root"),
ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalRH2200_PSET_"+options.cuts+".root"),
#ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalLH2400_PSET_"+options.cuts+".root"),
ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalRH2400_PSET_"+options.cuts+".root"),
#ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalLH2600_PSET_"+options.cuts+".root"),
ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalRH2600_PSET_"+options.cuts+".root"),
#ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalLH2800_PSET_"+options.cuts+".root"),
ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalRH2800_PSET_"+options.cuts+".root"),
#ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalLH3000_PSET_"+options.cuts+".root"),
ROOT.TFile(rootdir+Lumi+"/TWratefileweightedsignalRH3000_PSET_"+options.cuts+".root")
]


c1.Divide(2,2)
c1.cd(3)

# ttbar subtraction
if options.set=='data':
	probeeta1data.Add(probeeta1mc,-1)
	probeeta2data.Add(probeeta2mc,-1)
	tageta1data.Add(tageta1mc,-1)
	tageta2data.Add(tageta2mc,-1)

	probeeta1data.Add(probeeta1st,-1)
	probeeta2data.Add(probeeta2st,-1)
	tageta1data.Add(tageta1st,-1)
	tageta2data.Add(tageta2st,-1)


gPad.SetLeftMargin(0.16)

# Numerator and denominator plots
stack1.Add( probeeta1st, "Hist" )
stack1.Add( probeeta1mc, "Hist" )
stack1.Add( probeeta1data, "Hist" )
stack1.SetMaximum(stack1.GetMaximum() * 1.2 )
stack1.Draw()
stack1.GetYaxis().SetTitleOffset(OFF)
stack1.GetXaxis().SetRangeUser(400,1200)
prelim.DrawLatex( 0.25, 0.91, "#scale[1.0]{CMS Preliminary #sqrt{s} = 13 TeV   (0.00 < |#eta| < 0.80) }" )
c1.cd(4)
gPad.SetLeftMargin(0.16)


stack2.Add( probeeta2st, "Hist" )
stack2.Add( probeeta2mc, "Hist" )
stack2.Add( probeeta2data, "Hist" )
stack2.SetMaximum(stack2.GetMaximum() * 1.2 )
stack2.Draw()
stack2.GetYaxis().SetTitleOffset(OFF)
stack2.GetXaxis().SetRangeUser(400,1200)
prelim.DrawLatex( 0.25, 0.91, "#scale[1.0]{CMS Preliminary #sqrt{s} = 13 TeV   (0.80 < |#eta| < 2.40) }" )
c1.cd(1)
gPad.SetLeftMargin(0.16)


stack4.Add( tageta1st, "Hist" )
stack4.Add( tageta1mc, "Hist" )
stack4.Add( tageta1data, "Hist" )
stack4.SetMaximum(stack4.GetMaximum() * 1.2 )
stack4.Draw()
stack4.GetYaxis().SetTitleOffset(OFF)
stack4.GetXaxis().SetRangeUser(400,1200)
prelim.DrawLatex( 0.25, 0.91, "#scale[1.0]{CMS Preliminary #sqrt{s} = 13 TeV   (0.00 < |#eta| < 0.80) }" )
c1.cd(2)
gPad.SetLeftMargin(0.16)

stack5.Add( tageta2st, "Hist" )
stack5.Add( tageta2mc, "Hist" )
stack5.Add( tageta2data, "Hist" )
stack5.SetMaximum(stack5.GetMaximum() * 1.2 )
stack5.Draw()
stack5.GetYaxis().SetTitleOffset(OFF)
stack5.GetXaxis().SetRangeUser(400,1200)
prelim.DrawLatex( 0.25, 0.91, "#scale[1.0]{CMS Preliminary #sqrt{s} = 13 TeV   (0.80 < |#eta| < 2.40) }" )
# c1.cd(6)
gPad.SetLeftMargin(0.16)

c1.Print("plots/"+options.cuts+"/N-Dtagrates.pdf",'pdf')
c1.Print("plots/"+options.cuts+"/N-Dtagrates.png",'png')
c1.Print("plots/"+options.cuts+"/N-Dtagrates.root",'root')



c7.cd()
stack4.SetMinimum(0.001)
prelim.DrawLatex( 0.15, 0.91, "#scale[1.0]{CMS Preliminary #sqrt{s} = 13 TeV   (0.00 < |#eta| < 0.80) }" )
stack4.Draw()
stack4.GetYaxis().SetTitleOffset(0.8)
c8.cd()
stack5.SetMinimum(0.001)
prelim.DrawLatex( 0.15, 0.91, "#scale[1.0]{CMS Preliminary #sqrt{s} = 13 TeV   (0.80 < |#eta| < 2.40) }" )
stack5.Draw()
stack5.GetYaxis().SetTitleOffset(0.8)


leg2.AddEntry(probeeta1data,"QCD","f")
leg2.AddEntry(probeeta1mc,"ttbar","f")
leg2.AddEntry(probeeta1mc,"singletop","f")


mass = [1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]
for ifile in range(0,len(SigFiles)):
	if ifile<4:
		colorassn = ifile+1
	else:
		colorassn = ifile+2
		
	nseta1 = SigFiles[ifile].Get("pteta1")
	nseta2 = SigFiles[ifile].Get("pteta2")
	nseta1.SetLineColor(colorassn)
	nseta2.SetLineColor(colorassn)
	nseta1.Rebin(ptrebin)
	nseta2.Rebin(ptrebin)

	c7.cd()
	nseta1.Draw("samehist")
	c8.cd()
	nseta2.Draw("samehist")
	leg2.AddEntry(nseta1,"signal at "+str(mass[ifile])+"GeV","l")
c7.SetLogy()
c8.SetLogy()

c7.cd()
prelim.DrawLatex( 0.15, 0.91, "#scale[1.0]{CMS Preliminary #sqrt{s} = 13 TeV   (0.00 < |#eta| < 0.80)  }" )
leg2.Draw()
c8.cd()
prelim.DrawLatex( 0.15, 0.91, "#scale[1.0]{CMS Preliminary #sqrt{s} = 13 TeV   (0.80 < |#eta| < 2.40) }" )
leg2.Draw()


cleg.cd()
leg2.Draw()
cleg.Print('plots/legend.pdf', 'pdf')
c7.RedrawAxis()
c8.RedrawAxis()

c7.Print('plots/'+options.cuts+'/sigvsTR'+options.set+'eta1.root', 'root')
c7.Print('plots/'+options.cuts+'/sigvsTR'+options.set+'eta1.pdf', 'pdf')
c8.Print('plots/'+options.cuts+'/sigvsTR'+options.set+'eta2.root', 'root')
c8.Print('plots/'+options.cuts+'/sigvsTR'+options.set+'eta2.pdf', 'pdf')


trs = [None]*3

trs[0]= tagrates.Get("tagrateeta1")
trs[1]= tagrates.Get("tagrateeta2")

c4.cd()
c4.SetLeftMargin(0.16)

etastring = [
'0.00 < |#eta| < 0.80',
'0.80 < |#eta| < 2.40'
]

if options.set == 'data':
	plotTitle1 = 'Data'
elif options.set == 'QCD':
	plotTitle1 = 'QCD MC'
if options.cuts == 'rate_default':
	plotTitle2 = 'Signal Region'
elif options.cuts == 'rate_sideband':
	plotTitle2 = 'Sideband Region'
elif options.cuts == 'rate_sideband1':
	plotTitle2 = 'High W Mass Region'

for eta in range(0,2):
	print eta
	if eta == 0:
		etaRegion = 'Low Eta'
	elif eta == 1:
		etaRegion = 'High Eta'
	trs[eta].SetTitle('Derived from ' + plotTitle1 + ' - Applied to ' + plotTitle2 + ' - ' + etaRegion)
	trs[eta].GetXaxis().SetTitle('p_{T} (GeV)')
	trs[eta].GetYaxis().SetTitle('R_{P/F}')
	trs[eta].GetYaxis().SetTitleOffset(0.8)
	trs[eta].SetMaximum(0.20)
	trs[eta].SetMinimum(0.0)
	trs[eta].GetXaxis().SetRangeUser(400,1200)
	trs[eta].SetStats(0)
	c4.cd()

	trs[eta].Draw("histe")

	graphBP[eta].Draw("same")
	graphBPerrh[eta].Draw("same")
	graphBPerrl[eta].Draw("same")
	#mg[eta].Draw("same")

	#leg1.Draw()
	#prelim = ROOT.TLatex()
	#prelim.SetTextFont(42)
	#prelim.SetNDC()

	#prelim.DrawLatex( 0.2, 0.5, "#scale[1.0]{"+etastring[eta]+"}" )
	#insertlogo( c4, 2, 11 )
	#chis.DrawLatex( 0.20, 0.6, "#scale[1.0]{#chi^{2} / dof = "+strf(chi2eta1/ndofeta1)+"}" )
	c4.RedrawAxis()
	c4.Print('plots/'+options.cuts+'/tagrateeta'+str(eta+1)+options.set+'fitBP.root', 'root')
	c4.Print('plots/'+options.cuts+'/tagrateeta'+str(eta+1)+options.set+'fitBP.pdf', 'pdf')
	c4.Print('plots/'+options.cuts+'/tagrateeta'+str(eta+1)+options.set+'fitBP.png', 'png')

	for ifit in range(0,len(fits)):
		trs[eta].SetTitle(';p_{T} (GeV);R_{P/F}')
		trs[eta].GetYaxis().SetTitleOffset(0.8)
		trs[eta].SetMaximum(0.20)
		trs[eta].SetMinimum(0.0)
		trs[eta].GetXaxis().SetRangeUser(400,1200)
		trs[eta].SetStats(0)
		trs[eta].Draw("histe")
		graphs[eta][ifit].Draw('same')

		c4.RedrawAxis()
		c4.Print('plots/tagrateeta'+str(eta+1)+fittitles[ifit]+options.set+'PSET_'+options.cuts+'.root', 'root')
		c4.Print('plots/tagrateeta'+str(eta+1)+fittitles[ifit]+options.set+'PSET_'+options.cuts+'.pdf', 'pdf')

	

tagrates.Close()
ratedata.Close()
ratettbar.Close()
#tagrateswsig.Close()
SigFiles[0].Close()
SigFiles[1].Close()
#SigFiles[2].Close()
