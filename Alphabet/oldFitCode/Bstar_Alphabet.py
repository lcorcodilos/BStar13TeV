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
parser.add_option('-q', '--qcdsample', metavar='F', type='string', action='store',
				default       =       'all',
				dest          =       'qcdsample',
				help          =       'all or any comma separated combo of HT500, HT700, etc')
parser.add_option('-S', '--selection', metavar='F', type='string', action='store',
				default       =       'full',
				dest          =       'selection',
				help          =       'full, sjbtag_off, tau32_off')

(options, args) = parser.parse_args()


print "Options summary"
print "=================="
for  opt,value in options.__dict__.items():
		#print str(option)+ ": " + str(options[option]) 
		print str(opt) +': '+ str(value)
print "=================="
print ""

### DEFINE THE DISTRIBUTIONS YOU WANT TO USE:

# DISTRIBUTIONS YOU WANT TO ESTIMATE:

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

if options.cuts.find('default') != -1:
	wmass_cut = '(mass_w>65)&&(mass_w<105)'
elif options.cuts.find('sideband') != -1:
	wmass_cut = '(mass_w>30)&&(mass_w<65)'


# Before proceeding, need to reweight our dists to cross section, lumi, and number of events
# The weighting for this is stored in the TWminitree file, just need to grab and apply using the below
# function from Distribution_Header.py -LC 10/14/17

# Only want to do this with MC since data doesn't get this weight
if options.set == 'QCD':
	for distE in DistsWeWantToEstimate:
		distE.bstarReweight()
for distI in DistsWeWantToIgnore:
	distI.bstarReweight()

Bstar = Alphabetizer("Bstar", DistsWeWantToEstimate, DistsWeWantToIgnore)

# apply a preselection to the trees:
# Don't have any for W side because the minitrees already do this
print '(mass_tw>'+options.mtwcuts.split(',')[0]+')&&(mass_tw<'+options.mtwcuts.split(',')[1]+')'
presel = '('+wmass_cut+')&&(mass_tw>'+options.mtwcuts.split(',')[0]+')&&(mass_tw<'+options.mtwcuts.split(',')[1]+')'

# Do some binning
bins = array('d',[50,60,70,90,105,210,230,260,300])
truthbins = []
if options.set == "QCD":
	#Assuming here that the truth bins need to be around the region where we are looking for the tagrate -LC
	truthbins = array('d',[105,110,120,130,140,150,160,170,180,190,200,210])
	# truthbins = array('d',[165,170,175,180])
elif options.set == "data":
	truthbins = []

c2D = TCanvas('c2D','c2D',800,700)
c2D.SetRightMargin(0.15)
# Setup selection, tag, and antitag and do the 2D plot
if options.selection == 'full':
	selection 	= '(sjbtag>0.5426)&&(tau32<0.65)'
	tag 		= "(sjbtag>0.5426)&&(tau32<0.65)&&"+presel#+'&&(mass_top>105)&&(mass_top<210)'
	antitag 	= "!((sjbtag>0.5426)&&(tau32<0.65))&&"+presel#+'&&(mass_top>105)&&(mass_top<210)'

	Bstar.SetRegions(['mass_top','tau32',25,50,300,20,0,1],'('+presel+')')
	Bstar.TwoDPlot.GetYaxis().SetTitle('#tau_{32}')
	Bstar.TwoDPlot.GetXaxis().SetTitle('M_{Top}')
	Bstar.TwoDPlot.SetTitle(options.qcdsample+' - Mtw ['+options.mtwcuts+']')
	Bstar.TwoDPlot.Draw('COLZ')
	if options.qcdsample == 'all':
		printDir = 'results/'+options.cuts+'/'
	else:
		printDir = 'results/'+options.cuts+'/QCDbreakdown/'+QCDdir
	c2D.Print(printDir +'MtvsTau32_Mtw'+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+'.png','png')

