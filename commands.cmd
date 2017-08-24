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
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -v analyzer -c sideband1 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -v analyzer -c sideband1 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 1 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 2 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 3 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 4 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 5 -j 5
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 1 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 2 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 3 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 4 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 5 -j 5 -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 1 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 2 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 3 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 4 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -g on -c sideband1 -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -g on -c sideband1 -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -g on -c sideband1 -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -g on -c sideband1 -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -g on -c sideband1 -n 5 -j 5 -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -v analyzer  -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -v analyzer  -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -v analyzer  -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -v analyzer  -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 --noExtraPtCorrection
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbarscaleup -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbarscaledown -g on -v analyzer -c sideband1
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -v analyzer  -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -v analyzer  -c sideband1  -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -v analyzer  -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -v analyzer  -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1 -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -v analyzer  -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -v analyzer  -c sideband1   -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -v analyzer  -c sideband1  -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -v analyzer  -c sideband1  -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1 -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -v analyzer  -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -v analyzer  -c sideband1   -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -v analyzer  -c sideband1  -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -v analyzer  -c sideband1  -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1 -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -v analyzer  -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -v analyzer  -c sideband1   -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -v analyzer  -c sideband1  -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -v analyzer  -c sideband1  -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1 -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -v analyzer  -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -v analyzer  -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -v analyzer  -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -v analyzer  -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1 -a up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -v analyzer  -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -v analyzer  -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -v analyzer  -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -v analyzer  -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1 -a down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -v analyzer  -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -v analyzer  -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -v analyzer  -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -v analyzer  -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1 -b up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -v analyzer  -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -v analyzer  -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -v analyzer  -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -v analyzer  -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1 -b down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -v analyzer  -c sideband1  -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -v analyzer  -c sideband1   -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -v analyzer  -c sideband1  -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -v analyzer  -c sideband1   -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1 -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tW -g on -v analyzer  -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tWB -g on -v analyzer  -c sideband1  -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -v analyzer  -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -v analyzer  -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1 -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1 -p up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1200 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband1 -p down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband1 -p down

