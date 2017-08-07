

import os
import array
import glob
import math
import ROOT
import sys
import copy
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
parser.add_option('-s', '--set', metavar='F', type='string', action='store',
                  default	=	'data',
                  dest		=	'set',
                  help		=	'data or QCD')
parser.add_option('-b', '--blind', metavar='F', type='string', action='store',
                  default	=	'True',
                  dest		=	'blind',
                  help		=	'blind')
parser.add_option('--batch', metavar='F', action='store_true',
                  default=False,
                  dest='batch',
                  help='batch')

parser.add_option('-l', '--lumi', metavar='F', type='string', action='store',
                  default	=	'35867pb',
                  dest		=	'lumi',
                  help		=	'Lumi folder to look in')

(options, args) = parser.parse_args()


Lumi = options.lumi

cuts = options.cuts
drawDATA=True
if options.blind== "True" and options.set=="data" and options.cuts=="default":
	drawDATA=False

if options.batch:
	ROOT.gROOT.SetBatch(True)
	ROOT.PyConfig.IgnoreCommandLineOptions = True


import Bstar_Functions	
from Bstar_Functions import *

st1= ROOT.THStack("st1", "st1")

leg = TLegend(0.45, 0.35, 0.84, 0.84)
leg.SetFillColor(0)
leg.SetBorderSize(0)

rebin =4

Mult = 1.0

#Kfac=1.2
arange=4000.0
amin=0.8
#if options.cuts=='default' and options.set=='data':
#	arange=3500.0
#	amin=0.5



sigf = [
ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzerweightedsignalRH1200_Trigger_nominal_none_PSET_"+options.cuts+".root"),
ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzerweightedsignalRH2000_Trigger_nominal_none_PSET_"+options.cuts+".root"),
ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzerweightedsignalRH2800_Trigger_nominal_none_PSET_"+options.cuts+".root")
]

sigh = [
sigf[0].Get("Mtw"),
sigf[1].Get("Mtw"),
sigf[2].Get("Mtw")
]

sigh[0].Rebin(rebin)
sigh[1].Rebin(rebin)
sigh[2].Rebin(rebin)

sigh[0].SetLineStyle(5)
sigh[1].SetLineStyle(6)
sigh[2].SetLineStyle(7)

sigh[0].SetLineWidth(3)
sigh[1].SetLineWidth(3)
sigh[2].SetLineWidth(3)

sigh[0].SetLineColor(1)
sigh[1].SetLineColor(3)
sigh[2].SetLineColor(4)

#STmc 	= ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzerST_Trigger_nominal_none_PSET_"+options.cuts+".root")
TTmc 	= ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_"+options.cuts+".root")
if options.set == 'data':
	setstring = '' 
	print "running on data"
	DataB11 = ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzerdata_Trigger_nominal_none_PSET_"+options.cuts+".root")
	DataFS 	= DataB11.Get("Mtw") 			
	DataBE 	= DataB11.Get("QCDbkg") 		
	datapointcolor = 1	
elif options.set == 'QCD':
	setstring = 'QCD' 
	DataB11 = ROOT.TFile("rootfiles/"+Lumi+"/TWanalyzerQCD_Trigger_nominal_none_PSET_"+options.cuts+".root")
	DataFS 	= DataB11.Get("Mtw") 			
	DataBE 	= DataB11.Get("QCDbkg") 		
	DataFS.Add(TTmc.Get("Mtw")) 
	datapointcolor = 4
else:
	print 'Error: Set selection invalid.'




DataBE2d = DataB11.Get("QCDbkg2D") 

c1 = TCanvas('c1', 'QCD Full selection vs b pt tagging background', 700, 600)



main = ROOT.TPad("main", "main", 0, 0.3, 1, 1)
sub = ROOT.TPad("sub", "sub", 0, 0, 1, 0.3)

main.SetLeftMargin(0.16)
main.SetRightMargin(0.05)
main.SetTopMargin(0.11)
main.SetBottomMargin(0.0)

sub.SetLeftMargin(0.16)
sub.SetRightMargin(0.05)
sub.SetTopMargin(0)
sub.SetBottomMargin(0.3)

main.Draw()
sub.Draw()

main.cd()

output = ROOT.TFile( "TWanalyzer_output_PSET_"+options.cuts+".root", "recreate" )
output.cd()

TTmcFS = TTmc.Get("Mtw")
TTmcBE = TTmc.Get("QCDbkg")
TTmcBE2d = TTmc.Get("QCDbkg2D")
TTmcBEh = TTmc.Get("QCDbkgh")
TTmcBEl = TTmc.Get("QCDbkgl")


DataBEh = DataB11.Get("QCDbkgh")
DataBEl = DataB11.Get("QCDbkgl")

