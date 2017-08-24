
python Flist.py
tar czvf tarball.tgz Files*.txt TWTopPtSF.root plots/TWrate_Maker*.root fitdata/*.txt Tagrate*2D*.root rootlogon.C TWanalyzer.py ModMassFile_*.root Bstar_Functions.py Triggerweight_2jethack_data.root PileUp_Ratio_ttbar.root
mv Files*.txt txt_temp
./development/runManySections.py --createCommandFile --cmssw --addLog --setTarball=tarball.tgz \ptcorr.listOfJobs commands.cmd
./runManySections.py --submitCondor commands.cmd
condor_q lcorcodi
