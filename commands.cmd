# -*- sh -*- # for font lock mode
# variable definitions
- env = export SCRAM_ARCH=slc6_amd64_gcc491; eval `scramv1 project CMSSW CMSSW_7_4_1` ; cd CMSSW_7_4_1/src ; eval `scramv1 runtime -sh`; cd -
- tag = 
- output = outputFile=
- tagmode = none
- tarfile = /uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/BStar13TeV/tarball.tgz
- untardir = tardir
- copycommand = cp

# Sections listed
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -A on -v analyzer -c default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -A on -v analyzer -c default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c default -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c default -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c default -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c default -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c default -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c default -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c default -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c default -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c default -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c default -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c default -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c default -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c default -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c default -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbarscaleup -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbarscaledown -g on -A on -v analyzer -c default
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -A on -v analyzer -c rate_default -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -A on -v analyzer -c rate_default -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c rate_default -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c rate_default -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c rate_default -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c rate_default -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c rate_default -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbarscaleup -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbarscaledown -g on -A on -v analyzer -c rate_default
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c rate_default -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -A on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -A on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -A on -c sideband -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -A on -c sideband -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -A on -c sideband -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -A on -c sideband -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -A on -c sideband -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbarscaleup -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbarscaledown -g on -A on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -A on -v analyzer  -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -A on -v analyzer  -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -A on -v analyzer  -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -A on -v analyzer  -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -A on -v analyzer -c sideband -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -A on -v analyzer -c sideband -p down

