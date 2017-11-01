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
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 1 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 2 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 3 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 4 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 5 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 6 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 7 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 8 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 9 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 10 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 11 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 12 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 13 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 14 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 15 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 16 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 17 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 18 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 19 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_default -n 20 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s ttbar -g on -c rate_default
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT500 -g on -c rate_default
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT700 -g on -c rate_default
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT1000 -g on -c rate_default
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT1500 -g on -c rate_default
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT2000 -g on -c rate_default
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_t -g on -c rate_default
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tB -g on -c rate_default
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tW -g on -c rate_default
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tWB -g on -c rate_default
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 1 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 2 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 3 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 4 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 5 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 6 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 7 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 8 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 9 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 10 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 11 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 12 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 13 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 14 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 15 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 16 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 17 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 18 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 19 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband -n 20 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s ttbar -g on -c rate_sideband
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT500 -g on -c rate_sideband
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT700 -g on -c rate_sideband
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT1000 -g on -c rate_sideband
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT1500 -g on -c rate_sideband
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT2000 -g on -c rate_sideband
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_t -g on -c rate_sideband
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tB -g on -c rate_sideband
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tW -g on -c rate_sideband
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tWB -g on -c rate_sideband
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 1 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 2 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 3 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 4 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 5 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 6 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 7 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 8 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 9 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 10 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 11 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 12 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 13 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 14 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 15 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 16 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 17 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 18 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 19 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c rate_sideband1 -n 20 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s ttbar -g on -c rate_sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT500 -g on -c rate_sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT700 -g on -c rate_sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT1000 -g on -c rate_sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT1500 -g on -c rate_sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT2000 -g on -c rate_sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_t -g on -c rate_sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tB -g on -c rate_sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tW -g on -c rate_sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tWB -g on -c rate_sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 1 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 2 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 3 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 4 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 5 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 6 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 7 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 8 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 9 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 10 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 11 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 12 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 13 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 14 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 15 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 16 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 17 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 18 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 19 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c default -n 20 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s ttbar -g on -c default
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT500 -g on -c default
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT700 -g on -c default
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT1000 -g on -c default
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT1500 -g on -c default
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT2000 -g on -c default
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_t -g on -c default
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tB -g on -c default
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tW -g on -c default
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tWB -g on -c default
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 1 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 2 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 3 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 4 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 5 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 6 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 7 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 8 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 9 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 10 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 11 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 12 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 13 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 14 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 15 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 16 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 17 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 18 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 19 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband -n 20 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s ttbar -g on -c sideband
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT500 -g on -c sideband
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT700 -g on -c sideband
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT1000 -g on -c sideband
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT1500 -g on -c sideband
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT2000 -g on -c sideband
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_t -g on -c sideband
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tB -g on -c sideband
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tW -g on -c sideband
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tWB -g on -c sideband
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 1 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 2 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 3 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 4 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 5 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 6 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 7 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 8 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 9 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 10 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 11 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 12 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 13 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 14 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 15 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 16 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 17 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 18 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 19 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s data -g on -c sideband1 -n 20 -j 20
output_$(JID)        python ./tardir/TWminitrees.py -s ttbar -g on -c sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT500 -g on -c sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT700 -g on -c sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT1000 -g on -c sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT1500 -g on -c sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s QCDHT2000 -g on -c sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_t -g on -c sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tB -g on -c sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tW -g on -c sideband1
output_$(JID)        python ./tardir/TWminitrees.py -s singletop_tWB -g on -c sideband1

