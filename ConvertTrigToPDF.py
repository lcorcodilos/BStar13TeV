import ROOT
from ROOT import *

trigFile = TFile('Triggerweight_2jethack_data.root','open')
trigPlot = trigFile.Get('TriggerWeight_HLT_PFHT900ORHLT_PFHT800ORHLT_JET450_pre_HLT_PFHT475')

print "Bin errors: "
for b in range(trigPlot.GetNbinsX()):
	print str(trigPlot.GetBinError(b)) + ', ',

c = TCanvas('c','c',700,700)
c.cd()

trigPlot.Draw('E')

c.Print('TriggerWeight_HLT_PFHT900ORHLT_PFHT800ORHLT_JET450_pre_HLT_PFHT475.pdf','pdf')