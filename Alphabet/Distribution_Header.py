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

class DIST:
	def __init__(self, name, File, Tree, weight):
		self.name = name
		self.File = File
		self.Tree = Tree
		self.weight = weight

	# Lucas' code below
	def bstarReweight(self):
		rootFile = TFile(self.File, "READ")
		weightTree = rootFile.Get("Weight")
		weightv = array('d',[0])
		weightTree.SetBranchAddress("weightv",weightv)
		weightTree.GetEntry(0)
		print "Old weight for " + self.name + " is " + self.weight
		self.weight = "("+self.weight+"*"+str(weightv[0])+")"
		print "New weight for " + self.name + " is " + self.weight
		rootFile.Close()