#
import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy

import Converters
from Converters import *

def AlphabetSlicer(plot, bins, cut, which, center): # Takes a 2D plot and measures the Pass/Fail ratios in given bins
	# plot = 2D plot to perform the measurment on
	# bins = list of bins to measure the P/F ratio in (each bin will yield a A/B point
	# cut = Value to differentiate pass from fail. Should be on the y-axis of plot
	# which = ">" or "<", to tell you which way the cut goes
	# center = the x-var is recentered about the middle of the blinded region. This tells you where. You can leave it as 0 if you want.
	x = []
	y = []
	exl = []
	eyl = []
	exh = []
	eyh = []  # ALL OF THESE ARE THE COMPONENTS OF A TGraphAsymmErrors object.
	hx = []
	hy = []
	ehx = []
	ehy = []

	for b in bins: # loop through the bins (bins are along the mass axis and should contain a gap for the sigreg)
		passed = 0
		failed = 0
		for i in range(plot.GetNbinsX()):  # Get pass/failed
			for j in range(plot.GetNbinsY()):
				if (plot.GetXaxis().GetBinCenter(i) < b[1]) and (plot.GetXaxis().GetBinCenter(i) > b[0]):
					if which == ">":
						if plot.GetYaxis().GetBinCenter(j) < cut:
							failed = failed + plot.GetBinContent(i,j)
						else:
							passed = passed + plot.GetBinContent(i,j)
					if which == "<":
						if plot.GetYaxis().GetBinCenter(j) > cut:
							failed = failed + plot.GetBinContent(i,j)
						else:
							passed = passed + plot.GetBinContent(i,j)
		if passed < 0:
			passed = 0
		if failed < 0:
			failed = 0
		if passed == 0 or failed == 0:
			continue

		x.append((float((b[0]+b[1])/2.)-center))  # do the math in these steps (calculate error)
		exl.append(float((b[1]-b[0])/2.))
		exh.append(float((b[1]-b[0])/2.))
		y.append(passed/(failed))      # NOTE: negative bins are not corrected, if you're getting negative values your bins are too fine.
		ep = math.sqrt(passed)
		ef = math.sqrt(failed)
		err = (passed/failed)*math.sqrt((ep/passed)**2+(ef/failed)**2)
		eyh.append(err)
		if (passed/failed) - err > 0.:
			eyl.append(err)
		else:
			eyl.append(passed/failed)
	for i in x:
		print i
	G = TGraphAsymmErrors(len(x), scipy.array(x), scipy.array(y), scipy.array(exl), scipy.array(exh), scipy.array(eyl), scipy.array(eyh))
	return G  # Returns a TGAE which you can fit or plot.

