import Bstar_Functions	
from Bstar_Functions import WaitForJobs

import subprocess

subprocess.call(['sh grid_tagrate_sub.csh'], shell=True)
WaitForJobs('tagrate')

commands1 = []

commands1.append('python grid_tagrate_post.py -c rate_default')
commands1.append('python grid_tagrate_post.py -c rate_sideband')
commands1.append('python grid_tagrate_post.py -c rate_sideband1')


commands1.append('python TWrate_Maker.py -s QCD -c rate_default')
commands1.append('python TWrate_Maker.py -s QCD -c rate_sideband')
commands1.append('python TWrate_Maker.py -s QCD -c rate_sideband1')
commands1.append('python TWrate_Maker.py -s QCD -c rate_sideband1 -u off')
commands1.append('python TWrate_Maker.py -s QCD -c rate_sideband1 --noExtraPtCorrection')


commands1.append('python TWrate_Maker.py -s data -c rate_default')
commands1.append('python TWrate_Maker.py -s data -c rate_sideband')
commands1.append('python TWrate_Maker.py -s data -c rate_sideband1')
commands1.append('python TWrate_Maker.py -s data -c rate_sideband1 -u off')
commands1.append('python TWrate_Maker.py -s data -c rate_sideband1 --noExtraPtCorrection')



commands1.append('python TWrate_plotter.py -s QCD -c rate_default')
commands1.append('python TWrate_plotter.py -s QCD -c rate_sideband')
commands1.append('python TWrate_plotter.py -s QCD -c rate_sideband1')

commands1.append('python TWrate_plotter.py -s data -c rate_default')
commands1.append('python TWrate_plotter.py -s data -c rate_sideband')
commands1.append('python TWrate_plotter.py -s data -c rate_sideband1')

for s in commands1 :
	print 'executing ' + s
	subprocess.call( [s], shell=True )


subprocess.call(["sed -i '' 's/anaAlpha.listOfJobs/ana.listOfJobs/g' grid_analyzer_sub.csh"], shell=True)
subprocess.call(['sh grid_analyzer_sub.csh'], shell=True)
WaitForJobs('ana')

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