DataBE2d.Rebin(rebin)
TTmcFS.Rebin(rebin)
DataBE.Rebin(rebin)



print DataFS.Integral()
DataFS.Rebin(rebin)

DataBEl.Rebin(rebin)
DataBEh.Rebin(rebin)

TTmcBE.Rebin(rebin)
TTmcBE2d.Rebin(rebin)
TTmcBEh.Rebin(rebin)
TTmcBEl.Rebin(rebin)

unsubbkg = DataBE.Clone()

# Uncomment when using data -JL #
if options.set=='data':
	DataBE.Add(TTmcBE,-1)
	DataBEl.Add(TTmcBE,-1)
	DataBEh.Add(TTmcBE,-1)


output.cd()

DataQCDBEH=DataBE.Clone("DataQCDBEH")
DataQCDBEL=DataBE.Clone("DataQCDBEL")
DataTOTALBEH=DataBE.Clone("DataTOTALBEH")
DataTOTALBEL=DataBE.Clone("DataTOTALBEL")
output.cd()

for ibin in range(0,DataBE.GetNbinsX()+1):


	QCDfit1=abs((DataBEh.GetBinContent(ibin)-DataBEl.GetBinContent(ibin))/2.0)

	print ""
	print ibin

	print QCDfit1/max(DataBE.GetBinContent(ibin),0.001)
	

	QCDsys=QCDfit1
	QCDerror=QCDsys


	TTerrorup=0.
	TTerrordown=0.
	Totalerrorup=QCDerror
	Totalerrordown=QCDerror
	DataQCDBEH.SetBinContent(ibin,DataQCDBEH.GetBinContent(ibin)+QCDerror)
	DataQCDBEL.SetBinContent(ibin,DataQCDBEL.GetBinContent(ibin)-QCDerror)
	DataTOTALBEH.SetBinContent(ibin,DataTOTALBEH.GetBinContent(ibin)+Totalerrorup)
	DataTOTALBEL.SetBinContent(ibin,DataTOTALBEL.GetBinContent(ibin)-Totalerrordown)

print "QCD total error"
print (DataQCDBEH.Integral()-DataBE.Integral())/DataBE.Integral()
print 
DataQCDBEH.Write()
DataQCDBEL.Write()

DataTOTALBEH.Write()
DataTOTALBEL.Write()

DataTOTALBEL.Add(TTmcFS)
DataTOTALBEH.Add(TTmcFS)

#DataTOTALBEL.Add(STmcFS)
#DataTOTALBEH.Add(STmcFS)	


print (DataTOTALBEH.Integral()-DataTOTALBEL.Integral())/DataFS.Integral()	
print "total QCD"
print DataBE.Integral()


DataBE.SetFillColor(kYellow)
TTmcFS.SetFillColor(kRed)
#STmcFS.SetFillColor(6)

DataTOTALBEH.SetLineColor(kBlue)
DataTOTALBEH.SetLineWidth(2)
#DataTOTALBEH.SetLineStyle(2)

centerqcd = DataTOTALBEL.Clone("centerqcd")
centerqcd.SetFillColor(kYellow)
centerqcd.Add(TTmcFS,-1)
#centerqcd.Add(STmcFS,-1)

DataTOTALBEL.SetLineColor(kBlue)
DataTOTALBEL.SetLineWidth(2)
#DataTOTALBEL.SetFillColor(0)
#DataTOTALBEL.SetLineStyle(0)
#DataTOTALBEL.SetLineWidth(2)
#DataTOTALBEL.SetLineStyle(2)

sigst= ROOT.THStack("sigst", "sigst")
sigma = DataTOTALBEH.Clone("sigma")
sigma.SetFillStyle(3245)
sigma.SetFillColor(1)
sigma.SetLineColor(0)
centerqcd.SetLineColor(kYellow)

sigma.Add(DataTOTALBEL,-1)
#sigst.Add(STmcFS)
sigst.Add(TTmcFS)
sigst.Add(centerqcd)
sigst.Add(sigma)

st1.Add(TTmcFS)
st1.Add(DataBE)

bkgline=st1.GetStack().Last().Clone("bkgline")
bkgline.SetFillColor(0)
bkgline.SetFillStyle(0)
DataFS.SetLineColor(datapointcolor)
DataFS.SetMarkerColor(datapointcolor)
#leg.AddEntry( DataFS, 'Data', 'P')
if options.set == 'QCD':
	leg.AddEntry( DataFS, 'QCD FS + t#bar{t}', 'P')
	leg.AddEntry( DataBE, 'QCD Background', 'F')
elif options.set == 'data':
	if drawDATA:	
		leg.AddEntry( DataFS, 'data', 'P')
	leg.AddEntry( DataBE, 'QCD', 'F')
