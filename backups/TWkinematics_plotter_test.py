

import os
import array
import glob
import math
import ROOT
import sys
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True
from ROOT import *
from array import *
from optparse import OptionParser
gROOT.Macro("rootlogon.C")
gROOT.LoadMacro("insertlogo.C+")
parser = OptionParser()

parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
(options, args) = parser.parse_args()

cuts = options.cuts


import Bstar_Functions	
from Bstar_Functions import *

pie = TMath.Pi()

kinVar = ['Mtw', 	'EtaTop', 	'EtaW', 	'PtTop', 	'PtW', 		'PtTopW', 	'PhiTop', 	'PhiW', 	'dPhi'	]
kinBkg = ['', 		'ET', 		'EW', 		'PT', 		'PW', 		'PTW', 		'PhT', 		'PhW', 		'dPhi'	]
kinBin = [140, 		12, 		12, 		50, 		50,		35,		12,		12,		12	]
kinLow = [500, 		-2.4, 		-2.4, 		450, 		370,		0,		-pie,		-pie,		2.2	]
kinHigh= [4000, 	2.4, 		2.4, 		1500, 		1430,		700,		pie,		pie,		pie	]
rebin =  [5,		 1,		 1, 		 2,		 2,		 1,		 1,		 1,		 1	]
st1_label= [";M_{tw} (GeV);Counts", ";Eta_{t} (rad);Counts", ";Eta_{W} (rad);Counts", ";Pt_{t} (GeV);Counts", ";Pt_{W} (GeV);Counts", ";Pt_{tW} (GeV);Counts", ";Phi_{t} (rad)", ";Phi_{W} (rad);Counts", ";Delta Phi (rad);Counts"]
pull_label= [";M_{tw} (GeV);(Data-Bkg)/#sigma", ";Eta_{t} (rad);(Data-Bkg)/#sigma", ";Eta_{W} (rad);(Data-Bkg)/#sigma", ";Pt_{t} (GeV);(Data-Bkg)/#sigma", ";Pt_{W} (GeV);(Data-Bkg)/#sigma", ";Pt_{tW} (GeV);(Data-Bkg)/#sigma", ";Phi_{t} (rad)", ";Phi_{W} (rad);(Data-Bkg)/#sigma", ";Delta Phi (rad);(Data-Bkg)/#sigma"]

for i in range(0, len(kinVar)):
	print "kinVar = " + "'" + kinVar[i] + "'"
	print "kinBkg = " + "'" + kinBkg[i] + "'"

	st1 = ROOT.THStack('st1', 'st1')

	leg = TLegend(0.7, 0.6, 0.93, 0.9)
	leg.SetNColumns(1)
	leg.SetFillColor(0)
	leg.SetBorderSize(0)



#bins=[500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1200,1300,1400,1500,1700,1900,2300,2700,3100]
#bins.append(3000)
#bins2=array('d',bins)

	Mult = 1.0

#Kfac=1.2



	Data = ROOT.TFile("rootfiles/TWkinematicsQCD_Trigger_nominal_none_PSET_"+options.cuts+".root")
#DataMmup = ROOT.TFile("rootfiles/TWkinematicsdata_Trigger_none_none_modm_up_PSET_default.root")
#DataMmdown = ROOT.TFile("rootfiles/TWkinematicsdata_Trigger_none_none_modm_down_PSET_default.root")
	print "Root file opened"

	DataFS = Data.Get(kinVar[i])
	DataBE = Data.Get("QCDbkg" + kinBkg[i])

#DataBE2d = Data.Get("QCDbkg2D")
#DataBEMmup = DataMmup.Get("QCDbkg")
#DataBEMmdown = DataMmdown.Get("QCDbkg")
#DataBE2dup = Data.Get("QCDbkg2Dup")
#DataBE2ddown = Data.Get("QCDbkg2Ddown")
	#exec 'c%s = TCanvas(kinVar[i], "Data Full selection vs b pt tagging background", 700, 600)' % i
	#canvas[i] = TCanvas(kinVar[i], 'Data Full selection vs b pt tagging background', 700, 600)
	c1 = TCanvas(kinVar[i], 'Data Full selection vs b pt tagging background', 700, 700)
	main = ROOT.TPad("main", "main", 0, 0.3, 1, 1)
	sub = ROOT.TPad("sub", "sub", 0, 0, 1, 0.3)

	main.SetLeftMargin(0.16)
	main.SetRightMargin(0.05)
	main.SetTopMargin(0.1)
	main.SetBottomMargin(0.0)

	sub.SetLeftMargin(0.16)
	sub.SetRightMargin(0.05)
	sub.SetTopMargin(0)
	sub.SetBottomMargin(0.3)

	main.Draw()
	sub.Draw()

	main.cd()

	TTmc = ROOT.TFile("rootfiles/TWkinematicsweightedttbar_Trigger_nominal_none_PSET_"+options.cuts+".root")
	print "Opened ttbar file"