elif options.selection == 'tau32_off':
	selection 	= '(sjbtag>0.5426)'
	tag 		= "(sjbtag>0.5426)&&"+presel+'&&(mass_top>105)&&(mass_top<210)'
	antitag 	= "!((sjbtag>0.5426))&&"+presel+'&&(mass_top>105)&&(mass_top<210)'
	
	Bstar.SetRegions(['mass_top','sjbtag',21,165,180,20,0,1],'('+presel+')')
	Bstar.TwoDPlot.GetYaxis().SetTitle('Sub jet b-tag')
	Bstar.TwoDPlot.GetXaxis().SetTitle('M_{Top}')
	Bstar.TwoDPlot.SetTitle(options.qcdsample+' - Mtw ['+options.mtwcuts+']')
	Bstar.TwoDPlot.Draw('COLZ')
	printDir = 'results/'+options.cuts+'/MtvsSJbtag/'+QCDdir
	c2D.Print(printDir +'MtvsSJbtag_Mtw'+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+'.png','png')

elif options.selection == 'sjbtag_off':
	selection 	= '(tau32<0.5)'
	tag 		= "(tau32<0.5)&&"+presel+'&&(mass_top>105)&&(mass_top<210)'
	antitag 	= "!((tau32<0.5))&&"+presel+'&&(mass_top>105)&&(mass_top<210)'

	Bstar.SetRegions(['mass_top','tau32',21,165,180,20,0,1],'('+presel+')')
	Bstar.TwoDPlot.GetYaxis().SetTitle('#tau_{32}')
	Bstar.TwoDPlot.GetXaxis().SetTitle('M_{Top}')
	Bstar.TwoDPlot.SetTitle(options.qcdsample+' - Mtw ['+options.mtwcuts+']')
	Bstar.TwoDPlot.Draw('COLZ')
	printDir = 'results/'+options.cuts+'/MtvsTau32_noSJbtag/'+QCDdir
	c2D.Print(printDir +'MtvsTau32_noSJbtag_Mtw'+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+'.png','png')


center = 0
F = QuadraticFit([0.0], 50-center, 310-center, "quadfit", "EMRFNEX0")


Bstar.doRates('mass_top','(mass_top<105)||(mass_top>210)',selection,presel,bins,truthbins,F)

###### TESTING CODE FOR THE FIT ###########################
# onesT = TTree('onesT','onesT')
# myArray = array('d',[0])
# onesT.Branch('ones',myArray,'ones/D')

# onesH = TH1F('onesH','onesH',250,50,300)
# onesHup = TH1F('onesHup','onesHup',250,50,300)
# onesHdown = TH1F('onesHdown','onesHdown',250,50,300)

# Bstar.Fit.MakeConvFactor('ones', 0)

# for ibin in range(50,300):
# 	myArray[0] = ibin
# 	onesT.Fill()

# onesT.Draw('ones>>onesH',Bstar.Fit.ConvFact,'goff')
# onesT.Draw('ones>>onesHup',Bstar.Fit.ConvFactUp,'goff')
# onesT.Draw('ones>>onesHdown',Bstar.Fit.ConvFactDn,'goff')

# testC = TCanvas('testC','testC',800,700)
# onesH.Draw('hist')
# onesHup.Draw('same hist')
# onesHdown.Draw('same hist')

# parListUp = []
# err = F.ErrUp
# for par in range(9):
# 	# parListUp.append(str(round(err.GetParameter(par),10)))
# 	parListUp.append(str(err.GetParameter(par)))

# print '(0.008598535 + (x*-0.000400739) + (x*x*0.000005700) + sqrt((0.009759305*0.009759305) + (x*x*0.000249488*0.000249488) + (x*x*x*x*0.000001569*0.000001569) + (2*x*-0.000002385) + (2*x*x*0.000000014) + (2*x*x*x*-0.000000000)))'
# print '('+parListUp[0]+' + '+parListUp[1]+'*x + '+parListUp[2]+'*x*x'+' + sqrt(('+parListUp[3]+'*'+parListUp[3]+') + (x*x*'+parListUp[4]+'*'+parListUp[4]+') + (x*x*x*x*'+parListUp[5]+'*'+parListUp[5]+') + (2*x*'+parListUp[6]+') + (2*x*x*'+parListUp[7]+') + (2*x*x*x*'+parListUp[8]+'))'


