



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
import time
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

(options, args) = parser.parse_args()

gROOT.Macro("rootlogon.C")

import Bstar_Functions	
from Bstar_Functions import *

Cons = LoadConstants()

#Uncomment for the single lumi from BstarFunctions
cLumi = Cons['lumi']
lumiList = [cLumi]
Lumi = str(int(cLumi))+'pb'

#Process multiple lumis at once with this code otherwise use the above constant pull from BstarFunctions
#THIS FILE IS CURRENTLY ONLY SET TO RUN AT ONE LUMI NUMBER. NEED TO IMPLEMENT A LOOP THROUGH lumiList IF YOU WANT TO DO MORE
#lumiList = [1000, 5000, 10000]
#Lumi = ['1fb', '5fb', '10fb']

rootdir="rootfiles/"+Lumi+"/"

setstr = ""
if options.set=='QCD':
	setstr = 'QCD'
elif options.set=='data':
	setstr = 'Data'

#Make a bunch of txt files to store the fit parameters
saveout = sys.stdout

Outf1   =   open("fitdata/pol2input"+setstr+"_PSET_"+options.cuts+".txt", "w")
Outf2   =   open("fitdata/pol4input"+setstr+"_PSET_"+options.cuts+".txt", "w")
Outf3   =   open("fitdata/pol0input"+setstr+"_PSET_"+options.cuts+".txt", "w")
Outf4   =   open("fitdata/newfitinput"+setstr+"_PSET_"+options.cuts+".txt", "w")
Outf5   =   open("fitdata/newfiterrorinput"+setstr+"_PSET_"+options.cuts+".txt", "w")
Outf6   =   open("fitdata/bpinput"+setstr+"_PSET_"+options.cuts+".txt", "w")
Outf7   =   open("fitdata/bperrorinput"+setstr+"_PSET_"+options.cuts+".txt", "w")
Outf8   =   open("fitdata/pol3input"+setstr+"_PSET_"+options.cuts+".txt", "w")
Outf9   =   open("fitdata/expoconinput"+setstr+"_PSET_"+options.cuts+".txt", "w")
Outf10   =   open("fitdata/expoconerrorinput"+setstr+"_PSET_"+options.cuts+".txt", "w")
Outf11   =   open("fitdata/expolininput"+setstr+"_PSET_"+options.cuts+".txt", "w")
Outf12   =   open("fitdata/expolinerrorinput"+setstr+"_PSET_"+options.cuts+".txt", "w")
sto = sys.stdout  


p0 = 0.0
p1 = 0.0
p2 = 0.0
p3 = 0.0
p4 = 0.0

p00 = 0.0
p01= 0.0
p02= 0.0
p03= 0.0
p04 = 0.0
p11= 0.0
p12= 0.0
p13= 0.0
p14 = 0.0
p22= 0.0
p23= 0.0
p24 = 0.0
p33= 0.0
p34 = 0.0
p44 = 0.0


print "Running on "+options.set

#Load up data and ttbar
fdata = TFile(rootdir+"TWratefile"+options.set+"_PSET_"+options.cuts+".root")
fttbar = TFile(rootdir+"TWratefileweightedttbar"+"_PSET_"+options.cuts+".root")
fsingletop = TFile(rootdir+"TWratefilesingletop"+"_PSET_"+options.cuts+".root")


if options.set == 'QCD':

	output1 = ROOT.TFile( "ModMassFile_"+options.cuts+".root", "recreate" )
	output1.cd()

	ModM = fdata.Get("MpostFull")
	ModMd = fdata.Get("Mpre")

	ModM.Rebin(40)
	ModMd.Rebin(40)

	ModM.Scale(1/ModM.Integral())
	ModMd.Scale(1/ModMd.Integral())

	ModM.Divide(ModM,ModMd,1.0,1.0,"B")

	ModM.Write("rtmass")
	output1.Close()


#Load up signal to look at contamination
#SigFiles = [
#TFile(rootdir+"TWratefileweightedsignalright800_PSET_"+options.cuts+".root"),
#TFile(rootdir+"TWratefileweightedsignalright900_PSET_"+options.cuts+".root"),
#TFile(rootdir+"TWratefileweightedsignalright1000_PSET_"+options.cuts+".root"),
#TFile(rootdir+"TWratefileweightedsignalright1100_PSET_"+options.cuts+".root"),
#TFile(rootdir+"TWratefileweightedsignalright1200_PSET_"+options.cuts+".root"),
#TFile(rootdir+"TWratefileweightedsignalright1300_PSET_"+options.cuts+".root"),
#TFile(rootdir+"TWratefileweightedsignalright1400_PSET_"+options.cuts+".root"),
#]

