# PtReweightStudy.py - Lucas Corcodilos									#
# -------------------------------------									#
# Iteratively creates an extra flat scale factor for top pt reweighting.#
# Runs everything that it needs in standalone mode. Will make all 		#																		#
# needed rate and analyzer files and calculate and save SFs found from  #
# them.															 		#
# Nothing has been written to examine the results of this script.	 	#
# Only prints the scale factor numbers at the end. Might need to do  	#
# some sort of quick file rename so that the last iteration SF is 	 	#
# renamed as the zeroth so the main analysis grabs it.	-LC 8/28/17		#
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

# Going to need this stuff to keep values up-to-date
Cons = LoadConstants()
fLumi = Cons['lumi']
sLumi = str(int(fLumi))+'pb'
xsec_ttbar = Cons['xsec_ttbar']['PH']


# A weird note about the jobs that need to be processed
# - The non-ttbar rate jobs don't care about iteration (only ttbar gets the SF)
# - The non-ttbar analyzer jobs DO care about the iteration (since the we need to derive a SF from ttbar w/o a SF)

def MakeRateListOfJobs(iteration):
	thisIteration = str(iteration)
	newFile = open('ptcorrrate.listOfJobs','w')

	if iteration == 0:
		# Make the ttbar job - need to specify no extra correction for zeroth iteration
		newFile.write('python ./tardir/TWrate.py -s ttbar -g on -c rate_'+options.cuts+' --noExtraPtCorrection \n')

		# Make the data jobs - iteration doesn't matter
		for jobs in range(1,101):
			newFile.write('python ./tardir/TWrate.py -s data -g on -c rate_'+options.cuts+' -n '+str(jobs)+' -j 75\n')
		# Make the singletop jobs - iteration doesn't matter
		for chan in ['singletop_t','singletop_tB','singletop_tW','singletop_tWB']	:
			newFile.write('python ./tardir/TWrate.py -s '+chan+' -g on -c rate_'+options.cuts+' \n')
		for ht in ['500','700','1000','1500','2000']:
			for jobs in range(1,6):
				newFile.write('python ./tardir/TWrate.py -s QCDHT'+ht+' -g on -c rate_'+options.cuts+' -n '+str(jobs)+' -j 5 \n')
	else:
		# Make the ttbar job
		newFile.write('python ./tardir/TWrate.py -s ttbar -g on -c rate_'+options.cuts+' -i '+thisIteration+'\n')



def MakeAnaListOfJobs(iteration):
	thisIteration = str(iteration)
	newFile = open('ptcorrana.listOfJobs','w')

	# Make the data jobs - need proper iteration
	for jobs in range(1,101):
		newFile.write('python ./tardir/TWanalyzer.py -s data -g on -c '+options.cuts+' -i '+thisIteration+' -n '+str(jobs)+' -j 75\n')
	# Make the singletop jobs - need proper iteration
	for chan in ['singletop_t','singletop_tB','singletop_tW','singletop_tWB']:
		newFile.write('python ./tardir/TWanalyzer.py -s '+chan+' -g on -c '+options.cuts+' -i '+thisIteration+' \n')

	# Make the ttbar - always no extra pt correction but needs
	# to be remade each time since the Rp/f changes
	newFile.write('python ./tardir/TWanalyzer.py -s ttbar -g on -c '+options.cuts+' --noExtraPtCorrection \n')



