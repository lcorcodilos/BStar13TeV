python grid_analyzer_post.py -c default
cd rootfiles/35851pb/
python MakeVectorLike.py -c default
cd ../../

python grid_analyzer_post.py -c sideband
cd rootfiles/35851pb/
python MakeVectorLike.py -c sideband
cd ../../

python grid_analyzer_post.py -c sideband1
cd rootfiles/35851pb/
python MakeVectorLike.py -c sideband1
cd ../../

python PtReweightStudy.py

python TWanalyzer_plotter.py -s QCD -c default -v kinematics
python TWanalyzer_plotter.py -s QCD -c default
python TWanalyzer_plotter.py -s data -b on -c default -v kinematics
python TWanalyzer_plotter.py -s QCD -c sideband -v kinematics
python TWanalyzer_plotter.py -s data -c sideband -v kinematics
python TWanalyzer_plotter.py -s QCD -c sideband1 -v kinematics
python TWanalyzer_plotter.py -s data -c sideband1 -v kinematics
