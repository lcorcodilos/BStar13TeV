



###################################################################
##								 ##
## Name: Tagrate_Maker_B.py				         ##
## Author: Kevin Nash 						 ##
## Date: 6/5/2012						 ##
## Purpose: This program takes the root files created by  	 ##
##          TWrate.py and creates the average b-tagging rate, 	 ##
##	    then fits the average b-tagging rates		 ##
##          tagrates with a several functions 			 ##
##	    which are stored in the fitdata folder to be used    ##
##	    to weight the pre b tagged sample and create	 ##
##	    QCD background estimates				 ##
##								 ##
###################################################################

import os
import array
import glob
import math
import ROOT
import sys
from array import *
from ROOT import *
from optparse import OptionParser

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
                  default	=	'data',
                  dest		=	'set',
                  help		=	'data or QCD')

parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'rate_default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-p', '--printCanvas', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'printCanvas',
				  help		=	'on or off')
parser.add_option('-u', '--ptreweight', metavar='F', type='string', action='store',
				  default	=	'on',
				  dest		=	'ptreweight',
				  help		=	'on or off')
parser.add_option('-t', '--ttsub', metavar='F', type='string', action='store',
				  default	=	'on',
				  dest		=	'ttsub',
				  help		=	'on, off, or double')
parser.add_option('-i', '--iteration', metavar='F', type='int', action='store',
				  default	=	-1,
				  dest		=	'iteration',
				  help		=	'Scale factor iteration. Default -1 means pt study is off')
parser.add_option('--noExtraPtCorrection', metavar='F', action='store_false',
				  default=True,
				  dest='extraPtCorrection',
				  help='Call to turn off extraPtCorrection')

(options, args) = parser.parse_args()

if options.printCanvas == 'off':
	ROOT.gROOT.SetBatch(True)
	ROOT.PyConfig.IgnoreCommandLineOptions = True

gROOT.Macro("rootlogon.C")

import Bstar_Functions	
from Bstar_Functions import *

Cons = LoadConstants()

#Uncomment for the single lumi from BstarFunctions
cLumi = Cons['lumi']
lumiList = [cLumi]
Lumi = str(int(cLumi))+'pb'



#----------------Need to grab extra top pt reweight factor-------------------
ptTTString = ''
if not options.extraPtCorrection:
	ptTTString = '_noExtraPtCorrection'
if options.ptreweight == 'off':
	ptTTString = '_ptreweight_off'
#----------------------------------------------------------------------------

#TTbar subtraction string is set here
ttsubString = ''
if options.set=='data':
	if options.ttsub == 'on':
		ttsubString = ''
	elif options.ttsub == 'off':
		ttsubString = '_nottsub'
	elif options.ttsub == 'double':
		ttsubString = '_doublettsub'


rootdir="rootfiles/"+Lumi+"/"

setstr = ""
if options.set=='QCD':
	setstr = 'QCD'
elif options.set=='data':
	setstr = 'data'

#Make a bunch of txt files to store the fit parameters
saveout = sys.stdout

Outf0   =   open("fitdata/alphabet/Mt_pol2_"+setstr+"_fulleta_"+options.cuts+ttsubString+ptTTString+".txt", "w")
Outf1   =   open("fitdata/alphabet/Mt_pol2_"+setstr+"_eta1_"+options.cuts+ttsubString+ptTTString+".txt", "w")
Outf2   =   open("fitdata/alphabet/Mt_pol2_"+setstr+"_eta2_"+options.cuts+ttsubString+ptTTString+".txt", "w")


sto = sys.stdout  
p0 = 0.0
p1 = 0.0
p2 = 0.0
p3 = 0.0
p4 = 0.0

print "Running on "+options.set

#Load up data and ttbar
fdata = TFile(rootdir+"TWalphabetfile"+options.set+"_PSET_"+options.cuts+".root")
fttbar = TFile(rootdir+"TWalphabetfileweightedttbar"+"_PSET_"+options.cuts+ptTTString+".root")
fsingletop = TFile(rootdir+"TWalphabetfilesingletop"+"_PSET_"+options.cuts+".root")