output = TFile( "plots/TWrate_Maker_"+setstr+"_"+Lumi+"_PSET_"+options.cuts+".root", "recreate" )
output.cd()

# Get numerators and denominators for each eta region

num = fdata.Get("ptposttag")
den = fdata.Get("ptpretag")



# Ditto for ttbar and single top

ttnum = fttbar.Get("ptposttag")
ttden = fttbar.Get("ptpretag")

stnum = fsingletop.Get("ptposttag")
stden = fsingletop.Get("ptpretag")

ntot1 = ttnum.Integral() + num.Integral() + stnum.Integral()
dtot1 = ttden.Integral() + den.Integral() + stden.Integral()

bins=[]
#bins= [350,400,460,570,700,1000,1600]
bins= variableBins(den,16)
print bins

#time.sleep(10)

bins2=array('d',bins)

numr = num.Rebin(len(bins2)-1,"numr",bins2)
denr = den.Rebin(len(bins2)-1,"denr",bins2)

ttnumr = ttnum.Rebin(len(bins2)-1,"ttnumr",bins2)
ttdenr = ttden.Rebin(len(bins2)-1,"ttdenr",bins2)

stnumr = stnum.Rebin(len(bins2)-1,"stnumr",bins2)
stdenr = stden.Rebin(len(bins2)-1,"stdenr",bins2)


#TTbar subtraction is done here
if options.set=='data':
	print 'subtracting ttbar and single top'
	numr.Add(ttnumr,-1)
	denr.Add(ttdenr,-1)
	numr.Add(stnumr,-1)
	denr.Add(stdenr,-1)



outputa = TFile( "plots/"+options.cuts+"/B_tagging_sigcont"+setstr+".root", "recreate" )
outputa.cd()
mass = [1300,1500,1700,1900,2100,2300,2700]
#for ifile in range(0,len(SigFiles)):
#	nseta1 = SigFiles[ifile].Get("pteta1")
#	dseta1 = SigFiles[ifile].Get("pteta1pretag")
#	nseta2 = SigFiles[ifile].Get("pteta2")
#	dseta2 = SigFiles[ifile].Get("pteta2pretag")

#	nseta1r = nseta1.Rebin(len(bins2)-1,"nseta1r",bins2)
#	dseta1r = dseta1.Rebin(len(bins2)-1,"dseta1r",bins2)

#	nseta2r = nseta2.Rebin(len(bins2)-1,"nseta2r",bins2)
#	dseta2r = dseta2.Rebin(len(bins2)-1,"dseta2r",bins2)


	
#	nseta1r.Add(neta1r)
#	dseta1r.Add(deta1r)

#	nseta2r.Add(neta2r)
#	dseta2r.Add(deta2r)

#	tagrateseta1 = nseta1r.Clone("tagrateseta1"+str(mass[ifile]))
#	tagrateseta1.Divide(tagrateseta1,dseta1r,1.0,1.0,"B")

#	tagrateseta2 = nseta2r.Clone("tagrateseta2"+str(mass[ifile]))
#	tagrateseta2.Divide(tagrateseta2,dseta2r,1.0,1.0,"B")


#	tagrateseta1.Write()
#	tagrateseta2.Write()









output.cd()

# Create subtracted tagrates by division

tagrate = numr.Clone("tagrate")
#tagrateeta1.Divide(deta1r)
tagrate.Divide(tagrate,denr,1.0,1.0,"B")


tagrate.Write()


# The rest here writes the fit, and uses the covariance matrix to propagate errors for various functions

sys.stdout = saveout
print "------------------------------------"
print "POL2"
print "------------------------------------"
# This next line tells any print statement to go the the txt file Outf1
sys.stdout = Outf1
tagrate.Fit("pol2","F")
fitter = TVirtualFitter.GetFitter()

for i in range(0,3):
	print(fitter.GetParameter(i))

