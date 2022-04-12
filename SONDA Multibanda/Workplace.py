from cmath import log
from math import ceil
from turtle import color
from matplotlib import pyplot
from sympy import true
from Band_Selection import *
from BandData import *
from BandConstants import *
from PhysicalConstants import *
from UnitConversion import *
import numpy as np
import matplotlib.pyplot as plt

#Banda = Band_Selection()
#print(Band_Selection.getSlotsAttenuation(1,2,FcentralC))

''''''

Load = np.arange(70,300,10)

PB1 = [1E-5, 2E-5, 16E-5, 62E-5, 109E-5,
       231E-5, 387E-5, 573E-5, 844E-5,
       1131E-5, 1540E-5, 1962E-5, 2343E-5,
       2802E-5, 3236E-5, 3684E-5, 4127E-5,
       4707E-5, 5203E-5, 5771E-5, 6260E-5,
       6625E-5, 7101E-5]

PB2 = [13E-5, 45E-5, 124E-5, 225E-5, 370E-5,
       600E-5, 883E-5, 1191E-5, 1551E-5,
       1940E-5, 2344E-5, 2771E-5, 3284E-5,
       3760E-5, 4182E-5, 4740E-5, 5150E-5,
       5634E-5, 6145E-5, 6625E-5, 7058E-5,
       7561E-5, 8078E-5]

PB3 = [97E-5, 212E-5, 400E-5, 657E-5, 988E-5,
       1306E-5, 1788E-5, 2191E-5, 2680E-5,
       3100E-5, 3618E-5, 4081E-5, 4513E-5,
       5006E-5, 5472E-5, 5935E-5, 6405E-5,
       6878E-5, 7364E-5, 7899E-5, 8262E-5,
       8695E-5, 9144E-5]

PB4 = [1867E-5, 2022E-5, 2188E-5, 2461E-5, 2786E-5,
       3121E-5, 3521E-5, 3914E-5, 4345E-5,
       4824E-5, 5282E-5, 5744E-5, 6073E-5,
       6651E-5, 6990E-5, 7362E-5, 7851E-5,
       8211E-5, 8767E-5, 9145E-5, 9434E-5,
       9922E-5, 10331E-5]


PB1 = [0.0, 1E-5, 2E-5, 0.00016, 0.00042,
       0.00082, 0.00179, 0.00278, 0.00436,
       0.00665, 0.00962, 0.0133, 0.01713,
       0.02117, 0.02525, 0.02997, 0.03443,
       0.03928, 0.0449, 0.04956, 0.05478,
       0.05999, 0.06516] 

PB2 = [4e-05, 0.00021, 0.00059, 0.00147,
       0.00273, 0.00434, 0.00655, 0.00904,
       0.01187, 0.01555, 0.01938, 0.02353,
       0.02797, 0.03234, 0.03663, 0.04127,
       0.04668, 0.05062, 0.05718, 0.06162,
       0.06592, 0.07109, 0.07534]

PB3 = [0.00055, 0.00131, 0.00278, 0.00452,
       0.00726, 0.01049, 0.01448, 0.01807,
       0.02195, 0.0267, 0.03126, 0.03541,
       0.04036, 0.04475, 0.04917, 0.05346,
       0.05839, 0.06298, 0.06822, 0.07264,
       0.07641, 0.08122, 0.08516]

PB4 = [0.00151, 0.00323, 0.00549, 0.00935,
       0.01258, 0.01678, 0.02125, 0.0265,
       0.03072, 0.03595, 0.04124, 0.04588,
       0.05113, 0.05623, 0.06038, 0.06435,
       0.06893, 0.07341, 0.07862, 0.08304,
       0.08858, 0.09239, 0.09752]


PBA1 = [0.0001, 0.00049, 0.00113, 0.00224,
        0.00391, 0.00634, 0.00911, 0.01273,
        0.01612, 0.01977, 0.02473, 0.02881,
        0.03356, 0.03862, 0.04279, 0.04856,
        0.05313, 0.0587, 0.06316, 0.06779,
        0.07354, 0.07727, 0.0822]

PBA2 = [0.00089, 0.00196, 0.00381, 0.00605,
        0.00934, 0.01305, 0.01688, 0.02165,
        0.0267, 0.0304, 0.03622, 0.04055,
        0.04503, 0.05112, 0.05404, 0.05958,
        0.06411, 0.06882, 0.07425, 0.0779,
        0.083, 0.08755, 0.09181]

PBA3 = [0.03641, 0.03764, 0.03953, 0.04154,
        0.04473, 0.04853, 0.05237, 0.05607,
        0.06025, 0.06491, 0.06862, 0.07223,
        0.07646, 0.0804, 0.08523, 0.08868,
        0.09248, 0.09652, 0.09989, 0.10506,
        0.1074,	0.11165, 0.11603]

PBA4 = [0.0775, 0.07787, 0.0785, 0.07963,
        0.08119, 0.0828, 0.08529, 0.08752,
        0.0907, 0.09366, 0.09696, 0.09987,
        0.10353, 0.10734, 0.10989, 0.11438,
        0.1173, 0.12075, 0.1246, 0.12788,
        0.13197, 0.13458, 0.13847]

plt.figure(1)
plt.plot(Load, PB1, marker='s', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "blue") 
plt.plot(Load, PB2, marker='o', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "Orange")                  
plt.plot(Load, PB3, marker='^', markersize = 5, markeredgewidth = 2, markerfacecolor = 'w', linewidth = 3, color = "green")
plt.plot(Load, PB4, marker='d', markersize = 5, markeredgewidth = 2, markerfacecolor = 'w', linewidth = 3, color = "red")
plt.plot(Load, PBA1, marker='s', markersize = 5, markeredgewidth = 3, markerfacecolor = 'b', linewidth = 3, color = "blue") 
plt.plot(Load, PBA2, marker='o', markersize = 5, markeredgewidth = 3, markerfacecolor = 'orange', linewidth = 3, color = "Orange")                  
plt.plot(Load, PBA3, marker='^', markersize = 5, markeredgewidth = 2, markerfacecolor = 'g', linewidth = 3, color = "green")
plt.plot(Load, PBA4, marker='d', markersize = 5, markeredgewidth = 2, markerfacecolor = 'r', linewidth = 3, color = "red")
plt.yscale('log')
plt.xlabel("Carga na rede (Erlangs)")
plt.ylabel("Probabilidade de Bloqueio")
plt.legend([r"$\alpha$ = 0.1912 dB/km | d$_a$$_m$$_p$ = 60 km ",r"$\alpha$ = 0.1912 dB/km | d$_a$$_m$$_p$ = 70 km",r"$\alpha$ = 0.1912 dB/km | d$_a$$_m$$_p$ = 80 km",r"$\alpha$ = 0.1912 dB/km | d$_a$$_m$$_p$ = 90 km",r"$\alpha$ = 0.22 dB/km | d$_a$$_m$$_p$ = 60 km ",r"$\alpha$ = 0.22 dB/km | d$_a$$_m$$_p$ = 70 km",r"$\alpha$ = 0.22 dB/km | d$_a$$_m$$_p$ = 80 km",r"$\alpha$ = 0.22 dB/km | d$_a$$_m$$_p$ = 90 km"])
plt.grid(true)

plt.show()

"""
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
"""

