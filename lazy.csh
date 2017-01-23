#python TWrate_Maker.py -s QCD -c rate_default
#python TWrate_Maker.py -s QCD -c rate_sideband
#python TWrate_Maker.py -s data -c rate_default
#python TWrate_Maker.py -s data -c rate_sideband

#python TWrate_plotter.py -s QCD -c rate_default
#python TWrate_plotter.py -s QCD -c rate_sideband
#python TWrate_plotter.py -s data -c rate_default
#python TWrate_plotter.py -s data -c rate_sideband

python TWanalyzer_plotter.py -s QCD -c default
python TWanalyzer_plotter.py -s QCD -c sideband
python TWanalyzer_plotter.py -s data -c sideband
