import Bstar_Functions	
from Bstar_Functions import WaitForJobs

import subprocess

commands1 = []
commands1.append('cd Alphabet')

commands1.append('rm results/*')
commands1.append('python Bstar_Alphabet.py -s QCD -p 800,1200')
commands1.append('python Bstar_Alphabet.py -s QCD -p 1200,1500')
commands1.append('python Bstar_Alphabet.py -s QCD -p 1500,3000')
commands1.append('python Bstar_Alphabet.py -s data -p 800,1200')
commands1.append('python Bstar_Alphabet.py -s data -p 1200,1500')
commands1.append('python Bstar_Alphabet.py -s data -p 1500,3000')



for s in commands1 :
	print 'executing ' + s
	subprocess.call( [s], shell=True )

subprocess.call(["sed 's/-g on/-g on -A on/g' ana.listOfJobs > anaAlpha.listOfJobs"], shell=True)
subprocess.call(["sed -i '' 's/ana.listOfJobs/anaAlpha.listOfJobs/g' grid_analyzer_sub.csh"], shell=True)
subprocess.call(['sh grid_analyzer_sub.csh'], shell=True)
WaitForJobs('anaAlpha')

commands2 = []

commands2.append('python grid_analyzer_post.py -c default')
commands2.append('python grid_analyzer_post.py -c sideband')
commands2.append('python grid_analyzer_post.py -c sideband1')

commands2.append('cd rootfiles/35851pb/')
commands2.append('python MakeVectorLike.py')

commands2.append('python TWanalyzer_plotter.py -s QCD -c default -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s QCD -c default')
commands2.append('python TWanalyzer_plotter.py -s data -b on -c default -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s QCD -c sideband -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s data -c sideband -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s QCD -c sideband1 -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s data -c sideband1 -v kinematics')
commands2.append('python TWanalyzer_plotter.py -s data -c sideband1 -v kinematics -u off')
commands2.append('python TWanalyzer_plotter.py -s data -c sideband1 -v kinematics --noExtraPtCorrection')


for s in commands2 :
	print 'executing ' + s
	subprocess.call( [s], shell=True )
