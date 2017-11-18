import Bstar_Functions	
from Bstar_Functions import WaitForJobs

import subprocess

subprocess.call(['sh grid_minitrees_sub.csh'], shell=True)
WaitForJobs('minitrees')

commands2 = []

commands2.append('python grid_minitrees_post.py -c default')
commands2.append('python grid_minitrees_post.py -c sideband')
commands2.append('python grid_minitrees_post.py -c sideband1')

commands2.append('python grid_minitrees_post.py -c rate_default')
commands2.append('python grid_minitrees_post.py -c rate_sideband')
commands2.append('python grid_minitrees_post.py -c rate_sideband1')

for s in commands2 :
	print 'executing ' + s
	subprocess.call( [s], shell=True )
