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
				default       =       'data',
				dest          =       'set',
				help          =       'data or QCD')

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
lumi = 36420.0

### DEFINE THE DISTRIBUTIONS YOU WANT TO USE:

# DISTRIBUTIONS YOU WANT TO ESTIMATE:

# FORMAT IS:
# dist = ("name", "location of file", "name of tree", "weight (can be more complicated than just a number, see MC example below)")
if options.set == "data":
	Data = DIST("Data", "TWtreefile_data_t.root", "Tree", "weight")
	DistsWeWantToEstiamte = [Data]

elif options.set == "QCD":
	QCDHT500 = DIST("QCDHT500", "TWtreefile_QCDHT500_weighted_t.root", "Tree", "weight")
	QCDHT700 = DIST("QCDHT700", "TWtreefile_QCDHT700_weighted_t.root", "Tree", "weight")
	QCDHT1000 = DIST("QCDHT1000", "TWtreefile_QCDHT1000_weighted_t.root", "Tree", "weight")
	QCDHT1500 = DIST("QCDHT1500", "TWtreefile_QCDHT1500_weighted_t.root", "Tree", "weight")
	QCDHT2000 = DIST("QCDHT2000", "TWtreefile_QCDHT2000_weighted_t.root", "Tree", "weight")
	DistsWeWantToEstiamte = [QCDHT500, QCDHT700, QCDHT1000, QCDHT1500, QCDHT2000]

# DISTRIBUTIONS YOU NEED TO SUBTRACT (KNOWN MC CONTRIBUTIONS):
ttbar = DIST("ttbar", "TWtreefile_ttbar_weighted_t.root", "Tree", "weight")
st_s = DIST("st_s", "TWtreefile_singletop_s_weighted_t.root", "Tree", "weight")
st_t = DIST("st_t", "TWtreefile_singletop_t_weighted_t.root", "Tree", "weight")
st_tB = DIST("st_tB", "TWtreefile_singletop_tB_weighted_t.root", "Tree", "weight")


# Now we arrange them correctly:

DistsWeWantToIgnore = [ttbar, st_s, st_t, st_tB]

# Before proceeding, need to reweight our dists to cross section, lumi, and number of events
# The weighting for this is stored in the TWtreefile, just need to grab and apply using the below
# function from Bstar_Weights.py -LC 3/20/17

# Only want to do this with MC since data doesn't get this weight
if options.set == "QCD":
	for distE in DistsWeWantToEstiamte:
		distE.bstarReweight()
for distI in DistsWeWantToIgnore:
	distI.bstarReweight()

Bstar = Alphabetizer("Bstar", DistsWeWantToEstiamte, DistsWeWantToIgnore)

# apply a preselection to the trees:
# Marc had this as a set of cuts "(wpt>400...etc)" but since I've applied all of these in the TTree maker, we only want to pass a weight
presel = "(1.)"


# pick the two variables to do the estiamte it (in this case, Soft Drop Mass (from 70 to 350 in 48 bins) and tau32 (from 0 to 1))
var_array = ["tmass", "tau32", 48,70,350, 50, 0, 1] #Assuming that wmass will stop below 330 -LC
Bstar.SetRegions(var_array, presel) # make the 2D plot
C1 = TCanvas("C1", "", 800, 600)
C1.cd()
Bstar.TwoDPlot.Draw("box") # Show that plot:

################Temp code###################################
# C12 = TCanvas("C12", "", 800, 600)
# C12.cd()
# Bstar.Pplots.Draw("box")

# C13 = TCanvas("C13", "", 800, 600)
# C13.cd()
# Bstar.Mplots.Draw("box")


# raw_input("Press enter to continue...")
############################################################

# NOW DO THE ACTUAL ALPHABETIZATION: (Creating the regions)
# The command is: .GetRates(cut, bins, truthbins, center, fit)
cut = [0.54, "<"]
# so we need to give it bins:
bins = [[30,50],[50,70],[70,90],[90,105],[220,240],[240,260],[260,280],[280,300]]
# truth bins (we don't want any because we are looking at real data::)
if options.set == "QCD":
	#Assuming here that the truth bins need to be around the region where we are looking for the tagrate -LC
	truthbins = [[105,145],[140,180],[180,220]]
elif options.set == "data":
	truthbins = []

# a central value for the fit (could be 0 if you wanted to stay in the mass variable, we are looking at tops, so we'll give it 170 GeV)
center = 0.
# and finally, a fit, taken from the file "Converters.py". We are using the linear fit, so:

#Assuming the first array is okay, the second value should be min of wmass range, and third should be max -LC
#Last two strings are just name and opt
F = QuadraticFit([0.0], 30, 300, "quadfit", "EMRFNEX0")
#F = LinearFit([0.2,-0.2], -75, 75, "linFit1", "EMRNS")

# All the error stuff is handled by the LinearFit class. We shouldn't have to do anything else!

# So we just run:
Bstar.GetRates(cut, bins, truthbins, center, F)

## Let's plot the results:
C2 = TCanvas("C2", "", 800, 600)
C2.cd()
Bstar.G.Draw("AP")

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
C2.Print("fit_data_tau32%s_"%cut[0]+options.set+".pdf")
# Now we actually run the estiamte!

# cuts:

#Will have to change once I start doing rates for different bands  -LC
#Assumed that anittag is our tagrate sideband and tag is our selection -LC
'''Testing confirms that the tag cuts work but the antitag do not (leading to empty histos)
Even tried ((30<wmass)&(65>wmass)&(95<wmass)&(tau21<0.4)) but don't know what the issue is
Got singletop to work in the tester script with tag cuts (though it didn't work regularly).
Not sure about ttbar.
-LC (3/9/17)

'''
antitag = "(((tmass>30&tmass<105)||(tmass>220))&tau32<0.54)"
tag 	= "((tmass>105&tmass<220)&tau32<0.54)"


# var we want to look at:
var_array2 = ["tpt", 20,400,1200]

FILE = TFile("Tagrate_"+options.set+"_t.root", "RECREATE")
FILE.cd()


Bstar.MakeEst(var_array2, antitag, tag)

ptDistributions = TFile("ptDistributions.root","RECREATE")
ptDistributions.cd()

for i in Bstar.hists_MSR+Bstar.hists_EST+Bstar.hists_EST+Bstar.hists_MSR_SUB+Bstar.hists_EST_SUB+Bstar.hists_ATAG:
	i.Write()


ptDistributions.Close()

# now we can plot (maybe I should add some auto-plotting Bstar.Fit.fittions?)
hbins = [20,400,1200]
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

vartitle = "p_{T}_{top} (GeV)"

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
FILE.Write()
FILE.Save()
C3.Print("bkg_data_tau32%s"%cut[0]+options.set+".pdf")



f = open("transfer_fn.txt",'a')
f.write("{\n")
f.write("\n\tfirst = "+str(Bstar.Fit.fit.GetParameter(0))+";")
f.write("\n\tfirstErr = "+str(Bstar.Fit.fit.GetParErrors()[0])+";")
f.write("\n\tsecond = "+str(Bstar.Fit.fit.GetParameter(1))+";")
f.write("\n\tsecondErr = "+str(Bstar.Fit.fit.GetParErrors()[1])+";")
f.write("\n\tthird = "+str(Bstar.Fit.fit.GetParameter(2))+";")
f.write("\n\tthirdErr = "+str(Bstar.Fit.fit.GetParErrors()[2])+";")
f.write("\n}\n")

g = open("fn_bstar_QUAD_"+options.set+".txt",'w')
g.write(str(Bstar.Fit.fit.GetParameter(0)))
g.write("\n"+str(Bstar.Fit.fit.GetParameter(1)))
g.write("\n"+str(Bstar.Fit.fit.GetParameter(2)))

g_errUp = open("fn_bstar_QUAD_errUp_"+options.set+".txt",'w')
g_errUp.write(str(Bstar.Fit.fit.GetParameter(0)+Bstar.Fit.fit.GetParErrors()[0]))
g_errUp.write("\n"+str(Bstar.Fit.fit.GetParameter(1)+Bstar.Fit.fit.GetParErrors()[1]))
g_errUp.write("\n"+str(Bstar.Fit.fit.GetParameter(2)+Bstar.Fit.fit.GetParErrors()[2]))

g_errDown = open("fn_bstar_QUAD_errDown_"+options.set+".txt",'w')
g_errDown.write(str(Bstar.Fit.fit.GetParameter(0)-Bstar.Fit.fit.GetParErrors()[0]))
g_errDown.write("\n"+str(Bstar.Fit.fit.GetParameter(1)-Bstar.Fit.fit.GetParErrors()[1]))
g_errDown.write("\n"+str(Bstar.Fit.fit.GetParameter(2)-Bstar.Fit.fit.GetParErrors()[2]))


raw_input("Press enter to continue...")
