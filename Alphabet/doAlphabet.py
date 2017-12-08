import subprocess
import os
import ROOT
from ROOT import *

import array
from array import array

import Plotting_Header
from Plotting_Header import FindAndSetMax

import optparse
from optparse import OptionParser

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
				default       =       'QCD',
				dest          =       'set',
				help          =       'data or QCD')
parser.add_option('-p', '--mtwcuts', metavar='F', type='string', action='store',
				default		=	'700,1100,1200,1400,1600,1900,4000',
				dest		=	'mtwcuts',
				help		=	'Mtw cuts, low to high, separated by a comma')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
				default       =       'default',
				dest          =       'cuts',
				help          =       'Cuts type (ie default, rate, etc)')
parser.add_option('-q', '--qcdsample', metavar='F', type='string', action='store',
				default       =       'all',
				dest          =       'qcdsample',
				help          =       'all or any comma separated combo of HT500, HT700, etc')
parser.add_option('-m', '--make', metavar='F', type='string', action='store',
				default       =       'on',
				dest          =       'make',
				help          =       'Makes the alphabet Rpf files - On or off')
parser.add_option('-C', '--cheat', metavar='F', type='string', action='store',
				default       =       'off',
				dest          =       'cheat',
				help          =       'Turns the top mass blinding on and off and narrow')
parser.add_option('-e', '--estimate', metavar='F', type='string', action='store',
				default       =       'off',
				dest          =       'estimate',
				help          =       'run the estimate or not')
parser.add_option('-f', '--f', metavar='F', type='string', action='store',
				default       =       'quad',
				dest          =       'fit',
				help          =       'fit of Rp/f(mt) - lin,quad,new')
parser.add_option('-d', '--fit2d', metavar='F', type='string', action='store',
				default       =       'off',
				dest          =       'fit2d',
				help          =       'fit the fit parameters or or not')
parser.add_option('-D', '--run2d', metavar='F', type='string', action='store',
				default       =       'off',
				dest          =       'run2d',
				help          =       'run the 2D fit or or not')
parser.add_option('-t', '--test2d', metavar='F', type='string', action='store',
				default       =       'off',
				dest          =       'test2d',
				help          =       'Test the 2D fit or or not - recreate the fits in each Mtw slice')


(options, args) = parser.parse_args()

# parse the input into a list of strings
cutList = options.mtwcuts.split(',')

# Turns off plotting
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True

# ---- Make the estimate for each Mtw region -----
if options.make == 'on':
	# Run alphabet for the different mass ranges determined by the option
	commands1 = []
	for icut in range(len(cutList)-1):
		commands1.append('python Bstar_Alphabet.py -f '+options.fit+' -C ' + options.cheat+ ' -s '+options.set+' -c '+options.cuts+' -q '+options.qcdsample+' -e '+options.estimate+' -p '+cutList[icut]+','+cutList[icut+1])

	for s in commands1 :
		print 'executing ' + s
		subprocess.call([s], shell=True)

# Save the Mtw binning for the analyzer
myFile = TFile('results/'+options.cuts+'/MtwvsBkg_'+options.set+'_mtfit_'+options.fit+'_cheat_'+options.cheat+'.root','recreate')
Mtwbins = [float(thisBin) for thisBin in cutList]
binsHist = TH1I('binsHist','binsHist',len(Mtwbins)-1,array('f',Mtwbins))
binsHist.Write()


# --- Run the estimate (no error bars)--------
if options.estimate == 'on':
	# Grab the outputed files
	inFiles = []
	for icut in range(len(cutList)-1):
		if options.qcdsample != 'all':
			if os.path.exists('results/'+options.cuts+'/QCDbreakdown/'+options.qcdsample+'/Alphabet'+options.set+'_'+options.cuts+'_Mtw_'+cutList[icut]+'-'+cutList[icut+1]+'.root'):
				inFiles.append(TFile.Open('results/'+options.cuts+'/QCDbreakdown/'+options.qcdsample+'/Alphabet'+options.set+'_'+options.cuts+'_Mtw_'+cutList[icut]+'-'+cutList[icut+1]+'.root'))
			else:
				print 'File missing. Skipping results/'+options.cuts+'/QCDbreakdown/'+options.qcdsample+'/Alphabet'+options.set+'_'+options.cuts+'_Mtw_'+cutList[icut]+'-'+cutList[icut+1]+'.root'
		else:
			if os.path.exists('results/'+options.cuts+'/Alphabet'+options.set+'_'+options.cuts+'_Mtw_'+cutList[icut]+'-'+cutList[icut+1]+'.root'):
				inFiles.append(TFile.Open('results/'+options.cuts+'/Alphabet'+options.set+'_'+options.cuts+'_Mtw_'+cutList[icut]+'-'+cutList[icut+1]+'.root'))
			else:
				print 'File missing. Skipping results/'+options.cuts+'/Alphabet'+options.set+'_'+options.cuts+'_Mtw_'+cutList[icut]+'-'+cutList[icut+1]+'.root'		

	# Book some 'total' histograms
	totV = TH1F('FullMtwV','Alphabet estimate in full Mtw - '+options.cuts,35,500,4000)
	totN = TH1F('FullMtwN','Alphabet estimate in full Mtw - '+options.cuts,35,500,4000)
	totAT = TH1F('FullMtwAT','Alphabet estimate in full Mtw - '+options.cuts,35,500,4000)


	for file in inFiles:
		thisV = file.Get('V')
		totV.Add(thisV)

		thisN = file.Get('QCD')
		totN.Add(thisN)

		thisAT = file.Get('AT')
		totAT.Add(thisAT)


	cmain = TCanvas('c1','c1',800,700)
	cmain.cd()

	main = ROOT.TPad("main", "main", 0, 0, 1, 1)

	main.Draw()

	main.cd()

	leg2 = TLegend(0.75,0.75,0.95,0.95)
	leg2.SetLineColor(0)
	leg2.SetFillColor(0)

	leg2.AddEntry(totV, "Data in tag region", "PL")
	leg2.AddEntry(totN, "Data prediction", "F")

	FindAndSetMax([totV,totN])

	totV.SetLineColor(kBlack)
	totN.SetFillColor(kYellow)
	totN.SetLineColor(kBlack)


	totN.Draw('Hist')
	totV.Draw('same E0')
	leg2.Draw()

	cmain.Print('results/'+options.cuts+'/MtwvsBkg_'+options.set+'_'+options.qcdsample+'.png','png')

