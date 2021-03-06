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

gStyle.SetOptStat(0)
parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
				default       =       'QCD',
				dest          =       'set',
				help          =       'data or QCD')
parser.add_option('-p', '--mtwcuts', metavar='F', type='string', action='store',
				default		=	'800,1000',
				dest		=	'mtwcuts',
				help		=	'Mtw cuts, low to high, separated by a comma')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
				default       =       'default',
				dest          =       'cuts',
				help          =       'Cuts type (ie default, rate, etc)')
parser.add_option('-C', '--cheat', metavar='F', type='string', action='store',
				default       =       'off',
				dest          =       'cheat',
				help          =       'Turns the top mass blinding on and off - can also be narrow')
parser.add_option('-q', '--qcdsample', metavar='F', type='string', action='store',
				default       =       'all',
				dest          =       'qcdsample',
				help          =       'all or any comma separated combo of HT500, HT700, etc')
parser.add_option('-S', '--selection', metavar='F', type='string', action='store',
				default       =       'full',
				dest          =       'selection',
				help          =       'full, sjbtag_off, tau32_off')
parser.add_option('-e', '--estimate', metavar='F', type='string', action='store',
				default       =       'off',
				dest          =       'estimate',
				help          =       'run the estimate or not')
parser.add_option('-f', '--f', metavar='F', type='string', action='store',
				default       =       'quad',
				dest          =       'fit',
				help          =       'fit of Rp/f(mt) - lin,quad,new')
parser.add_option('-r', '--run2d', metavar='F', type='string', action='store',
				default       =       'off',
				dest          =       'run2d',
				help          =       'run the 2D fit or or not')

(options, args) = parser.parse_args()

# Turn on/off plotting the signal on the fit plots
plotSignal = False
if plotSignal:
	fSR1200 = TFile.Open('../local_studies/SR1200_top_mass_dist.root')
	hSR1200 = fSR1200.Get('hS1200')
	hSR1200.Scale(2/hSR1200.Integral())
	hSR1200.SetLineColor(kBlue)
	hSR1200.SetLineWidth(2)

print "Options summary"
print "=================="
for  opt,value in options.__dict__.items():
		#print str(option)+ ": " + str(options[option]) 
		print str(opt) +': '+ str(value)
print "=================="
print ""

# Turns off plotting
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True


# ------ Define the set of cuts (pt, dy, and tau21 already applied)-------
if options.cuts.find('default') != -1:
	wmass_cut = '(SDmass_w>65.)&&(SDmass_w<105.)'
elif options.cuts.find('sideband') != -1:
	wmass_cut = '(SDmass_w>30.)&&(SDmass_w<65.)'


if options.cheat == 'off':
	tSDmass_cut = '(SDmass_top>105)&&(SDmass_top<210)'
	tmass_cut = '!((mass_top>105)&&(mass_top<210))'
elif options.cheat == 'narrow':
	tSDmass_cut = '(SDmass_top>155)&&(SDmass_top<195)'
	tmass_cut = '!((mass_top>155)&&(mass_top<195))'
elif options.cheat == 'on':
	tSDmass_cut = '(SDmass_top>105)&&(SDmass_top<210)'
	tmass_cut = '(1)'
tau32_cut = '(tau32<0.65)'
sjbtag_cut = '(sjbtag>0.5426)'
mtw_cut = '(mass_tw>'+options.mtwcuts.split(',')[0]+'.)&&(mass_tw<'+options.mtwcuts.split(',')[1]+'.)'


# --------- Define the distributions to use -------------------------------

DistsWeWantToEstimate = []
# FORMAT IS:
# dist = ("name", "location of file", "name of tree", "weight (can be more complicated than just a number, see MC example below)")
if options.set == "data":
	Data = DIST("Data", "../rootfiles/35851pb/TWminitree_data_PSET_"+options.cuts+".root", "miniTree", "weight")
	DistsWeWantToEstimate = [Data]

	# DISTRIBUTIONS YOU NEED TO SUBTRACT (KNOWN MC CONTRIBUTIONS):
	ttbar = DIST("ttbar", "../rootfiles/35851pb/TWminitree_weightedttbar_PSET_"+options.cuts+".root", "miniTree", "weight")
	st_tW = DIST("st_tW", "../rootfiles/35851pb/TWminitree_weightedsingletop_tW_PSET_"+options.cuts+".root", "miniTree", "weight")
	st_tWB = DIST("st_tWB", "../rootfiles/35851pb/TWminitree_weightedsingletop_tWB_PSET_"+options.cuts+".root", "miniTree", "weight")
	st_t = DIST("st_t", "../rootfiles/35851pb/TWminitree_weightedsingletop_t_PSET_"+options.cuts+".root", "miniTree", "weight")
	st_tB = DIST("st_tB", "../rootfiles/35851pb/TWminitree_weightedsingletop_tB_PSET_"+options.cuts+".root", "miniTree", "weight")

	# Now we arrange them correctly:
	DistsWeWantToIgnore = [ttbar, st_tW, st_tWB, st_t, st_tB]

