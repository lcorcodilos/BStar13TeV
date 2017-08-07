fileNoJobs = raw_input("Please input the python command without the number of jobs to be split: ")
nJobs = int(raw_input("Please input the number of jobs you'd like to split the command into: "))

for i in range(nJobs):
	print fileNoJobs + " -n " + str(i+1) + " -j " + str(nJobs)