output = TFile( "plots/TWalphabet_Maker_"+setstr+"_"+Lumi+"_PSET_"+options.cuts+ttsubString+ptTTString+".root", "recreate" )
output.cd()

########################################
# Start with the full eta distribution #
########################################
# Grab the plots
MtPass = fdata.Get("MpassFull")
MtFail = fdata.Get("MfailFull")

ttMtPass = fttbar.Get('MpassFull')
ttMtFail = fttbar.Get('MfailFull')

stMtPass = fsingletop.Get('MpassFull')
stMtFail = fsingletop.Get('MfailFull')

# Setup some binning
massBins = [50,60,70,90,105,210,230,270]
massBins2=array('d',massBins)
# 'bins' are pt bins for later
bins= [400,540,570,600,650,720,850,1100,1700]
if options.set == 'QCD':
	bins= [400,540,570,600,650,720,850,1000,1300,1600,2000]
bins2 = array('d',bins)

# Rebin
MtPassr = MtPass.Rebin(len(massBins2)-1,"MtPassr",massBins2)
MtFailr = MtPass.Rebin(len(massBins2)-1,"MtFailr",massBins2)

ttMtPassr = ttMtPass.Rebin(len(massBins2)-1,"ttMtPassr",massBins2)
ttMtFailr = ttMtPass.Rebin(len(massBins2)-1,"ttMtFailr",massBins2)

stMtPassr = stMtPass.Rebin(len(massBins2)-1,"stMtPassr",massBins2)
stMtFailr = stMtPass.Rebin(len(massBins2)-1,"stMtFailr",massBins2)

# TTbar subtraction is done here
if options.set=='data':
	if options.ttsub == 'on':
		print 'subtracting ttbar and single top'
		MtPassr.Add(ttMtPassr,-1)
		MtFailr.Add(ttMtFailr,-1)
		MtPassr.Add(stMtPassr,-1)
		MtFailr.Add(stMtFailr,-1)
	elif options.ttsub == 'off':
		print 'not subtracting ttbar and single top'
	elif options.ttsub == 'double':
		print 'double subtracting ttbar and single top'
		MtPassr.Add(ttMtPassr,-2)
		MtFailr.Add(ttMtFailr,-2)
		MtPassr.Add(stMtPassr,-2)
		MtFailr.Add(stMtFailr,-2)

# Clone, Divide, and Write
MtRpf = MtPassr.Clone('MtRpf')
MtRpf.Divide(MtFailr)
MtRpf.Write()

# Now do a fit and save to the propper .txt files
sys.stdout = Outf0
MtRpf.Fit("pol2","F")
fitter = TVirtualFitter.GetFitter()

p0 = fitter.GetParameter(0)
p0e = fitter.GetParErrors()[0]
p1 = fitter.GetParameter(1)
p1e = fitter.GetParErrors()[1]
p2 = fitter.GetParameter(2)
p2e = fitter.GetParErrors()[2]

print str(p0)
print str(p0e)
print str(p1)
print str(p1e)
print str(p2)
print str(p2e)

sys.stdout = saveout


###################################
# Now do the separate eta regions #
###################################
# Grab the stuff
neta1 = fdata.Get("MpassEta1")
deta1 = fdata.Get("MfailEta1")

neta2 = fdata.Get("MpassEta2")
deta2 = fdata.Get("MfailEta2")

ttneta1 = fttbar.Get("MpassEta1")
ttdeta1 = fttbar.Get("MfailEta1")

ttneta2 = fttbar.Get("MpassEta2")
ttdeta2 = fttbar.Get("MfailEta2")

stneta1 = fsingletop.Get("MpassEta1")
stdeta1 = fsingletop.Get("MfailEta1")

stneta2 = fsingletop.Get("MpassEta2") 
stdeta2 = fsingletop.Get("MfailEta2")

neta1r = neta1.Rebin(len(massBins2)-1,"neta1r",massBins2)
deta1r = deta1.Rebin(len(massBins2)-1,"deta1r",massBins2)

neta2r = neta2.Rebin(len(massBins2)-1,"neta2r",massBins2)
deta2r = deta2.Rebin(len(massBins2)-1,"deta2r",massBins2)

