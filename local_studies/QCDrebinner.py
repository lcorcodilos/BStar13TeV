import ROOT
from ROOT import *

myFile = TFile('../rootfiles/35851pb/TWanalyzerQCD_Trigger_nominal_none_PSET_default.root')
myPlot = myFile.Get('Mtw')

myPlot.Rebin(5)

c = TCanvas('c','c',700,700)

myPlot.Draw('pE')

raw_input('waiting')