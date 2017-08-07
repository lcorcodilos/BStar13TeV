import ROOT
from ROOT import *
from optparse import OptionParser
parser = OptionParser()

parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
(options, args) = parser.parse_args()


ModFile = TFile("ModMassFile_"+options.cuts+".root")

hist = ModFile.Get("rtmass")
newHist = hist.Clone("ModPlot")
gStyle.SetOptStat(0)

c = TCanvas('c','c',800,600)

newHist.GetXaxis().SetTitle("M_{t} (GeV)")
newHist.GetYaxis().SetTitle("Weight")

c.SetBottomMargin(0.15)
newHist.SetTitle('')
newHist.Draw()
c.Print("ModMass_"+options.cuts+".pdf","pdf")