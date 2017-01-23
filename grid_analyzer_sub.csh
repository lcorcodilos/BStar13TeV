#! /bin/sh
tar czvf tarball.tgz fitdata ModMassFile*.root Tagrate*2D*.root rootlogon.C TWanalyzer.py TWsequencer.py Bstar_Functions.py TWrate.py Triggerweight_data80X.root PileUp_Ratio_ttbar.root PileUp_Ratio_signalLH*.root PileUp_Ratio_signalRH*.root
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \ana.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi