import ROOT
from ROOT import *

file = TFile.Open('../TTrees/TWtreefile_QCD_Trigger_nominal_none.root')
tree = file.Get('Tree')

# Look at the leading jet mass in 
#        |			 |			 |
#        |			 |			 |
#        |		1	 |		3	 |
#  tau21 |			 |			 |
#   0.4  |------------------------
#        |			 |			 |
#        |			 |			 |
#        |		2	 |		4	 |
#        |			 |			 |
#        |---------------------------
#		30			65			90
#					W mass

c1 = TCanvas('SBrpf','SBrpf',800,700)
c2 = TCanvas('SB','SB',800,700)
c3 = TCanvas('SRrpf','SRrpf',800,700)
c4 = TCanvas('SR','SR',800,700)

# Only care when the subleading jet has been tagged as a W
# Wmass = [low,high]
def preselFunc(Wmass):
				# ---------------------------- sub lead is a W------------------------------------------------------------     -----------------lead is not a top --------------------------------------------     
	thisPresel = '(tau2_subleading/tau1_subleading<0.4) && (mass_subleading>'+Wmass[0]+') && (mass_subleading<'+Wmass[1]+') && ((mass_leading<105) || (mass_leading>210)) && (tau3_leading/tau2_leading > 0.65)'
	return thisPresel

c1.cd()	  #              # ---- W mass region-----	 ------- W tau region------------  --just looking below 105--
tree.Draw('mass_leading',preselFunc(['30','65'])+'&&(tau2_leading/tau1_leading>0.4) && mass_leading<105')

c2.cd()
tree.Draw('mass_leading',preselFunc(['30','65'])+'&&(tau2_leading/tau1_leading<0.4) && mass_leading<105')

c3.cd()
tree.Draw('mass_leading',preselFunc(['65','105'])+'&&(tau2_leading/tau1_leading>0.4) && mass_leading<105')

c4.cd()
tree.Draw('mass_leading',preselFunc(['65','105'])+'&&(tau2_leading/tau1_leading<0.4) && mass_leading<105')

c1.Print('PassFailStudy/c1.pdf','pdf')
c2.Print('PassFailStudy/c2.pdf','pdf')
c3.Print('PassFailStudy/c3.pdf','pdf')
c4.Print('PassFailStudy/c4.pdf','pdf')

# Now also look at the low pt range
c1.cd()	  #              # ---- W mass region-----	 ------- W tau region------------
tree.Draw('mass_leading',preselFunc(['30','65'])+'&&(tau2_leading/tau1_leading>0.4) && mass_leading<105&&(pt_leading>400)&&(pt_leading<600)')

c2.cd()
tree.Draw('mass_leading',preselFunc(['30','65'])+'&&(tau2_leading/tau1_leading<0.4) && mass_leading<105&&(pt_leading>400)&&(pt_leading<600)')

c3.cd()
tree.Draw('mass_leading',preselFunc(['65','105'])+'&&(tau2_leading/tau1_leading>0.4) && mass_leading<105&&(pt_leading>400)&&(pt_leading<600)')

c4.cd()
tree.Draw('mass_leading',preselFunc(['65','105'])+'&&(tau2_leading/tau1_leading<0.4) && mass_leading<105&&(pt_leading>400)&&(pt_leading<600)')

c1.Print('PassFailStudy/c1_lowpt.pdf','pdf')
c2.Print('PassFailStudy/c2_lowpt.pdf','pdf')
c3.Print('PassFailStudy/c3_lowpt.pdf','pdf')
c4.Print('PassFailStudy/c4_lowpt.pdf','pdf')

# Now the high pt range
c1.cd()	  #              # ---- W mass region-----	 ------- W tau region------------
tree.Draw('mass_leading',preselFunc(['30','65'])+'&&(tau2_leading/tau1_leading>0.4) && mass_leading<105&&(pt_leading>600)')

c2.cd()
tree.Draw('mass_leading',preselFunc(['30','65'])+'&&(tau2_leading/tau1_leading<0.4) && mass_leading<105&&(pt_leading>600)')

c3.cd()
tree.Draw('mass_leading',preselFunc(['65','105'])+'&&(tau2_leading/tau1_leading>0.4) && mass_leading<105&&(pt_leading>600)')

c4.cd()
tree.Draw('mass_leading',preselFunc(['65','105'])+'&&(tau2_leading/tau1_leading<0.4) && mass_leading<105&&(pt_leading>600)')

c1.Print('PassFailStudy/c1_highpt.pdf','pdf')
c2.Print('PassFailStudy/c2_highpt.pdf','pdf')
c3.Print('PassFailStudy/c3_highpt.pdf','pdf')
c4.Print('PassFailStudy/c4_highpt.pdf','pdf')