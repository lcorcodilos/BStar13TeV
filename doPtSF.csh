python TWanalyzer_QCDorganizer.py
cd limitsetting/theta/BStarCombination/
python PrepareQCDHistsForCombination.py -t _nottsub
python PrepareQCDHistsForCombination.py -t _doublettsub
cp 35851pb/*.root ../
cd ..
python bstar_prepforTheta.py
python run_theta_mt.py
python bstar_PtSF.py
cd ../../
