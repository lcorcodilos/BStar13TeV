# -*- coding: utf-8 -*-
import scipy.interpolate


def histogram_filter(name):
    value = True
    if "tW" in name and "Q2" in name:
    	value = False
    return value

def external_to_internal(hname):
    m = {'bs1200': 'bs1200','bs1400': 'bs1400', 'bs1600':'bs1600', 'bs1800':'bs1800', 'bs2000':'bs2000', 'bs2200':'bs2200', 'bs2400':'bs2400', 'bs2600':'bs2600', 'bs2800':'bs2800', 'bs3000':'bs3000'}
    for old_pname in m:
        if ('__' + old_pname) in hname: hname = hname.replace('__' + old_pname, '__' + m[old_pname])
    return hname     



def get_model_semileptonic():
    files = ['BStarCombinationHistos_Left_Semileptonic.root']
    model = build_model_from_rootfile(files, histogram_filter, external_to_internal, include_mc_uncertainties=True)
    model.fill_histogram_zerobins()
    model.set_signal_processes('bs*')
    model.add_lognormal_uncertainty('zjets_rate',    math.log(1.20), 'ZJets')
    model.add_lognormal_uncertainty('diBoson_rate',  math.log(1.30), 'diBoson')


    model.add_lognormal_uncertainty('ttbar_rate',    math.log(1.053), 'ttbar')
    model.add_lognormal_uncertainty('tW_rate',       math.log(1.20), 'sttW')
    model.add_lognormal_uncertainty('tchannel_rate', math.log(1.15), 'stt')
    model.add_lognormal_uncertainty('schannel_rate', math.log(1.30), 'sts')


    model.add_lognormal_uncertainty('QCD_rate_El',      math.log(1.33), 'qcd','Ele_allJetLeptonMETMass')
    model.add_asymmetric_lognormal_uncertainty('QCD_rate_Mu',      math.log(2.0),math.log(2.69), 'qcd','Mu_allJetLeptonMETMass')

    model.add_lognormal_uncertainty('wjets_rate_El',    math.log(1.45), 'WJets','Ele_allJetLeptonMETMass')
    model.add_lognormal_uncertainty('wjets_rate_Mu',    math.log(1.30), 'WJets','Mu_allJetLeptonMETMass')
    for p in model.processes:
        if p == 'qcd': continue
        if p == 'WJets': continue
        model.add_lognormal_uncertainty('lumi', 0.026, p)
    return model

def get_model_hadronic():
    files = ['BStarCombinationHistos_Left_Allhadronic.root']
    model = build_model_from_rootfile(files, histogram_filter, external_to_internal, include_mc_uncertainties=True)
    model.fill_histogram_zerobins()
    model.set_signal_processes('bs*')
    for p in model.processes:
	if p=='qcd': continue
	if p=='ttbar':
	       	#model.add_lognormal_uncertainty('ttbar_xsec', math.log(1.058), p)
	    	model.add_asymmetric_lognormal_uncertainty('ttbar_xsec',math.log(1.055),math.log(1.048), p)
   	if p=='st': 
       		model.add_lognormal_uncertainty('st_TW_xsec', math.log(1.054), p)
      # 	model.add_lognormal_uncertainty('topsf', math.log(1.15), p)
       	model.add_lognormal_uncertainty('lumi', math.log(1.062), p)
        model.add_lognormal_uncertainty('wtag', math.log(1.010), p)
       #	model.add_lognormal_uncertainty('AK8btag', math.log(1.03), p)

    return model


