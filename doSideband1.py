import Bstar_Functions	
from Bstar_Functions import WaitForJobs

import subprocess

subprocess.call(['sh grid_tagrate_sub.csh'], shell=True)
WaitForJobs('tagrate')

commands1 = []

commands1.append('python grid_tagrate_post.py -c rate_sideband1')

commands1.append('python TWrate_Maker.py -s QCD -c rate_sideband1')

commands1.append('python TWrate_Maker.py -s data -c rate_sideband1')

commands1.append('python TWrate_plotter.py -s QCD -c rate_sideband1')

commands1.append('python TWrate_plotter.py -s data -c rate_sideband1')

for s in commands1 :
	print 'executing ' + s
	subprocess.call( [s], shell=True )

subprocess.call(['sh grid_analyzer_sub.csh'], shell=True)
WaitForJobs('ana')

commands2 = []

commands2.append('python grid_analyzer_post.py -c sideband1')
commands2.append('cd rootfiles/35851pb/')
commands2.append('python MakeVectorLike.py -c sideband1')
commands2.append('cd ../../')

# commands2.append('python PtReweightStudy.py')

commands2.append('python TWanalyzer_plotter.py -s QCD -c sideband1 -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s data -c sideband1 -v kinematics')

for s in commands2 :
	print 'executing ' + s
	subprocess.call( [s], shell=True )