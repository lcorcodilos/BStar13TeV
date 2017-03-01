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
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -v analyzer -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 1  -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 2  -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 3  -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 4  -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 5  -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 6  -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 7  -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 8  -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 9  -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 10 -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 11 -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 12 -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 13 -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 14 -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 15 -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 16 -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 17 -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 18 -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 19 -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s data -j 20 -n 20 -g on -v analyzer -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -j 2 -n 1 -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -j 2 -n 1 -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -j 2 -n 1 -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -j 2 -n 1 -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -j 2 -n 1 -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -j 2 -n 2 -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -j 2 -n 2 -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -j 2 -n 2 -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -j 2 -n 2 -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -j 2 -n 2 -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -j 2 -n 1 -g on -v analyzer  -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -j 2 -n 1 -g on -v analyzer  -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -j 2 -n 1 -g on -v analyzer  -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -j 2 -n 1 -g on -v analyzer  -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -j 2 -n 1 -g on -v analyzer  -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -j 2 -n 2 -g on -v analyzer  -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -j 2 -n 2 -g on -v analyzer  -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -j 2 -n 2 -g on -v analyzer  -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -j 2 -n 2 -g on -v analyzer  -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -j 2 -n 2 -g on -v analyzer  -c sideband -y up
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -j 2 -n 1 -g on -v analyzer  -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -j 2 -n 1 -g on -v analyzer  -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -j 2 -n 1 -g on -v analyzer  -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -j 2 -n 1 -g on -v analyzer  -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -j 2 -n 1 -g on -v analyzer  -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT500 -j 2 -n 2 -g on -v analyzer  -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT700 -j 2 -n 2 -g on -v analyzer  -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1000 -j 2 -n 2 -g on -v analyzer  -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT1500 -j 2 -n 2 -g on -v analyzer  -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s QCDHT2000 -j 2 -n 2 -g on -v analyzer  -c sideband -y down
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_s -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_t -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s singletop_tB -g on -v analyzer  -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbarscaleup -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbarscaledown -g on -v analyzer -c sideband
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband -J up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband -J down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband -R up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband -R down
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband -x up
output_$(JID)        python ./tardir/TWanalyzer.py -s ttbar -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1400 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1600 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH1800 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2000 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2200 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2400 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2600 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH2800 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalLH3000 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1200 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1400 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1600 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH1800 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2000 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2200 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2400 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2600 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH2800 -g on -v analyzer -c sideband -x down
output_$(JID)        python ./tardir/TWanalyzer.py -s signalRH3000 -g on -v analyzer -c sideband -x down

