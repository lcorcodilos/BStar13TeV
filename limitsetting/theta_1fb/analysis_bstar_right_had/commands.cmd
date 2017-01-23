# -*- sh -*- # for font lock mode
# variable definitions
- env = cd /uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/BStar13TeV/limitsetting/theta/analysis_bstar_right_had; eval `scramv1 runtime -sh`; cd -
- tag = 
- output = outputFile=
- tagmode = none
- tarfile = /uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/BStar13TeV/limitsetting/theta/analysis_bstar_right_had/analysis.tgz
- untardir = tardir
- copycommand = cp

# Sections listed
output_$(JID)        source ./tardir/thetaGridbs.sh 0
output_$(JID)        source ./tardir/thetaGridbs.sh 1
output_$(JID)        source ./tardir/thetaGridbs.sh 2
output_$(JID)        source ./tardir/thetaGridbs.sh 3
output_$(JID)        source ./tardir/thetaGridbs.sh 4
output_$(JID)        source ./tardir/thetaGridbs.sh 5

