import ROOT
from ROOT import *
oldFile = TFile('TWanalyzerweightedsignalLH1200_Trigger_nominal_none_PSET_default.root','open')
newFile = TFile('TWanalyzerweightedsignalLH1200_3p2_Trigger_nominal_none_PSET_default.root','open')
oldPlot = oldFile.Get('Mtw')
newPlot = newFile.Get('Mtw')

for b in range(oldPlot.GetXaxis().GetNbins()):
	oldContent = oldPlot.GetBinContent(b)
	newContent = newPlot.GetBinContent(b)
	if oldContent != newContent:
		print 'Contents dont match at bin ' + str(b)
		print '    2p5 bin value: ' + str(oldContent)
		print '    3p2 bin value: ' + str(newContent)