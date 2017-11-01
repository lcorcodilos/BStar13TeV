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


parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
				default       =       'QCD',
				dest          =       'set',
				help          =       'data or QCD')
parser.add_option('-p', '--ptcuts', metavar='F', type='string', action='store',
                  default	=	'400,600',
                  dest		=	'ptcuts',
                  help		=	'Pt cuts, low to high, separated by a comma')


(options, args) = parser.parse_args()


print "Options summary"
print "=================="
for  opt,value in options.__dict__.items():
		#print str(option)+ ": " + str(options[option]) 
		print str(opt) +': '+ str(value)
print "=================="
print ""

# Cons = LoadConstants()
# lumi = Cons['lumi']
lumi = 35851.0

### DEFINE THE DISTRIBUTIONS YOU WANT TO USE:

# DISTRIBUTIONS YOU WANT TO ESTIMATE:

# FORMAT IS:
# dist = ("name", "location of file", "name of tree", "weight (can be more complicated than just a number, see MC example below)")
if options.set == "data":
	Data = DIST("Data", "../rootfiles/35851pb/TWminitree_data_PSET_default.root", "miniTree", "weight")
	DistsWeWantToEstimate = [Data]

	# DISTRIBUTIONS YOU NEED TO SUBTRACT (KNOWN MC CONTRIBUTIONS):
	ttbar = DIST("ttbar", "../rootfiles/35851pb/TWminitree_weightedttbar_PSET_default.root", "miniTree", "weight")
	st_tW = DIST("st_tW", "../rootfiles/35851pb/TWminitree_weightedsingletop_tW_PSET_default.root", "miniTree", "weight")
	st_tWB = DIST("st_tWB", "../rootfiles/35851pb/TWminitree_weightedsingletop_tWB_PSET_default.root", "miniTree", "weight")
	st_t = DIST("st_t", "../rootfiles/35851pb/TWminitree_weightedsingletop_t_PSET_default.root", "miniTree", "weight")
	st_tB = DIST("st_tB", "../rootfiles/35851pb/TWminitree_weightedsingletop_tB_PSET_default.root", "miniTree", "weight")

	# Now we arrange them correctly:
	DistsWeWantToIgnore = [ttbar, st_tW, st_tWB, st_t, st_tB]

elif options.set == "QCD":
	QCDHT500 = DIST("QCDHT500", "../rootfiles/35851pb/TWminitree_weightedQCDHT500_PSET_default.root", "miniTree", "weight")
	QCDHT700 = DIST("QCDHT700", "../rootfiles/35851pb/TWminitree_weightedQCDHT700_PSET_default.root", "miniTree", "weight")
	QCDHT1000 = DIST("QCDHT1000", "../rootfiles/35851pb/TWminitree_weightedQCDHT1000_PSET_default.root", "miniTree", "weight")
	QCDHT1500 = DIST("QCDHT1500", "../rootfiles/35851pb/TWminitree_weightedQCDHT1500_PSET_default.root", "miniTree", "weight")
	QCDHT2000 = DIST("QCDHT2000", "../rootfiles/35851pb/TWminitree_weightedQCDHT2000_PSET_default.root", "miniTree", "weight")
	DistsWeWantToEstimate = [QCDHT500, QCDHT700, QCDHT1000, QCDHT1500, QCDHT2000]

	# Don't have any dists to ignore with QCD MC
	DistsWeWantToIgnore = []

	

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
print '(pt_top>'+options.ptcuts.split(',')[0]+')&&(pt_top<'+options.ptcuts.split(',')[1]+')'
presel = '(pt_top>'+options.ptcuts.split(',')[0]+')&&(pt_top<'+options.ptcuts.split(',')[1]+')'


# pick the two variables to do the Estimate it 
var_array = ['mass_top','tau32', 'sjbtag', 28, 30, 310,20,0,1,25,0,1] 
Bstar.SetRegions(var_array, presel) # make the 2D plot
C1 = TCanvas("C1", "", 800, 600)
C1.cd()
Bstar.ThreeDPlot.Draw() # Show that plot:

# NOW DO THE ACTUAL ALPHABETIZATION: (Creating the regions)
# The command is: .GetRates(cut, bins, truthbins, center, fit)
cut1 = [0.65, "<"] # On Tau32
cut2 = [0.5426, ">"] # On Sjbtag
# so we need to give it bins:
bins = [[50,60],[60,70],[70,90],[90,105],[210,230],[230,310]]
# truth bins (we don't want any because we are looking at real data::)
if options.set == "QCD":
	#Assuming here that the truth bins need to be around the region where we are looking for the tagrate -LC
	truthbins = [[105,140],[140,180],[180,210]]
elif options.set == "data":
	truthbins = []

# a central value for the fit (could be 0 if you wanted to stay in the mass variable, we are looking at tops, so we'll give it 170 GeV)
center = 0
# and finally, a fit, taken from the file "Converters.py". We are using the linear fit, so:

#Assuming the first array is okay, the second value should be min of wmass range, and third should be max -LC
#Last two strings are just name and opt
F = QuadraticFit([0.0], 50-center, 310-center, "quadfit", "EMRFNEX0")
#F = LinearFit([0.2,-0.2], -75, 75, "linFit1", "EMRNS")

# All the error stuff is handled by the LinearFit class. We shouldn't have to do anything else!

# So we just run:
Bstar.Get3DRates(cut1, cut2, bins, truthbins, center, F)

