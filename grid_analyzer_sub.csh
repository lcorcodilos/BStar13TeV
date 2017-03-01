#! /bin/sh
python Flist.py
tar czvf tarball.tgz Files*.txt fitdata ModMassFile*.root Tagrate*2D*.root rootlogon.C TWanalyzer.py TWsequencer.py Bstar_Functions.py TWrate.py Triggerweight_data80X.root PileUp_Ratio_ttbar.root PileUp_Ratio_signalLH*.root PileUp_Ratio_signalRH*.root
mv Files*.txt txt_temp
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \ana.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
