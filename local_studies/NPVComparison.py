import ROOT
from ROOT import *

gStyle.SetOptStat(0)

fdata = TFile("../THBnpvtesterdata.root",'open')
fttbar = TFile("../THBnpvtesterttbar.root",'open')
fQCD = TFile("../THBnpvtesterQCD.root",'open')

# Grab the histograms
DataReco = fdata.Get('reconpvhistpost')

QCDRecoPre = fQCD.Get('reconpvhistpre')
QCDRecoPost = fQCD.Get('reconpvhistpost')
QCDTruePre = fQCD.Get('truenpvhistpre')
QCDTruePost = fQCD.Get('truenpvhistpost')

TTRecoPre = fttbar.Get('reconpvhistpre')
TTRecoPost = fttbar.Get('reconpvhistpost')
TTTruePre = fttbar.Get('truenpvhistpre')
TTTruePost = fttbar.Get('truenpvhistpost')

# Normalize them
DataReco.Scale(1/DataReco.Integral())

QCDRecoPre.Scale(1/QCDRecoPre.Integral())
QCDRecoPost.Scale(1/QCDRecoPost.Integral())
QCDTruePre.Scale(1/QCDTruePre.Integral())
QCDTruePost.Scale(1/QCDTruePost.Integral())

TTRecoPre.Scale(1/TTRecoPre.Integral())
TTRecoPost.Scale(1/TTRecoPost.Integral())
TTTruePre.Scale(1/TTTruePre.Integral())
TTTruePost.Scale(1/TTTruePost.Integral())


# Create some canvases
cDataVsQCDVsTTreco = TCanvas('cDataVsQCDVsTTreco')
cDataVsQCDVsTTtrue = TCanvas('cDataVsQCDVsTTtrue')
cDataVsQCDVsTTrecopre = TCanvas('cDataVsQCDVsTTrecopre')
cDataVsQCDVsTTtruepre = TCanvas('cDataVsQCDVsTTtruepre')



# ----------- Reco Post ------------------------------
cDataVsQCDVsTTreco.cd()
TTRecoPost.SetMarkerColor(kRed)
QCDRecoPost.SetMarkerColor(kBlue)

QCDRecoPost.Draw('pE')
TTRecoPost.Draw('samepE')
DataReco.Draw('samepE')

# Make a legend
legend = TLegend(0.6,0.7,0.95,0.95)
legend.AddEntry(DataReco, 'Data Reco NPV', 'p')
legend.AddEntry(QCDRecoPost, 'QCD Reco NPV Post-Weight', 'p')
legend.AddEntry(TTRecoPost, 'TT Reco NPV Post-Weight', 'p')
legend.Draw()

cDataVsQCDVsTTreco.Print('PileupPlots/DataVsQCDVsTTreco.png','png')
# ------------ True Post -----------------------------
cDataVsQCDVsTTtrue.cd()
TTTruePost.SetMarkerColor(kRed)
QCDTruePost.SetMarkerColor(kBlue)

QCDTruePost.Draw('pE')
TTTruePost.Draw('samepE')
DataReco.Draw('samepE')

# Make a legend
legend = TLegend(0.6,0.7,0.95,0.95)
legend.AddEntry(DataReco, 'Data Reco NPV', 'p')
legend.AddEntry(QCDTruePost, 'QCD True NPV Post-Weight', 'p')
legend.AddEntry(TTTruePost, 'TT True NPV Post-Weight', 'p')
legend.Draw()

cDataVsQCDVsTTtrue.Print('PileupPlots/DataVsQCDVsTTtrue.png','png')
# ------------ Reco Pre -----------------------------
cDataVsQCDVsTTrecopre.cd()
TTRecoPre.SetMarkerColor(kRed)
QCDRecoPre.SetMarkerColor(kBlue)

TTRecoPre.Draw('pE')
QCDRecoPre.Draw('samepE')
DataReco.Draw('samepE')

# Make a legend
legend = TLegend(0.6,0.7,0.95,0.95)
legend.AddEntry(DataReco, 'Data Reco NPV', 'p')
legend.AddEntry(QCDRecoPre, 'QCD Reco NPV Pre-Weight', 'p')
legend.AddEntry(TTRecoPre, 'TT Reco NPV Pre-Weight', 'p')
legend.Draw()

cDataVsQCDVsTTrecopre.Print('PileupPlots/DataVsQCDVsTTrecopre.png','png')
# ------------- True Pre ----------------------------
cDataVsQCDVsTTtruepre.cd()
TTTruePre.SetMarkerColor(kRed)
QCDTruePre.SetMarkerColor(kBlue)

DataReco.Draw('pE')
TTTruePre.Draw('samepE')
QCDTruePre.Draw('samepE')


# Make a legend
legend = TLegend(0.6,0.7,0.95,0.95)
legend.AddEntry(DataReco, 'Data Reco NPV', 'p')
legend.AddEntry(QCDTruePre, 'QCD True NPV Pre-Weight', 'p')
legend.AddEntry(TTTruePre, 'TT True NPV Pre-Weight', 'p')
legend.Draw()

cDataVsQCDVsTTtruepre.Print('PileupPlots/DataVsQCDVsTTtruepre.png','png')