p0 = fitter.GetCovarianceMatrixElement(0,0)
p1 = 2*fitter.GetCovarianceMatrixElement(0,1)
p2 = 2*fitter.GetCovarianceMatrixElement(0,2) + fitter.GetCovarianceMatrixElement(1,1)
p3 = 2*fitter.GetCovarianceMatrixElement(2,1)
p4 = fitter.GetCovarianceMatrixElement(2,2)

sys.stdout = Outf2
print str(p0)
print str(p1)
print str(p2)
print str(p3)
print str(p4)


sys.stdout = saveout
print "------------------------------------"
print "POL0"
print "------------------------------------"
sys.stdout = Outf3
tagrate.Fit("pol0","F")
fitter = TVirtualFitter.GetFitter()
print(fitter.GetParameter(0))


sys.stdout = saveout
print "------------------------------------"
print "BIFPOLY"
print "------------------------------------"

# This is the fit we use.  BIFP is the bifurcation point

BIFP=500.0
BP =TF1("BP",BifPoly,400,4000,5)
BP.FixParameter(4,BIFP)

c4 = TCanvas('c4', 'Tagrate', 1300, 600)
c4.cd()
tagrate.Fit("BP","F")

sys.stdout = Outf6
fitter = TVirtualFitter.GetFitter()
print(fitter.GetParameter(0))
print(fitter.GetParameter(1))
print(fitter.GetParameter(2))
print(fitter.GetParameter(3))
print(BIFP)
print BP.GetChisquare()
print BP.GetNDF()
sys.stdout = Outf7

#These constants contain info about the uncertainty from the covariance matrix
p00 = fitter.GetCovarianceMatrixElement(0,0)
p01 = 2*fitter.GetCovarianceMatrixElement(0,1)
p02 = 2*fitter.GetCovarianceMatrixElement(0,2)
p03 = 2*fitter.GetCovarianceMatrixElement(0,3)
p11 = fitter.GetCovarianceMatrixElement(1,1)
p12 = 2*fitter.GetCovarianceMatrixElement(1,2)
p13 = 2*fitter.GetCovarianceMatrixElement(1,3)
p22 = fitter.GetCovarianceMatrixElement(2,2)
p23 = 2*fitter.GetCovarianceMatrixElement(2,3)
p33 = fitter.GetCovarianceMatrixElement(3,3)
#The funky order here is important 
print str(p00)
print str(p11)
print str(p22)
print str(p01)
print str(p02)
print str(p12)
print str(p33)
print str(p03)
print str(p13)
print(BIFP)



tagrate.Draw()
c4.Print("plots/"+options.cuts+"/WPTAGFIT"+setstr+".root","root")


sys.stdout = saveout
print "------------------------------------"
print "POL3"
print "------------------------------------"

#c1.cd()
sys.stdout = Outf8
tagrate.Fit("pol3","F")
fitter = TVirtualFitter.GetFitter()
for i in range(0,4):
	print(fitter.GetParameter(i))
#tagrateeta1.Draw()


expofitlin =TF1("expofitlin","expo(0) + pol1(2)")
sys.stdout = saveout
print "------------------------------------"
print "EXPO + LINEAR"
print "------------------------------------"

#expofitlin.SetParameter(0, -1.0e+00)
#expofitlin.SetParameter(1, -7.4e-03)
#expofitlin.SetParameter(2, 4.1e-02)
#expofitlin.SetParameter(3, 4.0e-06)

#c1.cd()
sys.stdout = Outf11
tagrate.Fit("expofitlin","F")
fitter = TVirtualFitter.GetFitter()
for i in range(0,4):
	print(fitter.GetParameter(i))
