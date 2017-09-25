#! /bin/sh
tar czvf tarball.tgz THBnpvtester.py Bstar_Functions.py PileUp_Ratio_ttbar.root rootlogon.C
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \npvtest.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi