import ROOT
from ROOT import *

gStyle.SetOptStat(0)

fttbar = TFile('TWPileupttbar.root','open')
fsignalRH1200 = TFile('TWPileupsignalRH1200.root','open')
fsignalRH2000 = TFile('TWPileupsignalRH2000.root','open')
fsignalRH2800 = TFile('TWPileupsignalRH2800.root','open')
fratio = TFile('PileUp_Ratio_ttbar.root','open')

httbar = fttbar.Get('npvhistUW')
hSR1200 = fsignalRH1200.Get('npvhistUW')
hSR2000 = fsignalRH2000.Get('npvhistUW')
hSR2800 = fsignalRH2800.Get('npvhistUW')

httbar.Scale(1/httbar.Integral())
hSR1200.Scale(1/hSR1200.Integral())
hSR2000.Scale(1/hSR2000.Integral())
hSR2800.Scale(1/hSR2800.Integral())

print httbar.Integral()

hratio = fratio.Get('Pileup_Ratio')

c1 = TCanvas('c1','c1',700,700)
c1.cd()

leg1 = TLegend(0.7,0.7,0.93,0.9)

httbarW = httbar.Clone('ttbarW')
httbarW.Multiply(hratio)
httbarW.SetLineColor(kBlack)
httbarW.SetTitle('')
httbarW.GetXaxis().SetTitle('NPV')
httbarW.GetYaxis().SetTitle('Fraction')

leg1.AddEntry(httbarW, 'Weighted ttbar MC', 'L')
leg1.AddEntry(httbar, 'Unweighted ttbar MC', 'L')

httbarW.Draw('samehistE')

httbar.SetLineColor(kRed)
httbar.Draw('samehistE')

leg1.Draw()

c2 = TCanvas('c2','c2',700,700)
c2.cd()

leg2 = TLegend(0.7,0.7,0.93,0.9)

hSR1200W = hSR1200.Clone('SR1200W')
hSR1200W.Multiply(hratio)
hSR1200W.SetLineColor(kBlack)
hSR1200W.SetTitle('')
hSR1200W.GetXaxis().SetTitle('NPV')
hSR1200W.GetYaxis().SetTitle('Fraction')

leg2.AddEntry(hSR1200W, 'Weighted SR1200 MC', 'L')
leg2.AddEntry(hSR1200, 'Unweighted SR1200 MC', 'L')

hSR1200W.Draw('samehistE')

hSR1200.SetLineColor(kRed)
hSR1200.Draw('samehistE')

leg2.Draw()

c3 = TCanvas('c3','c3',700,700)
c3.cd()

leg3 = TLegend(0.7,0.7,0.93,0.9)

hSR2000W = hSR2000.Clone('SR2000W')
hSR2000W.Multiply(hratio)
hSR2000W.SetLineColor(kBlack)
hSR2000W.SetTitle('')
hSR2000W.GetXaxis().SetTitle('NPV')
hSR2000W.GetYaxis().SetTitle('Fraction')

leg3.AddEntry(hSR2000W, 'Weighted SR2000 MC', 'L')
leg3.AddEntry(hSR2000, 'Unweighted SR2000 MC', 'L')

hSR2000W.Draw('samehistE')

hSR2000.SetLineColor(kRed)
hSR2000.Draw('samehistE')

leg3.Draw()

c4 = TCanvas('c4','c4',700,700)
c4.cd()

leg4 = TLegend(0.7,0.7,0.93,0.9)

hSR2800W = hSR2800.Clone('SR2800W')
hSR2800W.Multiply(hratio)
hSR2800W.SetLineColor(kBlack)
hSR2800W.SetTitle('')
hSR2800W.GetXaxis().SetTitle('NPV')
hSR2800W.GetYaxis().SetTitle('Fraction')

leg4.AddEntry(hSR2800W, 'Weighted SR2800 MC', 'L')
leg4.AddEntry(hSR2800, 'Unweighted SR2800 MC', 'L')

hSR2800W.Draw('samehistE')

hSR2800.SetLineColor(kRed)
hSR2800.Draw('samehistE')

leg4.Draw()

raw_input('holding')

c1.Print('PileupCorrection_ttbar.png','png')
c2.Print('PileupCorrection_signalRH1200.png','png')
c3.Print('PileupCorrection_signalRH2000.png','png')
c4.Print('PileupCorrection_signalRH2800.png','png')
