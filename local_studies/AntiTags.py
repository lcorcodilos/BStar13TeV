import ROOT
from ROOT import *

lowWmass = TFile('../rootfiles/35867pb/TWanalyzerQCD_Trigger_nominal_none_PSET_lowWmass.root')
highWmass = TFile('../rootfiles/35867pb/TWanalyzerQCD_Trigger_nominal_none_PSET_highWmass.root')
avg = TFile('../rootfiles/35867pb/TWanalyzerQCD_Trigger_nominal_none_PSET_default.root')


antiTag_noPF = avg.Get("preAntiTag")
antiTag_lowWmass = lowWmass.Get("QCDbkg")
antiTag_highWmass = highWmass.Get("QCDbkg")
antiTag_avg = avg.Get("QCDbkg")

c1 = TCanvas("c1", "c1", 600, 600)
c1.SetBottomMargin(0.15)
c1.SetLeftMargin(0.15)
gStyle.SetOptStat(0)

antiTag_noPF.Rebin(5)
antiTag_lowWmass.Rebin(5)
antiTag_highWmass.Rebin(5)
antiTag_avg.Rebin(5)

antiTag_noPF.SetLineColor(kGreen)
antiTag_lowWmass.SetLineColor(kBlue)
antiTag_highWmass.SetLineColor(kRed)
antiTag_avg.SetLineColor(kBlack)

antiTag_noPF.SetTitle("Antitag M_{tW} distributions")
antiTag_noPF.GetXaxis().SetTitle("M_{tW}")

antiTag_noPF.Draw("HIST")
antiTag_lowWmass.Draw("HIST SAME")
antiTag_highWmass.Draw("SAME HIST")
antiTag_avg.Draw("SAME HIST")

c1.Print("AntiTags.png","png")
c1.Close()

c1 = TCanvas("c1", "c1", 600, 600)
c1.SetBottomMargin(0.15)
c1.SetLeftMargin(0.15)
gStyle.SetOptStat(0)

antiTag_lowWmass.SetTitle("Antitag M_{tW} distributions")
antiTag_lowWmass.GetXaxis().SetTitle("M_{tW}")

antiTag_lowWmass.Draw("HIST SAME")
antiTag_highWmass.Draw("SAME HIST")
antiTag_avg.Draw("SAME HIST")

c1.Print("AntiTags2.png","png")
c1.Close()
lowWmass.Close()
highWmass.Close()
avg.Close()