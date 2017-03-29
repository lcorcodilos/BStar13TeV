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
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 1  -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 2  -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 3  -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 4  -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 5  -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 6  -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 7  -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 8  -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 9  -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 10 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 11 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 12 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 13 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 14 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 15 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 16 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 17 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 18 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 19 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 20 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 21 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 22 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 23 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 24 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s data -n 25 -j 25 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s ttbar -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s QCDHT500 -n 1 -j 2  -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s QCDHT700 -n 1 -j 2  -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s QCDHT1000   -n 1 -j 2  -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s QCDHT1500   -n 1 -j 2  -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s QCDHT2000  -n 1 -j 2  -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s QCDHT500 -n 2 -j 2  -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s QCDHT700 -n 2 -j 2  -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s QCDHT1000   -n 2 -j 2  -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s QCDHT1500   -n 2 -j 2  -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s QCDHT2000  -n 2 -j 2  -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s singletop_s -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s singletop_t -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s singletop_tB -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalRH1200 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalLH1400 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalRH1400 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalLH1600 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalRH1600 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalLH1800 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalRH1800 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalLH2000 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalRH2000 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalLH2200 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalRH2200 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalLH2400 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalRH2400 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalLH2600 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalRH2600 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalLH2800 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalRH2800 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalLH3000 -g on
output_$(JID)        python ./tardir/TWtree_Maker.py -s signalRH3000 -g on