elif options.set == "QCD":
	QCDHT500 = DIST("QCDHT500", "../rootfiles/35851pb/TWminitree_weightedQCDHT500_PSET_"+options.cuts+".root", "miniTree", "weight")
	QCDHT700 = DIST("QCDHT700", "../rootfiles/35851pb/TWminitree_weightedQCDHT700_PSET_"+options.cuts+".root", "miniTree", "weight")
	QCDHT1000 = DIST("QCDHT1000", "../rootfiles/35851pb/TWminitree_weightedQCDHT1000_PSET_"+options.cuts+".root", "miniTree", "weight")
	QCDHT1500 = DIST("QCDHT1500", "../rootfiles/35851pb/TWminitree_weightedQCDHT1500_PSET_"+options.cuts+".root", "miniTree", "weight")
	QCDHT2000 = DIST("QCDHT2000", "../rootfiles/35851pb/TWminitree_weightedQCDHT2000_PSET_"+options.cuts+".root", "miniTree", "weight")

	QCDdir = ''
	if options.qcdsample == 'all':
		DistsWeWantToEstimate = [QCDHT500, QCDHT700, QCDHT1000, QCDHT1500, QCDHT2000]
	elif options.qcdsample.find('HT500') != -1:
		DistsWeWantToEstimate.append(QCDHT500)
		QCDdir+='HT500/'
	elif options.qcdsample.find('HT700') != -1:
		DistsWeWantToEstimate.append(QCDHT700)
		QCDdir+='HT700/'
	elif options.qcdsample.find('HT1000') != -1:
		DistsWeWantToEstimate.append(QCDHT1000)
		QCDdir+='HT1000/'
	elif options.qcdsample.find('HT1500') != -1:
		DistsWeWantToEstimate.append(QCDHT1500)
		QCDdir+='HT1500/'
	elif options.qcdsample.find('HT2000') != -1:
		DistsWeWantToEstimate.append(QCDHT2000)
		QCDdir+='HT2000/'

	# Don't have any dists to ignore with QCD MC
	DistsWeWantToIgnore = []

# ------------------------------------------------------------------------
# Before proceeding, need to reweight our dists to cross section, lumi, and number of events
# The weighting for this is stored in the TWminitree file, just need to grab and apply using the below
# function from Distribution_Header.py -LC 10/14/17

# Only want to do this with MC since data doesn't get this weight
if options.set == 'QCD':
	for distE in DistsWeWantToEstimate:
		distE.bstarReweight()
for distI in DistsWeWantToIgnore:
	distI.bstarReweight()

# Create instance of Alphabetizer class
Bstar = Alphabetizer("Bstar", DistsWeWantToEstimate, DistsWeWantToIgnore)

# Define some selections - MakeCuts connects cuts with '&&'
presel = mtw_cut
selection = MakeCuts([sjbtag_cut,tau32_cut])
tag = MakeCuts([selection,presel,tSDmass_cut])
antitag = MakeCuts([sjbtag_cut,tau32_cut],'not') + '&&' + MakeCuts([presel,tSDmass_cut])

print 'Presel 		= ' + presel
print 'Selection 	= ' + selection
print 'Tag 		= ' + tag
print 'Antitag 	= ' + antitag

# -------------------- Do some binning -----------------------------------
bins = array('d',[75,85,95,105,210,250])
# bins = array('d',[75,85,95,105,115,125,135,145,155,165,175,185,195,210,230,260,320])
truthbins = []
if options.set == "QCD" and options.cheat == 'off':
	truthbins = array('d',[105,115,125,135,145,155,165,175,185,195,210])
	# truthbins = array('d',[165,170,175,180])
