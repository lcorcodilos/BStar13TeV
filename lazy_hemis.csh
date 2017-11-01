python TWrate_Maker.py -s QCD -c rate_default -H H0
python TWrate_Maker.py -s QCD -c rate_default -H H1

python TWrate_Maker.py -s QCD -c rate_sideband -H H0
python TWrate_Maker.py -s QCD -c rate_sideband -H H1

python TWrate_Maker.py -s QCD -c rate_sideband1 -H H0
python TWrate_Maker.py -s QCD -c rate_sideband1 -H H1

python TWrate_Maker.py -s data -c rate_default -H H0
python TWrate_Maker.py -s data -c rate_default -H H1

python TWrate_Maker.py -s data -c rate_sideband -H H0
python TWrate_Maker.py -s data -c rate_sideband -H H1

python TWrate_Maker.py -s data -c rate_sideband1 -H H0
python TWrate_Maker.py -s data -c rate_sideband1 -H H1