def Alphabet3DSlicer(plot, bins, cut1, which1, cut2, which2, center): # Takes a 3D plot and measures the Pass/Fail ratios in given bins
	# plot = 3D plot to perform the measurment on
	# bins = list of bins to measure the P/F ratio in (each bin will yield a A/B point
	# cut = Value to differentiate pass from fail. Should be on the y and z-axes of plot
	# which1(2) = ">" or "<", to tell you which way the cut goes
	# center = the x-var is recentered about the middle of the blinded region. This tells you where. You can leave it as 0 if you want.
	x = []
	y = []
	exl = []
	eyl = []
	exh = []
	eyh = []  # ALL OF THESE ARE THE COMPONENTS OF A TGraphAsymmErrors object.
	hx = []
	hy = []
	ehx = []
	ehy = []

	for b in bins: # loop through the bins (bins are along the mass axis and should contain a gap for the sigreg)
		passed = 0
		failed = 0
		for i in range(plot.GetNbinsX()):  # Get pass/failed
			for j in range(plot.GetNbinsY()):
				for k in range(plot.GetNbinsZ()):
					if (plot.GetXaxis().GetBinCenter(i) < b[1]) and (plot.GetXaxis().GetBinCenter(i) > b[0]):
						# Four different filling options based on cut directions. Inequality signs in strings should match what is in if statements
						if which1 == ">":
							if which2 == ">":
								# If both cuts pass, fill passed - else fill fail
								if (plot.GetYaxis().GetBinCenter(j) > cut1) and (plot.GetZaxis().GetBinCenter(k) > cut2):
									passed = passed + plot.GetBinContent(i,j,k)
								else:
									failed = failed + plot.GetBinContent(i,j,k)

							elif which2 == '<':
								# If both cuts pass, fill passed - else fill fail
								if (plot.GetYaxis().GetBinCenter(j) > cut1) and (plot.GetZaxis().GetBinCenter(k) < cut2):
									passed = passed + plot.GetBinContent(i,j,k)
								else:
									failed = failed + plot.GetBinContent(i,j,k)

						if which1 == "<":
							if which2 == '>':
								if (plot.GetYaxis().GetBinCenter(j) < cut1) and (plot.GetZaxis().GetBinCenter(k) > cut2):
									passed = passed + plot.GetBinContent(i,j,k)
								else:
									failed = failed + plot.GetBinContent(i,j,k)

							elif which2 == '<':
								if (plot.GetYaxis().GetBinCenter(j) < cut1) and (plot.GetZaxis().GetBinCenter(k) < cut2):
									passed = passed + plot.GetBinContent(i,j,k)
								else:
									failed = failed + plot.GetBinContent(i,j,k)

		if passed < 0:
			passed = 0
		if failed < 0:
			failed = 0
		if passed == 0 or failed == 0:
			continue

		x.append((float((b[0]+b[1])/2.)-center))  # do the math in these steps (calculate error)
		exl.append(float((b[1]-b[0])/2.))
		exh.append(float((b[1]-b[0])/2.))
		y.append(passed/(failed))      # NOTE: negative bins are not corrected, if you're getting negative values your bins are too fine.
		ep = math.sqrt(passed)
		ef = math.sqrt(failed)
		err = (passed/failed)*math.sqrt((ep/passed)**2+(ef/failed)**2)
		eyh.append(err)
		if (passed/failed) - err > 0.:
			eyl.append(err)
		else:
			eyl.append(passed/failed)
	for i in x:
		print i
	G = TGraphAsymmErrors(len(x), scipy.array(x), scipy.array(y), scipy.array(exl), scipy.array(exh), scipy.array(eyl), scipy.array(eyh))
	return G  # Returns a TGAE which you can fit or plot.

