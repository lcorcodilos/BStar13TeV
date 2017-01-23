# -*- sh -*- # for font lock mode
# variable definitions
- env = cd /uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/BStar13TeV; eval `scramv1 runtime -sh`; cd -
- tag = 
- output = outputFile=
- tagmode = none
- tarfile = /uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/BStar13TeV/tarball.tgz
- untardir = tardir
- copycommand = cp

# Sections listed
output_$(JID)        python ./tardir/TWvariables.py -s data -j 5 -n 1 -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s data -j 5 -n 2 -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s data -j 5 -n 3 -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s data -j 5 -n 4 -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s data -j 5 -n 5 -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s ttbar  -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s singletop_tW -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s singletop_tWB -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s signalLH1200 -g on  -c default
output_$(JID)        python ./tardir/TWvariables.py -s signalLH1400 -g on  -c default
output_$(JID)        python ./tardir/TWvariables.py -s signalLH1600 -g on  -c default
output_$(JID)        python ./tardir/TWvariables.py -s signalLH1800 -g on  -c default
output_$(JID)        python ./tardir/TWvariables.py -s signalLH2000 -g on  -c default
output_$(JID)        python ./tardir/TWvariables.py -s signalLH2200 -g on  -c default
output_$(JID)        python ./tardir/TWvariables.py -s signalLH2400 -g on  -c default
output_$(JID)        python ./tardir/TWvariables.py -s signalLH2600 -g on  -c default
output_$(JID)        python ./tardir/TWvariables.py -s signalLH2800 -g on  -c default
output_$(JID)        python ./tardir/TWvariables.py -s signalLH3000 -g on  -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT500 -j 3 -n 1   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT700 -j 3 -n 1   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT1000 -j 3 -n 1   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT1500 -j 3 -n 1   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT2000 -j 3 -n 1   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT500 -j 3 -n 2   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT700 -j 3 -n 2   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT1000 -j 3 -n 2   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT1500 -j 3 -n 2   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT2000 -j 3 -n 2   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT500 -j 3 -n 3   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT700 -j 3 -n 3   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT1000 -j 3 -n 3   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT1500 -j 3 -n 3   -g on -c default
output_$(JID)        python ./tardir/TWvariables.py -s QCDHT2000 -j 3 -n 3   -g on -c default