#TTmcScaleUp = ROOT.TFile("rootfiles/TWkinematicsttbar_Trigger_nominal_ScaleUp_PSET_"+options.cuts+".root")
#TTmcScaleDown = ROOT.TFile("rootfiles/TWkinematicsttbar_Trigger_nominal_ScaleDown_PSET_"+options.cuts+".root")

#TTmcPtSmearUp = ROOT.TFile("rootfiles/TWkinematicsttbar_Trigger_nominal_PtSmearUp_PSET_"+options.cuts+".root")
#TTmcPtSmearDown = ROOT.TFile("rootfiles/TWkinematicsttbar_Trigger_nominal_PtSmearDown_PSET_"+options.cuts+".root")

#TTmcQ2ScaleUp = ROOT.TFile("rootfiles/TWkinematicsttbarscaleup_Trigger_nominal_none_PSET_"+options.cuts+".root")
#TTmcQ2ScaleDown = ROOT.TFile("rootfiles/TWkinematicsttbarscaledown_Trigger_nominal_none_PSET_"+options.cuts+".root")




#TTmcEtaSmearUp = ROOT.TFile("rootfiles/TWkinematicsttbar_Trigger_nominal_EtaSmearUp_PSET_"+options.cuts+".root")
#TTmcEtaSmearDown = ROOT.TFile("rootfiles/TWkinematicsttbar_Trigger_nominal_EtaSmearDown_PSET_"+options.cuts+".root")

#TTmcTriggerUp = ROOT.TFile("rootfiles/TWkinematicsttbar_Trigger_up_none_PSET_"+options.cuts+".root")
#TTmcTriggerDown = ROOT.TFile("rootfiles/TWkinematicsttbar_Trigger_down_none_PSET_"+options.cuts+".root")

#output = ROOT.TFile( "TWkinematics_output_PSET_"+options.cuts+".root", "recreate" )
#output.cd()

	TTmcFS = TTmc.Get(kinVar[i])

#TTmcBE = TTmc.Get("QCDbkg")

#TTmcBE2d = TTmc.Get("QCDbkg2D")


#TTmcBEh = TTmc.Get("QCDbkgh")
#TTmcBEl = TTmc.Get("QCDbkgl")

	DataBEh = Data.Get("QCDbkg"+kinBkg[i]+"h")
	DataBEl = Data.Get("QCDbkg"+kinBkg[i]+"l")


#TTmcFSScaleUp = TTmcScaleUp.Get("Mtw")
#TTmcFSScaleDown = TTmcScaleDown.Get("Mtw")

#TTmcFSQ2ScaleUp = TTmcQ2ScaleUp.Get("Mtw")
#TTmcFSQ2ScaleDown = TTmcQ2ScaleDown.Get("Mtw")

#TTmcFSPtSmearUp = TTmcPtSmearUp.Get("Mtw")
#TTmcFSPtSmearDown = TTmcPtSmearDown.Get("Mtw")

#TTmcFSEtaSmearUp = TTmcEtaSmearUp.Get("Mtw")
#TTmcFSEtaSmearDown = TTmcEtaSmearDown.Get("Mtw")

#TTmcFSTriggerUp = TTmcTriggerUp.Get("Mtw")
#TTmcFSTriggerDown = TTmcTriggerDown.Get("Mtw")

#DataBEMmup = DataBEMmup.Rebin(len(bins2)-1,"",bins2)
#DataBEMmdown = DataBEMmdown.Rebin(len(bins2)-1,"",bins2)

#DataBE2dup = DataBE2dup.Rebin(len(bins2)-1,"",bins2)
#DataBE2ddown = DataBE2ddown.Rebin(len(bins2)-1,"",bins2)

#TTmcFSQ2ScaleUp = TTmcFSQ2ScaleUp.Rebin(len(bins2)-1,"",bins2)
#TTmcFSQ2ScaleDown = TTmcFSQ2ScaleDown.Rebin(len(bins2)-1,"",bins2)

