# Dist def
import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy

import Plotting_Header
from Plotting_Header import *

import sys
sys.path.append('..')
import Bstar_Functions
from Bstar_Functions import LoadConstants

class DIST:
	def __init__(self, name, File, Tree, weight):
		self.name = name
		self.File = File
		self.Tree = Tree
		self.weight = weight

	# Lucas' code below
	def bstarReweight(self):
		try:
			rootFile = TFile(self.File, "READ")
			weightTree = rootFile.Get("Weight")
			# weightv = array('d',[0])
			# weightTree.SetBranchAddress("weightv",weightv)
			weightTree.GetEntry(0)
			self.weight = "("+self.weight+"*"+str(weightTree.weightv)+")"
			print "New weight for " + self.name + " is " + self.weight
			rootFile.Close()
		except:
			print 'Weight tree not found in file - recalculating weight'

			# Load up the proper lumi and xsec
			Cons = LoadConstants()
			lumi = Cons['lumi']
			process = self.name.split('_')[0].split('HT')[0].lower()
			xsecs = Cons['xsec_'+process]
			
			if process == 'qcd':
				thisSet = self.name[self.name.find('HT'):]
			elif process == 'ttbar':
				thisSet = 'PH'
			elif process == 'st':
				thisSet = self.name[self.name.find('_')+1:].upper()
			
			thisXsec = xsecs[thisSet]

			# Get the number of events from the file
			rootFile = TFile(self.File, 'READ')
			nev = rootFile.Get('nev')
			events = float(nev.Integral())

			# Now make the normalization weight (lumi*xsec/number of events)
			newWeight = lumi*thisXsec/events
			self.weight = "("+self.weight+"*"+str(newWeight)+")"
			print "New weight for " + self.name + " is " + self.weight
			rootFile.Close()




