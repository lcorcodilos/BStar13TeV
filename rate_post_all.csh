python grid_tagrate_post.py -c rate_default
python grid_tagrate_post.py -c rate_sideband
python grid_tagrate_post.py -c rate_sideband1


python TWrate_Maker.py -s QCD -c rate_default
python TWrate_Maker.py -s QCD -c rate_sideband
python TWrate_Maker.py -s QCD -c rate_sideband1

python TWrate_Maker.py -s data -c rate_default
python TWrate_Maker.py -s data -c rate_sideband
python TWrate_Maker.py -s data -c rate_sideband1

python TWrate_plotter.py -s QCD -c rate_default
python TWrate_plotter.py -s QCD -c rate_sideband
python TWrate_plotter.py -s QCD -c rate_sideband1

python TWrate_plotter.py -s data -c rate_default
python TWrate_plotter.py -s data -c rate_sideband
python TWrate_plotter.py -s data -c rate_sideband1
