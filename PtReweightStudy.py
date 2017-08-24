# PtReweightStudy.py - Lucas Corcodilos									#
# -------------------------------------									#
# Creates an extra flat scale factor for top pt reweighting. Only works #
# AFTER '+options.cuts+' has been run since it needs up-to-date data, QCD bkg, #
# and singeltop distributions. Since these three things don't get 		#
# reweighted by the extra factor calculated here though, they don't 	#
# need to be re-run. However, the ttbar DOES need to be rerun since it 	#
# is effected. Currently the script automatically does this to make 	#
# sure it is not forgotten.												#
# --------------------------------------------------------------------- #

import ROOT
from ROOT import *

import Bstar_Functions	
from Bstar_Functions import *

import subprocess

from optparse import OptionParser

parser = OptionParser()

parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
				  default	=	'sideband1',
				  dest		=	'cuts',
				  help		=	'sideband1 or toy')

(options, args) = parser.parse_args()


Cons = LoadConstants()
fLumi = Cons['lumi']
sLumi = str(int(fLumi))+'pb'
xsec_ttbar = Cons['xsec_ttbar']['PH']

# Make the ttbar without the extra correction
commands1 = []
commands1.append('python TWanalyzer.py -s ttbar -c '+options.cuts+' --noExtraPtCorrection')
commands1.append('rm rootfiles/'+sLumi+'/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_'+options.cuts+'_extraPtCorrection_off.root')
commands1.append('python HistoWeight.py -i TWanalyzerttbar_Trigger_nominal_none_PSET_'+options.cuts+'_extraPtCorrection_off.root -o rootfiles/'+sLumi+'/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_'+options.cuts+'_extraPtCorrection_off.root -n auto -w ' + str(fLumi*xsec_ttbar))
commands1.append('mv TWanalyzerttbar_Trigger_nominal_none_PSET_'+options.cuts+'_extraPtCorrection_off.root temprootfiles/')
# Save the previous TWTopPtSF.root temporarily. If it's identical to new value
# then we don't need to remake TWanalyzerttbar...root at the end
commands1.append('mv TWTopPtSF.root TWTopPtSF_old.root')

for s in commands1 :
	print 'executing ' + s
	subprocess.call( [s], shell=True )

# Import the data, ttbar (without extra correction), and singletop
fdata = TFile('rootfiles/'+sLumi+'/TWanalyzerdata_Trigger_nominal_none_PSET_'+options.cuts+'.root','open')
fttbar = TFile('rootfiles/'+sLumi+'/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_'+options.cuts+'_extraPtCorrection_off.root','open')
fsingletop = TFile('rootfiles/'+sLumi+'/TWanalyzerweightedsingletop_Trigger_nominal_none_PSET_'+options.cuts+'.root','open')

# Create an output
out = TFile('TWTopPtSF.root','recreate')
out.cd()
outhist = TH1F('TopPtSF','Scale factor for top pt reweight',1,0,1)

# Grab the data and the bkg estimate
data = fdata.Get('PtTop')
qcdbkg = fdata.Get('QCDbkgPT')

# Grab the ttbar and its contribution to the bkg estimate
ttbar = fttbar.Get('PtTop')
ttbarbkg = fttbar.Get('QCDbkgPT')

# Grab the singletop and its contribution to the bkg estimate
singletop = fsingletop.Get('PtTop')
stbkg = fsingletop.Get('QCDbkgPT')

# Calculate total background value
totalbkg = qcdbkg.Clone('totalbkg')
# Subtract away the double counting
totalbkg.Add(ttbarbkg,-1)
totalbkg.Add(stbkg,-1)
# Add the stack together
totalbkg.Add(ttbar)
totalbkg.Add(singletop)

print "total bkg estimate integral: " + str(totalbkg.Integral())
print "data integral: " + str(data.Integral())

# First find the difference between the two distributions
diff = data.Integral() - totalbkg.Integral()

# Then figure out how much the ttbar mc needs to be scaled by to correct that difference
# If data > totalbkg, diff > 0 and scale factor brings bkg up
SF = diff/ttbar.Integral()

print "SF: " + str(SF)

outhist.SetBinContent(1,SF)

# Save
out.Write()
out.Close()

# Now compare against old value to see if we need to rerun the ttbar
newFile = TFile('TWTopPtSF.root','open')
oldFile = TFile('TWTopPtSF_old.root','open')

newHist = newFile.Get('TopPtSF')
oldHist = oldFile.Get('TopPtSF')

newSF = newHist.GetBinContent(1)
oldSF = oldHist.GetBinContent(1)

# Make the ttbar WITH the newly found extra correction
if newSF == oldSF:
	print "Scale factor did not change - no need to rerun"
else:
	print "Scale factor has changed. Rerunning ttbar with correction."
	subprocess.call(['sh grid_ptcorr_sub.csh'], shell=True)
	# Will quit any jobs fail
	WaitForJobs('ptcorr')


	commands2 = []
	# commands2.append('python grid_ptcorr_post.py -c default')
	# commands2.append('python grid_ptcorr_post.py -c sideband')
	commands2.append('python grid_ptcorr_post.py -c '+options.cuts)

	for s in commands2 :
		print 'executing ' + s
		subprocess.call( [s], shell=True )
