import ROOT
from ROOT import *

PileFile = TFile('../PileUp_Ratio_ttbar.root')
PilePlot = PileFile.Get('Pileup_Ratio')

PilePlot.GetXaxis().SetRange(20,50)

c = TCanvas('c','c',700,700)

PilePlot.Draw('pE')

raw_input('waiting')