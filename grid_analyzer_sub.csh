#! /bin/sh
# python Flist.py
tar czvf tarball.tgz plots/TWrate_Maker*.root bstar_theta_PtSF*.txt Alphabet/fn_bstar*.txt fitdata/*.txt Tagrate*2D*.root rootlogon.C TWanalyzer.py ModMassFile_*.root TWsequencer.py Bstar_Functions.py Triggerweight_2jethack_data.root PileUp_Ratio_ttbar.root
# mv Files*.txt txt_temp
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \ana.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
