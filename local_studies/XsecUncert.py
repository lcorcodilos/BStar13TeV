import ROOT
from ROOT import *

fSR1200 = TFile('../rootfiles/35851pb/TWanalyzerweightedsignalRH1200_Trigger_nominal_none_PSET_default.root')
fSR1200PDFup = TFile('../rootfiles/35851pb/TWanalyzerweightedsignalRH1200_Trigger_nominal_none_pdf_up_PSET_default.root')
fSR1200PDFdown = TFile('../rootfiles/35851pb/TWanalyzerweightedsignalRH1200_Trigger_nominal_none_pdf_down_PSET_default.root')

hSR1200 = fSR1200.Get('Mtw')
hSR1200PDFup = fSR1200PDFup.Get('Mtw')
hSR1200PDFdown = fSR1200PDFdown.Get('Mtw')

xsec_nom = hSR1200.Integral()/35851.0
xsec_up = hSR1200PDFup.Integral()/35851.0
xsec_down = hSR1200PDFdown.Integral()/35851.0

print 'Nominal xsec: ' + str(xsec_nom)
print 'Up xsec:      ' + str(xsec_up)
print 'Down xsec:    ' + str(xsec_down)