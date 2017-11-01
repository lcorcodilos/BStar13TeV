import ROOT
from ROOT import *

gStyle.SetOptStat(0)

# Create an output file
outfile = TFile('FlavorFraction_WvsTop.root','recreate')
outfile.cd()

# This file does all W space
# Specify which cuts we want to looks at - must have QCD MC minitrees for these
cuts = ['rate_sideband','rate_default','rate_highWmass','sideband','default','highWmass']

# Create the pass cuts
toptag = '((tau32<0.65)&&(sjbtag>0.5426))'
taggingDict = {'pass':toptag}#,'fail':'!'+toptag}

# Loop through the different cuts
for cut in cuts:
	# Need to go into each QCD set 
	for HT in ['500','700','1000','1500','2000']:
		# Open up the file
		htFile = TFile.Open('../rootfiles/35851pb/TWminitree_weightedQCDHT'+HT+'_PSET_'+cut+'.root')
		
		# Get the scale weight
		weightTree = htFile.Get('Weight')
		weightTree.GetEntry(0)

		# Set the weight of 'Tree' as the scale weight
		htTree = htFile.Get('Tree')
		htTree.SetWeight(weightTree.weightv)

		# Split into pass and fail distributions
		for tagging in taggingDict.keys():
			# Book a hist
			tagHist = TH2F('QCDHT'+HT+cut+tagging+'_WvsTop','QCDHT'+HT+cut+tagging+'_WvsTop',22,0,22,22,0,22)
			# Draw onto it
			htTree.Draw('flavor_w:flavor_top>>QCDHT'+HT+cut+tagging+'_WvsTop','weight*('+taggingDict[tagging]+'&&(pt_top<600)&&(pt_top>400))','goff')
			
			# Color the pass and fail differently
			if tagging == 'pass':	
				tagHist.SetLineColor(kRed)
			elif tagging == 'fail':
				tagHist.SetLineColor(kBlue)

			outfile.cd()
			tagHist.Write()

	# Now need to access each HT set and add them together
	outfile.cd()
	totTagHist = TH2F('QCD'+cut+'pass_WvsTop','QCD'+cut+'pass_WvsTop',22,0,22,22,0,22)
	# totAntitagHist = TH2F('QCD'+cut+'fail_WvsTop','QCD'+cut+'fail_WvsTop',22,0,22,22,0,22)

	for HT in ['500','700','1000','1500','2000']:
		totTagHist.Add(outfile.Get('QCDHT'+HT+cut+'pass_WvsTop'))
		# totAntitagHist.Add(outfile.Get('QCDHT'+HT+cut+'fail_WvsTop'))

	totTagHist.Write()
	# totAntitagHist.Write()