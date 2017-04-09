# BStar13TeV
## 4/7/19
Alphabet is working with the exception of QCD (stitching issue). Some changes were made in analyzer section that might affect using TWrate outputs. These can be sniffed out with some basic debugging though (the next time you go through the process of using them)

This is the commit before changing TW*.py to use TTrees instead of ntuples

### Known Issues
- QCD MC doesn't work in Alphabet (stitching)
- Alphabet fit not centered. Doing so will require changes in TWanalyzer