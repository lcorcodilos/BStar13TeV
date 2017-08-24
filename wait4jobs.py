import os.path
import subprocess
import sys
import time

from optparse import OptionParser

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
				  default	=	'ptcorr',
				  dest		=	'set',
				  help		=	'Whatever comes before .listOfJobs')

(options, args) = parser.parse_args()


# Runs grep to count the number of jobs - output will have non-digit characters b/c of wc
numberOfJobs = subprocess.check_output('grep "python" '+options.set+'.listOfJobs | wc -l', shell=True)
# Get rid of non-digits and convert to an int
numberOfJobs = int(filter(lambda x: x.isdigit(), numberOfJobs))

finishedJobs = 0
# Rudementary progress bar
while finishedJobs < numberOfJobs:
	# Count how many output files there are to see how many jobs finished
	finishedJobs = subprocess.check_output('ls output_*.log | wc -l', shell=True)
	finishedJobs = int(filter(lambda x: x.isdigit(), finishedJobs))
	# Print the count out
	sys.stdout.write("%i / %i finished...\r" % (finishedJobs,numberOfJobs))
	# Clear the buffer
	sys.stdout.flush()
	# Sleep for one second
	time.sleep(1)


print 'Jobs completed. Checking for errors...'
numberOfTracebacks = subprocess.check_output('grep -i "Traceback" output*.log | wc -l', shell=True)
numberOfSyntax = subprocess.check_output('grep -i "Syntax" output*.log | wc -l', shell=True)

numberOfTracebacks = int(filter(lambda x: x.isdigit(), numberOfTracebacks))
numberOfSyntax = int(filter(lambda x: x.isdigit(), numberOfSyntax))

# Check there are no syntax or traceback errors
# Future idea - check output file sizes
if numberOfTracebacks > 0:
	print numberOfTracebacks + ' job(s) failed with traceback error'
	quit()
elif numberOfSyntax > 0:
	print numberOfSyntax + ' job(s) failed with syntax error'
	quit()
else:
	print 'No errors!'