elif options.set == "QCD" and options.cheat == 'on':
	bins = array('d',[75,85,95,105,115,125,135,145,155,165,175,185,195,210,250])
elif options.cheat == 'narrow':
	bins = array('d',[75,85,95,105,115,125,135,145,155,195,210,250])
	truthbins = array('d',[155,165,175,185,195])
elif options.set == "data" and options.cheat == 'narrow':
	bins = array('d',[75,85,95,105,115,125,135,145,155,195,210,250])
	truthbins = array('d',[])

# -------------- Define the function to fit in the Mtop direction ----------
center = 0
if options.fit == 'quad':
	# fitfunction = '[0]+[1]*(x+'+str(center)+')+[2]*(x+'+str(center)+')**2'
	fitfunction = '[0]+[1]*x+[2]*x**2'
elif options.fit == 'lin':
	fitfunction = '[0]+[1]*(x+'+str(center)+')'
elif options.fit == 'new':
	fitfunction = '[0]*exp(x*[1]-x**2*[2])'# Gaussian divided by decaying exponential


# ---------------- Define a folder to save in ----------------------------
if options.qcdsample == 'all':
	printDir = 'results/'+options.cuts+'/'
else:
	printDir = 'results/'+options.cuts+'/QCDbreakdown/'+QCDdir

# --------------- Create a 2D plot of tau32 v Mt -------------------------
c2D = TCanvas('c2D','c2D',800,700)
c2D.SetRightMargin(0.15)

Bstar.SetRegions(['mass_top','tau32',18,70,250,20,0,1],'('+presel+')')
Bstar.TwoDPlot.GetYaxis().SetTitle('#tau_{32}')
Bstar.TwoDPlot.GetXaxis().SetTitle('M_{Top}')
Bstar.TwoDPlot.SetTitle(options.qcdsample+' - Mtw ['+options.mtwcuts+']')
Bstar.TwoDPlot.Draw('COLZ')

c2D.Print(printDir +'MtvsTau32_Mtw'+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+'.png','png')

# --------- Make a file to save out to ----------------------------
myFile = TFile(printDir+"Alphabet"+options.set+'_'+options.cuts+"_Mtw_"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".root", "recreate")
myFile.cd()

# ------------- Now Make the fit based on the Mt sideband ----------------
# If doing 1D Mtop fit with Mtw slices
if options.run2d.find('on') == -1:
	# This should do everything
	Bstar.doRatesFlexFit('mass_top',tmass_cut,selection,presel,bins,truthbins,fitfunction,center)


	# ------------ Plot the fit -------------------------------
	C1 = TCanvas("C1", "", 800, 600)
	C1.cd()

	Bstar.G.SetMarkerStyle(10)

	Bstar.G.SetMaximum(0.37)
	Bstar.G.Draw('AP')
	Bstar.EG.Draw("same")	
	Bstar.pG.Draw('p same')

	Bstar.G.SetTitle('Alphabet R_{P/F} - '+options.set+' - M_{tW} '+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1])
	Bstar.G.GetXaxis().SetTitle("M_{top} (GeV)")
	Bstar.G.GetYaxis().SetTitle("N_{passed}/N_{failed}")

	if Bstar.truthG != None:
		Bstar.truthG.SetMarkerStyle(25)
		Bstar.truthG.Draw("P same")

	leg = TLegend(0.15,0.7,0.35,0.88)
	leg.SetTextSize(.025)
	leg.SetLineColor(0)
	leg.SetFillColor(0)
	leg.AddEntry(Bstar.G, "events used in fit", "P")
	if Bstar.truthG != None:
		leg.AddEntry(Bstar.truthG, 'events not used in fit', 'P')

	if plotSignal and center == 0:
		hSR1200.Draw('samehist')
		leg.AddEntry(hSR1200, 'b* signal 1200 GeV', 'L')

	leg.Draw()

	

	C1.Print(printDir+"fit_"+options.set+"_Mtw"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".pdf")
	C1.Print(printDir+"fit_"+options.set+"_Mtw"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".png")

	myFile.cd()
	Bstar.EH.Write()
	Bstar.Fit.Write()


