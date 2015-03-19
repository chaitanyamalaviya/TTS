__author__ = 'aseschng'

import module_readData

dirname  = "D:\\Study\\URECA\\teaching_Python_obama\\"
infilename = 'ch1'
wavfilename = dirname+infilename+'.wav'
opwavfilename = dirname+'extractedo_'+infilename+'.wav'
wrdfilename = dirname+infilename+'.wrd'

myListDistWrds = module_readData.readWrdFile(wrdfilename)
print("P2 : number of distinct words found =", len(myListDistWrds))

wavSignal = module_readData.readWaveFile(wavfilename)
Fs = 16000;
mySigExtracted = module_readData.extractSignalByWord(wavSignal,myListDistWrds,Fs)
module_readData.writeWavFile(opwavfilename, mySigExtracted)
print("saving file ", opwavfilename)
