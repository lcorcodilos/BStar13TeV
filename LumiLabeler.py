import Bstar_Functions	
from Bstar_Functions import *

Cons = LoadConstants()
lumi = Cons['lumi']
Lumi = str(int(lumi/1000)) + 'fb'

files = [
	'TWanalyzerQCD_Trigger_nominal_none_PSET_default.root',
	'TWanalyzerweightedsignalright1200_Trigger_nominal_none_PSET_default.root',
	'TWanalyzerweightedsignalright1600_Trigger_nominal_none_PSET_default.root',
	'TWanalyzerweightedsignalright2000_Trigger_nominal_none_PSET_default.root',
	#'TWanalyzerdata_Trigger_none_none_PSET_default.root',
	'TWanalyzerweightedttbar_Trigger_nominal_none_PSET_default.root'
	]


commands = []

for f in files
	commands.append('mv ' + f + '/'+Lumi)

for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )