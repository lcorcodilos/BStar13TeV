#! /bin/sh
python Flist.py
tar czvf tarball.tgz Files*.txt rootlogon.C TWTrigger.py Bstar_Functions.py
mv Files*.txt txt_temp
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \trig.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
