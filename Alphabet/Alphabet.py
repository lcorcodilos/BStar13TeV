# Class def for full Alphabetization.
# Does everything except the pretty plots, but makes all components available.

import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy
import numpy

# Our functions:
import Alphabet_Header
from Alphabet_Header import *
import Plotting_Header
from Plotting_Header import *
import Converters
from Converters import *
import Distribution_Header
from Distribution_Header import *

class Alphabetizer:
	def __init__(self, name, Dist_Plus, Dist_Minus):
		self.name = name
		self.DP = Dist_Plus
		self.DM = Dist_Minus
	def SetRegions(self, var_array, presel):
	# var_array = [x var, y var, x n bins, x min, x max, y n bins, y min, y max]
		self.X = var_array[0]
		self.Pplots = TH2F("added"+self.name, "", var_array[2], var_array[3],var_array[4],var_array[5],var_array[6],var_array[7])
		self.Mplots = TH2F("subbed"+self.name, "", var_array[2], var_array[3],var_array[4],var_array[5],var_array[6],var_array[7])
		for i in self.DP:
			quick2dplot(i.File, i.Tree, self.Pplots, var_array[0], var_array[1], presel, i.weight)
		for j in self.DM:
			quick2dplot(j.File, j.Tree, self.Mplots, var_array[0], var_array[1], presel, j.weight)
		self.TwoDPlot = self.Pplots.Clone("ThreeDPlot_"+self.name)
		self.TwoDPlot.Add(self.Mplots, -1.)
	# def GetRates(self, cut, bins, truthbins, center, FIT):
	# 	self.center = center
	# 	self.G = AlphabetSlicer(self.TwoDPlot, bins, cut[0], cut[1], center) # makes the A/B slices
	# 	if len(truthbins)>0:
	# 		self.truthG = AlphabetSlicer(self.TwoDPlot, truthbins, cut[0], cut[1], center) # makes the A/B slices
	# 	else:
	# 		self.truthG = None
	# 	self.Fit = FIT # reads the right class in, should be initialized and set up already
	# 	AlphabetFitter(self.G, self.Fit) # creates all three distributions (nominal, up, down)
	# def Get3DRates(self, cut1, cut2, bins, truthbins, center, FIT):
	# 	self.center = center
	# 	self.G = Alphabet3DSlicer(self.ThreeDPlot, bins, cut1[0], cut1[1], cut2[0], cut2[1], center) # makes the A/B/C slices
	# 	if len(truthbins)>0:
	# 		self.truthG = Alphabet3DSlicer(self.ThreeDPlot, truthbins, cut1[0], cut1[1], cut2[0], cut2[1], center) # makes the A/B/C slices
	# 	else:
	# 		self.truthG = None
	# 	self.Fit = FIT # reads the right class in, should be initialized and set up already
	# 	AlphabetFitter(self.G, self.Fit) # creates all three distributions (nominal, up, down)
	def doRates(self, var, varCuts, passCuts, presel, bins, truthbins, fitFunc):
		# LC 11/1/17
		# Does the job of SetRegions and GetRates but doesn't waste time making a multi-dimensional histogram
		# to define cut regions (which is an inexact method!)
		# var - tree variable that we want to look at in range we want to see it
		# varCuts - ex '(mass_top<105)||(mass_top>210)'
		# passCuts - cuts to define 'pass'; a string like '(sjbtag>0.5426)&&(tau32<0.65)'
		# presel - preselection that's always applied
		# bins - bins for var
		self.G = AlphabetNDSlicer(self.DP, self.DM, var, varCuts, passCuts, presel, bins)
		if len(truthbins)>0:
			self.truthG = AlphabetNDSlicer(self.DP, self.DM, var, '!('+varCuts+')', passCuts, presel, truthbins) # makes the A/B/C slices
		else:
			self.truthG = None

		self.Fit = fitFunc # reads the right class in, should be initialized and set up already
		AlphabetFitter(self.G, self.Fit) # creates all three distributions (nominal, up, down)

	def doRatesFlexFit(self, var, varCuts, passCuts, presel, bins, truthbins, fitFunc, center=0):
		# LC 11/14/17
		# Same as doRates but with more flexible fit

		self.G = AlphabetNDSlicer(self.DP, self.DM, var, varCuts, passCuts, presel, bins, center)
		if len(truthbins)>0:
			self.truthG = AlphabetNDSlicer(self.DP, self.DM, var, '!('+varCuts+')', passCuts, presel, truthbins, center) # makes the A/B/C slices
		else:
			self.truthG = None

		self.pG = self.G.Clone()

		# Now do the fitting
		self.fitFunc = fitFunc
		# If we have something with an exponential
		if self.fitFunc.find('exp') != -1:
			paramGuesses, paramUpperLims, paramLowerLims = self.fitParamGuess(self.G,bins,truthbins, center)
			self.Fit = TF1("fit", self.fitFunc, bins[0]-center, bins[-1]-center)
			self.Fit.SetParameter(0,paramGuesses[0])
			self.Fit.SetParameter(1,paramGuesses[1])
			self.Fit.SetParameter(2,paramGuesses[2])
			self.Fit.SetParLimits(0,paramLowerLims[0],paramUpperLims[0])
			self.Fit.SetParLimits(1,paramLowerLims[1],paramUpperLims[1])
			self.Fit.SetParLimits(2,paramLowerLims[2],paramUpperLims[2])
			self.FitResults = self.G.Fit(self.Fit,'BRME')

			# If the fit is bad, try a different set of points
			if self.Fit.GetChisquare() > 4.0:
				paramGuesses2, paramUpperLims2, paramLowerLims2 = self.fitParamGuess(self.G,bins,truthbins, center, True)
				self.Fit2 = TF1("fit", self.fitFunc, bins[0]-center, bins[-1]-center)
				self.Fit2.SetParameter(0,paramGuesses2[0])
				self.Fit2.SetParameter(1,paramGuesses2[1])
				self.Fit2.SetParameter(2,paramGuesses2[2])
				self.Fit2.SetParLimits(0,paramLowerLims2[0],paramUpperLims2[0])
				self.Fit2.SetParLimits(1,paramLowerLims2[1],paramUpperLims2[1])
				self.Fit2.SetParLimits(2,paramLowerLims2[2],paramUpperLims2[2])
				self.Fit2Results = self.G.Fit(self.Fit2,'BRME')
				
				# Check they aren't worse than the ones before
				if self.Fit2.GetChisquare() < self.Fit.GetChisquare():
					self.Fit = self.Fit2
					print 'Found a better fit by switching points'

		else:
			self.Fit = TF1("fit", self.fitFunc, bins[0]-center, bins[-1]-center)
			self.FitResults = self.G.Fit(self.Fit)

		self.EH = TH1F('EH','EH',1000,bins[0]-center,bins[-1]-center)
		self.EG = TGraphErrors(1000)
		for i in range(1000):
			self.EG.SetPoint(i, bins[0]-center + i*(bins[-1]- bins[0])/1000., 0)
			self.EH.SetBinContent(i,0)
		TVirtualFitter.GetFitter().GetConfidenceIntervals(self.EG,0.68)
		TVirtualFitter.GetFitter().GetConfidenceIntervals(self.EH,0.68)
		self.EG.SetLineColorAlpha(kRed,0.2)
		self.Ndof = self.Fit.GetNDF()
		self.Chi2 = self.Fit.GetChisquare()

		

	
	def fitParamGuess(self, graph, bins, truthbins, center, trydiff=False):
		# Creates parameter guess by taking three points and solving the equation
		# for the three parameters for those points.
		# ONLY WORKS FOR GAUSSIAN OVER DECAYING EXPONENTIAL
		# fitFunc - string of the fit with parameters in [] form
		# graph - the graph of the three points (should just be self.G)
		# bins and truthbins - same as doRatesFlexFit, used to determine the third point to use 

		# First pick the points to evaluate
		xpoint1 = (bins[0]+bins[1])/2 - center # second point
		xpoint2 = (bins[4]+bins[3])/2 - center # fourth point
		# Will try two different 3rd points because sometimes the fit is really bad with one or the other
		# Will only try second config if Chi2 of first is > 4
		if trydiff == False:
			xpoint3 = (bins[bins.index(truthbins[-1])+1] + truthbins[-1])/2 - center # first point after truth gap
		elif trydiff == True:
			xpoint3 = (bins[-1]+bins[-2])/2 - center # last point

		for xpoint in [xpoint1,xpoint2,xpoint3]:
			print '['+str(xpoint)+', '+str(graph.Eval(xpoint))+']'


		# ASSUMES FUNCTION OF FORM a*exp(x*b-x**2*c) - will solve using numpy.linalg.solve(a,b)
		# where a*x=b
		# Technically we solve ln(y) = -c*x**2 + b*x + a
		aMatrix = numpy.array([[1,xpoint1,-(xpoint1**2)],[1,xpoint2,-(xpoint2**2)],[1,xpoint3,-(xpoint3**2)]])
		bVector = numpy.array([math.log(graph.Eval(xpoint1)),math.log(graph.Eval(xpoint2)),math.log(graph.Eval(xpoint3))])
		sol = numpy.linalg.solve(aMatrix,bVector)

		# Solution is ordered [log(a),b,c] so need to take e^a to get final values
		paramGuesses = [math.exp(sol[0]),sol[1],sol[2]]
		print paramGuesses
		paramUpperLims = []
		paramLowerLims = []
		for p in paramGuesses:
			if p <=0:
				print 'A parameter is less than zero and shouldnt be! ' + str(p)
				p = -1*p
				print 'Changed to ' + str(p)
			# Do some upper limits based on the order of the parameter (lower limts can just be 0)

			# This was tested in isolated environment and works
			# Example - 160 returns 1000 and 0.005 returns 0.01
			# order = 1.
			# if p > order:
			# 	while p > order:
			# 		thisOrder = int(order*10)
			# 		order = order*10.
			# elif p < order:
			# 	while p < order:
			# 		thisOrder = order
			# 		order = order/10.
			# paramUpperLims.append(thisOrder)
			paramUpperLims.append(2.*p)
			paramLowerLims.append(0.*p)
		return paramGuesses, paramUpperLims, paramLowerLims


	# DOESN'T WORK WITH CURRENT FITTING CODE
	def MakeEst(self, var_array, rate_var, antitag, tag, center=0):
	# makes an estimate in a region, based on an anti-tag region, of that variable in all dists
	# var_array - array for what we are plotting 
	# rate_var - var in which the rate was made
		self.Fit.MakeConvFactor(rate_var, center)
		self.hists_EST = []
		self.hists_EST_SUB = []
		self.hists_EST_UP = []
		self.hists_EST_SUB_UP = []
		self.hists_EST_DN = []
		self.hists_EST_SUB_DN = []
		self.hists_MSR = []
		self.hists_MSR_SUB = []
		self.hists_ATAG = []
		for i in self.DP:
			temphist = TH1F("Hist_VAL"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			temphistN = TH1F("Hist_NOMINAL"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			temphistU = TH1F("Hist_UP"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			temphistD = TH1F("Hist_DOWN"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			temphistA = TH1F("Hist_ATAG"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			quickplot(i.File, i.Tree, temphist, var_array[0], tag, i.weight)
			quickplot(i.File, i.Tree, temphistN, var_array[0], antitag, "("+i.weight+"*"+self.Fit.ConvFact+")")
			quickplot(i.File, i.Tree, temphistU, var_array[0], antitag, "("+i.weight+"*"+self.Fit.ConvFactUp+")")
			quickplot(i.File, i.Tree, temphistD, var_array[0], antitag, "("+i.weight+"*"+self.Fit.ConvFactDn+")")
			quickplot(i.File, i.Tree, temphistA, var_array[0], antitag, i.weight)
			self.hists_MSR.append(temphist)
			self.hists_EST.append(temphistN)
			self.hists_EST_UP.append(temphistU)
			self.hists_EST_DN.append(temphistD)
			self.hists_ATAG.append(temphistA) 
		for i in self.DM:
			temphist = TH1F("Hist_SUB_VAL"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			temphistN = TH1F("Hist_SUB_NOMINAL"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			temphistU = TH1F("Hist_SUB_UP"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			temphistD = TH1F("Hist_SUB_DOWN"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			temphistA = TH1F("Hist_SUB_ATAG"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			quickplot(i.File, i.Tree, temphist, var_array[0], tag, i.weight)
			quickplot(i.File, i.Tree, temphistN, var_array[0], antitag, "("+i.weight+"*"+self.Fit.ConvFact+")")
			quickplot(i.File, i.Tree, temphistU, var_array[0], antitag, "("+i.weight+"*"+self.Fit.ConvFactUp+")")
			quickplot(i.File, i.Tree, temphistD, var_array[0], antitag, "("+i.weight+"*"+self.Fit.ConvFactDn+")")
			quickplot(i.File, i.Tree, temphistA, var_array[0], antitag, i.weight)
			self.hists_MSR_SUB.append(temphist)
			self.hists_EST_SUB.append(temphistN)
			self.hists_EST_SUB_UP.append(temphistU)
			self.hists_EST_SUB_DN.append(temphistD)
			self.hists_ATAG.append(temphistA)

	def MakeEstFlexFit(self, var_array, rate_var, antitag, tag, center=0, twod=0, twodMode=0):
	# makes an estimate in a region, based on an anti-tag region, of that variable in all dists
	# var_array - array for what we are plotting 
	# rate_var - var in which the rate was made
	# twod - 0 if no 2D fit, 2D fit Tfile otherwise
	# twodMode - center of Mtw bin if running twod and want to do discrete Rpf weighting, 0 otherwise
		print self.fitFunc
		if twod == 0:
			fitString = CustomFit2String(rate_var,self.fitFunc,str(center),twod,twodMode,self.Fit)
			twodstring = ''
		else:
			fitString = CustomFit2String(rate_var,self.fitFunc,str(center),twod,twodMode)
			twodstring = '2d'

		print 'Fit = ' + fitString
		self.hists_EST = []
		self.hists_EST_SUB = []
		self.hists_MSR = []
		self.hists_MSR_SUB = []
		self.hists_ATAG = []
		for i in self.DP:
			temphist = TH1F("Hist_VAL"+twodstring+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			temphistN = TH1F("Hist_NOMINAL"+twodstring+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			temphistA = TH1F("Hist_ATAG"+twodstring+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			quickplot(i.File, i.Tree, temphist, var_array[0], tag, i.weight)
			quickplot(i.File, i.Tree, temphistN, var_array[0], antitag, "("+i.weight+"*"+fitString+")")
			quickplot(i.File, i.Tree, temphistA, var_array[0], antitag, i.weight)
			self.hists_MSR.append(temphist)
			self.hists_EST.append(temphistN)
			self.hists_ATAG.append(temphistA) 
		for i in self.DM:
			temphist = TH1F("Hist_SUB_VAL"+twodstring+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			temphistN = TH1F("Hist_SUB_NOMINAL"+twodstring+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			temphistA = TH1F("Hist_SUB_ATAG"+twodstring+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
			quickplot(i.File, i.Tree, temphist, var_array[0], tag, i.weight)
			quickplot(i.File, i.Tree, temphistN, var_array[0], antitag, "("+i.weight+"*"+fitString+")")
			quickplot(i.File, i.Tree, temphistA, var_array[0], antitag, i.weight)
			self.hists_MSR_SUB.append(temphist)
			self.hists_EST_SUB.append(temphistN)
			self.hists_ATAG.append(temphistA)

	
def CustomFit2String(var,fitFunc,center,twod,twodMode=0,fit=False):
	# Need to convert the fitFunc (of form '[0]+[1]*x...') to a string
	# with the actual parameters in for [0],[1], etc and 'x' replace with our var
	# twod - 0 if not running 2D fit, is the relevant 2D Tfile otherwise
	thisFitFunc = '('
	
	# Need to have our own find algo to avoid messing up exp when 'x' gets replaced with var
	# .find cannot be used with .replace because .find only finds the index of the first instance and
	# .replace replaces all instances. Can't pick and choose instances then.

	# Build an index of all 'real x's
	xIndex = []
	for ichar in range(len(fitFunc)):
		char = fitFunc[ichar]
		if char == "x" and fitFunc[ichar-1] != 'e' and fitFunc[ichar+1] != 'p':
			xIndex.append(ichar)

	# Now build a new string with any 'real' x replaced by var
	for ix in range(len(xIndex)):
		# If on the first value, start at 0, end at first x
		if ix == 0:
			start = 0
			stop = xIndex[ix]
		# otherwise, start IN FRONT of the ix-1 value (+1 because you don't want to include the x)
		else:
			start = xIndex[ix-1]+1
			stop = xIndex[ix]
		# need to grab left side of string and then rebuild the string
		leftside = fitFunc[start:stop]

		thisFitFunc += leftside + '(' + var + '-' + str(center) + ')'

	# Finish up by adding the final right side
	thisFitFunc += fitFunc[xIndex[-1]+1:]

	# Now swap in the parameter values
	if twod == 0:
		pars = []
		for ipar in range(fit.GetNpar()):
			thisPar = str(fit.GetParameter(ipar))
			thisFitFunc = thisFitFunc.replace('['+str(ipar)+']','('+thisPar+')')
	else:
		paramFits = {} # Dictionary of parameters for the fits of the Mtw slice parameters
		nParams = 0
		# Sort through the keys in the file and find the p*fit objects
		for key in twod.GetListOfKeys():
			if key.GetClassName() == 'TF1':
				# Grab the fit and get the parameters and store in paramFits dictionary
				keyname = key.GetName()
				thisFit = twod.Get(keyname)
				nParams+=1
				paramFits[keyname] = []
				for ipar in range(thisFit.GetNpar()):
					paramFits[keyname].append(thisFit.GetParameter(ipar))
		
		# Now construct a 2D fit string to feed into MakeEstFlexFit() -- SPECIFIC TO PARAMETERS BEING FIT WITH A LINE
		if twodMode != 0:
			for ipar in range(nParams):
				thisP0 = str(paramFits['p'+str(ipar)+'fit'][0])
				thisP1 = str(paramFits['p'+str(ipar)+'fit'][1])
				thisFittedParameterFunction = '('+thisP0+'+('+twodMode+')*'+thisP1+')'
				thisFitFunc = thisFitFunc.replace('['+str(ipar)+']',thisFittedParameterFunction)

		else:
			for ipar in range(nParams):
				thisP0 = str(paramFits['p'+str(ipar)+'fit'][0])
				thisP1 = str(paramFits['p'+str(ipar)+'fit'][1])
				thisFittedParameterFunction = '('+thisP0+'+(mass_tw)*'+thisP1+')'
				thisFitFunc = thisFitFunc.replace('['+str(ipar)+']',thisFittedParameterFunction)


	return thisFitFunc+')'

