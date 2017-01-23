
###################################################################
##								 ##
## Name: Bstar_Functions.py	   			         ##
## Author: Kevin Nash 						 ##
## Date: 5/13/2015						 ##
## Purpose: This contains all functions used by the              ##
##	    analysis.  A method is generally placed here if 	 ##
##	    it is called more than once in reproducing all	 ##
##	    analysis results.  The functions contained here 	 ##
##	    Are capable of tuning the analysis - such as changing##
##	    cross sections, updating lumi, changing file	 ##
##	    locations, etc. with all changes propegating 	 ##
##	    to all relevant files automatically.  		 ##
##								 ##
###################################################################


import os
import array
import glob
import math
from math import sqrt
import ROOT
import sys
import cppyy
from array import *
from ROOT import *
from DataFormats.FWLite import Events, Handle
#This is the most impostant Function.  Correct information here is essential to obtaining valid results.
#In order we have Luminosity, top tagging scale factor, cross sections for wprime right,left,mixed,ttbar,qcd, and singletop and their corresponding event numbers
#If I wanted to access the left handed W' cross section at 1900 GeV I could do Xsecl1900 = LoadConstants()['xsec_wpl']['1900']
def LoadConstants():
	 return  {
		'lumi':2530.0,
		'wtagsf':0.979,
		'wtagsfsig':0.979,
		'xsec_bsl':{'1200': 1.944,'1400': 0.7848,'1600': 0.3431,'1800': 0.1588,'2000': 0.07711,'2200': 0.03881,'2400': 0.02015,'2600': 0.01073,'2800': 0.005829,'3000': 0.003234},
		'xsec_bsr':{'1200': 1.936,'1400': 0.7816,'1600': 0.3416,'1800': 0.1583,'2000': 0.07675,'2200': 0.03864,'2400': 0.02008,'2600': 0.01068,'2800': 0.005814,'3000': 0.003224},
		'xsec_bpl':{'B1200': 0.0016852,'B1400': 0.0007134,'B1600': 0.0003220,'B1800': 0.0001523,'T1200': 0.0016852,'T1400': 0.0007134,'T1600': 0.0003220,'T1800': 0.0001523},
		'xsec_ttbar':{'MG':831.76,'PH':831.76,'PHscaleup':831.76,'PHscaledown':831.76},
		'xsec_qcd':{'300':7823,'470':648.2,'600':186.9,'800':32.293,'1000':9.4183,'1400':0.84265,'800_BROKEN':32.293,'FLAT7000':2022100000,'HT500':31630,'HT700':6802,'HT1000':1206,'HT1500':120.4,'HT2000':25.25},
		'xsec_st':{'S':11.36,'T':216.97,'TW':35.85,'TWB':35.85},
		#'nev_bsl':{'800':197537,'900':197119 ,'1000': 196274,'1100':195982,'1200': 189705,'1300': 194684,'1400':193308 ,'1500': 193758,'1600':190049,'1700': 193192,'1800':192717 ,'1900': 189458,'2000':174468},		
		'nev_bsr':{'1200':100000,'1400':98200,'1600':100000,'1800':97600,'2000':99200,'2200':100000,'2400':97800,'2600':99200,'2800':99200,'3000':100000},
		'nev_bpl':{'B1200': 100000,'B1400': 99200,'B1600': 99200,'B1800': 97600, 'T1200': 299200, 'T1400': 300000,'T1600': 293400,'T1800': 299600},
		'nev_ttbar':{'MG':11339232, 'PH':186921800,'PHscaleup':38411467,'PHscaledown':39461147},
 		'nev_qcd':{'300':2933611,'470':1936832,'600':1964128,'800':1937216,'1000':1487136,'1400':197959,'FLAT7000':209851.27,'HT500':19665695,'HT700':15547962,'HT1000':5049267,'HT1500':3939077,'HT2000':1981228},
		'nev_st':{'S':984400,'T':49858384,'TW':1000000 ,'TWB':999400}
		}