#TTmcFSScaleUp = TTmcFSScaleUp.Rebin(len(bins2)-1,"",bins2)
#TTmcFSScaleDown =  TTmcFSScaleDown.Rebin(len(bins2)-1,"",bins2)

#TTmcFSPtSmearUp =  TTmcFSPtSmearUp.Rebin(len(bins2)-1,"",bins2)
#TTmcFSPtSmearDown =  TTmcFSPtSmearDown.Rebin(len(bins2)-1,"",bins2)

#TTmcFSEtaSmearUp = TTmcFSEtaSmearUp.Rebin(len(bins2)-1,"",bins2)
#TTmcFSEtaSmearDown = TTmcFSEtaSmearDown.Rebin(len(bins2)-1,"",bins2)

#TTmcFSTriggerUp = TTmcFSTriggerUp.Rebin(len(bins2)-1,"",bins2)
#TTmcFSTriggerDown = TTmcFSTriggerDown.Rebin(len(bins2)-1,"",bins2)


#DataBE2d = DataBE2d.Rebin(len(bins2)-1,"",bins2)
	DataFS.Add(TTmcFS)
#TTmcFS = TTmcFS.Rebin(len(bins2)-1,"",bins2)
#DataBE = DataBE.Rebin(len(bins2)-1,"",bins2)
#DataFS = DataFS.Rebin(len(bins2)-1,"",bins2)
#print DataFS.Integral()
#DataBEl = DataBEl.Rebin(len(bins2)-1,"",bins2)
#DataBEh = DataBEh.Rebin(len(bins2)-1,"",bins2)

	TTmcFS = TTmcFS.Rebin(rebin[i])
	DataBE = DataBE.Rebin(rebin[i])
	DataFS = DataFS.Rebin(rebin[i])
	print DataFS.Integral()
	DataBEl = DataBEl.Rebin(rebin[i])
	DataBEh = DataBEh.Rebin(rebin[i])


#TTmcBE = TTmcBE.Rebin(len(bins2)-1,"",bins2)
#TTmcBE2d = TTmcBE2d.Rebin(len(bins2)-1,"",bins2)
#TTmcBEh = TTmcBEh.Rebin(len(bins2)-1,"",bins2)
#TTmcBEl = TTmcBEl.Rebin(len(bins2)-1,"",bins2)

#subtract weighted TT pretags

#unsubbkg = DataBE.Clone()

#DataBE.Add(TTmcBE,-1)
#DataBE2d.Add(TTmcBE2d,-1)
#DataBE2dup.Add(TTmcBE2d,-1)
#DataBE2ddown.Add(TTmcBE2d,-1)
#DataBEl.Add(TTmcBE,-1)
#DataBEh.Add(TTmcBE,-1)
#DataBEMmup.Add(TTmcBE,-1)
#DataBEMmdown.Add(TTmcBE,-1)


#singletop = ROOT.TH1F("singletop",     "singletop",     	  	      140, 500, 4000 )
#singletop = singletop.Rebin(len(bins2)-1,"",bins2)

#schanst = ROOT.TH1F("schanst",     "singletop",     	  	      140, 500, 4000 )
#schanst = schanst.Rebin(len(bins2)-1,"",bins2)
#for ifile in range(0,len(stops)):
#	sfiles.append(ROOT.TFile("rootfiles/TWkinematicsweighted"+stops[ifile]+"_Trigger_nominal_none_PSET_"+options.cuts+".root"))
#	shists.append(sfiles[ifile].Get("Mtw"))
#	ssubs.append(sfiles[ifile].Get("QCDbkg"))

#	ssubsh.append(sfiles[ifile].Get("QCDbkgh"))
#	ssubsl.append(sfiles[ifile].Get("QCDbkgl"))
#	shists[ifile] = shists[ifile].Rebin(len(bins2)-1,"",bins2)
#	ssubs[ifile] = ssubs[ifile].Rebin(len(bins2)-1,"",bins2)
#	ssubsh[ifile] = ssubsh[ifile].Rebin(len(bins2)-1,"",bins2)
#	ssubsl[ifile] = ssubsl[ifile].Rebin(len(bins2)-1,"",bins2)
	#print str((Luminosity*stopxsecs[ifile]*TeffScale)/stopnevents[ifile])    