leg.AddEntry( TTmcFS, 't#bar{t}', 'F')

leg.AddEntry( sigma, '1 #sigma background uncertainty', 'F')
leg.AddEntry( sigh[0], 'b* at 1400 GeV', 'L')
leg.AddEntry( sigh[1], 'b* at 2000 GeV', 'L')
leg.AddEntry( sigh[2], 'b* at 2600 GeV', 'L')

#c1.cd()
#c1.SetLeftMargin(0.17)

st1.SetMaximum(DataTOTALBEH.GetMaximum() * 1.3)
st1.SetMinimum(1.0)
st1.SetTitle(';M_{tw} (GeV);Counts per 100 GeV')
st1.Draw("hist")
gPad.SetLeftMargin(.16)
st1.GetYaxis().SetTitleOffset(0.9)
#DataTOTALBEH.Draw("histsame")
#DataTOTALBEL.Draw("histsame")
sigst.Draw("samehist")
bkgline.Draw("samehist")
sigh[0].Draw("samehist")
sigh[1].Draw("samehist")
sigh[2].Draw("samehist")


DataFS1	    = TH1D("DataFS1",     "mass W' in b+1",     	  	      140, 500, 4000 )
DataFS1.Rebin(rebin)
for ibin in range(1,DataFS.GetNbinsX()+1):
	DataFS1.SetBinContent(ibin,DataFS.GetBinContent(ibin))

DataFS1.SetBinErrorOption(DataFS1.kPoisson)
DataFS1 = DataFS
if drawDATA:	
	DataFS1.Draw("samepE")

leg.Draw()
prelim = TLatex()
prelim.SetNDC()


#insertlogo( main, 2, 11 )


#prelim.DrawLatex( 0.5, 0.91, "#scale[0.8]{CMS Preliminary, 13 TeV, 2553 pb^{-1}}" )
#prelim.DrawLatex( 0.2, 0.83, "#scale[0.8]{"+text+"}" )
#insertlogo( main, 4, 11 )
st1.GetXaxis().SetRangeUser(500.0,arange)
sub.cd()
gPad.SetLeftMargin(.16)
totalH = st1.GetStack().Last().Clone("totalH")
#totalH.Add(TTmcFS)
pull = Make_Pull_plot( DataFS1,totalH,DataTOTALBEH,DataTOTALBEL )


	
#pull.GetXaxis().SetRangeUser(0,3000)
pull.SetFillColor(kBlue)
pull.SetTitle(';M_{tw} (GeV);(Data-Bkg)/#sigma')
pull.SetStats(0)


pull.GetYaxis().SetRangeUser(-2.9,2.9)
pull.GetXaxis().SetLabelSize(0.05)
pull.GetYaxis().SetLabelSize(0.05)


LS = .13

pull.GetYaxis().SetTitleOffset(0.4)
pull.GetXaxis().SetTitleOffset(0.9)
pull.SetStats(0)
    

pull.GetYaxis().SetLabelSize(LS)
pull.GetYaxis().SetTitleSize(LS)
pull.GetYaxis().SetNdivisions(306)
pull.GetXaxis().SetLabelSize(LS)
pull.GetXaxis().SetTitleSize(LS)
if drawDATA:	
	pull.Draw("hist")
else:
	pull.Draw("axis")
pull.GetXaxis().SetRangeUser(500.0,arange)

line2=ROOT.TLine(500.0,0.0,arange,0.0)
line2.SetLineColor(0)
line1=ROOT.TLine(500.0,0.0,arange,0.0)
line1.SetLineStyle(2)

line2.Draw()
line1.Draw()
gPad.Update()

main.RedrawAxis()

c1.Print('plots/MtwvsBkg_BifPoly_fit_'+setstring+'PSET_'+options.cuts+'.root', 'root')
c1.Print('plots/MtwvsBkg_BifPoly_fit_'+setstring+'PSET_'+options.cuts+'.pdf', 'pdf')
c1.Print('plots/MtwvsBkg_BifPoly_fit_'+setstring+'PSET_'+options.cuts+'.png', 'png')
main.SetLogy()
st1.SetMaximum( DataBEh.GetMaximum() * 50000 )
st1.SetMinimum( amin)
main.RedrawAxis()

c1.Print('plots/MtwvsBkgsemilog_BifPoly_fit_'+setstring+'PSET_'+options.cuts+'.root', 'root')
c1.Print('plots/MtwvsBkgsemilog_BifPoly_fit_'+setstring+'PSET_'+options.cuts+'.pdf', 'pdf')
c1.Print('plots/MtwvsBkgsemilog_BifPoly_fit_'+setstring+'PSET_'+options.cuts+'.png', 'png')