if __name__ == "__main__":
	
	# # Backup the old scale factor
	# subprocess.call(['mv TWTopPtSF.root TWTopPtSF_old.root'], shell=True)

	# # Make zeroth scale factor (with value 0)
	# fZerothSF = TFile('TWTopPtSF_0.root','recreate')
	# hZerothSF = TH1F('TWTopPtSF_0', '0th scale factor for top pt reweight',1,0,1)
	# hZerothSF.SetBinContent(1,0)
	# hZerothSF.Write()
	# fZerothSF.Close()

	# # Need to start by making the zeroth rate files
	# MakeRateListOfJobs(0)
	# subprocess.call(['sh grid_ptcorrrate_sub.csh'], shell=True)
	# WaitForJobs('ptcorrrate')


	# # Post process the zeroth rate jobs
	# commands = []
	# commands.append('python grid_ptcorrrate_post.py -i 0 -c rate_'+options.cuts)
	# commands.append('python TWrate_Maker.py -c rate_'+options.cuts+' -s QCD --noExtraPtCorrection')
	# commands.append('python TWrate_Maker.py -c rate_'+options.cuts+' -s data --noExtraPtCorrection')
	# for s in commands :
	# 	print 'executing ' + s
	# 	subprocess.call( [s], shell=True )


	# # Make the analyzer files (data, st, ttbar without the extra correction)
	# MakeAnaListOfJobs(0)
	# subprocess.call(['sh grid_ptcorrana_sub.csh'], shell=True)
	# WaitForJobs('ptcorrana')


	# # Post process the zeroth ana jobs
	# subprocess.call(['python grid_ptcorrana_post.py -i 0 -c '+options.cuts], shell=True )	

	# Loop through the first four iterations (counting NO flat SF as zeroth order)
	for i in range(1,11):
		# Define the pt string
		ptString = '_ptSF'+str(i-1)

		print '------------ Begin finding SF iteration ' + str(i) + '---------------------'

		# Create an output
		out = TFile('TWTopPtSF_'+str(i)+'.root','recreate')
		out.cd()

		outhist = TH1F('TWTopPtSF_'+str(i), str(i)+' scale factor for top pt reweight',1,0,1)

		# Import the most recent data and singletop and ttbar
		fdata = TFile('rootfiles/'+sLumi+'/TWanalyzerdata_Trigger_nominal_none_PSET_'+options.cuts+ptString+'.root','open')
		fsingletop = TFile('rootfiles/'+sLumi+'/TWanalyzerweightedsingletop_Trigger_nominal_none_PSET_'+options.cuts+ptString+'.root','open')
		fttbar = TFile('rootfiles/'+sLumi+'/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_'+options.cuts+'_extraPtCorrection_off.root','open')

		# Grab the data and the bkg estimate
		data = fdata.Get('PtTop')
		qcdbkg = fdata.Get('QCDbkgPT')

		# Grab the ttbar and the bkg estimate
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

		print "total bkg estimate integral for iteration "+str(i)+": " + str(totalbkg.Integral())
		print "data integral for iteration "+str(i)+": " + str(data.Integral())

		# First find the difference between the two distributions
		diff = data.Integral() - totalbkg.Integral()

		# Then figure out how much the ttbar mc needs to be scaled by to correct that difference
		# If data > totalbkg, diff > 0 and scale factor brings bkg up
		SF = diff/ttbar.Integral()

		print "SF for iteration "+str(i)+": " + str(SF)

		out.cd()
		# Set, write, and save
		outhist.SetBinContent(1,SF)
		outhist.Write()
		out.Close()

		# Generate a list of jobs that use the newest scale factor (ptcorrrate.listOfJobs) to remake Rp/f
		# Should be for newly weighted ttbar only since data and singletop dont get a reweight (we'll remake everything with the final SF applied at the end)
		# MakeRateListOfJobs(i) -- Removed this because we only reprocess the ttbar so will just do it in session
		# Run, Wait, and Process
		# subprocess.call(['sh grid_ptcorrrate_sub.csh'], shell=True) 
		# WaitForJobs('ptcorrrate')

		commands = []
		commands.append('python TWrate.py -s ttbar -c rate_'+options.cuts+' -i '+str(i))
		commands.append('python grid_ptcorrrate_post.py -c rate_'+options.cuts+' -i '+str(i))
		commands.append('python TWrate_Maker.py -c rate_'+options.cuts+' -s QCD -i '+str(i))
		commands.append('python TWrate_Maker.py -c rate_'+options.cuts+' -s data -i '+str(i))
		for s in commands :
			print 'executing ' + s
			subprocess.call( [s], shell=True )

		# Rerun analyzer
		MakeAnaListOfJobs(i)
		subprocess.call(['sh grid_ptcorrana_sub.csh'], shell=True) 
		WaitForJobs('ptcorrana')
		subprocess.call(['python grid_ptcorrana_post.py -c '+options.cuts+' -i '+str(i)], shell=True)

		# With new data and single top, we can loop through again

	# Print the scale factors
	for i in range(11):
		file = TFile('TWTopPtSF_'+str(i)+'.root','open')
		hist = file.Get('TWTopPtSF_'+str(i))
		print 'Scale factor iteration '+str(i)+': '+str(hist.GetBinContent(1))





