import ROOT
from ROOT import *

myFile = TFile('../limitsetting/theta/BStarCombination/allhadronicleft35851pb_mtw.root')

SR2800 = myFile.Get('mtw_allhad__bs2800')
SR2800up = myFile.Get('mtw_allhad__bs2800__pdf__plus')
SR2800down = myFile.Get('mtw_allhad__bs2800__pdf__minus')

c = TCanvas('c','c',700,700)

SR2800.SetLineColor(kBlack)
SR2800up.SetLineColor(kRed)
SR2800down.SetLineColor(kBlue)


SR2800up.Draw('hist')
SR2800.Draw('samehist')
SR2800down.Draw('samehist')

raw_input('waiting')