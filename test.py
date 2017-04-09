#! /usr/bin/env python
import os
import glob
import math
from math import sqrt
#import quickroot
#from quickroot import *
import ROOT 
from ROOT import *
import sys
from DataFormats.FWLite import Events, Handle
from optparse import OptionParser
import Bstar_Functions	
from Bstar_Functions import *

TTR = TTR_Init('QUAD','sideband','data','')
TTR_errUp = TTR_Init('QUAD_errUp','sideband','data','')
TTR_errDown = TTR_Init('QUAD_errDown','sideband','data','')



c1 = TCanvas("c1", "c1", 700, 700)
c1.cd()
TTR[0].SetLineColor(1)
TTR[0].Draw()
TTR_errUp[0].SetLineColor(2)
TTR_errUp[0].Draw("same")
TTR_errDown[0].SetLineColor(4)
TTR_errDown[0].Draw("same")


raw_input('Press enter...')