def get_model_dileptonic():
    #files = ['HistoForShapeLimitbStarDileptonLeft.root']
    files = ['BStarCombinationHistos_Left_Dileptonic.root']
    model = build_model_from_rootfile(files, include_mc_uncertainties=True)
    #model = build_model_from_rootfile(files, histogram_filter, external_to_internal, include_mc_uncertainties=True)
    model.fill_histogram_zerobins()
    model.set_signal_processes('bs*')
    for p in model.processes:
        model.add_lognormal_uncertainty('lumi', 0.026, p)
        model.add_lognormal_uncertainty('flatUnc', math.log(1.165), p) ## backgrounds include PU/PDF/LeptonSFTrig/ID/Iso MET qqbar
    for p in model.signal_processes:
        model.add_lognormal_uncertainty('flatUnc', math.log(1.328), p) ## bs signal include PU/PDF/LeptonSFTrig/ID/Iso MET qqbar, this will over-write the flatUnc for previous setting
    #for p in model.processes:
    #   model.add_lognormal_uncertainty('lumi', 0.026, p)
    #   model.add_lognormal_uncertainty('flat_unc', math.log(1.125), p)
    #model.add_lognormal_uncertainty('schannel_rate', math.log(1.30), 'sts')
    #model.add_lognormal_uncertainty('tchannel_rate', math.log(1.15), 'stt')
    model.add_lognormal_uncertainty('tW_rate',    math.log(1.20), 'sttW')
    model.add_lognormal_uncertainty('ttbar_rate', math.log(1.053), 'ttbar')
    model.add_lognormal_uncertainty('zjets_rate',    math.log(1.20), 'ZJets')
    model.add_lognormal_uncertainty('wjets_rate',    math.log(1.30), 'WJets')
    model.add_lognormal_uncertainty('diBoson_rate',  math.log(1.30), 'diBoson')
    return model


def limits_comb(model, step = 1):
   if step==0:
       runs = bayesian_quantiles(model,'toys:0',1000, run_theta=False)
       print runs
       for point in runs:
		runs[point].get_configfile(Options())
       return

   model_summary(model)

   expected_limits = bayesian_quantiles(model, 'toys:0', 1000, run_theta=True)
   plot_expected = limit_band_plot(expected_limits, True)
   observed_limits = bayesian_quantiles(model, 'data', 10)
   plot_observed = limit_band_plot(observed_limits, False)
   report_limit_band_plot(plot_expected, plot_observed, 'Bayesian', 'bayesian')

   plot_expected.write_txt('expected_hadronic_semileptonic_limits_Left.txt')
   plot_observed.write_txt('observed_hadronic_semileptonic_limits_Left.txt')

   parVals = mle(model, input = 'data', n=1, with_error=True, with_covariance=False,options = myopts)
   print parVals
   for p in model.get_parameters([]):
    		parameter_values[p] = parVals['bs1600'][p][0][0]
   print "ML params"
   print parameter_values
   print
   histos = evaluate_prediction(model, parameter_values, include_signal = False)
   write_histograms_to_rootfile(histos, 'Left_hisos_at_ML.root')

   saveout = sys.stdout
   Outf1   =   open("Leftnuisance.txt", "w")
   sys.stdout = Outf1
   print parVals
   sys.stdout = saveout


   report.write_html('htmlout_Left_hadronic_semileptonic')
def limits_semilep(model, step = 1):
   if step==0:
       runs = bayesian_quantiles(model,'toys:0',1000, run_theta=False)
       print runs
       for point in runs:
		runs[point].get_configfile(Options())
       return

   model_summary(model)

   expected_limits = bayesian_quantiles(model, 'toys:0', 1000, run_theta=True)
   plot_expected = limit_band_plot(expected_limits, True)
   observed_limits = bayesian_quantiles(model, 'data', 10)
   plot_observed = limit_band_plot(observed_limits, False)
   report_limit_band_plot(plot_expected, plot_observed, 'Bayesian', 'bayesian')


   plot_expected.write_txt('expected_semileptonic_limits_Left.txt')
   plot_observed.write_txt('observed_semileptonic_limits_Left.txt')


   parVals = mle(model, input = 'data', n=1, with_error=True, with_covariance=False,options = myopts)
   print parVals
   for p in model.get_parameters([]):
    		parameter_values[p] = parVals['bs1600'][p][0][0]
   print "ML params"
   print parameter_values
   print
   histos = evaluate_prediction(model, parameter_values, include_signal = False)
   write_histograms_to_rootfile(histos, 'Left_hisos_at_ML.root')

   saveout = sys.stdout
   Outf1   =   open("Leftnuisance.txt", "w")
   sys.stdout = Outf1
   print parVals
   sys.stdout = saveout



   report.write_html('htmlout_Left_semileptonic')
