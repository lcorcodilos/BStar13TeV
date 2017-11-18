import ROOT
from ROOT import *

#
# Part 1: Compare passing and failing distributions with different tau32 cuts
#

fQCDs = []
NoTau32CutPass = TH1F('NoTau32CutPass','NoTau32CutPass',25,50,300)
HighTau32CutPass = TH1F('HighTau32CutPass','HighTau32CutPass',25,50,300)
LowTau32CutPass = TH1F('LowTau32CutPass','LowTau32CutPass',25,50,300)

NoTau32CutFail = TH1F('NoTau32CutFail','NoTau32CutFail',25,50,300)
HighTau32CutFail = TH1F('HighTau32CutFail','HighTau32CutFail',25,50,300)
LowTau32CutFail = TH1F('LowTau32CutFail','LowTau32CutFail',25,50,300)

for ht in ['700','1000','1500','2000']:
	htFile = TFile.Open('../rootfiles/35851pb/TWminitree_weightedQCDHT'+ht+'_PSET_default.root') 
	htTree = htFile.Get('miniTree')

	htWeight = htFile.Get('Weight')
	htWeight.GetEntry(0)
	htNormWeight = htWeight.weightv

	htNoTau32CutPass = TH1F('htNoTau32CutPass','htNoTau32CutPass',25,50,300)
	htHighTau32CutPass = TH1F('htHighTau32CutPass','htHighTau32CutPass',25,50,300)
	htLowTau32CutPass = TH1F('htLowTau32CutPass','htLowTau32CutPass',25,50,300)

	htNoTau32CutFail = TH1F('htNoTau32CutFail','htNoTau32CutFail',25,50,300)
	htHighTau32CutFail = TH1F('htHighTau32CutFail','htHighTau32CutFail',25,50,300)
	htLowTau32CutFail = TH1F('htLowTau32CutFail','htLowTau32CutFail',25,50,300)

	htTree.Draw('mass_top>>htNoTau32CutPass','(weight*'+str(htNormWeight)+')*((mass_w<95)&&(mass_w>65)&&(sjbtag>0.5426))','goff')
	htTree.Draw('mass_top>>htHighTau32CutPass','(weight*'+str(htNormWeight)+')*((mass_w<95)&&(mass_w>65)&&(tau32<0.65)&&(sjbtag>0.5426))','goff')
	htTree.Draw('mass_top>>htLowTau32CutPass','(weight*'+str(htNormWeight)+')*((mass_w<95)&&(mass_w>65)&&(tau32<0.5)&&(sjbtag>0.5426))','goff')

	htTree.Draw('mass_top>>htNoTau32CutFail','(weight*'+str(htNormWeight)+')*((mass_w<95)&&(mass_w>65)&&!(sjbtag>0.5426))','goff')
	htTree.Draw('mass_top>>htHighTau32CutFail','(weight*'+str(htNormWeight)+')*((mass_w<95)&&(mass_w>65)&&!((tau32<0.65)&&(sjbtag>0.5426)))','goff')
	htTree.Draw('mass_top>>htLowTau32CutFail','(weight*'+str(htNormWeight)+')*((mass_w<95)&&(mass_w>65)&&!((tau32<0.5)&&(sjbtag>0.5426)))','goff')

	NoTau32CutPass.Add(htNoTau32CutPass)
	HighTau32CutPass.Add(htHighTau32CutPass)
	LowTau32CutPass.Add(htLowTau32CutPass)

	NoTau32CutFail.Add(htNoTau32CutFail)
	HighTau32CutFail.Add(htHighTau32CutFail)
	LowTau32CutFail.Add(htLowTau32CutFail)



cFull = TCanvas('cFull','cFull',1800,600)
cFull.Divide(3,1)

for hist in [NoTau32CutPass, NoTau32CutFail, HighTau32CutPass, HighTau32CutFail, LowTau32CutPass, LowTau32CutFail]:
	hist.Scale(1/hist.Integral())

NoTau32CutPass.SetLineColor(kBlack)
HighTau32CutPass.SetLineColor(kRed)
LowTau32CutPass.SetLineColor(kBlue)

NoTau32CutFail.SetLineColor(kBlack)
HighTau32CutFail.SetLineColor(kRed)
LowTau32CutFail.SetLineColor(kBlue)

NoTau32CutFail.SetLineStyle(2)
HighTau32CutFail.SetLineStyle(2)
LowTau32CutFail.SetLineStyle(2)

cFull.cd(1)
NoTau32CutFail.Draw('histE')
NoTau32CutPass.Draw('same histE')
cFull.cd(2)
HighTau32CutFail.Draw('histE')
HighTau32CutPass.Draw('same histE')
cFull.cd(3)
LowTau32CutFail.Draw('histE')
LowTau32CutPass.Draw('same histE')

cFull.Print('TopMassTester2.pdf','pdf')


#
# Part 2: Compare 
# 