#! /bin/sh
tar czvf tarball.tgz Alphabet/fn_bstar*.txt fitdata/ Tagrate*2D*.root rootlogon.C TWanalyzer.py ModMassFile_*.root TWsequencer.py Bstar_Functions.py Triggerweight_data80X.root PileUp_Ratio_ttbar.root PileUp_Ratio_signalLH*.root PileUp_Ratio_signalRH*.root
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \ana.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
