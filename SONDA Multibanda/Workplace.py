from cmath import log
from math import ceil
from matplotlib import pyplot
from Band_Selection import *
from BandData import *
from BandConstants import *
from PhysicalConstants import *
from UnitConversion import *
import numpy as np
import matplotlib.pyplot as plt

Banda = Band_Selection()
print(Band_Selection.getSlotsAttenuation(1,2,193.4E12))





'''
NFo = db_to_abs(NFO)
NFe = db_to_abs(NFE)
NFs = db_to_abs(NFS)
NFc = db_to_abs(NFC)
NFl = db_to_abs(NFL)



def WavelenghtConv(freq):
    
    wl = c/freq
    return wl

def Namp(dij, damp):
    
    namp = math.ceil((dij/damp) - 1)
    return namp

def Gain(freq, dij, damp, fiber):
    
    gain = ( 10**(Banda.getSlotsAttenuation(fiber,freq)*dij)/float(10) ) ** ( -1/(1 + Namp(dij,damp)) )
    return gain

def Noise(freq, dij, damp, noise_figure, fiber):        
        # This is the ASE Noise Modelling
        noise = Namp(dij,damp) * noise_figure * h * freq * BRef * (1-Gain(freq,dij,damp,fiber))
        return noise


RO = Noise(FO,200,50,NFo,2)
RE = Noise(FE,200,50,NFe,2)
RS = Noise(FS,200,50,NFs,2)
RC = Noise(FC,200,50,NFc,2)
RL = Noise(FL,200,50,NFl,2)

print(Gain(FO,0.000001,50,1))

L = WavelenghtConv(F)

LO = WavelenghtConv(FO)
LE = WavelenghtConv(FE)
LS = WavelenghtConv(FS)
LC = WavelenghtConv(FC)
LL = WavelenghtConv(FL)

plt.plot(LO, RO, LE, RE, LS, RS, LC, RC, LL, RL)
plt.xlabel("Comprimento de onda (m)")
plt.ylabel("P[Ase] (dBm)")
plt.legend([])
plt.grid()
plt.show()
'''

