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
(options, args) = parser.parse_args()


# Initialize file list
files = []
outfile = TFile('FlavorFraction_QCD.root','recreate')

# Create the pass cuts
toptag = '((tau32<0.65)&&(sjbtag>0.5426))'
taggingDict = {'pass':toptag,'fail':'!'+toptag}

# List of files
fileList = ['../rootfiles/35851pb/TWratefileQCD_PSET_rate_'+options.cuts+'.root',
			'../rootfiles/35851pb/TWratefileQCD_PSET_'+options.cuts+'.root'
			]

histList = []

# Create a list of cuts in same order as files for later reference
cuts = ['rate_'+options.cuts,options.cuts]

iFile = 0

# For each file...
for file in fileList:
	# Setup a TChain to avoid segfaults since all your trees have the same name
	thisChain = TChain('Tree')
	thisChain.Add(file)

	# Split into pass and fail distributions
	for tagging in taggingDict.keys():

		# Define a blank histogram
		thisHist = TH1F('QCD'+cuts[iFile]+tagging+'_FlavFrac','QCD'+cuts[iFile]+tagging+'_FlavFrac',23,0,22)
		# Draw onto it
		thisChain.Draw('abs(flavor)>>QCD'+cuts[iFile]+tagging+'_FlavFrac','weight*('+taggingDict[tagging]+'&&(tpt<600)&&(tpt>400))','goff')#

		histList.append('QCD'+cuts[iFile]+tagging+'_FlavFrac')

		# thisHist.SetMaximum(0.55)

		# Color the pass and fail differently
		if tagging == 'pass':
			thisHist.SetLineColor(kRed)
		elif tagging == 'fail':
			thisHist.SetLineColor(kBlue)
			
		thisHist.Write()
	
	iFile+=1

cSB = TCanvas('SB','SB',700,800)
cSB.Divide(1,2)

leg = TLegend(0.35,0.7,0.7,0.9)

SBPass = outfile.Get('QCD'+options.cuts+'pass_FlavFrac')
SBFail = outfile.Get('QCD'+options.cuts+'fail_FlavFrac')
# Normalize the histogram
SBPassNorm = SBPass.Clone('QCD'+options.cuts+'pass_FlavFracNorm')
SBFailNorm = SBFail.Clone('QCD'+options.cuts+'fail_FlavFracNorm')
SBPassNorm.Scale(1/SBPassNorm.Integral())
SBFailNorm.Scale(1/SBFailNorm.Integral())


# Set title on norms
SBPassNorm.SetTitle('QCD '+options.cuts+' flavor fraction of top tagged jet')
SBPassNorm.SetMaximum(0.55)
leg.AddEntry(SBPassNorm,'pass')
leg.AddEntry(SBFailNorm,'fail')
cSB.cd(2)
SBPassNorm.Draw('histE')
SBFailNorm.Draw('samehistE')
leg.Draw()

SBRpfPass = outfile.Get('QCDrate_'+options.cuts+'pass_FlavFrac')
SBRpfFail = outfile.Get('QCDrate_'+options.cuts+'fail_FlavFrac')
#Normalize the histograms
SBRpfPassNorm = SBRpfPass.Clone('QCDrate_'+options.cuts+'pass_FlavFracNorm')
SBRpfFailNorm = SBRpfFail.Clone('QCDrate_'+options.cuts+'fail_FlavFracNorm')
SBRpfPassNorm.Scale(1/SBRpfPassNorm.Integral())
SBRpfFailNorm.Scale(1/SBRpfFailNorm.Integral())

outfile.Write()

# Set title on norms
SBRpfPassNorm.SetTitle('QCD '+options.cuts+' Rp/f flavor fraction of top tagged jet')
SBRpfPassNorm.SetMaximum(0.55)
cSB.cd(1)
SBRpfPassNorm.Draw('histE')
SBRpfFailNorm.Draw('samehistE')
leg.Draw()

cSB.Print('FlavorFractionNorm_'+options.cuts+'_QCD.pdf','pdf')


# ---- Now we're going to estimate the pass distribution in the signal region using the rp/f region ------
# New canvas for unscaled histograms
cTotal = TCanvas('cTotal','cTotal',700,800)
cTotal.Divide(1,2)

leg2 = TLegend(0.35,0.7,0.7,0.9)

SBRpf = SBRpfPass.Clone('QCD'+options.cuts+'Rpf_FlavFrac')
SBRpf.Divide(SBRpfFail)

cTotal.cd(1)
SBRpf.SetTitle('R_{P/F} '+options.cuts)
SBRpf.Draw('hist')

SBPassEst = SBFail.Clone('QCD'+options.cuts+'PassEstimated_FlavFrac')
SBPassEst.Multiply(SBRpf)
# SBPassEst.Scale(1/SBPassEst.Integral())

cTotal.cd(2)
SBPass.SetLineColor(kRed)
SBPassEst.SetLineColor(kViolet-6)
SBPass.SetTitle('QCD MC Flavor Fraction Pass and Estimated distributions - '+options.cuts)

leg2.AddEntry(SBPassNorm,'pass')
leg2.AddEntry(SBPassEst,'estimate')

SBPass.Draw('histE')
SBPassEst.Draw('samehistE')
leg2.Draw()

cTotal.Print('FlavorFraction_'+options.cuts+'_QCD_PassVsEst.pdf','pdf')




