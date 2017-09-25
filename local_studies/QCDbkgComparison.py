import ROOT
from ROOT import *

# doubleTTsub = TFile('/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/BStar13TeV/rootfiles/35851pb_doubleTTsub/TWanalyzerdata_Trigger_nominal_none_PSET_sideband1.root','open')
# noTTsub = TFile('/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/BStar13TeV/rootfiles/35851pb_noTTsub/TWanalyzerdata_Trigger_nominal_none_PSET_sideband1.root','open')

doubleTTsub = TFile('../rootfiles/35851pb_doubleTTsub/TWanalyzerdata_Trigger_nominal_none_PSET_sideband1.root','open')
noTTsub = TFile('../rootfiles/35851pb_noTTsub/TWanalyzerdata_Trigger_nominal_none_PSET_sideband1.root','open')

c = TCanvas('c','c',800,700)
c.cd()

QCDdoubleTTsub = doubleTTsub.Get('QCDbkg')
QCDnoTTsub = noTTsub.Get('QCDbkg')

QCDdoubleTTsub.SetMarkerColor(kRed)
QCDnoTTsub.SetMarkerColor(kBlue)

leg = TLegend(0.6,0.7,0.95,0.95)
leg.AddEntry(QCDnoTTsub,'QCD bkg - no ttbar subtraction')
leg.AddEntry(QCDdoubleTTsub, 'QCD bkg - double ttbar subtraction')

QCDnoTTsub.Draw('')
QCDdoubleTTsub.Draw('same')
leg.Draw()

c.Print('plots/QCDbkgComparison.pdf','pdf')