def AlphabetNDSlicer(DP,DM,var, varCuts, passCuts, presel, bins, center):
	# LC 11/1/17
	# Does the job of AlphabetSlicer in N-dimensions by avoiding a multi-dimensional histogram
	# to define cut regions (which is an inexact method!) and instead using TCuts
	# DP - distribution plus
	# DM - distribution minus
	# var - tree variable that we want to look at in range we want to see it
	# varCuts - cuts for blinded region, ex '(mass_top<105)||(mass_top>210)'
	# passCuts - cuts to define 'pass'; a string like '(sjbtag>0.5426)&&(tau32<0.65)'
	# presel - preselection that's always applied
	# bins - bins for var (can be truth in which case varCuts needs to be inverted)
	# center - usually 0. Allows you to recent the Rpf
	RatePassP = TH1F('PassPlus_'+var,'PassPlus_'+var,len(bins)-1,bins)
	RateFailP = TH1F('FailPlus_'+var,'FailPlus_'+var,len(bins)-1,bins)
	RatePassM = TH1F('PassMinus_'+var,'PassMinus_'+var,len(bins)-1,bins)
	RateFailM = TH1F('FailMinus_'+var,'FailMinus_'+var,len(bins)-1,bins)
	# RatePassP.Sumw2() 
	# RateFailP.Sumw2()
	# RatePassM.Sumw2()
	# RateFailM.Sumw2()

	# Fill pass and fail distribtions for plus and minus sets
	for i in DP:
		tempFile = TFile.Open(i.File)
		tempTree = tempFile.Get(i.Tree)

		tempPassP = TH1F('tempPassP','tempPassP',len(bins)-1,bins)
		tempFailP = TH1F('tempFailP','tempFailP',len(bins)-1,bins)
		tempPassP.Sumw2()
		tempFailP.Sumw2()

		tempTree.Draw(var+'>>tempPassP',i.weight+'*(('+passCuts+')&&('+presel+')&&('+varCuts+'))','goff e')
		tempTree.Draw(var+'>>tempFailP',i.weight+'*(!('+passCuts+')&&('+presel+')&&('+varCuts+'))','goff e')

		RatePassP.Add(tempPassP,1.)
		RateFailP.Add(tempFailP,1.)
	for i in DM:
		tempFile = TFile.Open(i.File)
		tempTree = tempFile.Get(i.Tree)

		tempPassM = TH1F('tempPassM','tempPassM',len(bins)-1,bins)
		tempFailM = TH1F('tempFailM','tempFailM',len(bins)-1,bins)
		tempPassM.Sumw2()
		tempFailM.Sumw2()


		tempTree.Draw(var+'>>tempPassM',i.weight+'*(('+passCuts+')&&('+presel+')&&('+varCuts+'))','goff e')
		tempTree.Draw(var+'>>tempFailM',i.weight+'*(!('+passCuts+')&&('+presel+')&&('+varCuts+'))','goff e')
		RatePassM.Add(tempPassM,1.)
		RateFailM.Add(tempFailM,1.)

	# Subtract away the minus distributions
	RatePass = RatePassP.Clone()
	RatePass.Add(RatePassM,-1)
	RateFail = RateFailP.Clone()
	RateFail.Add(RateFailM,-1)

	print 'Pass entries: ' + str(RatePass.GetEntries())
	print 'Fail entries: ' + str(RateFail.GetEntries())

	Rpf = RatePass.Clone()
	Rpf.Divide(RateFail)

	Rpf.Draw()

	# Now need to build a TGAE that supports doing a fit
	x = [float((bins[i]+bins[i+1])/2.-center) for i in range(0,len(bins)-1) if Rpf.GetBinContent(i+1) > 0]
	exl = [float((bins[i+1]-bins[i])/2.) for i in range(0,len(bins)-1) if Rpf.GetBinContent(i+1) > 0]
	exh = exl
	y = [Rpf.GetBinContent(i) for i in range(1,len(bins)) if Rpf.GetBinContent(i) > 0]
	# ep = [math.sqrt(RatePass.GetBinContent(i)) for i in range(1,len(bins))]
	# ef = [math.sqrt(RateFail.GetBinContent(i)) for i in range(1,len(bins))]
	# eyh = [Rpf.GetBinContent(i+1)*math.sqrt((ep[i]/RatePass.GetBinContent(i+1))**2+(ef[i]/RateFail.GetBinContent(i+1))**2) if (RatePass.GetBinContent(i+1)>0. and RateFail.GetBinContent(i+1)>0.) else 0 for i in range(0,len(bins)-1)]
	eyh = [Rpf.GetBinError(i) for i in range(1,len(bins)) if Rpf.GetBinContent(i) > 0]
	eyl = eyh
	nbinsx = len(x)

	G = TGraphAsymmErrors(nbinsx, scipy.array(x), scipy.array(y), scipy.array(exl), scipy.array(exh), scipy.array(eyl), scipy.array(eyh))

	return G

def AlphabetFitter(G, F): # Linear fit to output of above function, fitting with form F
	# Want an arbitrary F: Need to provide conversion from Fit to the Error: use Converter.
	G.Fit(F.fit, F.Opt)
	fitter = TVirtualFitter.GetFitter()
	F.Converter(fitter)

# ONLY WORKS WITH &&
def MakeCuts(listOfCuts, notStatus=''):
	if notStatus == '':
		out = '('
	elif notStatus == 'not':
		out = '!('
	for icut in range(len(listOfCuts)):
		out+= listOfCuts[icut]
		# if not on last item
		if icut != len(listOfCuts)-1:
			out+= '&&'
	out+=')'
	return out

#RooDataHist pred("pred", "Prediction from SB", RooArgList( x ), h_SR_Prediction);
#RooFitResult * r_bg=bg.fitTo(pred, RooFit::Range(SR_lo, SR_hi), RooFit::Save());
#RooPlot *aC_plot=x.frame();
#pred.plotOn(aC_plot, RooFit::MarkerColor(kPink+2));
#bg.plotOn(aC_plot, RooFit::VisualizeError(* r_bg, 1), RooFit::FillColor(kGray+1),   RooFit::FillStyle(3001));
#bg.plotOn(aC_plot, RooFit::LineColor(kBlack));
#pred.plotOn(aC_plot, RooFit::LineColor(kBlack), RooFit::MarkerColor(kBlack));
