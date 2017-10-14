import ROOT
from ROOT import *

fThetaNom = TFile('histos-bstar-ttbarrate_syst.root','open') 
fThetaUp = TFile('histos-bstar-ttbarrateup_syst.root','open')
fThetaDown = TFile('histos-bstar-ttbarratedown_syst.root','open')
fTtbar = TFile('BStarCombination/allhadronicright35851pb_doublettsub_mt.root','open') # could also be noTTsub since we're grabbing the tt distribution which is identical in the two files

hThetaNom = fThetaNom.Get('mt_allhad__ttbar')
hThetaUp = fThetaUp.Get('mt_allhad__ttbar')
hThetaDown = fThetaDown.Get('mt_allhad__ttbar')
hTtbar = fTtbar.Get('mt_allhad__ttbar')

SF = (hThetaNom.Integral()-hTtbar.Integral())/hTtbar.Integral()
SFup = (hThetaUp.Integral()-hTtbar.Integral())/hTtbar.Integral()
SFdown = (hThetaDown.Integral()-hTtbar.Integral())/hTtbar.Integral()

print "SF = " + str(SF) + ' + ' + str(SFup-SF) + ' - ' + str(SF - SFdown)

out = open('../../bstar_theta_PtSF.txt','w')

out.write(str(SF)+'\n')
out.write(str(SFup-SF)+'\n')
out.write(str(SF-SFdown)+'\n')

out.close()