# ------ 2D - Grab the fit parameters and put them in a TGraph -------
if options.fit2d == 'on':
	# Make a nested dict to store the parameters
	# {'low-high':
	#	{'low':int lowval,
	#	'high':int highval,
	# 	'file': Tfile
	#	'params':[p0,p1,p2,...]}
	# }
	paramDict = {}
	for ibinSide in range(len(cutList)-1):
		lowWall = cutList[ibinSide]
		highWall = cutList[ibinSide+1]
		tempDict = { 'low':int(lowWall),
											'high':int(highWall),
											'file':TFile.Open('results/'+options.cuts+'/Alphabet'+options.set+'_'+options.cuts+'_Mtw_'+lowWall+'-'+highWall+'.root'),
											'params':[],
											'paramsE':[]}
	# Now grab and store the parameters in the dict
		thisFile = tempDict['file']
		thisFit = thisFile.Get('fit')
		nparams = thisFit.GetNpar()
		for ipar in range(nparams):
			tempDict['params'].append(thisFit.GetParameter(ipar)) 
			tempDict['paramsE'].append(thisFit.GetParError(ipar)) 

		paramDict[lowWall+'-'+highWall] = tempDict

	# Now we have a nicely sorted dictionary with all of the elements to make a TGraph for each parameter
	# Let's book as many TGraphs as we need

	# for each different tgraph (parameter)
	for ipar in range(nparams):
		x = []
		ex = []
		y = []
		ey = []
		# for each x bin
		for band in paramDict.keys():
			lowWall = paramDict[band]['low']
			highWall = paramDict[band]['high']

			# Get the x center
			x.append(float(lowWall+highWall)/2.)
			# Get the width (x error)
			ex.append(float(highWall-lowWall)/2.)
			# Get the y value (parameter value for that Mtw bin)
			y.append(paramDict[band]['params'][ipar])
			# Get the error on the y value
			ey.append(paramDict[band]['paramsE'][ipar])

		# print x
		# print y
		# print ex
		# print ey

		thisTGraph = TGraphErrors(len(x),array('d',x),array('d',y),array('d',ex),array('d',ey))
		thisTGraph.SetName('p'+str(ipar))
		thisTGraph.SetTitle('p'+str(ipar))

		# # Now we can fit each one of this
		parFit = TF1('p'+str(ipar)+'fit','pol1',float(cutList[0]),float(cutList[-1]))#'[0]*exp([1]*x)+[2]'
		# parFit.SetParameter(1,1200)
		# parFit.SetParLimits(1,900,1300)
		# parFit.SetParameter(2,200)
		# parFit.SetParLimits(2,100,500)
		# if ipar == 0:
		# 	parFit.SetParameter(0,-0.1)
		# 	parFit.SetParLimits(0,-0.2,0.001)
		# 	parFit.SetParameter(3,-0.06)
		# 	parFit.SetParLimits(3,-0.07,-0.04)
		# elif ipar == 1:
		# 	parFit.SetParameter(0,0.0012)
		# 	parFit.SetParLimits(0,0.0001,0.002)
		# 	parFit.SetParameter(3,0.0008)
		# 	parFit.SetParLimits(3,0,0.001)
			

		parFit.SetLineColor(kBlue)
		FitResults = thisTGraph.Fit(parFit)
		# print 'Chi2 for p' +str(ipar)+': ' + str(parFit.GetChisquare())
		parErrs = TGraphErrors(1000)
		parErrs.SetName('parFitErrs')
		for i in range(1000):
			parErrs.SetPoint(i, float(cutList[0]) + i*(float(cutList[-1])- float(cutList[0]))/1000., 0)
		TVirtualFitter.GetFitter().GetConfidenceIntervals(parErrs,0.68)

		parErrs.SetLineColorAlpha(kBlue,0.2)

		myFile.cd()
		thisTGraph.Write()
		parErrs.Write()
		parFit.Write()

		cTGraph = TCanvas('cTGraph','cTGraph',800,700)
		thisTGraph.Draw('ap')
		parErrs.Draw('p same')
		cTGraph.Print('results/'+options.cuts+'/p'+str(ipar)+'fit_'+options.set+'_'+options.qcdsample+'_mtfit_'+options.fit+'_cheat_'+options.cheat+'.png','png')

myFile.Close()

# Now we do one final cross check and rerun the estimate but with the parameter fits
if options.run2d == 'on':
	print 'executing ' + 'python Bstar_Alphabet.py -D '+options.run2d+' -f '+options.fit+' -C ' + options.cheat+ ' -s '+options.set+' -c '+options.cuts+' -q '+options.qcdsample+' -e '+options.estimate+' -p '+cutList[0]+','+cutList[-1]
	subprocess.call(['python Bstar_Alphabet.py -D '+options.run2d+' -f '+options.fit+' -C ' + options.cheat+ ' -s '+options.set+' -c '+options.cuts+' -q '+options.qcdsample+' -e '+options.estimate+' -p '+cutList[0]+','+cutList[-1]], shell=True)

