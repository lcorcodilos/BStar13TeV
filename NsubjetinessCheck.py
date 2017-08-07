import ROOT
from ROOT import *
import array
from array import *

file = TFile('TTrees/TWtreefile_data_Trigger_nominal_none.root')
tree = file.Get("Tree")

newFile = TFile('Nsubjetiness.root','recreate')
newTree = TTree("taus","taus")

treeVars = {"tau32":array('d',[0]), "tau21":array('d',[0])}

for v in treeVars.keys():
	newTree.Branch(v, treeVars[v], v+"/D")

Tau32vsTau21 = TH2F("Tau32 vs Tau21", "Tau32 vs Tau21", 
					20, 0.0, 1.0,
					20, 0.0, 1.0)

Cuts = {	'wpt':[400.0,float("inf")],
			'tpt':[400.0,float("inf")],
			'dy':[0.0,1.8],
			'tmass':[105.0,210.0],
			'tau32':[0.0,0.65],
			'tau21':[0.4,1.0],
			'sjbtag':[0.46,1.0],
			'wmass':[65.0,105.0],
			'eta1':[0.0,0.8],
			'eta2':[0.8,2.4],
			'eta':[0.0,2.4]
			}

count = 0
totev = tree.GetEntries()
nev = totev/10

for event in tree:
	while count < nev:
		count += 1
		if count % 100000 == 0 :
			print  '--------- Processing Event ' + str(count) +'   -- percent complete ' + str(100*count/totev) + '% -- '

		doneAlready = False
		for hemis in ['hemis0','hemis1']:
			if hemis == 'hemis0':
				# Load up the ttree values
				tVals = {
					"tau1":tree.tau1_leading,
					"tau2":tree.tau2_leading,
					"tau3":tree.tau3_leading,
					"phi":tree.phi_leading,
					"mass":tree.mass_leading,
					"pt":tree.pt_leading,
					"eta":tree.eta_leading,
					"sjbtag":tree.sjbtag_leading,
					"SDmass":tree.SDmass_leading
				}

				wVals = {
					"tau1":tree.tau1_subleading,
					"tau2":tree.tau2_subleading,
					"tau3":tree.tau3_subleading,
					"phi":tree.phi_subleading,
					"mass":tree.mass_subleading,
					"pt":tree.pt_subleading,
					"eta":tree.eta_subleading,
					"sjbtag":tree.sjbtag_subleading,
					"SDmass":tree.SDmass_subleading
				}

			if hemis == 'hemis1' and doneAlready == False  :
				wVals = {
					"tau1":tree.tau1_leading,
					"tau2":tree.tau2_leading,
					"tau3":tree.tau3_leading,
					"phi":tree.phi_leading,
					"mass":tree.mass_leading,
					"pt":tree.pt_leading,
					"eta":tree.eta_leading,
					"sjbtag":tree.sjbtag_leading,
					"SDmass":tree.SDmass_leading
				}

				tVals = {
					"tau1":tree.tau1_subleading,
					"tau2":tree.tau2_subleading,
					"tau3":tree.tau3_subleading,
					"phi":tree.phi_subleading,
					"mass":tree.mass_subleading,
					"pt":tree.pt_subleading,
					"eta":tree.eta_subleading,
					"sjbtag":tree.sjbtag_subleading,
					"SDmass":tree.SDmass_subleading
				}

			elif hemis == 'hemis1' and doneAlready == True:
				continue

			if tVals['tau2'] <= 0 or wVals['tau1'] <= 0:
				continue

			# Define variables
			tjet = TLorentzVector()
			tjet.SetPtEtaPhiM(tVals["pt"],tVals["eta"],tVals["phi"],tVals["mass"])
			wjet = TLorentzVector()
			wjet.SetPtEtaPhiM(wVals["pt"],wVals["eta"],wVals["phi"],wVals["mass"])

			dy_val = abs(tjet.Rapidity()-wjet.Rapidity())
			ht = tjet.Perp() + wjet.Perp()
			tau32val = tVals["tau3"]/tVals['tau2']
			tau21val = wVals["tau2"]/wVals['tau1']
			SJ_csvval = tVals["sjbtag"]

			# Define cuts
			wpt_cut = Cuts['wpt'][0]<wjet.Perp()<Cuts['wpt'][1]
			tpt_cut = Cuts['tpt'][0]<tjet.Perp()<Cuts['tpt'][1]
			dy_cut = Cuts['dy'][0]<=dy_val<Cuts['dy'][1]
			tmass_cut = Cuts['tmass'][0]<tVals["SDmass"]<Cuts['tmass'][1]
			ht_cut = ht > 1100.0			
			tau21_cut =  Cuts['tau21'][0]<=tau21val<Cuts['tau21'][1]
			tau32_cut =  Cuts['tau32'][0]<=tau32val<Cuts['tau32'][1]
			sjbtag_cut = Cuts['sjbtag'][0]<SJ_csvval<=Cuts['sjbtag'][1]
			if type(Cuts['wmass'][0]) is float:
				wmass_cut = Cuts['wmass'][0]<=wVals["SDmass"]<Cuts['wmass'][1]
			elif type(Cuts['wmass'][0]) is list:
				wmass_cut = Cuts['wmass'][0][0]<=wVals["SDmass"]<Cuts['wmass'][0][1] or Cuts['wmass'][1][0]<=wVals["SDmass"]<Cuts['wmass'][1][1] 
			else:
				print "wmass type error" 
				continue

			if wpt_cut and tpt_cut and dy_cut and tmass_cut and wmass_cut and ht_cut:
				Tau32vsTau21.Fill(tau21val,tau32val)

				tempVars = {"tau32":tau32val,"tau21":tau21val}

				for key in treeVars.keys():
					treeVars[key][0] = tempVars[key]
				try:
					newTree.Fill()
				except:
					print "Failure at " + str(count)

				doneAlready = True

c1 = TCanvas('c1','c1', 600, 600)
Tau32vsTau21.Draw()
c1.Print("Nsubjetiness.pdf",'pdf')