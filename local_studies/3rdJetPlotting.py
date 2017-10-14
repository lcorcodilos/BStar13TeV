import ROOT
from ROOT import *

import math

gStyle.SetOptStat(0)

# from optparse import OptionParser
# parser = OptionParser()

# parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
# 				  default	=	'rate_default',
# 				  dest		=	'cuts',
# 				  help		=	'Cuts type (ie default, rate, etc)')
# (options, args) = parser.parse_args()

# Create an output file
outfile = TFile('3rdJetHists.root','recreate')
outfile.cd()

# Specify which cuts we want to looks at - must have QCD MC minitrees for these
cuts = ['rate_sideband','rate_default','rate_highWmass','sideband','default','highWmass']

passedW3rdJetCounts = {'rate_sideband':0,'rate_default':0,'rate_highWmass':0,'sideband':0,'default':0,'highWmass':0}

#
# Start by making some histograms and storing them in outfile
#
for cut in cuts:
	file = TFile('../rootfiles/35851pb/TWminitree_QCD_PSET_'+cut+'.root','open')
	tree = file.Get("Tree")

	# topJetHist2D = TH2F('topJetHist2D_'+cut,'top jet '+cut,16,0,2*math.pi,24,-2.4,2.4)
	# WJetHist2D = TH2F('WJetHist2D_'+cut,'W jet '+cut,16,0,2*math.pi,24,-2.4,2.4)
	# thirdJetHist2D = TH2F('thirdJetHist2D_'+cut,'3rd jet '+cut,16,0,2*math.pi,24,-2.4,2.4)

	topJetHist1DPass = TH1F('topJetHist1DPass_'+cut,'Pass top jet '+cut,16,0,2*math.pi)
	topJetHist1DFail = TH1F('topJetHist1DFail_'+cut,'Fail top jet '+cut,16,0,2*math.pi)

	thirdJetHist1DPass = TH1F('thirdJetHist1DPass_'+cut,'Pass 3rd jet '+cut,16,0,2*math.pi)
	thirdJetHist1DFail = TH1F('thirdJetHist1DFail_'+cut,'Fail 3rd jet '+cut,16,0,2*math.pi)

	passedW3rdJetCount = 0
	for entry in range(tree.GetEntries()):
		tree.GetEntry(entry)

		topptcut = (tree.pt_top < 600) and (tree.pt_top > 400)

		if topptcut:
			toptag = (tree.tau32 < 0.65) and (tree.sjbtag < 0.5426)

			# Need to do a trick so that we can easily see the top and W
			# Will set wjet so it's always at pi/2 but then need to adjust the position of the top and 3rd jet
			# Can't just take abs(wjet.phi()-tjet.phi()) for example because say the W is at phi = 0, then a tjet
			# at either 2pi/3 or 4pi/3 will return the same value for abs(wjet.phi()-tjet.phi()). Doing this will
			# make it look like there's an imbalance of the third jet that prefers values < pi

			wjet_OldPhi = tree.phi_w
			wjet_NewPhi = 0
			rotation = wjet_NewPhi - wjet_OldPhi
			
			tjet_OldPhi = tree.phi_top
			tjet_NewPhi = tjet_OldPhi + rotation
			if tjet_NewPhi > 2*math.pi:
				tjet_NewPhi = tjet_NewPhi - 2*math.pi
			elif tjet_NewPhi < 0:
				tjet_NewPhi = 2*math.pi + tjet_NewPhi

			thirdjet_OldPhi = tree.phi_3
			thirdjet_NewPhi = thirdjet_OldPhi + rotation
			if thirdjet_NewPhi > 2*math.pi:
				thirdjet_NewPhi = thirdjet_NewPhi - 2*math.pi
			elif thirdjet_NewPhi < 0:
				thirdjet_NewPhi = 2*math.pi + thirdjet_NewPhi

			if toptag:
				topJetHist1DPass.Fill(tjet_NewPhi,tree.weight)
				thirdJetHist1DPass.Fill(thirdjet_NewPhi,tree.weight)
				passedW3rdJetCounts[cut] += 1

			else:
				topJetHist1DFail.Fill(tjet_NewPhi,tree.weight)
				thirdJetHist1DFail.Fill(thirdjet_NewPhi,tree.weight)

	outfile.cd()

	topJetHist1DPass.Write()
	topJetHist1DFail.Write()

	thirdJetHist1DPass.Write()
	thirdJetHist1DFail.Write()