def limits_allhad(model, step = 1):
   if step==0:
       runs = bayesian_quantiles(model,'toys:0',1000, run_theta=False)
       print runs
       for point in runs:
		runs[point].get_configfile(Options())
       return

   model_summary(model)

   expected_limits = bayesian_quantiles(model, 'toys:0', 1000, run_theta=True)
   plot_expected = limit_band_plot(expected_limits, True)
   observed_limits = bayesian_quantiles(model, 'data', 10)
   plot_observed = limit_band_plot(observed_limits, False)
   report_limit_band_plot(plot_expected, plot_observed, 'Bayesian', 'bayesian')


   plot_expected.write_txt('expected_hadronic_limits_Left.txt')
   plot_observed.write_txt('observed_hadronic_limits_Left.txt')


   parVals = mle(model, input = 'data', n=1, with_error=True, with_covariance=False,options = myopts)
   print parVals
   for p in model.get_parameters([]):
    		parameter_values[p] = parVals['bs1600'][p][0][0]
   print "ML params"
   print parameter_values
   print
   histos = evaluate_prediction(model, parameter_values, include_signal = False)
   write_histograms_to_rootfile(histos, 'Left_hisos_at_ML.root')

   saveout = sys.stdout
   Outf1   =   open("Leftnuisance.txt", "w")
   sys.stdout = Outf1
   print parVals
   sys.stdout = saveout



   report.write_html('./htmlout_Left_hadronic')

def limits_dilep(model, step = 1):
   if step==0:
       runs = bayesian_quantiles(model,'toys:0',1000, run_theta=False)
       print runs
       for point in runs:
		runs[point].get_configfile(Options())
       return

   model_summary(model)

   expected_limits = bayesian_quantiles(model, 'toys:0', 1000, run_theta=True)
   plot_expected = limit_band_plot(expected_limits, True)
   observed_limits = bayesian_quantiles(model, 'data', 10)
   plot_observed = limit_band_plot(observed_limits, False)
   report_limit_band_plot(plot_expected, plot_observed, 'Bayesian', 'bayesian')



   parVals = mle(model, input = 'data', n=1, with_error=True, with_covariance=False,options = myopts)
   print parVals
   for p in model.get_parameters([]):
    		parameter_values[p] = parVals['bs1600'][p][0][0]
   print "ML params"
   print parameter_values
   print
   histos = evaluate_prediction(model, parameter_values, include_signal = False)
   write_histograms_to_rootfile(histos, 'Left_hisos_at_ML.root')

   saveout = sys.stdout
   Outf1   =   open("Leftnuisance.txt", "w")
   sys.stdout = Outf1
   print parVals
   sys.stdout = saveout



   plot_expected.write_txt('expected_dileptonic_limits_Left.txt')
   plot_observed.write_txt('observed_dileptonic_limits_Left.txt')

   report.write_html('htmlout_Left_dileptonic')


channel = 'had'

myopts = Options()
myopts.set('minimizer', 'strategy', 'newton_vanilla')
parameter_values = {}
###COMB###
if channel=='comb':
	model = get_model_hadronic()
	model_semileptonic = get_model_semileptonic()
	model.combine(model_semileptonic)
	model_dilep = get_model_dileptonic()
	model.combine(model_dilep)
	for p in model.distribution.get_parameters():
    		d = model.distribution.get_distribution(p)
    		if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
        		model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])

	limits_comb(model, 1)

	
###HAD###
elif channel=='had':
	model = get_model_hadronic()

	for p in model.distribution.get_parameters():
    		d = model.distribution.get_distribution(p)
    		if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
        		model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])

	limits_allhad(model, 1)

###LEP###
elif channel=='semilep':
	model = get_model_semileptonic()

	for p in model.distribution.get_parameters():
    		d = model.distribution.get_distribution(p)
    		if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
        		model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])

	limits_semilep(model, 1)

	
###DILEP###
elif channel=='dilep':
	model   = get_model_dileptonic()

	for p in model.distribution.get_parameters():
    		d = model.distribution.get_distribution(p)
    		if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
        		model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])

	limits_dilep(model, 1)