sys.stdout = Outf12
p00 = fitter.GetCovarianceMatrixElement(0,0)
p01 = 2*fitter.GetCovarianceMatrixElement(0,1)
p02 = 2*fitter.GetCovarianceMatrixElement(0,2)
p03 = 2*fitter.GetCovarianceMatrixElement(0,3)
p04 = 2*fitter.GetCovarianceMatrixElement(0,4)
p11 = fitter.GetCovarianceMatrixElement(1,1)
p12 = 2*fitter.GetCovarianceMatrixElement(1,2)
p13 = 2*fitter.GetCovarianceMatrixElement(1,3)
p14 = 2*fitter.GetCovarianceMatrixElement(1,4)
p22 = fitter.GetCovarianceMatrixElement(2,2)
p23 = 2*fitter.GetCovarianceMatrixElement(2,3)
p24 = 2*fitter.GetCovarianceMatrixElement(2,4)
p33 = fitter.GetCovarianceMatrixElement(3,3)
p34 = 2*fitter.GetCovarianceMatrixElement(3,4)
p44 = fitter.GetCovarianceMatrixElement(4,4)
print str(p00)
print str(p01)
print str(p02)
print str(p03)
print str(p04)
print str(p11)
print str(p12)
print str(p13)
print str(p14)
print str(p22)
print str(p23)
print str(p24)
print str(p33)
print str(p34)
print str(p44)
#tagrateeta1.Draw()

sys.stdout = saveout
print "------------------------------------"
print "EXPO + CONSTANT"
print "------------------------------------"
expofit =TF1("expofit","expo(0) + pol0(2)")

#expofit.SetParameter(0, -1.03e+00);
#expofit.SetParameter(1, 0.05);
#expofit.SetParameter(2, 0.2);

#c1.cd()
sys.stdout = Outf9
tagrate.Fit("expofit","F")
fitter = TVirtualFitter.GetFitter()
for i in range(0,3):
	print(fitter.GetParameter(i))
sys.stdout = Outf10
p00 = fitter.GetCovarianceMatrixElement(0,0)
p01 = 2*fitter.GetCovarianceMatrixElement(0,1)
p02 = 2*fitter.GetCovarianceMatrixElement(0,2)
p03 = 2*fitter.GetCovarianceMatrixElement(0,3)
p11 = fitter.GetCovarianceMatrixElement(1,1)
p12 = 2*fitter.GetCovarianceMatrixElement(1,2)
p13 = 2*fitter.GetCovarianceMatrixElement(1,3)
p22 = fitter.GetCovarianceMatrixElement(2,2)
p23 = 2*fitter.GetCovarianceMatrixElement(2,3)
p33 = fitter.GetCovarianceMatrixElement(3,3)
print str(p00)
print str(p01)
print str(p02)
print str(p03)
print str(p11)
print str(p12)
print str(p13)
print str(p22)
print str(p23)
print str(p33)
#tagrateeta1.Draw()

sys.stdout = saveout
print "------------------------------------"
print "FIT"
print "------------------------------------"
FIT =TF1("FIT","[0]*([1]+x)/([2]+x)+[3]*x")
sys.stdout = Outf4
tagrate.Fit("FIT","F")
fitter = TVirtualFitter.GetFitter()
print(fitter.GetParameter(0))
print(fitter.GetParameter(1))
print(fitter.GetParameter(2))
print(fitter.GetParameter(3))

p00 = fitter.GetCovarianceMatrixElement(0,0)
p01 = 2*fitter.GetCovarianceMatrixElement(0,1)
p02 = 2*fitter.GetCovarianceMatrixElement(0,2)
p03 = 2*fitter.GetCovarianceMatrixElement(0,3)
p11 = fitter.GetCovarianceMatrixElement(1,1)
p12 = 2*fitter.GetCovarianceMatrixElement(1,2)
p13 = 2*fitter.GetCovarianceMatrixElement(1,3)
p22 = fitter.GetCovarianceMatrixElement(2,2)
p23 = 2*fitter.GetCovarianceMatrixElement(2,3)
p33 = fitter.GetCovarianceMatrixElement(3,3)
sys.stdout = Outf5
#print_options.set_float_precision(2)
print str(p00)
print str(p01)
print str(p02)
print str(p03)
print str(p11)
print str(p12)
print str(p13)
print str(p22)
print str(p23)
print str(p33)

#The rest of this file makes the 3d mistag rates (parameterized in pt,eta,Mtw)

output1 = ROOT.TFile( "Tagrate"+setstr+"2D_"+options.cuts+".root", "recreate" )
output2 = ROOT.TFile( "plots/"+options.cuts+"/Tagrate"+setstr+"2Ddelta.root", "recreate" )

output = ROOT.TFile( "plots/"+options.cuts+"/Tagrate"+setstr+"Slices.root", "recreate" )

#This is one number that controls the automatic variable binning sensitivity
bres = 0.8

pre=[]