#This is also a very impostant Function.  The analysis runs on "PSETS", which correspond to the TYPE variable here.
#These each load a cut profile.  For instance 'default' is the standard selection used to set limits
def LoadCuts(TYPE):
	if TYPE=='default':
 		return  {
			'wpt':[400.0,float("inf")],
			'tpt':[400.0,float("inf")],
			'dy':[0.0,1.8],
			'tmass':[110.0,210.0],
			'nsubjets':[1,10],
			'tau32':[0.0,0.61],
			'tau21':[0.0,0.6],
			'minmass':[-float("inf"),float("inf")],
			'sjbtag':[0.760,1.0],
			'wmass':[65.0,105.0],
			'eta1':[0.0,0.8],
			'eta2':[0.8,2.4]
			}
	if TYPE=='rate_default':
 		return  {
			'wpt':[400.0,float("inf")],
			'tpt':[400.0,float("inf")],
			'dy':[0.0,1.8],
			'tmass':[110.0,210.0],
			'nsubjets':[1,10],
			'tau32':[0.0,0.61],
			'tau21':[0.0,0.6],
			'minmass':[-float("inf"),float("inf")],
			'sjbtag':[0.760,1.0],
			'wmass':[[30.0,65.0],[105,float("inf")]],
			'eta1':[0.0,0.8],
			'eta2':[0.8,2.4]
			}
	# Used for ttbar validation
	if TYPE=='sideband1':
 		return  {
			'wpt':[400.0,float("inf")],
			'tpt':[400.0,float("inf")],
			'dy':[0.0,1.8],
			'tmass':[110.0,210.0],
			'nsubjets':[1,10],
			'tau32':[0.0,0.61],
			'tau21':[0.6,1.0],
			'minmass':[-float("inf"),float("inf")],
			'sjbtag':[0.760,1.0],
			'wmass':[130.0,float("inf")],
			'eta1':[0.0,0.8],
			'eta2':[0.8,2.4]
			}
	if TYPE=='rate_sideband1':
 		return  {
			'wpt':[400.0,float("inf")],
			'tpt':[400.0,float("inf")],
			'dy':[0.0,1.8],
			'tmass':[110.0,210.0],
			'nsubjets':[1,10],
			'tau32':[0.0,0.61],
			'tau21':[0.0,0.6],
			'minmass':[-float("inf"),float("inf")],
			'sjbtag':[0.760,1.0],
			'wmass':[[30.0,65.0],[105.0,130.0]],
			'eta1':[0.0,0.8],
			'eta2':[0.8,2.4]
			}
	# Sideband closure test
	if TYPE=='sideband':
 		return  {
			'wpt':[400.0,float("inf")],
			'tpt':[400.0,float("inf")],
			'dy':[0.0,1.8],
			'tmass':[110.0,210.0],
			'nsubjets':[1,10],
			'tau32':[0.0,0.61],
			'tau21':[0.6,1.0],
			'minmass':[-float("inf"),float("inf")],
			'sjbtag':[0.760,1.0],
			'wmass':[[30.0,65.0],[105.0,130.0]],
			'eta1':[0.0,0.8],
			'eta2':[0.8,2.4]
			}
	if TYPE=='rate_sideband':
 		return  {
			'wpt':[400.0,float("inf")],
			'tpt':[400.0,float("inf")],
			'dy':[0.0,1.8],
			'tmass':[110.0,210.0],
			'nsubjets':[1,10],
			'tau32':[0.0,0.61],
			'tau21':[0.0,0.6],
			'minmass':[-float("inf"),float("inf")],
			'sjbtag':[0.760,1.0],
			'wmass':[[30.0,65.0],[105.0,130.0]],
			'eta1':[0.0,0.8],
			'eta2':[0.8,2.4]
			}

