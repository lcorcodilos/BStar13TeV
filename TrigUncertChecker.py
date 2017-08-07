import ROOT
from ROOT import *

myFile = TFile("TWanalyzerttbar_Trigger_nominal_none_job1of5_PSET_default.root",'open')

n = myFile.Get('Mtw')
u = myFile.Get('Mtwtrigup')
d = myFile.Get('Mtwtrigdown')
n.Rebin(4)
u.Rebin(4)
d.Rebin(4)
c = TCanvas('c','c',700,700)
u.SetLineColor(kRed)
d.SetLineColor(kBlue)
n.SetLineColor(kBlack)
u.Draw("hist")
d.Draw("samehist")
n.Draw("samehist")

raw_input("holding")