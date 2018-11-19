import Bstar_Functions	
from Bstar_Functions import WaitForJobs

import subprocess

# commands1 = []
# commands1.append('cd Alphabet/')
# commands1.append('source allAlpha.csh')
# commands1.append('cd ../')
# for s in commands1 :
#	print 'executing ' + s
#	subprocess.call( [s], shell=True )

#subprocess.call(["sed 's/-g on/-g on -A on/g' ana.listOfJobs > anaAlpha.listOfJobs"], shell=True)
#subprocess.call(["sed -i 's/ana.listOfJobs/anaAlpha.listOfJobs/g' grid_analyzer_sub.csh"], shell=True)
#subprocess.call(['sh grid_analyzer_sub.csh'], shell=True)
#WaitForJobs('anaAlpha')

commands2 = []

commands2.append('python grid_analyzer_post.py -c default -A on')
commands2.append('python grid_analyzer_post.py -c sideband -A on')
commands2.append('python grid_analyzer_post.py -c rate_default -A on')

# commands2.append('cd rootfiles/35851pb/')
# commands2.append('python MakeVectorLike.py')

commands2.append('python TWanalyzer_plotter.py -s QCD -A on -c default -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s QCD -A on -c default')
commands2.append('python TWanalyzer_plotter.py -s data -A on -b on -c default -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s QCD -A on -c sideband -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s data -A on -c sideband -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s QCD -A on -c rate_default -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s data -A on -c rate_default -v kinematics')
# commands2.append('python TWanalyzer_plotter.py -s QCD -c sideband1 -v kinematics')
# commands2.append('python TWanalyzer_plotter.py -s data -c sideband1 -v kinematics')
# commands2.append('python TWanalyzer_plotter.py -s data -c sideband1 -v kinematics -u off')
# commands2.append('python TWanalyzer_plotter.py -s data -c sideband1 -v kinematics --noExtraPtCorrection')


for s in commands2 :
	print 'executing ' + s
	subprocess.call( [s], shell=True )
