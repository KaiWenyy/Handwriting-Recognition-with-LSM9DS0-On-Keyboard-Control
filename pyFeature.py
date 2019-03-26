import numpy as np
from scipy import signal, fftpack

import random as rd
import matplotlib.pyplot as plt

def rms(l):
    return np.sqrt(mean(np.square(l)))


def maxFrequency(A):
    #A=[]

    N = len(A)
    # sample spacing
    T = 2.273 / 1000.0 #sample rate
    x = np.linspace(0.0, N*T, N)
    #y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

    y=A
    yf = fftpack.fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
    #print(xf)
    #print(xf,1.0/(2.0*T)/(N/2-1),len(xf))


    #fig, ax = plt.subplots()
    #ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
    #plt.show()
    #print(A)
    value, interval = abs(yf), 1.0/(2.0*T)/(N/2-1) #value, inteval
    return highestPeaklocate(value) * interval
    
def mean(l):
    return np.mean(l)

def std(l):
    return np.std(l)

def dataPoints(l):
    l = np.array(l)
    return np.size(l)

def highestPeakVal(l):
    return np.amax(l)

def lowestPeakVal(l):
    return np.amin(l)

def highestPeaklocate(l):
    return np.argmax(l)

def lowestPeaklocate(l):
    return np.argmin(l)

def peakNum(l):
    '''
    indexes = signal.find_peaks_cwt(l, np.arange(5, 10))
    indexed = np.array(indexes) - 1
    return np.size(indexed)
    '''
    num=0
    for i in range(3,len(l)-4,1):
        if l[i]>l[i-1] and l[i]>l[i-2] and l[i]>l[i-3] and l[i]>l[i+1] and l[i]>l[i+2] and l[i]>l[i+3] and l[i]>100:
            num+=1
        elif l[i]<l[i-1] and l[i]<l[i-2] and l[i]<l[i-3] and l[i]<l[i+1] and l[i]<l[i+2] and l[i]<l[i+3] and l[i]<-100:
            num+=1
    return num

if __name__ == '__main__':    
    vec = [rd.randint(-2500,2500) for i in xrange(3000)]
    print(vec)
    print(rms(vec))
    print(mean(vec))
    print(std(vec))
    print(dataPoints(vec))
    print(highestPeakVal(vec))
    print(highestPeaklocate(vec))
    print(peakNum(vec))
    print(maxFrequency(vec))
