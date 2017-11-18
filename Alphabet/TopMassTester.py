import ROOT
from ROOT import *

# fQCDs = []

# for ht in ['700','1000','1500','2000']:
# 	TFile.Open('../rootfiles/35851pb/TWtreefile_QCDHT'+ht+'_Trigger_nominal_none.root') 

# 	weightTree = htFile.Get('miniTree')


fHT1000 = TFile.Open('../rootfiles/35851pb/TWminitree_weightedQCDHT1000_PSET_default.root')

tHT1000 = fHT1000.Get('miniTree')

hNoWmassCut = TH1F('hNoWmassCut','hNoWmassCut',25,50,300)
hLowWmassCut = TH1F('hLowWmassCut','hLowWmassCut',25,50,300)
hSigWmassCut = TH1F('hSigWmassCut','hSigWmassCut',25,50,300)

tWeight = fHT1000.Get('Weight')
tWeight.GetEntry(0)
normWeight = tWeight.weightv

cHT1000 = TCanvas('cHT1000','cHT1000',1500,400)
cHT1000.Divide(3,1)

cHT1000.cd(1)
tHT1000.Draw('mass_top>>hNoWmassCut','(weight*'+str(normWeight)+')*((tau32<0.65)&&(sjbtag>0.5426))','histE')
cHT1000.cd(2)
tHT1000.Draw('mass_top>>hLowWmassCut','(weight*'+str(normWeight)+')*((mass_w<65)&&(mass_w>30)&&(tau32<0.65)&&(sjbtag>0.5426))','histE')
cHT1000.cd(3)
tHT1000.Draw('mass_top>>hSigWmassCut','(weight*'+str(normWeight)+')*((mass_w<95)&&(mass_w>65)&&(tau32<0.65)&&(sjbtag>0.5426))','histE')

hNoWmassCut.SetLineColor(kBlack)
hLowWmassCut.SetLineColor(kRed)
hSigWmassCut.SetLineColor(kBlue)

hNoWmassCut.Draw('histE')
hLowWmassCut.Draw('histE')
hSigWmassCut.Draw('histE')

cHT1000.Print('TopMassTester.pdf','pdf')