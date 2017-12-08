# python doAlphabet.py -c default -s QCD -f lin -m on -e on -C off -d on
# python doAlphabet.py -c default -s QCD -f lin -m on -e on -C on -d on
# python doAlphabet.py -c default -s QCD -f lin -m on -e on -C narrow -d on

python doAlphabet.py -c default -s QCD -C narrow -f lin -m on -e off -d off
python doAlphabet.py -c sideband -s QCD -C narrow -f lin -m on -e off -d off
python doAlphabet.py -c rate_default -s QCD -C narrow -f lin -m on -e off -d off

# python doAlphabet.py -c default -s data -C on
# python doAlphabet.py -c sideband -s data -C on
# python doAlphabet.py -c rate_default -s data -C on

