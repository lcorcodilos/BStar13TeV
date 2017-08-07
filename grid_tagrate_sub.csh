#! /bin/sh
python Flist.py
tar czvf tarball.tgz Files*.txt Bstar_Functions.py rootlogon.C TWrate.py TWsequencer.py Triggerweight_2jethack_data.root PileUp_Ratio_ttbar.root 
mv Files*.txt txt_temp
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \tagrate.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
