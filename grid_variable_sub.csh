#! /bin/sh
python Flist.py
tar czvf tarball.tgz Files*.txt ModMassFile*.root rootlogon.C TWvariables.py fitdata TWsequencer.py Bstar_Functions.py Triggerweight_2jethack_data.root PileUp_Ratio_ttbar.root 
mv Files*.txt txt_temp
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \var.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