#This function loads up Ntuples based on what type of set you want to analyze.  
#This needs to be updated whenever new Ntuples are produced (unless the file locations are the same).
def Load_Ntuples(string,bx):
	print 'running on ' + string 
	if string == 'ttbar':
 		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/TT_TuneCUETP8M1_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M1_13TeV-powheg-pythia8_B2GAnaFW_V1p2_76x_Slim_V12/*/0000/*.root")
	if string == 'ttbarscaleup':
 		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/TT_TuneCUETP8M1_13TeV-powheg-scaleup-pythia8/crab_TT_TuneCUETP8M1_13TeV-powheg-scaleup-pythia8_B2GAnaFW_V2p1_76x_Slim_V12/*/0000/*.root")
	if string == 'ttbarscaledown':
 		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/TT_TuneCUETP8M1_13TeV-powheg-scaledown-pythia8/crab_TT_TuneCUETP8M1_13TeV-powheg-scaledown-pythia8_B2GAnaFW_V2p1_76x_Slim_V12/*/0000/*.root")


	if string == 'QCDHT500':
 		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1p1_76x_Slim_V12/*/0000/*.root")
 	if string == 'QCDHT700':
 		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1p1_76x_Slim_V12/*/0000/*.root")
 	if string == 'QCDHT1000':
 		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1p1_76x_Slim_V12/*/0000/*.root")
 	if string == 'QCDHT1500':
 		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1p1_76x_Slim_V12/*/0000/*.root")
	if string == 'QCDHT2000':
 		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1p1_76x_Slim_V12/*/0000/*.root")

	
	if string == 'data':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/JetHT/crab_JetHT_Run2015D-16Dec2015_B2GAnaFW_V1p3_76x_Slim_V12_v1/*/0000/*.root")
		#files += glob.glob("/uscms_data/d3/knash/SlimNtuples/JetHT/crab_JetHT_Run2015D-PromptReco-v4_B2GAnaFW_V8p4_Slim_V10/*/0000/*.root")



	if string == 'signalRH1200':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BstarToTW_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BStar13TeV_V2p1_RH_B2GAnaFW_M1200_76x_Slim_V12/*/0000/*.root")
	if string == 'signalRH1400':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BstarToTW_M-1400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BStar13TeV_V2p1_RH_B2GAnaFW_M1400_76x_Slim_V12/*/0000/*.root")
	if string == 'signalRH1600':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BstarToTW_M-1600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BStar13TeV_V2p1_RH_B2GAnaFW_M1600_76x_Slim_V12/*/0000/*.root")
	if string == 'signalRH1800':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BstarToTW_M-1800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BStar13TeV_V2p1_RH_B2GAnaFW_M1800_76x_Slim_V12/*/0000/*.root")
	if string == 'signalRH2000':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BstarToTW_M-2000_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BStar13TeV_V2p1_RH_B2GAnaFW_M2000_76x_Slim_V12/*/0000/*.root")
	if string == 'signalRH2200':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BstarToTW_M-2200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BStar13TeV_V2p1_RH_B2GAnaFW_M2200_76x_Slim_V12/*/0000/*.root")
	if string == 'signalRH2400':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BstarToTW_M-2400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BStar13TeV_V2p1_RH_B2GAnaFW_M2400_76x_Slim_V12/*/0000/*.root")
	if string == 'signalRH2600':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BstarToTW_M-2600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BStar13TeV_V2p1_RH_B2GAnaFW_M2600_76x_Slim_V12/*/0000/*.root")
	if string == 'signalRH2800':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BstarToTW_M-2800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BStar13TeV_V2p1_RH_B2GAnaFW_M2800_76x_Slim_V12/*/0000/*.root")
	if string == 'signalRH3000':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BstarToTW_M-3000_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BStar13TeV_V2p1_RH_B2GAnaFW_M3000_76x_Slim_V12/*/0000/*.root")

	if string == 'signalLH1200':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/*/0000/*.root")
	if string == 'signalLH1400':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-1400_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-1400_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/*/0000/*.root")
	if string == 'signalLH1600':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-1600_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-1600_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/*/0000/*.root")
	if string == 'signalLH1800':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-1800_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-1800_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/*/0000/*.root")
	if string == 'signalLH2000':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-2000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-2000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/*/0000/*.root")
	if string == 'signalLH2200':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-2200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-2200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/*/0000/*.root")
	if string == 'signalLH2400':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-2400_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-2400_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/*/0000/*.root")
	if string == 'signalLH2600':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-2600_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-2600_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/*/0000/*.root")
	if string == 'signalLH2800':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-2800_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-2800_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/*/0000/*.root")
	if string == 'signalLH3000':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-3000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-3000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/*/0000/*.root")


	if string == 'BprimeBToTW1200':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BprimeBToTW_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BPrime_B_RH_13TeV_B2GAnaFW_M1200_Slim_V7/160201_192733/0000/*.root")
	if string == 'BprimeBToTW1400':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BprimeBToTW_M-1400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BPrime_B_RH_13TeV_B2GAnaFW_M1400_Slim_V7/160201_192745/0000/*.root")
	if string == 'BprimeBToTW1600':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BprimeBToTW_M-1600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BPrime_B_RH_13TeV_B2GAnaFW_M1600_Slim_V7/160201_192723/0000/*.root")
	if string == 'BprimeBToTW1800':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BprimeBToTW_M-1800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BPrime_B_RH_13TeV_B2GAnaFW_M1800_Slim_V7/160201_192757/0000/*.root")

	if string == 'BprimeTToTW1200':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BprimeTToTW_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BPrime_T_RH_13TeV_B2GAnaFW_M1200_Slim_V7/160201_192821/0000/*.root")
	if string == 'BprimeTToTW1400':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BprimeTToTW_M-1400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BPrime_T_RH_13TeV_B2GAnaFW_M1400_Slim_V7/160201_192834/0000/*.root")
	if string == 'BprimeTToTW1600':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BprimeTToTW_M-1600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BPrime_T_RH_13TeV_B2GAnaFW_M1600_Slim_V7/160201_192847/0000/*.root")
	if string == 'BprimeTToTW1800':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/BprimeTToTW_M-1800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BPrime_T_RH_13TeV_B2GAnaFW_M1800_Slim_V7/160201_192857/0000/*.root")


	if string == 'BprimeB2GBToTW1200':
		files = glob.glob("/eos/uscms/store/user/knash/BprimeBToTW_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BprimeBToTW_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_V8p4_25ns/160129_184718/0000/*.root")
	if string == 'BprimeB2GBToTW1400':
		files = glob.glob("/eos/uscms/store/user/knash/BprimeBToTW_M-1400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BprimeBToTW_M-1400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_V8p4_25ns/160129_190629/0000/*.root")
	if string == 'BprimeB2GBToTW1600':
		files = glob.glob("/eos/uscms/store/user/knash/BprimeBToTW_M-1600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BprimeBToTW_M-1600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_v2_B2GAnaFW_V8p4_25ns/160129_203107/0000/*.root")
	if string == 'BprimeB2GBToTW1800':
		files = glob.glob("/eos/uscms/store/user/knash/BprimeBToTW_M-1800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BprimeBToTW_M-1800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_V8p4_25ns/160129_190700/0000/*.root")

	if string == 'BprimeB2GTToTW1200':
		files = glob.glob("/eos/uscms/store/user/knash/BprimeTToTW_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BprimeTToTW_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_V8p4_25ns/160129_190716/0000/*.root")
	if string == 'BprimeB2GTToTW1400':
		files = glob.glob("/eos/uscms/store/user/knash/BprimeTToTW_M-1400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BprimeTToTW_M-1400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_V8p4_25ns/160129_190736/0000/*.root")
	if string == 'BprimeB2GTToTW1600':
		files = glob.glob("/eos/uscms/store/user/knash/BprimeTToTW_M-1600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BprimeTToTW_M-1600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_V8p4_25ns/160129_190751/0000/*.root")
	if string == 'BprimeB2GTToTW1800':
		files = glob.glob("/eos/uscms/store/user/knash/BprimeTToTW_M-1800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BprimeTToTW_M-1800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_V8p4_25ns/160129_195310/0000/*.root")


	if string == 'singletop_tW':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/crab_ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_V1p1_76x_Slim_V12/*/0000/*.root")
	if string == 'singletop_tWB':
		files = glob.glob("/uscms_data/d3/knash/SlimNtuples/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/crab_ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_V1p1_76x_Slim_V12/*/0000/*.root")

	# For B2G event counting
	if string == 'B2Gttbarup':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/TT_TuneCUETP8M1_13TeV-powheg-scaleup-pythia8/crab_TT_TuneCUETP8M1_13TeV-powheg-scaleup-pythia8_B2GAnaFW_76X_V2p1/160505_142719/0000/*.root")
	if string == 'B2Gttbardown':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/TT_TuneCUETP8M1_13TeV-powheg-scaledown-pythia8/crab_TT_TuneCUETP8M1_13TeV-powheg-scaledown-pythia8_B2GAnaFW_76X_V2p1/*/0000/*.root")
	if string == 'B2GsignalRH1200':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_76X_V2p1/*/0000/*.root")
	if string == 'B2GsignalRH1400':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-1400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-1400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_76X_V2p1/*/0000/*.root")
	if string == 'B2GsignalRH1600':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-1600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-1600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_76X_V2p1/*/0000/*.root")
	if string == 'B2GsignalRH1800':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-1800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-1800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_76X_V2p1/*/0000/*.root")
	if string == 'B2GsignalRH2000':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-2000_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-2000_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_76X_V2p1/*/0000/*.root")
	if string == 'B2GsignalRH2200':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-2200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-2200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_76X_V2p1/*/0000/*.root")
	if string == 'B2GsignalRH2400':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-2400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-2400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_76X_V2p1/*/0000/*.root")
	if string == 'B2GsignalRH2600':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-2600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-2600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_76X_V2p1/*/0000/*.root")
	if string == 'B2GsignalRH2800':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-2800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-2800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_76X_V2p1/*/0000/*.root")
	if string == 'B2GsignalRH3000':
		files = glob.glob("/eos/uscms/store/user/lcorcodi/BstarToTW_M-3000_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_BstarToTW_M-3000_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_B2GAnaFW_76X_V2p1/*/0000/*.root")


	for i in range(0,len(files)):
		files[i] = files[i].replace('/eos/uscms','root://cmsxrootd.fnal.gov//')
	
	
	
	try:
		print 'A total of ' + str(len(files)) + ' files'
	except:
		print 'Bad files option'
		files = []
	return files

#This function initializes the average b tagging rates used for QCD determination
#It tages the type of functional form as an argument.  The default fit is Bifpoly

def BTR_Init(ST,CUT,di,setval):

	if setval.find("QCD")==-1:
		setval = "Data"


	if ST == 'Bifpoly':
		TRBPE1 = open("./"+di+"fitdata/bpinput"+setval+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open("./"+di+"fitdata/bpinput"+setval+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit = TF1("eta1fit",BifPoly,0,1400,5)
		eta2fit = TF1("eta2fit",BifPoly,0,1400,5)
		Params = 5
	if ST == 'Bifpoly_err':
		TRBPE1 = open("./"+di+"fitdata/bperrorinput"+setval+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open("./"+di+"fitdata/bperrorinput"+setval+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit=TF1("eta1fit",BifPolyErr,0,1400,10)
		eta2fit=TF1("eta2fit",BifPolyErr,0,1400,10)
		Params = 10

	if ST == 'pol0':
		TRBPE1 = open("./"+di+"fitdata/pol0input"+setval+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open("./"+di+"fitdata/pol0input"+setval+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit = TF1("eta1fit",'pol0',0,1400)
		eta2fit = TF1("eta2fit",'pol0',0,1400)
		Params = 1

	if ST == 'pol2':
		TRBPE1 = open("./"+di+"fitdata/pol2input"+setval+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open("./"+di+"fitdata/pol2input"+setval+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit = TF1("eta1fit",'pol2',0,1400)
		eta2fit = TF1("eta2fit",'pol2',0,1400)
		Params = 3

	if ST == 'pol3':
		TRBPE1 = open("./"+di+"fitdata/pol3input"+setval+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open("./"+di+"fitdata/pol3input"+setval+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit = TF1("eta1fit",'pol3',0,1400)
		eta2fit = TF1("eta2fit",'pol3',0,1400)
		Params = 4
	if ST == 'FIT':
		TRBPE1 = open("./"+di+"fitdata/newfitinput"+setval+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open("./"+di+"fitdata/newfitinput"+setval+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit = TF1("eta1fit",'[0]*([1]+x)/([2]+x)+[3]*x',0,1400)
		eta2fit = TF1("eta2fit",'[0]*([1]+x)/([2]+x)+[3]*x',0,1400)
		Params = 4
	if ST == 'expofit':
		TRBPE1 = open("./"+di+"fitdata/expoconinput"+setval+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open("./"+di+"fitdata/expoconinput"+setval+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit = TF1("eta1fit",'expo(0) + pol0(2)',0,1400)
		eta2fit = TF1("eta2fit",'expo(0) + pol0(2)',0,1400)
		Params = 3

	TBP1 = TRBPE1.read()
	TBP2 = TRBPE2.read()
	
	for i in range(0,Params):

		eta1fit.SetParameter(i,float(TBP1.split('\n')[i]) )
		eta2fit.SetParameter(i,float(TBP2.split('\n')[i]) )

	return [eta1fit.Clone(),eta2fit.Clone()] 


#This function initializes the average b tagging rates used for QCD determination
#It tages the type of functional form as an argument.  The default fit is Bifpoly

#This is a poorly written function, but I cant think of a better way to do this 
#It works, but you should be able to just have one input
def TTR_Init(ST,CUT,SET,di):
	if ST == 'Bifpoly':
		TRBPE1 = open(di+"fitdata/bpinput"+SET+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open(di+"fitdata/bpinput"+SET+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit = TF1("eta1fit",BifPoly,0,2000,5)
		eta2fit = TF1("eta2fit",BifPoly,0,2000,5)
		Params = 5
	if ST == 'Bifpoly_err':
		TRBPE1 = open(di+"fitdata/bperrorinput"+SET+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open(di+"fitdata/bperrorinput"+SET+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit=TF1("eta1fit",BifPolyErr,0,2000,10)
		eta2fit=TF1("eta2fit",BifPolyErr,0,2000,10)
		Params = 10

	if ST == 'pol0':
		TRBPE1 = open(di+"fitdata/pol0input"+SET+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open(di+"fitdata/pol0input"+SET+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit = TF1("eta1fit",'pol0',0,2000)
		eta2fit = TF1("eta2fit",'pol0',0,2000)
		Params = 1

	if ST == 'pol2':
		TRBPE1 = open(di+"fitdata/pol2input"+SET+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open(di+"fitdata/pol2input"+SET+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit = TF1("eta1fit",'pol2',0,2000)
		eta2fit = TF1("eta2fit",'pol2',0,2000)
		Params = 3

	if ST == 'pol3':
		TRBPE1 = open(di+"fitdata/pol3input"+SET+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open(di+"fitdata/pol3input"+SET+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit = TF1("eta1fit",'pol3',0,2000)
		eta2fit = TF1("eta2fit",'pol3',0,2000)
		Params = 4
	if ST == 'FIT':
		TRBPE1 = open(di+"fitdata/newfitinput"+SET+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open(di+"fitdata/newfitinput"+SET+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit = TF1("eta1fit",'[0]*([1]+x)/([2]+x)+[3]*x',0,2000)
		eta2fit = TF1("eta2fit",'[0]*([1]+x)/([2]+x)+[3]*x',0,2000)
		Params = 4
	if ST == 'expofit':
		TRBPE1 = open(di+"fitdata/expoconinput"+SET+"eta1_PSET_"+CUT+".txt")
		TRBPE1.seek(0)
		TRBPE2 = open(di+"fitdata/expoconinput"+SET+"eta2_PSET_"+CUT+".txt")
		TRBPE2.seek(0)
		eta1fit = TF1("eta1fit",'expo(0) + pol0(2)',0,2000)
		eta2fit = TF1("eta2fit",'expo(0) + pol0(2)',0,2000)
		Params = 3

	TBP1 = TRBPE1.read()
	TBP2 = TRBPE2.read()
	
	for i in range(0,Params):

		eta1fit.SetParameter(i,float(TBP1.split('\n')[i]) )
		eta2fit.SetParameter(i,float(TBP2.split('\n')[i]) )


	return [eta1fit.Clone(),eta2fit.Clone()] 

#This takes the average b tagging rates that are initialized in the above function and produces 
#A QCD background estimate based on them 
def bkg_weight(blv, funcs, etabins):
	for ibin in range(0,len(etabins)):
		if (etabins[ibin][0] <= abs(blv.Eta()) < etabins[ibin][1]) :
			tagratept = funcs[ibin].Eval(blv.Perp())		
	return tagratept

#This is the bifurcated polynomial function and its associated uncertainty 
def BifPoly( x, p ):
	xx=x[0]
	if xx<p[4]:
      		return p[0]+p[1]*xx+p[2]*(xx-p[4])**2
        else:
		return p[0]+p[1]*xx+p[3]*(xx-p[4])**2
def BifPolyErr( x, p ):
	xx=x[0]
	if xx<p[9]:
      		return p[0]+p[1]*xx**2+p[2]*(xx-p[9])**4+p[3]*xx+p[4]*(xx-p[9])**2+p[5]*xx*(xx-p[9])**2
        else:
		return p[0]+p[1]*xx**2+p[6]*(xx-p[9])**4+p[3]*xx+p[7]*(xx-p[9])**2+p[8]*xx*(xx-p[9])**2

#This looks up the PDF uncertainty
def PDF_Lookup( pdfs , pdfOP ):
	iweight = 0.0
	#print "LEN"
	#print len(pdfs)
	ave =  pdfs
	ave =  reduce(lambda x, y: x + y, pdfs) / len(pdfs)
	#print ave
       	for pdf in pdfs :
             	iweight = iweight + (pdf-ave)*(pdf-ave)

        if pdfOP == "up" :
        	return 1+sqrt((iweight) / (len(pdfs)))
        else :
          	return 1-sqrt((iweight) / (len(pdfs)))
#This looks up the b tagging scale factor or uncertainty
def Trigger_Lookup( H , TRP ):
        Weight = 1.0
	Weightup = 1.0
	Weightdown = 1.0
        if H < 1200.0:
                bin0 = TRP.FindBin(H) 
                jetTriggerWeight = TRP.GetBinContent(bin0)
                Weight = jetTriggerWeight
		deltaTriggerEff  = 0.5*(1.0-jetTriggerWeight)
                Weightup  =   min(1.0,jetTriggerWeight + deltaTriggerEff)
                Weightdown  =   max(0.0,jetTriggerWeight - deltaTriggerEff)
		
	return [Weight,Weightup,Weightdown]

#This looks up the PDF uncertainty
def SFT_Lookup( pttop ):
	ttagsf = [[0.82,0.09],[0.93,0.20]]
	ttagsfregions = [[0,550],[550,float("inf")]]

	for ipttop in range(0,len(ttagsfregions)):
		if ttagsfregions[ipttop][0]<pttop<=ttagsfregions[ipttop][1]:
			return [ttagsf[ipttop][0],ttagsf[ipttop][0]-ttagsf[ipttop][1],ttagsf[ipttop][0]+ttagsf[ipttop][1]]


#
def Trigger_Pass(tnamestr,trigs,bits):
	###TAKE OUT!
	#tnamestr = ['HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p45_v2','HLT_PFHT800_v1']

	for t in range(0,len(trigs)):
		for tname in tnamestr:	
			if trigs[t]==tname and bits[t] :
				return True
	return False

#This looks up the ttbar pt reweighting scale factor 
def PTW_Lookup( GP ):
		genTpt = -100.
		genTBpt = -100	
		for ig in GP :
			isT = ig.pdgId() == 6 and ig.status() == 3
			isTB = ig.pdgId() == -6 and ig.status() == 3
			if isT:
				genTpt = ig.Perp()
			if isTB:
				genTBpt = ig.Perp()	
		if (genTpt<0) or (genTBpt<0):
			print "ERROR"

      		wTPt = exp(0.156-0.00137*genTpt)
      		wTbarPt = exp(0.156-0.00137*genTBpt)
      		return sqrt(wTPt*wTbarPt)

def Initlv(string,post=''):
	PtHandle 	= 	Handle (  "vector<float> "  )
	PtLabel  	= 	( string+post , string.replace("jets","jet")+"Pt")

	EtaHandle 	= 	Handle (  "vector<float> "  )
	EtaLabel  	= 	( string+post , string.replace("jets","jet")+"Eta")

	PhiHandle 	= 	Handle (  "vector<float> "  )
	PhiLabel  	= 	( string+post , string.replace("jets","jet")+"Phi")

	MassHandle 	= 	Handle (  "vector<float> "  )
	MassLabel  	= 	( string+post , string.replace("jets","jet")+"Mass")

	return [[PtHandle,PtLabel],[EtaHandle,EtaLabel],[PhiHandle,PhiLabel],[MassHandle,MassLabel]]
 
def Makelv(vector,event):
 
     	event.getByLabel (vector[0][1], vector[0][0])
     	Pt 		= 	vector[0][0].product()
 
     	event.getByLabel (vector[1][1], vector[1][0])
     	Eta 		= 	vector[1][0].product()
 
     	event.getByLabel (vector[2][1], vector[2][0])
     	Phi 		= 	vector[2][0].product()
 
     	event.getByLabel (vector[3][1], vector[3][0])
     	Mass 		= 	vector[3][0].product()
 
 	lvs = []
 	for i in range(0,len(Pt)):
 
 		#lvs.append(ROOT.Math.LorentzVector('ROOT::Math::PtEtaPhiM4D<double>')(Pt[i],Eta[i],Phi[i],Mass[i]))
 
 		lvs.append(TLorentzVector())
 		lvs[i].SetPtEtaPhiM(Pt[i],Eta[i],Phi[i],Mass[i])
 	return lvs
 
 
def Hemispherize(LV1,LV2):
 	tjets = [[],[]]
 	wjets = [[],[]]
 	for iLV1 in range(0,len(LV1)):
 		if abs(Math.VectorUtil.DeltaPhi(LV1[0],LV1[iLV1]))> TMath.Pi()/2:
 			tjets[1].append(iLV1)
 		else:
 			tjets[0].append(iLV1)
 	for iLV2 in range(0,len(LV2)):
 		if abs(Math.VectorUtil.DeltaPhi(LV1[0],LV2[iLV2]))> TMath.Pi()/2:
 			wjets[1].append(iLV2)
 		else:
 			wjets[0].append(iLV2)
 	return tjets,wjets

#This is just a quick function to automatically make a tree
#This is used right now to automatically output branches used to validate the cuts used in a run
def Make_Trees(Floats):
        t = TTree("Tree", "Tree");
	print "Booking trees"
	for F in Floats.keys():
    		t.Branch(F, Floats[F], F+"/D")
	return t

#This takes all of the alternative fit forms for the average b tagging rate and 
#Compares them to the chosen nominal fit (bifpoly).  It outputs the mean squared error uncertainty from this comparison 
def Fit_Uncertainty(List):
	sigmah	    = List[0]
	fits=len(List)-1
	for ihist in range(0,len(List)):
		if List[ihist].GetName() == 'QCDbkgBifpoly':
			nominalhist = List[ihist]
	for ibin in range(0,nominalhist.GetXaxis().GetNbins()+1):

		mse=0.0
		sigma=0.0
		sumsqdiff = 0.0
		for ihist in range(0,len(List)):
			if List[ihist].GetName() != 'QCDbkgBifpoly':
				sumsqdiff+=(List[ihist].GetBinContent(ibin)-nominalhist.GetBinContent(ibin))*(List[ihist].GetBinContent(ibin)-nominalhist.GetBinContent(ibin))
		mse = sumsqdiff/fits
		sigma = sqrt(mse)
		sigmah.SetBinContent(ibin,sigma)
	
	return sigmah

#Same as Fit_Uncertainty but optimized to work with kinematic variables
def kinFit_Uncertainty(List,kinVar):
	sigmah	    = List[0]
	fits=len(List)-1
	for ihist in range(0,len(List)):
		if List[ihist].GetName() == 'QCDbkg'+kinVar+'Bifpoly':
			nominalhist = List[ihist]
	for ibin in range(0,nominalhist.GetXaxis().GetNbins()+1):

		mse=0.0
		sigma=0.0
		sumsqdiff = 0.0
		for ihist in range(0,len(List)):
			if List[ihist].GetName() != 'QCDbkg'+kinVar+'Bifpoly':
				sumsqdiff+=(List[ihist].GetBinContent(ibin)-nominalhist.GetBinContent(ibin))*(List[ihist].GetBinContent(ibin)-nominalhist.GetBinContent(ibin))
		mse = sumsqdiff/fits
		sigma = sqrt(mse)
		sigmah.SetBinContent(ibin,sigma)
	
	return sigmah

#Makes the blue pull plots
def Make_Pull_plot( DATA,BKG,BKGUP,BKGDOWN ):
	pull = DATA.Clone("pull")
	pull.Add(BKG,-1)
	sigma = 0.0
	FScont = 0.0
	BKGcont = 0.0
	for ibin in range(1,pull.GetNbinsX()+1):
		FScont = DATA.GetBinContent(ibin)
		BKGcont = BKG.GetBinContent(ibin)
		if FScont>=BKGcont:
			FSerr = DATA.GetBinErrorLow(ibin)
			BKGerr = abs(BKGUP.GetBinContent(ibin)-BKG.GetBinContent(ibin))
		if FScont<BKGcont:
			FSerr = DATA.GetBinErrorUp(ibin)
			BKGerr = abs(BKGDOWN.GetBinContent(ibin)-BKG.GetBinContent(ibin))
		sigma = sqrt(FSerr*FSerr + BKGerr*BKGerr)
		if FScont == 0.0:
			pull.SetBinContent(ibin, 0.0 )	
		else:
			if sigma != 0 :
				pullcont = (pull.GetBinContent(ibin))/sigma
				pull.SetBinContent(ibin, pullcont)
			else :
				pull.SetBinContent(ibin, 0.0 )
	return pull
#Some lazy string formatting functions 
def strf( x ):
	return '%.2f' % x

def strf1( x ):
	return '%.0f' % x
