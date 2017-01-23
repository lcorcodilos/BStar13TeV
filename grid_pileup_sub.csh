tar czvf tarball.tgz TWPileup.py Bstar_Functions.py rootlogon.C TWTrigger.py
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \pile.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
