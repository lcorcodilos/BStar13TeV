import ROOT
from ROOT import *

files = {
"QCD_default": TFile('../rootfiles/35867pb/TWratefileQCD_PSET_default.root'),
"SR1200_default": TFile('../rootfiles/35867pb/TWratefileweightedsignalRH1200_PSET_default.root'),
"SR2000_default": TFile('../rootfiles/35867pb/TWratefileweightedsignalRH2000_PSET_default.root'),
"SR2800_default": TFile('../rootfiles/35867pb/TWratefileweightedsignalRH2800_PSET_default.root'),

"QCD_sideband": TFile('../rootfiles/35867pb/TWratefileQCD_PSET_sideband.root'),
"SR1200_sideband": TFile('../rootfiles/35867pb/TWratefileweightedsignalRH1200_PSET_sideband.root'),
"SR2000_sideband": TFile('../rootfiles/35867pb/TWratefileweightedsignalRH2000_PSET_sideband.root'),
"SR2800_sideband": TFile('../rootfiles/35867pb/TWratefileweightedsignalRH2800_PSET_sideband.root'),

"QCD_rate_default": TFile('../rootfiles/35867pb/TWratefileQCD_PSET_rate_default.root'),
"SR1200_rate_default": TFile('../rootfiles/35867pb/TWratefileweightedsignalRH1200_PSET_rate_default.root'),
"SR2000_rate_default": TFile('../rootfiles/35867pb/TWratefileweightedsignalRH2000_PSET_rate_default.root'),
"SR2800_rate_default": TFile('../rootfiles/35867pb/TWratefileweightedsignalRH2800_PSET_rate_default.root'),

"QCD_rate_sideband": TFile('../rootfiles/35867pb/TWratefileQCD_PSET_rate_sideband.root'),
"SR1200_rate_sideband": TFile('../rootfiles/35867pb/TWratefileweightedsignalRH1200_PSET_rate_sideband.root'),
"SR2000_rate_sideband": TFile('../rootfiles/35867pb/TWratefileweightedsignalRH2000_PSET_rate_sideband.root'),
"SR2800_rate_sideband": TFile('../rootfiles/35867pb/TWratefileweightedsignalRH2800_PSET_rate_sideband.root')
}



for file in sorted(files.keys()):
	hEta1Count = files[file].Get("eta1Count")
	hEta2Count = files[file].Get("eta2Count")

	eta1Count = int(hEta1Count.Integral())
	eta2Count = int(hEta2Count.Integral())

	print file + " eta1: " + str(eta1Count)
	print file + " eta2: " + str(eta2Count)
	try:
		print file + " eta1/eta2 ratio: " + str(float(eta1Count)/float(eta2Count))
	except:
		print file + " eta1/eta2 ratio: division by zero"
	print '\n'
