import Bstar_Functions	
from Bstar_Functions import WaitForJobs

import subprocess

subprocess.call(['sh grid_analyzer_sub.csh'], shell=True)
WaitForJobs('ana')

commands2 = []

commands2.append('python grid_analyzer_post.py -c default')
commands2.append('cd rootfiles/35851pb/')
commands2.append('cd ../../')

commands2.append('python grid_analyzer_post.py -c sideband')
commands2.append('cd rootfiles/35851pb/')
commands2.append('cd ../../')

commands2.append('python grid_analyzer_post.py -c sideband1')
commands2.append('cd rootfiles/35851pb/')
commands2.append('python MakeVectorLike.py')
commands2.append('cd ../../')

#commands2.append('python PtReweightStudy.py')

commands2.append('python TWanalyzer_plotter.py -s QCD -c default -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s QCD -c default')
commands2.append('python TWanalyzer_plotter.py -s data -b on -c default -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s QCD -c sideband -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s data -c sideband -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s QCD -c sideband1 -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s data -c sideband1 -v kinematics')

for s in commands2 :
	print 'executing ' + s
	subprocess.call( [s], shell=True )
