import ROOT
from ROOT import *
import subprocess

masses = [1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]

# Get a list of all the LH1200 files
listOfLH1200Files = subprocess.check_output('ls TWanalyzerweightedsignalLH1200_Trigger_nominal_*.root',shell=True)
listOfFileTemplates = []

# Convert into a list generic to hand and mass
for item in listOfLH1200Files.split('\n'):
	newitem = item.replace('LH1200','RHANDRMASS')
	listOfFileTemplates.append(newitem)


# Create a list with all the masses - just call it the left list for now
listOfLeftFiles1 = []
for mass in masses:
	for fileString in listOfFileTemplates:
		listOfLeftFiles1.append(fileString.replace('RMASS',str(mass)))

# Duplicate
listOfRightFiles1 = listOfLeftFiles1

# Specify handedness
listOfLeftFiles1 = [left.replace('RHAND','LH') for left in listOfLeftFiles1]
listOfRightFiles1 = [right.replace('RHAND','RH') for right in listOfRightFiles1]

# Remove empty entries
listOfLeftFiles = list(filter(None, listOfLeftFiles1))
listOfRightFiles = list(filter(None, listOfRightFiles1))


# Cross check
for index in range(len(listOfLeftFiles)):
	if listOfLeftFiles[index].replace('LH','RH') != listOfRightFiles[index]:
		print listOfLeftFiles[index].replace('LH','RH') +' != '+ listOfRightFiles[index]
		break
	# else:
	# 	print listOfLeftFiles[index].replace('LH','RH') +' = '+ listOfRightFiles[index]

# Now hadd
commands = []
commands.append('rm TWanalyzerweightedsignalvector*_Trigger_nominal_*.root')
for index in range(len(listOfLeftFiles)):
	nameVectorFile = listOfLeftFiles[index].replace('LH','vector')
	commands.append('rm ' + nameVectorFile)
	commands.append('hadd ' + nameVectorFile + ' ' + listOfLeftFiles[index] + ' ' + listOfRightFiles[index])


for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )