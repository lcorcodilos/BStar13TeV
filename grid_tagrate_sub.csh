#! /bin/sh
python Flist.py
tar czvf tarball.tgz Files*.txt ModMassFile.root Bstar_Functions.py rootlogon.C TWrate.py TWsequencer.py TRIG_EFFICWPHTdata_dijet8TeV.root Triggerweight_data80X.root PileUp_Ratio_ttbar.root PileUp_Ratio_signalL*.root PileUp_Ratio_signalR*.root
mv Files*.txt txt_temp
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \tagrate.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