dpre=[]

numNOSUB = fdata.Get("MtwwptcomparepostSB1")
denNOSUB = fdata.Get("MtwwptcomparepreSB1")


numttbar = fttbar.Get("MtwwptcomparepostSB1")
denttbar = fttbar.Get("MtwwptcomparepreSB1")

numstbar = fsingletop.Get("MtwwptcomparepostSB1")
denstbar = fsingletop.Get("MtwwptcomparepreSB1")

num = numNOSUB.Clone("num")
num.Add(numttbar,-1)
num.Add(numstbar,-1)

den = denNOSUB.Clone("den")
den.Add(denttbar,-1)
den.Add(denstbar,-1)

slop = []

vavg = []


numr = ROOT.TH2F("numr",  "Comparison wpt and Mtw",   		len(bins2)-1, bins2,  140,  500,  4000 )
denr = ROOT.TH2F("demr",  "Comparison wpt and Mtw",   		len(bins2)-1, bins2,  140,  500,  4000 )

#test = TCanvas("test","test",1300,600)
#test.cd()
#b1 = neta1.GetXaxis().FindBin(bins2[1])
#b2 = neta1.GetXaxis().FindBin(bins2[2]-1.0)
#tester = deta1.ProjectionY("SB1projYdeta1_"+str(bins2[1])+"_to_"+str(bins2[2]),b1,b2,"e")
#tester.Draw("same")
#test.Print('tester.root')
#c3.cd()



