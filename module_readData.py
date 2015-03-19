__author__ = 'aseschng'

import wave
import struct
import math

class C_mystruct():
        def __init__(self, label, st, et):
                self.label = label
                self.startTime = [];
                self.endTime = [];
                self.startTime.append(float(st))
                self.endTime.append(float(et))
                self.count  = 1;

# This function reads the word infroomaton from Obama document
# 3 columns , starttime endtime  word

def readWrdFile(filename):

    thisfile = open(filename, "r")
    print ("P1: opening"+filename)

    myDistinctWrd = {}

    for line in thisfile.readlines():
        tokenstring = line.split(" ")
        keyWord = tokenstring[2].strip()

        if keyWord in myDistinctWrd:
                tmpV = myDistinctWrd[keyWord]
                tmpV.count = tmpV.count+1;
                tmpV.startTime.append(tokenstring[0])
                tmpV.endTime.append(tokenstring[1])
        else:
                tmpV = C_mystruct(keyWord, tokenstring[0], tokenstring[1])
                myDistinctWrd[keyWord]= tmpV;

    return myDistinctWrd


def readWaveFile(wavfilename):

    ipWave = wave.open(wavfilename,"rb")
    numFrames = ipWave.getnframes()
    print(ipWave.getparams()," numFrames =", numFrames)
    ipRaw = ipWave.readframes(numFrames)
    return ipRaw


def extractSignalByWord(ipRaw, myDistintWordList,Fs):

    mylist_sorted = sorted(myDistintWordList.keys())

    values = []
    frameRate = Fs
    for item in mylist_sorted:
        tmpV = myDistintWordList[item]

        if tmpV.count > 2:
            print ("word = ", tmpV.label," and count = ",tmpV.count)

            for idx in range (0, tmpV.count):
                st1 = 2*int(round(float(tmpV.startTime[idx])*frameRate))
                et1 = 2*int(round(float(tmpV.endTime[idx])*frameRate))

                for i in range(st1,et1):
                    values.append(ipRaw[i])

                # lets stuff some zeros between all found sequences
                for j in range(0,1000):
                    values.append(chr(0))

    return values

def writeWavFile(writefilename,mySig):
    opWave = wave.open(writefilename,"wb")
    numChannel= 1
    sampWidth = 2
    frameRate = 16000
    opWave.setparams((1,2,16000,0,'NONE','not compressed'))
    value_str = " ".join(mySig)
    opWave.writeframes(value_str)
    opWave.close()