#	DataBE.Add(ssubs[ifile],-1)
#	DataBEl.Add(ssubsl[ifile],-1)
#	DataBEh.Add(ssubsh[ifile],-1)  
#	singletop.SetFillColor(6)
#	singletop.Add(shists[ifile])
#	if ifile<=1:
#		schanst.Add(shists[ifile])

#st1.Add(singletop)

#output.cd()

	fittitles = ["pol0","pol2","pol3","FIT","Bifpoly","expofit"]
	QCDbkg_ARR = []
	for ihist in range(0,len(fittitles)):
		print "Appending to QCDbkh_ARR - " + "QCDbkg"+kinBkg[i]+str(fittitles[ihist])
		QCDbkg_ARR.append(Data.Get("QCDbkg"+kinBkg[i]+str(fittitles[ihist])))
		#QCDbkg_ARR[ihist] = QCDbkg_ARR[ihist].Rebin(len(bins2)-1,"",bins2)
		QCDbkg_ARR[ihist] = QCDbkg_ARR[ihist].Rebin(rebin[i])

	BEfiterrh = kinFit_Uncertainty(QCDbkg_ARR, kinBkg[i])

#sig3d = DataBE2dup.Clone()
#sig2d = DataBEh.Clone()
#sig3d.Add(DataBE2d,-1)
#sig2d.Add(DataBE,-1)
#extrasig = sig3d.Clone()




#for ibin in range(1,sig3d.GetNbinsX()+1):
#	cont3d = sig3d.GetBinContent(ibin)
#	cont2d = sig2d.GetBinContent(ibin)
#	newcont = sqrt(max(cont3d*cont3d-cont2d*cont2d,0.0))
#	extrasig.SetBinContent(ibin,newcont)


#output.cd()
	DataQCDBEH=DataBE.Clone("DataQCDBEH")
	DataQCDBEL=DataBE.Clone("DataQCDBEL")
	DataTOTALBEH=DataBE.Clone("DataTOTALBEH")
	DataTOTALBEL=DataBE.Clone("DataTOTALBEL")

	for ibin in range(0,DataBE.GetNbinsX()):
#	PtScaleup=(TTmcFSScaleUp.GetBinContent(ibin) -TTmcFS.GetBinContent(ibin))
#	Q2Scaleup=(TTmcFSQ2ScaleUp.GetBinContent(ibin) -TTmcFS.GetBinContent(ibin))
#	PtSmearup=(TTmcFSPtSmearUp.GetBinContent(ibin) -TTmcFS.GetBinContent(ibin))
#	EtaSmearup=(TTmcFSEtaSmearUp.GetBinContent(ibin) -TTmcFS.GetBinContent(ibin))
#	Triggerup=(TTmcFSTriggerUp.GetBinContent(ibin) -TTmcFS.GetBinContent(ibin))


#	PtScaledown=(TTmcFSScaleDown.GetBinContent(ibin) -TTmcFS.GetBinContent(ibin))
#	Q2Scaledown=(TTmcFSQ2ScaleDown.GetBinContent(ibin) -TTmcFS.GetBinContent(ibin))
#	PtSmeardown=(TTmcFSPtSmearDown.GetBinContent(ibin) -TTmcFS.GetBinContent(ibin))
#	EtaSmeardown=(TTmcFSEtaSmearDown.GetBinContent(ibin) -TTmcFS.GetBinContent(ibin))
#	Triggerdown=(TTmcFSTriggerDown.GetBinContent(ibin) -TTmcFS.GetBinContent(ibin))

#	ups = [PtScaleup,Q2Scaleup,PtSmearup,EtaSmearup,Triggerup]
#	downs = [PtScaledown,Q2Scaledown,PtSmeardown,EtaSmeardown,Triggerdown]
	
#	upstr = ["PtScaleup","Q2Scaleup","PtSmearup","EtaSmearup","Triggerup"]
#	downstr = ["PtScaledown","Q2Scaledown","PtSmeardown","EtaSmeardown","Triggerdown"]

#	sigsqup = 0.
#	sigsqdown = 0.

#	for i in range(0,len(ups)):
#		upsig = max(ups[i],downs[i],0.)
#		downsig = min(ups[i],downs[i],0.)
#		sigsqup+=upsig*upsig
#		sigsqdown+=downsig*downsig

