#! /bin/sh
python Flist.py
tar czvf tarball.tgz Files*.txt TWPileup.py Bstar_Functions.py rootlogon.C
mv Files*.txt txt_temp
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \pile.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