#####################################
# Now we actually run the Estimate! #
#####################################
if options.estimate == 'on' and options.run2d == 'off':
	# var we want to look at:
	mtw_bins = (int(options.mtwcuts.split(',')[1])-int(options.mtwcuts.split(',')[0]))/100
	# var_array2 = ["mass_tw", mtw_bins,float(options.mtwcuts.split(',')[0]),float(options.mtwcuts.split(',')[1])]
	var_array2 = ['mass_tw',35,500,4000]
	# var_array2 = ['mass_top',23,70,300]

	# Make the estimated distributions
	Bstar.MakeEstFlexFit(var_array2, 'mass_top',antitag, tag, center)
	hbins = var_array2[1:]

	# Going to quickly save everything out for later debugging
	for i in Bstar.hists_MSR+Bstar.hists_MSR_SUB+Bstar.hists_EST+Bstar.hists_EST_SUB+Bstar.hists_ATAG:
		i.Write()

	AT = TH1F('AT','',hbins[0],hbins[1], hbins[2])
	for i in Bstar.hists_ATAG:
		AT.Add(i,1.)
	AT.Write()
	Vtemp = TH1F('Vtemp','',hbins[0],hbins[1], hbins[2])
	for i in Bstar.hists_MSR:
		Vtemp.Add(i,1.)
	Vtemp.Write()

	# the real value is the sum of the histograms in self.hists_MSR
	V = TH1F("V", "", hbins[0],hbins[1], hbins[2])
	for i in Bstar.hists_MSR:
		V.Add(i,1.)

	# the estimate is the sum of the histograms in self.hists_EST and self.hist_MSR_SUB
	N = TH1F("QCD", "", hbins[0], hbins[1], hbins[2])
	for i in Bstar.hists_EST:
		N.Add(i,1.)
	for i in Bstar.hists_MSR_SUB:
		N.Add(i,1.)
	for i in Bstar.hists_EST_SUB:
		N.Add(i,-1.)
	# # We can do the same thing for the Up and Down shapes:
	# NU = TH1F("QCD_Up", "", hbins[0],hbins[1], hbins[2])
	# for i in Bstar.hists_EST_UP:
	# 	NU.Add(i,1.)
	# for i in Bstar.hists_MSR_SUB:
	# 	NU.Add(i,1.)
	# for i in Bstar.hists_EST_SUB_UP:
	# 	NU.Add(i,-1.)
	# ND = TH1F("QCD_Down", "", hbins[0],hbins[1], hbins[2])
	# for i in Bstar.hists_EST_DN:
	# 	ND.Add(i,1.)
	# for i in Bstar.hists_MSR_SUB:
	# 	ND.Add(i,1.)
	# for i in Bstar.hists_EST_SUB_DN:
	# 	ND.Add(i,-1.)


# ---- Lots of plot formatting --------------
	vartitle = "M_{tW} (GeV)"

	# NU.SetLineColor(kBlack)
	# ND.SetLineColor(kBlack)
	# NU.SetLineStyle(2)
	# ND.SetLineStyle(2)
	N.SetLineColor(kBlack)
	N.SetFillColor(kPink+3)

	V.SetStats(0)
	# V.Sumw2()
	V.SetLineColor(1)
	V.SetFillColor(0)
	V.SetMarkerColor(1)
	V.SetMarkerStyle(20)
	N.GetYaxis().SetTitle("events / "+str((hbins[2]-hbins[1])/hbins[0])+" GeV")
	N.GetXaxis().SetTitle(vartitle)

	leg2 = TLegend(0.75,0.75,0.95,0.95)
	#leg2.SetHeader("cut @ #tau_{2}/#tau_{1} < 0.5")
	leg2.SetLineColor(0)
	leg2.SetFillColor(0)
	leg2.AddEntry(V, "Data in tag region", "PL")
	leg2.AddEntry(N, "Data prediction", "F")
	# leg2.AddEntry(NU, "uncertainty", "F")


	FindAndSetMax([V,N])#, NU, ND])
	C3 = TCanvas("C3", "", 800, 600)
	C3.cd()
	N.Draw("Hist")
	V.Draw("same E0")
	# NU.Draw("same")
	# ND.Draw("same")
	leg2.Draw()
	
# --- Write out the canvas ---------------------
	C3.Print(printDir+"bkg_"+options.set+"_Mtw"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".pdf")
	C3.Print(printDir+"bkg_"+options.set+"_Mtw"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".png")