ttneta1r = ttneta1.Rebin(len(massBins2)-1,"ttneta1r",massBins2)
ttdeta1r = ttdeta1.Rebin(len(massBins2)-1,"ttdeta1r",massBins2)

ttneta2r = ttneta2.Rebin(len(massBins2)-1,"ttneta2r",massBins2)
ttdeta2r = ttdeta2.Rebin(len(massBins2)-1,"ttdeta2r",massBins2)

stneta1r = stneta1.Rebin(len(massBins2)-1,"stneta1r",massBins2)
stdeta1r = stdeta1.Rebin(len(massBins2)-1,"stdeta1r",massBins2)

stneta2r = stneta2.Rebin(len(massBins2)-1,"stneta2r",massBins2)
stdeta2r = stdeta2.Rebin(len(massBins2)-1,"stdeta2r",massBins2)


#TTbar subtraction is done here
if options.set=='data':
	if options.ttsub == 'on':
		print 'subtracting ttbar and single top'
		neta1r.Add(ttneta1r,-1)
		deta1r.Add(ttdeta1r,-1)
		neta2r.Add(ttneta2r,-1)
		deta2r.Add(ttdeta2r,-1)
		neta1r.Add(stneta1r,-1)
		deta1r.Add(stdeta1r,-1)
		neta2r.Add(stneta2r,-1)
		deta2r.Add(stdeta2r,-1)
	elif options.ttsub == 'off':
		print 'not subtracting ttbar and single top'
	elif options.ttsub == 'double':
		print 'double subtracting ttbar and single top'
		neta1r.Add(ttneta1r,-2)
		deta1r.Add(ttdeta1r,-2)
		neta2r.Add(ttneta2r,-2)
		deta2r.Add(ttdeta2r,-2)
		neta1r.Add(stneta1r,-2)
		deta1r.Add(stdeta1r,-2)
		neta2r.Add(stneta2r,-2)
		deta2r.Add(stdeta2r,-2)

output.cd()

# Create subtracted Rp/f by division
MtRpfEta1 = neta1r.Clone("MtRpfEta1")
MtRpfEta1.Divide(deta1r)
MtRpfEta2 = neta2r.Clone("MtRpfEta2")
MtRpfEta2.Divide(deta2r)
MtRpfEta1.Write()
MtRpfEta2.Write()


# The rest here writes the fit, and uses the covariance matrix to propagate errors for various functions

sys.stdout = saveout
print "------------------------------------"
print "POL2"
print "------------------------------------"
# This next line tells any print statement to go the the txt file Outf1
sys.stdout = Outf1
MtRpfEta1.Fit("pol2","F")
fitter = TVirtualFitter.GetFitter()

p0 = fitter.GetParameter(0)
p0e = fitter.GetParErrors()[0]
p1 = fitter.GetParameter(1)
p1e = fitter.GetParErrors()[1]
p2 = fitter.GetParameter(2)
p2e = fitter.GetParErrors()[2]

print str(p0)
print str(p0e)
print str(p1)
print str(p1e)
print str(p2)
print str(p2e)

sys.stdout = Outf2
MtRpfEta2.Fit("pol2","F")
fitter = TVirtualFitter.GetFitter()

p0 = fitter.GetParameter(0)
p0e = fitter.GetParErrors()[0]
p1 = fitter.GetParameter(1)
p1e = fitter.GetParErrors()[1]
p2 = fitter.GetParameter(2)
p2e = fitter.GetParErrors()[2]

print str(p0)
print str(p0e)
print str(p1)
print str(p1e)
print str(p2)
print str(p2e)

sys.stdout = saveout

#############################################################
# Now we try to do the 2D Rp/f (parameterized in pt and Mt) #
#############################################################
output.cd()

#This is one number that controls the automatic variable binning sensitivity
bres = 0.8

pre1=[]
pre2=[]	

dpre1=[]
dpre2=[]	

# Two eta regions - will combine at end for one big region
neta1NOSUB = fdata.Get("MtvsptPasseta1")
deta1NOSUB = fdata.Get("MtvsptFaileta1")

neta2NOSUB = fdata.Get("MtvsptPasseta2")
deta2NOSUB = fdata.Get("MtvsptFaileta2")