## Let's plot the results:
C2 = TCanvas("C2", "", 800, 600)
C2.cd()
Bstar.G.Draw("AP")

Bstar.G.SetTitle('Alphabet R_{P/F} - '+options.set+' - Top Pt '+options.ptcuts.split(',')[0]+'-'+options.ptcuts.split(',')[1])
Bstar.G.GetXaxis().SetTitle("M_{top} (GeV)")
Bstar.G.GetYaxis().SetTitle("N_{passed}/N_{failed}")
Bstar.Fit.fit.Draw("same")
Bstar.Fit.ErrUp.SetLineStyle(2)
Bstar.Fit.ErrUp.Draw("same")
Bstar.Fit.ErrDn.SetLineStyle(2)
Bstar.Fit.ErrDn.Draw("same")
if Bstar.truthG != None:
	Bstar.truthG.Draw("same")
leg = TLegend(0.2,0.6,0.5,0.89)
leg.SetLineColor(0)
leg.SetFillColor(0)
#leg.SetHeader("cut @ #tau_{2}/#tau_{1} < 0.5")
leg.AddEntry(Bstar.G, "events used in fit", "PL")
leg.AddEntry(Bstar.Fit.fit, "fit", "L")
leg.AddEntry(Bstar.Fit.ErrUp, "fit errors", "L")
leg.Draw()

# raw_input('waiting')

C2.Print("fit_tau32_%s_"%cut1[0]+'sjbtag_%s'%cut2[0]+'_'+options.set+"_pt"+options.ptcuts.split(',')[0]+'-'+options.ptcuts.split(',')[1]+".pdf")
# Now we actually run the Estimate!

# antitag is the cuts needed to create the fail distribution from the original ttree
# tag is the same but to make the pass distribution

tag 	= "(tau32<0.65)&&(sjbtag>0.5426)&&"+presel
antitag = "!((tau32<0.65)&&(sjbtag>0.5426))&&"+presel

# var we want to look at:
var_array2 = ["mass_top", 10,105,210]

myFile = TFile("Alphabet"+options.set+"_Mt_for_pt"+options.ptcuts.split(',')[0]+'-'+options.ptcuts.split(',')[1]+".root", "recreate")
myFile.cd()

# Make the estimated distributions
Bstar.MakeEst(var_array2, antitag, tag)

# now we can plot (maybe I should add some auto-plotting Bstar.Fit.fittions?)
hbins = [10,105,210]

# Going to quickly save everything out for later debugging
MtDistributions = TFile("Mt_Distributions.root","RECREATE")
MtDistributions.cd()
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
MtDistributions.Close()



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
NU = TH1F("QCD_CMS_scale_13TeVUp", "", hbins[0],hbins[1], hbins[2])
for i in Bstar.hists_EST_UP:
	NU.Add(i,1.)
for i in Bstar.hists_MSR_SUB:
	NU.Add(i,1.)
for i in Bstar.hists_EST_SUB_UP:
	NU.Add(i,-1.)
ND = TH1F("QCD_CMS_scale_13TeVDown", "", hbins[0],hbins[1], hbins[2])
for i in Bstar.hists_EST_DN:
	ND.Add(i,1.)
for i in Bstar.hists_MSR_SUB:
	ND.Add(i,1.)
for i in Bstar.hists_EST_SUB_DN:
	ND.Add(i,-1.)

vartitle = "M_{top} (GeV)"

NU.SetLineColor(kBlack)
ND.SetLineColor(kBlack)
NU.SetLineStyle(2)
ND.SetLineStyle(2)
N.SetLineColor(kBlack)
N.SetFillColor(kPink+3)



V.SetStats(0)
V.Sumw2()
V.SetLineColor(1)
V.SetFillColor(0)
V.SetMarkerColor(1)
V.SetMarkerStyle(20)
N.GetYaxis().SetTitle("events / "+str((hbins[2]-hbins[1])/hbins[0])+" GeV")
N.GetXaxis().SetTitle(vartitle)

leg2 = TLegend(0.6,0.6,0.89,0.89)
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
myFile.Write()
myFile.Save()
C3.Print("bkg_data_tau32%s"%cut1[0]+options.set+"_pt"+options.ptcuts.split(',')[0]+'-'+options.ptcuts.split(',')[1]+".pdf")



f = open("transfer_fn.txt",'a')
f.write("{\n")
f.write("\n\tfirst = "+str(Bstar.Fit.fit.GetParameter(0))+";")
f.write("\n\tfirstErr = "+str(Bstar.Fit.fit.GetParErrors()[0])+";")
f.write("\n\tsecond = "+str(Bstar.Fit.fit.GetParameter(1))+";")
f.write("\n\tsecondErr = "+str(Bstar.Fit.fit.GetParErrors()[1])+";")
f.write("\n\tthird = "+str(Bstar.Fit.fit.GetParameter(2))+";")
f.write("\n\tthirdErr = "+str(Bstar.Fit.fit.GetParErrors()[2])+";")
f.write("\n}\n")

g = open("fn_bstar_QUAD_"+options.set+"_pt"+options.ptcuts.split(',')[0]+'-'+options.ptcuts.split(',')[1]+".txt",'w')
for i in range(9):
	# Tecnically grabs parameters from errUp but the first three are the same as in the nominal fit
	# and the next 6 are identital to ErrDown (it's the equation they are put in that's different)
	g.write(str(Bstar.Fit.ErrUp.GetParameter(i))+"\n")




