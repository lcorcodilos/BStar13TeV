import ROOT
from ROOT import *

oldFile = TFile('~/Desktop/Temp/PileUp_Ratio_ttbar.root')
newFile = TFile('../PileUp_Ratio_ttbar.root')

oldRatio = oldFile.Get('Pileup_Ratio')
newRatio = newFile.Get('Pileup_Ratio')

for ibin in range(1,oldRatio.GetNbinsX()+1):
	if oldRatio.GetBinContent(ibin) != newRatio.GetBinContent(ibin):
		print "For bin " + str(ibin) + ': ' + str(newRatio.GetBinContent(ibin)/oldRatio.GetBinContent(ibin))