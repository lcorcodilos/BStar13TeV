import ROOT
import subprocess

from ROOT import *

commands = []

HTpoints = ['700','1000','1500','2000']

for point in HTpoints:
	commands.append('rm TWanalyzerQCDHT'+point+'_Trigger_nominal_nonepileup_unweighted_PSET_default.root')
	commands.append('rm TWanalyzerQCDHT'+point+'_Trigger_nominal_none_PSET_default.root')
	commands.append('hadd TWanalyzerQCDHT'+point+'_Trigger_nominal_nonepileup_unweighted_PSET_default.root TWanalyzerQCDHT'+point+'_Trigger_nominal_nonepileup_unweighted_job*_PSET_default.root')
	commands.append('hadd TWanalyzerQCDHT'+point+'_Trigger_nominal_none_PSET_default.root TWanalyzerQCDHT'+point+'_Trigger_nominal_none_job*_PSET_default.root')

commands.append('rm TWanalyzerQCD_Trigger_nominal_nonepileup_unweighted_PSET_default.root')
commands.append('rm TWanalyzerQCD_Trigger_nominal_none_PSET_default.root')

commands.append('hadd TWanalyzerQCD_Trigger_nominal_nonepileup_unweighted_PSET_default.root TWanalyzerQCDHT*_Trigger_nominal_nonepileup_unweighted_PSET_default.root')
commands.append('hadd TWanalyzerQCD_Trigger_nominal_none_PSET_default.root TWanalyzerQCDHT*_Trigger_nominal_none_PSET_default.root')

commands.append('rm output_*.log')
#commands.append('rm *job*.root')

for s in commands :
	print 'executing ' + s
	subprocess.call( [s], shell=True )

frate = TFile('TWanalyzerQCD_Trigger_nominal_nonepileup_unweighted_PSET_default.root')
fana = TFile('TWanalyzerQCD_Trigger_nominal_none_PSET_default.root')

hrate = frate.Get('Mtw')

hana = fana.Get('Mtw')

c = TCanvas('c','c',1400,700)
c.Divide(2)

c.cd(1)
hrate.Draw()

c.cd(2)
hana.Draw()

# hrates = []
# hanas = []

# for i in range(1,9):
# 	hrates.append(frate.Get('Mtw_cut'+str(i)))
# 	hanas.append(fana.Get('Mtw_cut'+str(i)))


# c1 = TCanvas('c1','c1',1800,1000)
# c1.Divide(4,2)

# for i in range(4):
# 	c1.cd(i+1)
# 	hrates[i].Draw()

# for i in range(4):
# 	c1.cd(i+5)
# 	hanas[i].Draw()

# c2 = TCanvas('c2','c2',1800,1000)
# c2.Divide(4,2)

# for i in range(4,8):
# 	c2.cd(i-3)
# 	hrates[i].Draw()

# for i in range(4,8):
# 	c2.cd(i+1)
# 	hanas[i].Draw()

raw_input('holding')