neta1ttbar = fttbar.Get("MtvsptPasseta1")
deta1ttbar = fttbar.Get("MtvsptFaileta1")

neta2ttbar = fttbar.Get("MtvsptPasseta2")
deta2ttbar = fttbar.Get("MtvsptFaileta2")

neta1stbar = fsingletop.Get("MtvsptPasseta1")
deta1stbar = fsingletop.Get("MtvsptFaileta1")

neta2stbar = fsingletop.Get("MtvsptPasseta2")
deta2stbar = fsingletop.Get("MtvsptFaileta2")

neta1 = neta1NOSUB.Clone("MtvsptPasseta1")
neta1.Add(neta1ttbar,-1)
neta1.Add(neta1stbar,-1)

neta2 = neta2NOSUB.Clone("MtvsptPasseta2")
neta2.Add(neta2ttbar,-1)
neta2.Add(neta2stbar,-1)

deta1 = deta1NOSUB.Clone("MtvsptFaileta1")
deta1.Add(deta1ttbar,-1)
deta1.Add(deta1stbar,-1)

deta2 = deta2NOSUB.Clone("MtvsptFaileta2")
deta2.Add(deta2ttbar,-1)
deta2.Add(deta2stbar,-1)



# X-axis = pt, Y-axis = mass
neta1r = ROOT.TH2F("neta1r",  "Comparison tpt and Mt",   		len(bins2)-1, bins2,  len(massBins2)-1, massBins2 )
deta1r = ROOT.TH2F("deta1r",  "Comparison tpt and Mt",   		len(bins2)-1, bins2,  len(massBins2)-1, massBins2 )

neta2r = ROOT.TH2F("neta2r",  "Comparison tpt and Mt",   		len(bins2)-1, bins2,  len(massBins2)-1, massBins2 )
deta2r  = ROOT.TH2F("deta2r",  "Comparison tpt and Mt",   		len(bins2)-1, bins2,  len(massBins2)-1, massBins2 )

# Initialize some stuff
pre1=[]
pre2=[]	

dpre1=[]
dpre2=[]	

slopeta1 = []
slopeta2 = []

vavg1 = []
vavg2 = []