#	CrossSection=0.22*TTmcFS.GetBinContent(ibin)
		TTstat=TTmcFS.GetBinError(ibin)
		if DataBE.GetBinContent(ibin)>0:
			QCDstat=DataBE.GetBinError(ibin)
		else:
			QCDstat=0.
		QCDfit=abs(BEfiterrh.GetBinContent(ibin))
		QCDfit1=abs((DataBEh.GetBinContent(ibin)-DataBEl.GetBinContent(ibin))/2)
#	QCDfit2=abs(DataBE2d.GetBinContent(ibin)-DataBE.GetBinContent(ibin))
#	QCDfit3=abs(extrasig.GetBinContent(ibin))
#	QCDMm=abs((DataBEMmup.GetBinContent(ibin)-DataBEMmdown.GetBinContent(ibin))/2)


		QCDsys=sqrt(QCDfit*QCDfit + QCDfit1*QCDfit1)
		QCDerror= sqrt(QCDstat*QCDstat+QCDsys*QCDsys)
		TTerrorup=sqrt(TTstat*TTstat)
		TTerrordown=sqrt(TTstat*TTstat)
		Totalerrorup=sqrt(QCDerror*QCDerror+TTerrorup*TTerrorup)
		Totalerrordown=sqrt(QCDerror*QCDerror+TTerrordown*TTerrordown)
		DataQCDBEH.SetBinContent(ibin,DataQCDBEH.GetBinContent(ibin)+QCDerror)
		DataQCDBEL.SetBinContent(ibin,DataQCDBEL.GetBinContent(ibin)-QCDerror)
		DataTOTALBEH.SetBinContent(ibin,DataTOTALBEH.GetBinContent(ibin)+Totalerrorup)
		DataTOTALBEL.SetBinContent(ibin,DataTOTALBEL.GetBinContent(ibin)-Totalerrordown)
	print "QCD total error"
	print (DataQCDBEH.Integral()-DataBE.Integral())/DataBE.Integral()
	print 


	DataTOTALBEL.Add(TTmcFS)
	DataTOTALBEH.Add(TTmcFS)
#DataTOTALBEL.Add(singletop)
#DataTOTALBEH.Add(singletop)

#for ifile in range(0,len(stops)):
#	DataTOTALBEL.Add(shists[ifile])
#	DataTOTALBEH.Add(shists[ifile])		

	DataBE.SetFillColor(kYellow)
	TTmcFS.SetFillColor(kRed)

	DataTOTALBEH.SetLineColor(kBlue)
	DataTOTALBEH.SetLineWidth(2)
#DataTOTALBEH.SetLineStyle(2)

	centerqcd = DataTOTALBEL.Clone("centerqcd")
	centerqcd.SetFillColor(kYellow)
	centerqcd.Add(TTmcFS,-1)
#centerqcd.Add(singletop,-1)

	DataTOTALBEL.SetLineColor(kBlue)
	DataTOTALBEL.SetLineWidth(2)
#DataTOTALBEL.SetFillColor(0)
#DataTOTALBEL.SetLineStyle(0)
#DataTOTALBEL.SetLineWidth(2)
#DataTOTALBEL.SetLineStyle(2)

	sigst= ROOT.THStack("sigst", "sigst")
	sigma = DataTOTALBEH.Clone("sigma")
	sigma.SetFillStyle(3245)
	sigma.SetFillColor(1)
	sigma.SetLineColor(0)
	centerqcd.SetLineColor(kYellow)

	sigma.Add(DataTOTALBEL,-1)
#sigst.Add(singletop)
	sigst.Add(TTmcFS)
	sigst.Add(centerqcd)
	sigst.Add(sigma)


	st1.Add(TTmcFS)
	st1.Add(DataBE)

	bkgline=st1.GetStack().Last().Clone("bkgline")
	bkgline.SetFillColor(0)
	bkgline.SetFillStyle(0)

	leg.AddEntry( DataFS, 'Data', 'P')
	leg.AddEntry( DataBE, 'QCD background prediction', 'F')	
	leg.AddEntry( TTmcFS, 't#bar{t} MC prediction', 'F')
#leg.AddEntry( singletop, 'Single top quark MC prediction', 'F')
	leg.AddEntry( sigma, '1 #sigma background uncertainty', 'F')
#leg.AddEntry( sigh[0], 'W`_{R} at 1500 GeV', 'L')
#leg.AddEntry( sigh[1], 'W`_{R} at 1900 GeV', 'L')
#leg.AddEntry( sigh[2], 'W`_{R} at 2300 GeV', 'L')

