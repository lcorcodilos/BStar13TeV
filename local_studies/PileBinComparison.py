import ROOT
from ROOT import *

ttbarFile = TFile('../TTrees/TWtreefile_ttbar_Trigger_nominal_none.root','open')
QCDFile = TFile('../TTrees/TWtreefile_QCD_Trigger_nominal_none.root')

ttbarTree = ttbarFile.Get('Tree')
QCDTree = QCDFile.Get('Tree')

ttbarTree.Draw("pileBin>>ttbarHist","","goff");
QCDTree.Draw("pileBin>>QCDHist",'',"goff");

ttbarHist.SetLineColor(kRed)

ttbarHist.Scale(1/ttbarHist.Integral())
QCDHist.Scale(1/QCDHist.Integral())

c = TCanvas('c','c',700,700)

hs = THStack('hs','hs')
hs.Add(ttbarHist);
hs.Add(QCDHist);
hs.Draw("nostackhist");

raw_input('waiting')