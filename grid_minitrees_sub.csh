#! /bin/sh
#python Flist.py
tar czvf tarball.tgz Bstar_Functions.py bstar_theta_PtSF*.txt rootlogon.C TWminitrees.py Triggerweight_2jethack_data.root PileUp_Ratio_ttbar.root 
#mv Files*.txt txt_temp
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \minitrees.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
