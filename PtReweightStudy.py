import ROOT
from ROOT import *

fdata = TFile('rootfiles/35851pb/TWanalyzerdata_Trigger_nominal_none_PSET_sideband1.root','open')
fttbar = TFile('rootfiles/35851pb/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_sideband1.root','open')
fsingletop = TFile('rootfiles/35851pb/TWanalyzerweightedsingletop_Trigger_nominal_none_PSET_sideband1.root','open')

out = TFile('TWTopPtSF.root','recreate')
out.cd()
outhist = TH1F('TopPtSF','Scale factor for top pt reweight',1,0,1)

data = fdata.Get('PtTop')
qcdbkg = fdata.Get('QCDbkgPT')

ttbar = fttbar.Get('PtTop')
ttbarbkg = fttbar.Get('QCDbkgPT')

singletop = fsingletop.Get('PtTop')
stbkg = fsingletop.Get('QCDbkgPT')


totalbkg = qcdbkg.Clone('totalbkg')
# Subtract away the double counting
totalbkg.Add(ttbarbkg,-1)
totalbkg.Add(stbkg,-1)
# Add the stack together
totalbkg.Add(ttbar)
totalbkg.Add(singletop)

print "total bkg estimate integral: " + str(totalbkg.Integral())
print "data integral: " + str(data.Integral())

# First find the difference between the two distributions
diff = data.Integral() - totalbkg.Integral()

# Then figure out how much the ttbar mc needs to be scaled by to correct that difference
# If data > totalbkg, diff > 0 and scale factor brings bkg up
SF = diff/ttbar.Integral()

print "SF: " + str(SF)

outhist.SetBinContent(1,SF)

out.Write()
out.Close()

