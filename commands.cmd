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

