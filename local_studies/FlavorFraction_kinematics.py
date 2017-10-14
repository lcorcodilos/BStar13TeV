import ROOT
from ROOT import *

from optparse import OptionParser

import FlavorFractionFunctions
from FlavorFractionFunctions import *

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
				  default	=	'QCD',
				  dest		=	'set',
				  help		=	'data or ttbar')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
				  default	=	'sideband',
				  dest		=	'cuts',
				  help		=	'default, sideband, rate_sideband, etc')

(options, args) = parser.parse_args()

# Load cuts - dictionary
# allCuts = LoadTCuts(options.cuts)

inFile = TFile.Open('../rootfiles/35851pb/TWanalyzer'+options.set+'_Trigger_nominal_none_PSET_'+options.cuts+'.root')
inTree = inFile.Get('Tree')

ptFile = TFile('TopPt_Flavors_'+options.set+'_'+options.cuts+'.root','recreate')
ptFile.cd()

partonDict = {'d':1,'u':2,'s':3,'c':4,'b':5,'t':6,'g':21}

for flavor in partonDict.keys():
	hist = TH1F('TopPt_'+flavor,'TopPt_'+flavor,12,400,1000)
	inTree.Project('TopPt_' + flavor, 'tpt', 'abs(flavor)=='+str(partonDict[flavor]))
	ptFile.Write()

ptFile.Close()