# thisConvFitUp = TF1('thisConvFitUp','(0.008598535 + (x*-0.000400739) + (x*x*0.000005700) + sqrt((0.009759305*0.009759305) + (x*x*0.000249488*0.000249488) + (x*x*x*x*0.000001569*0.000001569) + (2*x*-0.000002385) + (2*x*x*0.000000014) + (2*x*x*x*-0.000000000)))',50,300)
# thisConvFitUp.Draw('same')

# thisParFitUp = TF1('thisParFitUp','('+parListUp[0]+' + '+parListUp[1]+'*x + '+parListUp[2]+'*x*x'+' + sqrt(('+parListUp[3]+'*'+parListUp[3]+') + (x*x*'+parListUp[4]+'*'+parListUp[4]+') + (x*x*x*x*'+parListUp[5]+'*'+parListUp[5]+') + (2*x*'+parListUp[6]+') + (2*x*x*'+parListUp[7]+')))',50,300) # + (2*x*x*x*'+parListUp[8]+')
# thisParFitUp.SetLineColor(kPink)
# thisParFitUp.Draw('same')


# raw_input('waiting')

########## END TESTING CODE ###############################


C1 = TCanvas("C1", "", 800, 600)
C1.cd()

Bstar.G.SetMaximum(0.5)
Bstar.G.Draw("AP")

Bstar.G.SetTitle('Alphabet R_{P/F} - '+options.set+options.qcdsample+' - M_{tW} '+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1])
Bstar.G.GetXaxis().SetTitle("M_{top} (GeV)")
Bstar.G.GetYaxis().SetTitle("N_{passed}/N_{failed}")
Bstar.Fit.fit.Draw("same")
Bstar.Fit.ErrUp.SetLineStyle(2)
Bstar.Fit.ErrUp.Draw("same")
Bstar.Fit.ErrDn.SetLineStyle(2)
Bstar.Fit.ErrDn.Draw("same")
if Bstar.truthG != None:
	Bstar.truthG.Draw("same")
leg = TLegend(0.15,0.7,0.35,0.9)
leg.SetTextSize(.025)
leg.SetLineColor(0)
leg.SetFillColor(0)
#leg.SetHeader("cut @ #tau_{2}/#tau_{1} < 0.5")
leg.AddEntry(Bstar.G, "events used in fit", "PL")
leg.AddEntry(Bstar.Fit.fit, "fit", "L")
leg.AddEntry(Bstar.Fit.ErrUp, "fit errors", "L")
leg.Draw()

# raw_input('waiting')

C1.Print(printDir+"fit_"+options.set+"_Mtw"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".pdf")
C1.Print(printDir+"fit_"+options.set+"_Mtw"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".png")



#####################################
# Now we actually run the Estimate! #
#####################################

# antitag is the cuts needed to create the fail distribution from the original ttree
# tag is the same but to make the pass distribution



# var we want to look at:
mtw_bins = (int(options.mtwcuts.split(',')[1])-int(options.mtwcuts.split(',')[0]))/100
# var_array2 = ["mass_tw", mtw_bins,float(options.mtwcuts.split(',')[0]),float(options.mtwcuts.split(',')[1])]
# var_array2 = ['mass_tw',40,500,4000]
var_array2 = ['mass_top',25,50,300]

myFile = TFile(printDir+"Alphabet"+options.set+'_'+options.cuts+"_Mtw_"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".root", "recreate")
myFile.cd()

# Make the estimated distributions
Bstar.MakeEst(var_array2, 'mass_top',antitag, tag, center)

