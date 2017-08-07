import ROOT
from ROOT import *
from optparse import OptionParser

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
				  default	=	'data',
				  dest		=	'set',
				  help		=	'data or ttbar')
parser.add_option('-n', '--num', metavar='F', type='string', action='store',
				  default	=	'all',
				  dest		=	'num',
				  help		=	'job number')
parser.add_option('-j', '--jobs', metavar='F', type='string', action='store',
				  default	=	'1',
				  dest		=	'jobs',
				  help		=	'number of jobs')
(options, args) = parser.parse_args()
print "Options summary"
print "=================="
for  opt,value in options.__dict__.items():
	#print str(option)+ ": " + str(options[option]) 
	print str(opt) +': '+ str(value)
print "=================="
print ""
di = ""
if options.grid == 'on':
	di = "tardir/"
	sys.path.insert(0, 'tardir/')

gROOT.Macro(di+"rootlogon.C")

import Bstar_Functions	
from Bstar_Functions import *


#----Trigger Naming------
tname = options.tname.split(',')
tnamestr = ''
for iname in range(0,len(tname)):
	tnamestr+=tname[iname]
	if iname!=len(tname)-1:
		tnamestr+='OR'

		
if tnamestr=='HLT_PFHT900ORHLT_AK8PFJet450':
	tnameformat='nominal'
elif tnamestr=='':
	tnameformat='none'
else:
	tnameformat=tnamestr
		

#------Basics-----------
pie = math.pi 

#Load up cut values based on what selection we want to run 
Cuts = LoadCuts(options.cuts)
wpt = Cuts['wpt']
tpt = Cuts['tpt']
dy = Cuts['dy']
tmass = Cuts['tmass']
tau32 = Cuts['tau32']
tau21 = Cuts['tau21']
sjbtag = Cuts['sjbtag']
wmass = Cuts['wmass']
eta1 = Cuts['eta1']
eta2 = Cuts['eta2']

Cons = LoadConstants()
lumi = Cons['lumi']
Lumi = str(lumi/1000)+'fb'

#------For large datasets we need to parallelize the processing
jobs=int(options.jobs)
if jobs != 1:
	num=int(options.num)
	jobs=int(options.jobs)
	print "Running over " +str(jobs)+ " jobs"
	print "This will process job " +str(num)
else:
	print "Running over all events"

mainDir = "/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/BStar13TeV/TTrees/"
file = TFile(mainDir + "TWtreefile_"+options.set+"_Trigger_nominal_none.root")

tree = file.Get("Tree")

if jobs != 1:
	f = TFile( "Tau21vWmass_"+options.set+"_job"+options.num+"of"+options.jobs+".root", "recreate" )
else:
	f = TFile( "Tau21vWmass_"+options.set+".root", "recreate" )


c1 = TCanvas("c1","c1",600,600)

Tau21vWmass = TH2F('Tau21vWmass', 'Tau21vWmass', 20, 0, 500, 10, 0, 1)
Tau21vWmass.Sumw2()

print "Hist made"

count = 0
jobiter = 0
print "Start looping"
treeEntries = tree.GetEntries()

# Design the splitting if necessary
if jobs != 1:
	evInJob = int(treeEntries/jobs)
	
	lowBinEdge = evInJob*(num-1)
	highBinEdge = evInJob*num

	if num == jobs:
		highBinEdge = treeEntries

else:
	lowBinEdge = 0
	highBinEdge = treeEntries

nev.SetBinContent(1,B2Gnev)
print "Range of events: (" + str(lowBinEdge) + ", " + str(highBinEdge) + ")"

for entry in range(lowBinEdge,highBinEdge):
	tree.GetEntry(entry)
	count	= 	count + 1

	if count % 100000 == 0 :
	  print  '--------- Processing Event ' + str(count) +'   -- percent complete ' + str(100*count/(highBinEdge-lowBinEdge)) + '% -- '

	doneAlready = False

	for hemis in ['hemis0','hemis1']:
		if hemis == 'hemis0':
			# Load up the ttree values
			tVals = {
				"tau1":tree.tau1_leading,
				"tau2":tree.tau2_leading,
				"tau3":tree.tau3_leading,
				"phi":tree.phi_leading,
				"mass":tree.mass_leading,
				"pt":tree.pt_leading,
				"eta":tree.eta_leading,
				"sjbtag":tree.sjbtag_leading,
				"SDmass":tree.SDmass_leading
			}

			wVals = {
				"tau1":tree.tau1_subleading,
				"tau2":tree.tau2_subleading,
				"tau3":tree.tau3_subleading,
				"phi":tree.phi_subleading,
				"mass":tree.mass_subleading,
				"pt":tree.pt_subleading,
				"eta":tree.eta_subleading,
				"sjbtag":tree.sjbtag_subleading,
				"SDmass":tree.SDmass_subleading
			}

		if hemis == 'hemis1' and doneAlready == False  :
			wVals = {
				"tau1":tree.tau1_leading,
				"tau2":tree.tau2_leading,
				"tau3":tree.tau3_leading,
				"phi":tree.phi_leading,
				"mass":tree.mass_leading,
				"pt":tree.pt_leading,
				"eta":tree.eta_leading,
				"sjbtag":tree.sjbtag_leading,
				"SDmass":tree.SDmass_leading
			}

			tVals = {
				"tau1":tree.tau1_subleading,
				"tau2":tree.tau2_subleading,
				"tau3":tree.tau3_subleading,
				"phi":tree.phi_subleading,
				"mass":tree.mass_subleading,
				"pt":tree.pt_subleading,
				"eta":tree.eta_subleading,
				"sjbtag":tree.sjbtag_subleading,
				"SDmass":tree.SDmass_subleading
			}

		elif hemis == 'hemis1' and doneAlready == True:
			continue

		# Remake the lorentz vectors
		tjet = TLorentzVector()
		tjet.SetPtEtaPhiM(tVals["pt"],tVals["eta"],tVals["phi"],tVals["mass"])

		wjet = TLorentzVector()
		wjet.SetPtEtaPhiM(wVals["pt"],wVals["eta"],wVals["phi"],wVals["mass"])

		ht = tjet.Perp() + wjet.Perp()

		if ht < 1100.0:
			continue

		weight = 1.0

		
		
	cList[i].Print('Plot_Tau21vWmass_'+stringList[i]+'.pdf','pdf')
	print "done"