# Loop through pt bins
for ibin in range(0,len(bins2)-1):
		# Grab two current bins adjacent to each other
		bin1 = neta1.GetXaxis().FindBin(bins2[ibin])
		bin2 = neta1.GetXaxis().FindBin(bins2[ibin+1]-1.0)

		# Project Y axis onto bin range (between just the two bins)
		pre1.append(neta1.ProjectionY("SB1projYeta1_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]),bin1,bin2,"e"))
		pre2.append(neta2.ProjectionY("SB1projYeta2_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]),bin1,bin2,"e"))

		dpre1.append(deta1.ProjectionY("SB1projYdeta1_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]),bin1,bin2,"e"))
		dpre2.append(deta2.ProjectionY("SB1projYdeta2_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]),bin1,bin2,"e"))
		
		print "" 
		print bins2[ibin]
		print "THIS"
		print pre1[ibin].Integral()
		print dpre1[ibin].Integral()
		print "EQUALS"
		print neta1.Integral(bin1,bin2,0,-1)
		print deta1.Integral(bin1,bin2,0,-1)


		#breaks on rate_sideband so need this
		times = 0
		if dpre2[ibin].Integral() == 0:
			times = times + 1
			print times
			continue

		# Average rate for that bin
		vavg1.append(pre1[ibin].Integral()/dpre1[ibin].Integral())
		vavg2.append(pre2[ibin].Integral()/dpre2[ibin].Integral())

		tempbin1 = 0
		error1 = ROOT.Double(1.0)

		fcont = False

		# some variable binning in Y direction starting at 70 and going to 270
		binning1= array('d',[])
		int1 = pre1[ibin].Integral()
		binning1.append(70.0)
		for ibin1 in range(1,pre1[ibin].GetNbinsX()-1):
			cont = pre1[ibin].IntegralAndError(tempbin1+1,ibin1,error1)
			if cont > 0.0:
				if not fcont:
					tempbin1 = ibin1
					binning1.append(pre1[ibin].GetBinLowEdge(tempbin1))
					fcont = True
				if error1*int1/(cont*cont) < .5:
					tempbin1 = ibin1
					binning1.append(pre1[ibin].GetBinLowEdge(tempbin1) + pre1[ibin].GetBinWidth(tempbin1))


		binning1.append(270.0)
		print binning1
		fcont = False
		tempbin2 = 0
		error2 = ROOT.Double(1.0)

		# Now for eta 2
		binning2= array('d',[])
		int2 = pre2[ibin].Integral()
		binning2.append(70.0)
		for ibin2 in range(1,pre2[ibin].GetNbinsX()-1):
			cont = pre2[ibin].IntegralAndError(tempbin2+1,ibin2,error2)
			if cont > 0.0:
				if not fcont:
					tempbin2 = ibin2
					binning2.append(pre1[ibin].GetBinLowEdge(tempbin2))
					fcont = True
				if error2*int2/(cont*cont) < bres:
					tempbin2 = ibin2
					binning2.append(pre2[ibin].GetBinLowEdge(tempbin2) + pre2[ibin].GetBinWidth(tempbin2))
		binning2.append(270.0)
		fcont = False
		tempbin3 = 0
		error3 = ROOT.Double(1.0)

		
		# More rebinning
		pre1[ibin] = pre1[ibin].Rebin(len(binning1)-1,"SB1projYeta1_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]),binning1)
		pre2[ibin] = pre2[ibin].Rebin(len(binning2)-1,"SB1projYeta2_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]),binning2)

		dpre1[ibin] = dpre1[ibin].Rebin(len(binning1)-1,"SB1projYdeta1_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]),binning1)
		dpre2[ibin] = dpre2[ibin].Rebin(len(binning2)-1,"SB1projYdeta2_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]),binning2)
	
		
		for ibin1 in range(1,neta1r.GetNbinsY()):
			bcont = neta1r.GetYaxis().GetBinCenter(ibin1)

			bin1de1 = pre1[ibin].FindBin(bcont)
			bin1de2 = pre2[ibin].FindBin(bcont)
	
			neta1r.SetBinContent(ibin+1,ibin1,pre1[ibin].GetBinContent(bin1de1))
			deta1r.SetBinContent(ibin+1,ibin1,dpre1[ibin].GetBinContent(bin1de1))

			neta2r.SetBinContent(ibin+1,ibin1,pre2[ibin].GetBinContent(bin1de2))
			deta2r.SetBinContent(ibin+1,ibin1,dpre2[ibin].GetBinContent(bin1de2))


			neta1r.SetBinError(ibin+1,ibin1,pre1[ibin].GetBinError(bin1de1))
			deta1r.SetBinError(ibin+1,ibin1,dpre1[ibin].GetBinError(bin1de1))

			neta2r.SetBinError(ibin+1,ibin1,pre2[ibin].GetBinError(bin1de2))
			deta2r.SetBinError(ibin+1,ibin1,dpre2[ibin].GetBinError(bin1de2))

		pre1[ibin].Divide(pre1[ibin],dpre1[ibin],1,1,"B")
		pre2[ibin].Divide(pre2[ibin],dpre2[ibin],1,1,"B")

		pre1[ibin].Fit("pol1","F")
		fitter = TVirtualFitter.GetFitter()
		slopeta1.append(fitter.GetParameter(1))

		pre2[ibin].Fit("pol1","F")
		fitter = TVirtualFitter.GetFitter()
		slopeta2.append(fitter.GetParameter(1))



		pre1[ibin].Fit("pol0","F")
		fitter = TVirtualFitter.GetFitter()
		AVG1 = fitter.GetParameter(0)

		pre2[ibin].Fit("pol0","F")
		fitter = TVirtualFitter.GetFitter()
		AVG2 = fitter.GetParameter(0)


		pull1= pre1[ibin].Clone("PULL_SB1projYeta1_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]))
		for ibin1 in range(1,pull1.GetNbinsX()+1):
			if pull1.GetBinError(ibin1)!=0.0:
				pull1.SetBinContent(ibin1,(pull1.GetBinContent(ibin1)-AVG1)/pull1.GetBinError(ibin1))
				print (pull1.GetBinContent(ibin1)-AVG1)/pull1.GetBinError(ibin1)
			else:
				pull1.SetBinContent(ibin1,0.0)
		pull2= pre2[ibin].Clone("PULL_SB1projYeta2_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]))
		for ibin2 in range(1,pull2.GetNbinsX()+1):
			if pull2.GetBinError(ibin2)!=0.0:
				pull2.SetBinContent(ibin2,(pull2.GetBinContent(ibin2)-AVG2)/pull2.GetBinError(ibin2))
			else:
				pull2.SetBinContent(ibin1,0.0)


		print ""

		pull1.SetFillColor(kBlue)
		pull2.SetFillColor(kBlue)

		output.cd()



tagrateeta1 = neta1r.Clone("tagrateeta1")
tagrateeta1.Divide(tagrateeta1,deta1r,1,1,"B")

tagrateeta2 = neta2r.Clone("tagrateeta2")
tagrateeta2.Divide(tagrateeta2,deta2r,1,1,"B")


output1.cd()
tagrateeta1.Write("SB1tagrate2Deta1")
tagrateeta2.Write("SB1tagrate2Deta2")

c1 = TCanvas('c1SB1', 'Pt fitted tagrate in 0.0 < Eta <0.5', 800, 500)
tagrateeta1.Draw("COLZ")
c1.RedrawAxis()
c1.Print('plots/'+options.cuts+'/Tagrate'+setstr+'Eta1SB1'+'.root', 'root')
c1.Print('plots/'+options.cuts+'/Tagrate'+setstr+'Eta1SB1'+'.pdf', 'pdf')
c2 = TCanvas('c2SB1', 'Pt fitted tagrate in 0.5 < Eta <1.15', 800, 500)
tagrateeta2.Draw("COLZ")
c2.RedrawAxis()
c2.Print('plots/'+options.cuts+'/Tagrate'+setstr+'Eta2SB1'+'.root', 'root')
c2.Print('plots/'+options.cuts+'/Tagrate'+setstr+'Eta2SB1'+'.pdf', 'pdf')
c3 = TCanvas('c3SB1', 'Pt fitted tagrate in 1.15 < Eta <2.4', 800, 500)


print len(vavg1)
print vavg2

output1.cd()
tagrateeta1.Write()
tagrateeta2.Write()

SB2dtempeta1 = tagrateeta1.Clone("SB2dtempeta1")
SB2dtempeta2 = tagrateeta2.Clone("SB2dtempeta2")

c1 = TCanvas('c12d', 'SB2d Pt fitted tagrate in 0.0 < Eta <0.5', 800, 500)
#TGaxis.SetMaxDigits(2);
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.16)
#c1.SetRightMargin(0.19)
SB2dtempeta1.GetYaxis().SetTitleOffset(1.0)
SB2dtempeta1.GetZaxis().SetLabelOffset(0.1)
SB2dtempeta1.SetTitle(';Pt_{b} (GeV);M_{tb} (GeV)')
SB2dtempeta1.SetStats(0)
SB2dtempeta1.SetMaximum(0.11)
SB2dtempeta1.SetMinimum(0.0)
palette = SB2dtempeta1.GetListOfFunctions().FindObject("palette")
palette.SetX1NDC(0.85)
palette.SetX2NDC(0.9)
SB2dtempeta1.Draw("COLZ")
gPad.Update()
gPad.RedrawAxis()
c1.RedrawAxis()
c1.Print('plots/'+options.cuts+'/Tagrate'+setstr+'Eta1SB2dSB1.root', 'root')
c1.Print('plots/'+options.cuts+'/Tagrate'+setstr+'Eta1SB2dSB1.pdf', 'pdf')

c2 = TCanvas('c22d', 'SB2d Pt fitted tagrate in 0.5 < Eta <1.15', 800, 500)
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.16)
gStyle.SetPalette(1)
SB2dtempeta2.GetYaxis().SetTitleOffset(1.0)
SB2dtempeta2.GetZaxis().SetLabelOffset(0.1)
SB2dtempeta2.SetTitle(';Pt_{b} (GeV);M_{tb} (GeV)')
SB2dtempeta2.SetStats(0)
SB2dtempeta2.SetMaximum(0.11)
SB2dtempeta2.SetMinimum(0.0)
palette = SB2dtempeta2.GetListOfFunctions().FindObject("palette")
palette.SetX1NDC(0.85)
palette.SetX2NDC(0.9)
SB2dtempeta2.Draw("COLZ")
gPad.Update()
gPad.RedrawAxis()
c3.RedrawAxis()
c3.Print('plots/'+options.cuts+'/Tagrate'+setstr+'Eta2SB2dSB1.root', 'root')
c3.Print('plots/'+options.cuts+'/Tagrate'+setstr+'Eta2SB2dSB1.pdf', 'pdf')




output2.cd()
SBtempeta1 = tagrateeta1.Clone("SBdeltaeta1")
SBtempeta2 = tagrateeta2.Clone("SBdeltaeta2")

for xbin in range(0,SBtempeta1.GetNbinsX()+1):
			for ybin in range(0,SBtempeta1.GetNbinsY()+1):
				if SBtempeta1.GetBinContent(xbin,ybin)>0.0:
					for irange in range(0,len(bins)-1):
						#print "from " +str(bins[irange])+ " to " +str(bins[irange+1])
						#print "pt = " + str(SBtempeta1.GetXaxis().GetBinCenter(xbin))
						if bins[irange]<SBtempeta1.GetXaxis().GetBinCenter(xbin)<bins[irange+1]:
							SBtempeta1.SetBinContent(xbin,ybin,SBtempeta1.GetBinContent(xbin,ybin)-vavg1[irange])
				#else:
				#	SBtempeta1.SetBinContent(xbin,ybin,-999)

for xbin in range(0,SBtempeta2.GetNbinsX()+1):
			for ybin in range(0,SBtempeta2.GetNbinsY()+1):
				if SBtempeta2.GetBinContent(xbin,ybin)>0.0:
					for irange in range(0,len(bins)-1):
						#print "from " +str(bins[irange])+ " to " +str(bins[irange+1])
						#print "pt = " + str(SBtempeta1.GetXaxis().GetBinCenter(xbin))
						if bins[irange]<SBtempeta2.GetXaxis().GetBinCenter(xbin)<bins[irange+1]:
							SBtempeta2.SetBinContent(xbin,ybin,SBtempeta2.GetBinContent(xbin,ybin)-vavg2[irange])
				#else:
				#	SBtempeta2.SetBinContent(xbin,ybin,-999)

output2.cd()
SBtempeta1.Write()
SBtempeta2.Write()

c1 = TCanvas('c1SB1', 'SBSUB Pt fitted tagrate in 0.0 < Eta <0.5', 800, 500)
gPad.SetLeftMargin(0.16)
#gPad.SetRightMargin(0.16)
SBtempeta1.GetYaxis().SetTitleOffset(0.8)
SBtempeta1.SetTitle(';Pt_{b} (GeV);M_{tb} (GeV)')
SBtempeta1.SetStats(0)
SBtempeta1.SetMaximum(0.015)
SBtempeta1.SetMinimum(-0.015)
SBtempeta1.Draw("COLZ")
c1.RedrawAxis()
c1.Print('plots/'+options.cuts+'/Tagrate'+setstr+'Eta1SBSUBSB1.root', 'root')
c1.Print('plots/'+options.cuts+'/Tagrate'+setstr+'Eta1SBSUBSB1.pdf', 'pdf')
c2 = TCanvas('c2SB1', 'SBSUB Pt fitted tagrate in 0.5 < Eta <1.15', 800, 500)
gPad.SetLeftMargin(0.16)
#gPad.SetRightMargin(0.16)
SBtempeta2.GetYaxis().SetTitleOffset(0.8)
SBtempeta2.SetTitle(';Pt_{b} (GeV);M_{tb} (GeV)')
SBtempeta2.SetStats(0)
SBtempeta2.SetMaximum(0.025)
SBtempeta2.SetMinimum(-0.025)
SBtempeta2.Draw("COLZ")
c2.RedrawAxis()
c2.Print('plots/'+options.cuts+'/Tagrate'+setstr+'Eta2SBSUBSB1.root', 'root')
c2.Print('plots/'+options.cuts+'/Tagrate'+setstr+'Eta2SBSUBSB1.pdf', 'pdf')