# now we can plot (maybe I should add some auto-plotting Bstar.Fit.fittions?)
hbins = var_array2[1:]

# Going to quickly save everything out for later debugging
MtwDistributions = TFile(printDir+"Mtw_Distributions_"+options.set+'_'+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".root","RECREATE")
MtwDistributions.cd()
for i in Bstar.hists_MSR+Bstar.hists_MSR_SUB+Bstar.hists_EST+Bstar.hists_EST_SUB+Bstar.hists_ATAG:
	i.Write()
for i in Bstar.hists_EST_UP + Bstar.hists_EST_DN:
	i.Write()

AT = TH1F('AT','',hbins[0],hbins[1], hbins[2])
for i in Bstar.hists_ATAG:
	AT.Add(i,1.)
AT.Write()
Vtemp = TH1F('Vtemp','',hbins[0],hbins[1], hbins[2])
for i in Bstar.hists_MSR:
	Vtemp.Add(i,1.)
Vtemp.Write()
MtwDistributions.Close()



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
# We can do the same thing for the Up and Down shapes:
NU = TH1F("QCD_Up", "", hbins[0],hbins[1], hbins[2])
for i in Bstar.hists_EST_UP:
	NU.Add(i,1.)
for i in Bstar.hists_MSR_SUB:
	NU.Add(i,1.)
for i in Bstar.hists_EST_SUB_UP:
	NU.Add(i,-1.)
ND = TH1F("QCD_Down", "", hbins[0],hbins[1], hbins[2])
for i in Bstar.hists_EST_DN:
	ND.Add(i,1.)
for i in Bstar.hists_MSR_SUB:
	ND.Add(i,1.)
for i in Bstar.hists_EST_SUB_DN:
	ND.Add(i,-1.)

vartitle = "M_{tW} (GeV)"

NU.SetLineColor(kBlack)
ND.SetLineColor(kBlack)
NU.SetLineStyle(2)
ND.SetLineStyle(2)
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
leg2.AddEntry(NU, "uncertainty", "F")


FindAndSetMax([V,N, NU, ND])
C3 = TCanvas("C3", "", 800, 600)
C3.cd()
N.Draw("Hist")
V.Draw("same E0")
NU.Draw("same")
ND.Draw("same")
leg2.Draw()
C3.Print(printDir+"bkg_"+options.set+"_Mtw"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".pdf")
C3.Print(printDir+"bkg_"+options.set+"_Mtw"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".png")

myFile.cd()
N.Write()
V.Write()
NU.Write()
ND.Write()
myFile.Write()
myFile.Close()


f = open("transfer_fn.txt",'a')
f.write("{\n")
f.write("\n\tfirst = "+str(Bstar.Fit.fit.GetParameter(0))+";")
f.write("\n\tfirstErr = "+str(Bstar.Fit.fit.GetParErrors()[0])+";")
f.write("\n\tsecond = "+str(Bstar.Fit.fit.GetParameter(1))+";")
f.write("\n\tsecondErr = "+str(Bstar.Fit.fit.GetParErrors()[1])+";")
f.write("\n\tthird = "+str(Bstar.Fit.fit.GetParameter(2))+";")
f.write("\n\tthirdErr = "+str(Bstar.Fit.fit.GetParErrors()[2])+";")
f.write("\n}\n")

g = open(printDir+"fn_bstar_QUAD_"+options.set+"_Mtw"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".txt",'w')
for i in range(9):
	# Tecnically grabs parameters from errUp but the first three are the same as in the nominal fit
	# and the next 6 are identital to ErrDown (it's the equation they are put in that's different)
	g.write(str(Bstar.Fit.ErrUp.GetParameter(i))+"\n")


# MtwDistributions = TFile.Open("Mtw_Distributions_"+options.set+"_"+options.mtwcuts.split(',')[0]+'-'+options.mtwcuts.split(',')[1]+".root")