outfile.Write()

#
# Now we go through the plots, make an Rp/f for each cut and apply it
#

WmassRegions = ['sideband','default','highWmass']

for reg in WmassRegions:
	# Get pass and fail hists in high tau21 region
	topRPass = outfile.Get('topJetHist1DPass_rate_'+reg)
	topRFail = outfile.Get('topJetHist1DFail_rate_'+reg)
	thirdRPass = outfile.Get('thirdJetHist1DPass_rate_'+reg)
	thirdRFail = outfile.Get('thirdJetHist1DFail_rate_'+reg)

	# Get pass and fail hists in low tau21 region
	topPass = outfile.Get('topJetHist1DPass_'+reg)
	topFail = outfile.Get('topJetHist1DFail_'+reg)
	thirdPass = outfile.Get('thirdJetHist1DPass_'+reg)
	thirdFail = outfile.Get('thirdJetHist1DFail_'+reg)

	# Clone the pass distributions in ratio region
	topRpf = topRPass.Clone('topRpf_'+reg)
	thirdRpf = thirdRPass.Clone('thirdRpf_'+reg)

	# Divide the clones by fail distribution to get the Rp/f
	topRpf.Divide(topRFail)
	thirdRpf.Divide(thirdRFail)

	# Clone the fail distributions in LOW tau21 region
	topEst = topFail.Clone('topEst_'+reg)
	thirdEst = thirdFail.Clone('thirdEst_'+reg)

	# Multiply the clones by the derived Rp/f
	topEst.Multiply(topRpf)
	thirdEst.Multiply(thirdRpf)

	# Make a canvas
	cAll = TCanvas('cAll','cAll',600,900)
	cAll.Divide(1,2)
	leg = TLegend(0.75,0.75,0.95,0.95)

	# Make the hists pretty
	topEst.SetLineColor(kBlue)
	topPass.SetLineColor(kRed)
	thirdEst.SetLineColor(kBlue)
	thirdPass.SetLineColor(kRed)

	leg.AddEntry(topPass,'Pass')
	leg.AddEntry(topEst,'Estimated')

	topPass.SetTitle('Top jet - '+reg)
	topPass.GetXaxis().SetTitle('\phi from W jet')
	thirdPass.SetTitle('Third jet - '+reg)
	thirdPass.GetXaxis().SetTitle('\phi from W jet')


	cAll.cd(1)

	# Need to draw the hist lines first as 'copies' and then do the error bars to get the filling right
	topPass.DrawCopy('hist')
	topEst.DrawCopy('samehist')
	topEst.SetFillColor(kBlue)
	topPass.SetFillColor(kRed)
	topEst.SetFillStyle(3004)
	topPass.SetFillStyle(3005)
	topPass.Draw('samee2')
	topEst.Draw('samee2')

	leg.Draw()

	cAll.cd(2)

	thirdPass.DrawCopy('hist')
	thirdEst.DrawCopy('samehist')
	thirdEst.SetFillColor(kBlue)
	thirdPass.SetFillColor(kRed)
	thirdEst.SetFillStyle(3004)
	thirdPass.SetFillStyle(3005)
	thirdPass.Draw('samee2')
	thirdEst.Draw('samee2')

	leg.Draw()


	cAll.Print('plots/3rdJetDeltaPhi_'+reg+'.pdf','pdf')

	cAll.Close()


	#
	# Finally, we want to know what percent of top-tagged events actually have a third jet
	#
	if reg != 'highWmass':
		ratefile = TFile.Open('../rootfiles/35851pb/TWratefileQCD_PSET_'+reg+'.root')
		ratetree = ratefile.Get('Tree')
		totalTopTags = float(ratetree.GetEntries())
		passedW3rdJetCount = float(passedW3rdJetCounts[reg])
		percent3rd = passedW3rdJetCount/totalTopTags*100
		print 'Percent of events top-tagged events with a 3rd jet: ' + str(percent3rd)