for ibin in range(0,len(bins2)-1):

		bin1 = num.GetXaxis().FindBin(bins2[ibin])
		bin2 = num.GetXaxis().FindBin(bins2[ibin+1]-1.0)

		pre.append(num.ProjectionY("SB1projY_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]),bin1,bin2,"e"))

		dpre.append(den.ProjectionY("SB1projYd_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]),bin1,bin2,"e"))
		
		print "" 
		print bins2[ibin]
		print "THIS"
		print pre[ibin].Integral()
		print dpre[ibin].Integral()
		print "EQUALS"
		print num.Integral(bin1,bin2,0,-1)
		print den.Integral(bin1,bin2,0,-1)


		#breaks on rate_sideband so need this
		times = 0
		if dpre[ibin].Integral() == 0:
			times = times + 1
			print times
			continue


		vavg.append(pre[ibin].Integral()/dpre[ibin].Integral())

		tempbin1 = 0
		error1 = ROOT.Double(1.0)

		fcont = False

		binning1= array('d',[])
		int1 = pre[ibin].Integral()
		binning1.append(500.0)
		for ibin1 in range(1,pre[ibin].GetNbinsX()-1):
			cont = pre[ibin].IntegralAndError(tempbin1+1,ibin1,error1)
			if cont > 0.0:
				if not fcont:
					tempbin1 = ibin1
					binning1.append(pre[ibin].GetBinLowEdge(tempbin1))
					fcont = True
				if error1*int1/(cont*cont) < .5:
					tempbin1 = ibin1
					binning1.append(pre[ibin].GetBinLowEdge(tempbin1) + pre[ibin].GetBinWidth(tempbin1))

		binning1.append(4000.0)
		print binning1
		fcont = False
		tempbin3 = 0
		error3 = ROOT.Double(1.0)

		


		pre[ibin] = pre[ibin].Rebin(len(binning1)-1,"SB1projY_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]),binning1)

		dpre[ibin] = dpre[ibin].Rebin(len(binning1)-1,"SB1projYd_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]),binning1)

	
		for ibin1 in range(1,numr.GetNbinsY()):
			bcont = numr.GetYaxis().GetBinCenter(ibin1)

			bin1d = pre[ibin].FindBin(bcont)
	
			numr.SetBinContent(ibin+1,ibin1,pre[ibin].GetBinContent(bin1d))
			denr.SetBinContent(ibin+1,ibin1,dpre[ibin].GetBinContent(bin1d))


			numr.SetBinError(ibin+1,ibin1,pre[ibin].GetBinError(bin1d))
			denr.SetBinError(ibin+1,ibin1,dpre[ibin].GetBinError(bin1d))


		pre[ibin].Divide(pre[ibin],dpre[ibin],1,1,"B")


		pre[ibin].Fit("pol1","F")
		fitter = TVirtualFitter.GetFitter()
		slop.append(fitter.GetParameter(1))



		pre[ibin].Fit("pol0","F")
		fitter = TVirtualFitter.GetFitter()
		AVG = fitter.GetParameter(0)


		pull= pre[ibin].Clone("PULL_SB1projY_"+str(bins2[ibin])+"_to_"+str(bins2[ibin+1]))
		for ibin1 in range(1,pull.GetNbinsX()+1):
			if pull.GetBinError(ibin1)!=0.0:
				pull.SetBinContent(ibin1,(pull.GetBinContent(ibin1)-AVG)/pull.GetBinError(ibin1))
				print (pull.GetBinContent(ibin1)-AVG)/pull.GetBinError(ibin1)
			else:
				pull.SetBinContent(ibin1,0.0)

		print ""

		pull.SetFillColor(kBlue)

		output.cd()



tagrate = numr.Clone("tagrate")
tagrate.Divide(tagrate,denr,1,1,"B")

output1.cd()
tagrate.Write("SB1tagrate2D")

c1 = TCanvas('c1SB1', 'Pt fitted tagrate', 800, 500)
tagrate.Draw("COLZ")
c1.RedrawAxis()
c1.Print('plots/'+options.cuts+'/Tagrate'+setstr+'SB1'+'.root', 'root')
c1.Print('plots/'+options.cuts+'/Tagrate'+setstr+'SB1'+'.pdf', 'pdf')


print vavg

output1.cd()
tagrate.Write()

SB2dtemp = tagrate.Clone("SB2dtemp")

c1 = TCanvas('c12d', 'SB2d Pt fitted tagrate', 800, 500)
#TGaxis.SetMaxDigits(2);
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.16)
#c1.SetRightMargin(0.19)
SB2dtemp.GetYaxis().SetTitleOffset(1.0)
SB2dtemp.SetTitle(';Pt_{t} (GeV);M_{tW} (GeV)')
SB2dtemp.SetStats(0)
SB2dtemp.SetMaximum(0.11)
SB2dtemp.SetMinimum(0.0)
palette = SB2dtemp.GetListOfFunctions().FindObject("palette")
palette.SetX1NDC(0.85)
palette.SetX2NDC(0.9)
SB2dtemp.Draw("COLZ")
gPad.Update()
gPad.RedrawAxis()
c1.RedrawAxis()
c1.Print('plots/'+options.cuts+'/Tagrate'+setstr+'SB2dSB1.root', 'root')
c1.Print('plots/'+options.cuts+'/Tagrate'+setstr+'SB2dSB1.pdf', 'pdf')


output2.cd()
SBtemp = tagrate.Clone("SBdelta")

for xbin in range(0,SBtemp.GetNbinsX()+1):
			for ybin in range(0,SBtemp.GetNbinsY()+1):
				if SBtemp.GetBinContent(xbin,ybin)>0.0:
					for irange in range(0,len(bins)-1):
						#print "from " +str(bins[irange])+ " to " +str(bins[irange+1])
						#print "pt = " + str(SBtempeta1.GetXaxis().GetBinCenter(xbin))
						if bins[irange]<SBtemp.GetXaxis().GetBinCenter(xbin)<bins[irange+1]:
							SBtemp.SetBinContent(xbin,ybin,SBtemp.GetBinContent(xbin,ybin)-vavg[irange])
				#else:
				#	SBtempeta1.SetBinContent(xbin,ybin,-999)


output2.cd()
SBtemp.Write()

c1 = TCanvas('c1SB1', 'SBSUB Pt fitted tagrate', 800, 500)
gPad.SetLeftMargin(0.16)
#gPad.SetRightMargin(0.16)
SBtemp.GetYaxis().SetTitleOffset(0.8)
SBtemp.SetTitle(';Pt_{t} (GeV);M_{tW} (GeV)')
SBtemp.SetStats(0)
SBtemp.SetMaximum(0.015)
SBtemp.SetMinimum(-0.015)
SBtemp.Draw("COLZ")
c1.RedrawAxis()
c1.Print('plots/'+options.cuts+'/Tagrate'+setstr+'SBSUBSB1.root', 'root')
c1.Print('plots/'+options.cuts+'/Tagrate'+setstr+'SBSUBSB1.pdf', 'pdf')



