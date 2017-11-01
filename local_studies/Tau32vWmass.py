#############################################################
# Tau32vWmass.py - Used to plot Tau32 v W mass for QCD MC	#
# after a designated preselection. Uses TWminitrees so 		#
# the built in preselection already includes pt, dy, eta,	#
# dphi, tau21, w mass, and top mass							#
# - LC 10/27/17
#############################################################

import ROOT
from ROOT import *

gStyle.SetOptStat(0)
import FlavorFractionFunctions
from FlavorFractionFunctions import *

from optparse import OptionParser
parser = OptionParser()
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'sideband',
                  dest		=	'cuts',
                  help		=	'sideband or default')
parser.add_option('-b', '--sjbtag', metavar='F', type='string', action='store',
                  default	=	'on',
                  dest		=	'sjbtag',
                  help		=	'on or off') # Doesn't matter whether sjbtag is marked as part of preselection or not
(options, args) = parser.parse_args()


# Initialize output file
outfile = TFile('Tau32vWmass_.root','recreate')

# Determine whether we cut sjbtag
sjbtag = '(sjbtag>0.5426)'
taggingDict = {'_sjbtag_on':sjbtag,'_sjbtag_off':'!'+sjbtag}

for band in ['rate_sideband','sideband','rate_default','default']:
	# Need to go into each QCD set 
	for HT in ['500','700','1000','1500','2000']:
		# Open up the file
		htFile = TFile.Open('../rootfiles/35851pb/TWratefileweightedQCDHT'+HT+'_PSET_'+band+'.root')
		
		# Get the scale weight
		weightTree = htFile.Get('Weight')
		weightTree.GetEntry(0)

		# Set the weight of 'Tree' as the scale weight
		htTree = htFile.Get('Tree')
		htTree.SetWeight(weightTree.weightv)

		# Split into pass and fail distributions
		for tagging in taggingDict.keys():
			# Book a hist
			tagHist = TH2F('QCDHT'+HT+band+tagging+'_Tau32vWmass','QCDHT'+HT+band+tagging+'_Tau32vWmass',15,30,105,10,0,1)
			# Draw onto it
			htTree.Draw('tau32:wmass>>QCDHT'+HT+band+tagging+'_Tau32vWmass','weight*('+taggingDict[tagging]+')','goff') #
			
			# Color the pass and fail differently
			if tagging == '_sjbtag_on':	
				tagHist.SetLineColor(kRed)
			elif tagging == '_sjbtag_off':
				tagHist.SetLineColor(kBlue)

			outfile.cd()
			tagHist.Write()

	# Now need to access each HT set and add them together
	outfile.cd()
	totOnHist = TH2F('QCD'+band+'_sjbtag_on_Tau32vWmass','QCD'+band+'_sjbtag_on_Tau32vWmass',15,30,105,10,0,1)
	totOffHist = TH2F('QCD'+band+'_sjbtag_off_Tau32vWmass','QCD'+band+'_sjbtag_off_Tau32vWmass',15,30,105,10,0,1)

	for HT in ['500','700','1000','1500','2000']:
		totOnHist.Add(outfile.Get('QCDHT'+HT+band+'_sjbtag_on_Tau32vWmass'))
		totOffHist.Add(outfile.Get('QCDHT'+HT+band+'_sjbtag_off_Tau32vWmass'))

	totOnHist.Write()
	totOffHist.Write()


cPlot = TCanvas('Plot','Plot',800,700)
cPlot.SetRightMargin(0.15)

# Grab each of the eight histograms
hOnLow = outfile.Get('QCDsideband_sjbtag_on_Tau32vWmass')
hOffLow = outfile.Get('QCDsideband_sjbtag_off_Tau32vWmass')

hOnHigh = outfile.Get('QCDdefault_sjbtag_on_Tau32vWmass')
hOffHigh = outfile.Get('QCDdefault_sjbtag_off_Tau32vWmass')

hRpfOnLow = outfile.Get('QCDrate_sideband_sjbtag_on_Tau32vWmass')
hRpfOffLow = outfile.Get('QCDrate_sideband_sjbtag_off_Tau32vWmass')

hRpfOnHigh = outfile.Get('QCDrate_default_sjbtag_on_Tau32vWmass')
hRpfOffHigh = outfile.Get('QCDrate_default_sjbtag_off_Tau32vWmass')

# Add the mass regions together
hOn = hOnLow.Clone('QCD_sjbtag_on_Tau32vWmass')
hOff = hOffLow.Clone('QCD_sjbtag_off_Tau32vWmass')
hOn.Add(hOnHigh)
hOff.Add(hOffHigh)

hRpfOn = hRpfOnLow.Clone('QCDrate_sjbtag_on_Tau32vWmass')
hRpfOff = hRpfOffLow.Clone('QCDrate_sjbtag_off_Tau32vWmass')
hRpfOn.Add(hRpfOnHigh)
hRpfOff.Add(hRpfOffHigh)


# Do low Tau21 first
hOn.SetTitle('QCD MC - #tau_{32} v W mass - sjbtag on')
hOn.GetXaxis().SetTitle('W mass (GeV)')
hOn.GetYaxis().SetTitle('#tau_{32}')
hOn.Draw('colz')

cPlot.Print(hOn.GetName()+'.png','png')

hOff.SetTitle('QCD MC - #tau_{32} v W mass - sjbtag off')
hOff.GetXaxis().SetTitle('W mass (GeV)')
hOff.GetYaxis().SetTitle('#tau_{32}')
hOff.Draw('colz')

cPlot.Print(hOff.GetName()+'.png','png')

# Now high Tau21
hRpfOn.SetTitle('QCD MC - Inverted #tau_{21} - #tau_{32} v W mass - sjbtag on')
hRpfOn.GetXaxis().SetTitle('W mass (GeV)')
hRpfOn.GetYaxis().SetTitle('#tau_{32}')
hRpfOn.Draw('colz')

cPlot.Print(hRpfOn.GetName()+'.png','png')

hRpfOff.SetTitle('QCD MC - Inverted #tau_{21} - #tau_{32} v W mass - sjbtag off')
hRpfOff.GetXaxis().SetTitle('W mass (GeV)')
hRpfOff.GetYaxis().SetTitle('#tau_{32}')
hRpfOff.Draw('colz')

cPlot.Print(hRpfOff.GetName()+'.png','png')


outfile.Close()



