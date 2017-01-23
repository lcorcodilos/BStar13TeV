#! /bin/sh
tar czvf tarball.tgz rootlogon.C EventCounter.py Bstar_Functions.py 
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \count.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