#c1.cd()
#c1.SetLeftMargin(0.17)
#st1.GetXaxis().SetRangeUser(0,3000)
	st1.SetMaximum(DataTOTALBEH.GetMaximum() * 1.3)
	st1.SetMinimum(1.0)
	st1.SetTitle(st1_label[i])
	st1.Draw("hist")
	gPad.SetLeftMargin(.16)
	st1.GetYaxis().SetTitleOffset(0.9)
#DataTOTALBEH.Draw("histsame")
#DataTOTALBEL.Draw("histsame")
	sigst.Draw("samehist")
	bkgline.Draw("samehist")
#sigh[0].Draw("samehist")
#sigh[1].Draw("samehist")
#sigh[2].Draw("samehist")


	DataFS1	    = TH1D("DataFS1",     str(kinVar[i])+" in b+1",     	  	      kinBin[i], kinLow[i], kinHigh[i] )
#pythonDataFS1 = DataFS1.Rebin(len(bins2)-1,"",bins2)
	DataFS1 = DataFS1.Rebin(rebin[i])
	for ibin in range(1,DataFS.GetNbinsX()+1):
		DataFS1.SetBinContent(ibin,DataFS.GetBinContent(ibin))

	DataFS1.SetBinErrorOption(DataFS1.kPoisson)
	DataFS1=DataFS
	DataFS1.Draw("samepE")

	leg.Draw()

	prelim = TLatex()
	prelim.SetNDC()


	insertlogo( main, 4, 11 )


#prelim.DrawLatex( 0.5, 0.91, "#scale[0.8]{CMS Preliminary, 8 TeV, 19.7 fb^{-1}}" )
	sub.cd()
	gPad.SetLeftMargin(.16)
	totalH = st1.GetStack().Last().Clone("totalH")
#totalH.Add(TTmcFS)
	pull = Make_Pull_plot( DataFS1,totalH,DataTOTALBEH,DataTOTALBEL )


	
#pull.GetXaxis().SetRangeUser(0,3000)
	pull.SetFillColor(kBlue)
	pull.SetTitle(pull_label[i])
	pull.SetStats(0)


	pull.GetYaxis().SetRangeUser(-2.9,2.9)
	pull.GetXaxis().SetLabelSize(0.05)
	pull.GetYaxis().SetLabelSize(0.05)


	LS = .13

	pull.GetYaxis().SetTitleOffset(0.4)
	pull.GetXaxis().SetTitleOffset(0.9)
	pull.SetStats(0)
    
    
	pull.GetYaxis().SetLabelSize(LS)
	pull.GetYaxis().SetTitleSize(LS)
	pull.GetYaxis().SetNdivisions(306)
	pull.GetXaxis().SetLabelSize(LS)
	pull.GetXaxis().SetTitleSize(LS)

	pull.Draw("hist")

	line2=ROOT.TLine(500.0,0.0,4000.0,0.0)
	line2.SetLineColor(0)
	line1=ROOT.TLine(500.0,0.0,4000.0,0.0)
	line1.SetLineStyle(2)

	line2.Draw()
	line1.Draw()
	gPad.Update()

	main.RedrawAxis()

	c1.Print('plots/' + kinVar[i] + 'vsBkg_BifPoly_fit_kin_PSET_'+options.cuts+'.root', 'root')
	c1.Print('plots/' + kinVar[i] + 'vsBkg_BifPoly_fit_kin_PSET_'+options.cuts+'.pdf', 'pdf')
	c1.Print('plots/' + kinVar[i] + 'vsBkg_BifPoly_fit_kin_PSET_'+options.cuts+'.png', 'png')
	main.SetLogy()
	st1.SetMaximum( DataBEh.GetMaximum() * 5000 )
	st1.SetMinimum( 0.1)
	main.RedrawAxis()

	c1.Print('plots/' + kinVar[i] + 'vsBkgsemilog_BifPoly_fit_kin_PSET_'+options.cuts+'.root', 'root')
	c1.Print('plots/' + kinVar[i] + 'vsBkgsemilog_BifPoly_fit_kin_PSET_'+options.cuts+'.pdf', 'pdf')
	c1.Print('plots/' + kinVar[i] + 'vsBkgsemilog_BifPoly_fit_kin_PSET_'+options.cuts+'.png', 'png')