# --- Save the histograms ----------------------
	myFile.cd()
	N.Write()
	V.Write()
	# NU.Write()
	# ND.Write()


# If doing the 2D fit and grabbing fitted parameter distributions
# Discrete 2D
if options.run2d.find('on') != -1:
	# Grab the saved file with the parameter fits
	TwoDFitFile = TFile.Open('results/'+options.cuts+'/MtwvsBkg_'+options.set+'_mtfit_'+options.fit+'_cheat_'+options.cheat+'.root')

	if options.run2d == 'on_disc':
		# var we want to look at:
		mtw_bins = (int(options.mtwcuts.split(',')[1])-int(options.mtwcuts.split(',')[0]))/100
		mtw_center = (int(options.mtwcuts.split(',')[1])+int(options.mtwcuts.split(',')[0]))/2
		var_array2 = ['mass_tw',35,500,4000]

		Bstar.fitFunc = fitfunction

		# Same as MakeEstFlexFit except it reconstructs an Rp/f for the Mtw bin center
		Bstar.MakeEstFlexFit(var_array2,'mass_top',antitag, tag, center,TwoDFitFile,mtw_center)

		hbins = var_array2[1:]

		# the real value is the sum of the histograms in self.hists_MSR
		V = TH1F("V2d", "", hbins[0],hbins[1], hbins[2])
		for i in Bstar.hists_MSR:
			V.Add(i,1.)

		# the estimate is the sum of the histograms in self.hists_EST and self.hist_MSR_SUB
		N = TH1F("QCD2d", "", hbins[0], hbins[1], hbins[2])
		for i in Bstar.hists_EST:
			N.Add(i,1.)
		for i in Bstar.hists_MSR_SUB:
			N.Add(i,1.)
		for i in Bstar.hists_EST_SUB:
			N.Add(i,-1.)
		


	# OLD CODE WE DON'T WANT TO RUN RIGHT NOW - CONTINUOUS 2D
	if options.run2d == 'on':
		# var we want to look at:
		mtw_bins = (int(options.mtwcuts.split(',')[1])-int(options.mtwcuts.split(',')[0]))/100
		var_array2 = ['mass_tw',35,500,4000]

		Bstar.fitFunc = fitfunction

		Bstar.MakeEstFlexFit(var_array2,'mass_top',antitag, tag, center,TwoDFitFile)

		hbins = var_array2[1:]

		# the real value is the sum of the histograms in self.hists_MSR
		V = TH1F("V2d", "", hbins[0],hbins[1], hbins[2])
		for i in Bstar.hists_MSR:
			V.Add(i,1.)

		# the estimate is the sum of the histograms in self.hists_EST and self.hist_MSR_SUB
		N = TH1F("QCD2d", "", hbins[0], hbins[1], hbins[2])
		for i in Bstar.hists_EST:
			N.Add(i,1.)
		for i in Bstar.hists_MSR_SUB:
			N.Add(i,1.)
		for i in Bstar.hists_EST_SUB:
			N.Add(i,-1.)


# ---- Lots of plot formatting --------------
	vartitle = "M_{tW} (GeV)"

	N.SetLineColor(kBlack)
	N.SetFillColor(kPink+3)

	V.SetStats(0)
	V.SetLineColor(1)
	V.SetFillColor(0)
	V.SetMarkerColor(1)
	V.SetMarkerStyle(20)
	N.GetYaxis().SetTitle("events / "+str((hbins[2]-hbins[1])/hbins[0])+" GeV")
	N.GetXaxis().SetTitle(vartitle)

	leg2 = TLegend(0.75,0.75,0.95,0.95)
	leg2.SetLineColor(0)
	leg2.SetFillColor(0)
	leg2.AddEntry(V, "Data in tag region", "PL")
	leg2.AddEntry(N, "Data prediction", "F")

	FindAndSetMax([V,N])
	C3 = TCanvas("C3", "", 800, 600)
	C3.cd()
	N.Draw("Hist")
	V.Draw("same E0")

	leg2.Draw()
	
# --- Write out the canvas ---------------------
	C3.Print(printDir+"bkg_"+options.set+"_Mtw"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".pdf")
	C3.Print(printDir+"bkg_"+options.set+"_Mtw"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".png")

# --- Save the histograms ----------------------
	myFile.cd()
	N.Write()
	V.Write()


myFile.Write()
myFile.Close()

