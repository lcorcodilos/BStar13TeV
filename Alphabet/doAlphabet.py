import subprocess
import os
import ROOT
from ROOT import *

import Plotting_Header
from Plotting_Header import FindAndSetMax

import Bstar_Functions
from Bstar_Functions import Make_Pull_plot

import optparse
from optparse import OptionParser

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
				default       =       'QCD',
				dest          =       'set',
				help          =       'data or QCD')
parser.add_option('-p', '--mtwcuts', metavar='F', type='string', action='store',
				default		=	'800,1000,1200,1400,1600,4000',
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
				help          =       'Makes the alphabet files - On or off')
parser.add_option('-e', '--estimate', metavar='F', type='string', action='store',
				default       =       'off',
				dest          =       'estimate',
				help          =       'run the estimate or not')


(options, args) = parser.parse_args()

# parse the input into a list of strings
cutList = options.mtwcuts.split(',')

if options.make == 'on':
	# Run alphabet for the different mass ranges determined by the option
	commands1 = []
	for icut in range(len(cutList)-1):
		commands1.append('python Bstar_Alphabet.py -s '+options.set+' -c '+options.cuts+' -q '+options.qcdsample+' -e '+options.estimate+' -p '+cutList[icut]+','+cutList[icut+1])

	for s in commands1 :
		print 'executing ' + s
		subprocess.call([s], shell=True)

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
				print 'results/'+options.cuts+'/Alphabet'+options.set+'_'+options.cuts+'_Mtw_'+cutList[icut]+'-'+cutList[icut+1]+'.root'
			else:
				print 'File missing. Skipping results/'+options.cuts+'/Alphabet'+options.set+'_'+options.cuts+'_Mtw_'+cutList[icut]+'-'+cutList[icut+1]+'.root'		

	totV = TH1F('FullMtwV','Alphabet estimate in full Mtw - '+options.cuts,23,70,300)
	totN = TH1F('FullMtwN','Alphabet estimate in full Mtw - '+options.cuts,23,70,300)
	# totNup = TH1F('FullMtwNup','Alphabet estimate in full Mtw - '+options.cuts,25,50,300)
	# totNdown = TH1F('FullMtwNdown','Alphabet estimate in full Mtw - '+options.cuts,25,50,300)


	for file in inFiles:
		thisV = file.Get('V')
		totV.Add(thisV)

		thisN = file.Get('QCD')
		totN.Add(thisN)

		# thisNup = file.Get('QCD_Up')
		# totNup.Add(thisNup)

		# thisNdown = file.Get('QCD_Down')
		# totNdown.Add(thisNdown)

	main = TCanvas('c1','c1',800,700)
	main.cd()

	main = ROOT.TPad("main", "main", 0, 0, 1, 1)
	# main = ROOT.TPad("main", "main", 0, 0.3, 1, 1)
	# sub = ROOT.TPad("sub", "sub", 0, 0, 1, 0.3)
	# main.SetBottomMargin(0.0)

	# main.SetLeftMargin(0.16)
	# main.SetRightMargin(0.05)
	# main.SetTopMargin(0.1)

	# sub.SetLeftMargin(0.16)
	# sub.SetRightMargin(0.05)
	# sub.SetTopMargin(0)
	# sub.SetBottomMargin(0.3)

	main.Draw()
	# sub.Draw()

	main.cd()

	leg2 = TLegend(0.75,0.75,0.95,0.95)
	leg2.SetLineColor(0)
	leg2.SetFillColor(0)

	leg2.AddEntry(totV, "Data in tag region", "PL")
	leg2.AddEntry(totN, "Data prediction", "F")
	# leg2.AddEntry(totNup, "uncertainty", "F")

	FindAndSetMax([totV,totN])#,totNup,totNdown])

	totV.SetLineColor(kBlack)
	totN.SetFillColor(kYellow)
	totN.SetLineColor(kBlack)
	# totNup.SetLineColor(kBlack)
	# totNup.SetLineStyle(2)
	# totNdown.SetLineColor(kBlack)
	# totNdown.SetLineStyle(2)

	totN.Draw('Hist')
	totV.Draw('same E0')
	# totNup.Draw('same')
	# totNdown.Draw('same')
	leg2.Draw()

	# sub.cd()

	# pull = Make_Pull_plot(totV,totN,totNup,totNdown)

	# pull.SetFillColor(kBlue)
	# pull.SetStats(0)
	# pull.GetYaxis().SetRangeUser(-2.9,2.9)
	# pull.SetTitle(";M_{tw} (GeV);(Data-Bkg)/#sigma")
	# pull.GetXaxis().SetLabelSize(0.05)
	# pull.GetYaxis().SetLabelSize(0.13)

	# LS = .13

	# pull.GetYaxis().SetTitleOffset(0.4)
	# pull.GetXaxis().SetTitleOffset(0.9)

	# pull.GetYaxis().SetLabelSize(LS)
	# pull.GetYaxis().SetTitleSize(LS)
	# pull.GetYaxis().SetNdivisions(306)
	# pull.GetXaxis().SetLabelSize(LS)
	# pull.GetXaxis().SetTitleSize(LS)


	# pull.Draw('hist')

	main.Print('results/'+options.cuts+'/MtwvsBkg_'+options.set+'_'+options.qcdsample+'.png','png')