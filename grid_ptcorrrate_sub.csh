
python Flist.py
tar czf tarball.tgz Files*.txt TWTopPtSF_*.root rootlogon.C TWrate.py Bstar_Functions.py Triggerweight_2jethack_data.root PileUp_Ratio_ttbar.root
mv Files*.txt txt_temp
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \ptcorrrate.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
