# TEST AREA
import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy
from optparse import OptionParser

# Our Bstar.Fit.fittions:
import Alphabet_Header
from Alphabet_Header import *
import Plotting_Header
from Plotting_Header import *
import Converters
from Converters import *
import Distribution_Header
from Distribution_Header import *
import Alphabet
from Alphabet import *

ttbar = DIST("ttbar", "TWtreefile_ttbarweighted.root", "Tree", "weight")
ttbar.bstarReweight()

var_array2 = ["tpt", 20,400,1200]

antitag = "(((wmass>30&wmass<65)||(wmass>95))&tau21<0.4)"
tag 	= "((wmass>65&wmass<95)&tau21<0.4)"

plot = TH1F("Hist_NOMINAL_test", "", var_array2[1], var_array2[2], var_array2[3])


temp = plot.Clone("temp") # Allows to add multiple distributions to the plot
chain = ROOT.TChain(ttbar.Tree)
chain.Add(ttbar.File)
chain.Draw(var_array2[0]+">>"+"temp", ttbar.weight+"*"+antitag, "goff") # Actual plotting (and making of the cut + Weighing if necsr)
plot.Add(temp)
tempCanvas = TCanvas("temp", "", 800, 600)
tempCanvas.cd()
plot.Draw()

raw_input("Press a key to continue...")