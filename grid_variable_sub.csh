#! /bin/sh
tar czvf tarball.tgz ModMassFile*.root rootlogon.C TWvariables.py fitdata TWsequencer.py Bstar_Functions.py Triggerweight_data80X.root PileUp_Ratio_ttbar.root PileUp_Ratio_signal*.root 
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \var.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
