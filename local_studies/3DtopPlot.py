import ROOT
from ROOT import *

fQCD_sideband = TFile('../rootfiles/35867pb/TWvariablesQCD_Trigger_nominal_none_PSET_sideband.root')
fData_sideband = TFile('../rootfiles/35867pb/TWvariablesdata_Trigger_nominal_none_PSET_sideband.root')
fQCD_default = TFile('../rootfiles/35867pb/TWvariablesQCD_Trigger_nominal_none_PSET_default.root')

hQCD_sideband = fQCD_sideband.Get('MtvPtvTau32')
hData_sideband = fData_sideband.Get('MtvPtvTau32')
hQCD_default = fQCD_default.Get('MtvPtvTau32')

cQCD_sideband = TCanvas('cQCD_sideband', 'QCD MC in sideband', 600, 600)
cData_sideband = TCanvas('cData_sideband', 'Data in sideband', 600, 600)
cQCD_default = TCanvas('cQCD_default', 'QCD MC in signal region', 600, 600)

cQCD_sideband.cd()
hQCD_sideband.Draw("BOX")

cData_sideband.cd()
hData_sideband.Draw("BOX")

cQCD_default.cd()
hQCD_default.Draw('BOX')

cQCD_sideband.Print('plots/MtvPtvTau32_QCD_sideband.png','png')
cData_sideband.Print('plots/MtvPtvTau32_data_sideband.png','png')
cQCD_default.Print('plots/MtvPtvTau32_QCD_default.png','png')