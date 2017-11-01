
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


# ONLY HAS THE FUNCTIONS THAT USE FWLITE -LC


from DataFormats.FWLite import Runs
import os
import array
import ROOT
import sys
from array import *
from ROOT import *
from DataFormats.FWLite import Events, Handle

def Initlv(string,post=''):
	PtHandle 	= 	Handle (  "vector<float> "  )
	PtLabel  	= 	( string+post , string.replace("jets","jet")+"PuppiPt")

	EtaHandle 	= 	Handle (  "vector<float> "  )
	EtaLabel  	= 	( string+post , string.replace("jets","jet")+"PuppiEta")

	PhiHandle 	= 	Handle (  "vector<float> "  )
	PhiLabel  	= 	( string+post , string.replace("jets","jet")+"PuppiPhi")

	MassHandle 	= 	Handle (  "vector<float> "  )
	MassLabel  	= 	( string+post , string.replace("jets","jet")+"PuppiMass")

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
 
