
from cmath import log
from matplotlib import pyplot
import scipy
from Band_Selection import *
from BandData import *
from BandConstants import *
from PhysicalConstants import *
import numpy as np
import matplotlib.pyplot as plt

Banda = Band_Selection()

#PARÂMETROS DA FIBRA
power = 0.001 #W
CDispersion = 21.3 #ps/nm/km
Slope = 0.067 #ps/nm²/km
CRaman = 0.028 #1/W/km
CNonLinear = 1.2 #W-¹km-¹
nsp = 5 #Adimensional
v = 200.67E12 #THz
Aten1550 = 0.165 #dB/km
Aten1590 = 0.171 #dB/km
Aten1495 = 0.177 #dB/km
Aten1410 = 0.217 #dB/km
span = 100 #km


'''
#ATENUAÇÃO VARIANDO LINEARMENTE
AtenTot = F*0
for a in range(0,len(F)):
    AtenTot[a] = 0.41 - 0.00005*a
PaseTot = 2*nsp*h*F*BSlot*(AtenTot*span-1)
PT = []
for i in range(0,len(F)):
    PT.append(10*log(PaseTot[i]/10**-3,10))


print(AtenTot)

plt.figure(1)
plt.plot(F,PT)
plt.xlabel("Frequency (Hz)")
plt.ylabel("P[ase] (dBm)")
plt.legend(["Full-Band"])
plt.grid()
'''

''' #ATENUAÇÃO CONSTANTE (VALORES INFORMADOS)
AtenE = FE*0 + Aten1410
AtenS = FS*0 + Aten1495
AtenC = FC*0 + Aten1550
AtenL = FL*0 + Aten1590

PaseL = 2*nsp*h*FL*BSlot*(AtenL*span-1)
PaseC = 2*nsp*h*FC*BSlot*(AtenC*span-1)
PaseS = 2*nsp*h*FS*BSlot*(AtenS*span-1)
PaseE = 2*nsp*h*FE*BSlot*(AtenE*span-1)
'''

''' #ATENUAÇÃO PELA MODELAGEM FEITA '''
control = 0

#gain = Banda.getSlotsAttenuation(1)*100
if control == 1:
    gainL = Banda.getSlotsAttenuation_L(1)*span
    gainC = Banda.getSlotsAttenuation_C(1)*span
    gainS = Banda.getSlotsAttenuation_S(1)*span
    gainE = Banda.getSlotsAttenuation_E(1)*span
    gainO = Banda.getSlotsAttenuation_O(1)*span
else:
    gainL = Banda.getSlotsAttenuation_L(2)*span
    gainC = Banda.getSlotsAttenuation_C(2)*span
    gainS = Banda.getSlotsAttenuation_S(2)*span
    gainE = Banda.getSlotsAttenuation_E(2)*span
    gainO = Banda.getSlotsAttenuation_O(2)*span

PaseL = 2*nsp*h*FL*BSlot*(gainL-1)
PaseC = 2*nsp*h*FC*BSlot*(gainC-1)
PaseS = 2*nsp*h*FS*BSlot*(gainS-1)
PaseE = 2*nsp*h*FE*BSlot*(gainE-1)
PaseO = 2*nsp*h*FO*BSlot*(gainO-1)


PL = []
PC = []
PS = []
PE = []
PO = []

for i in range(0,len(FL)):
    PL.append(10*log(PaseL[i]/10**-3,10))

for i in range(0,len(FC)):
    PC.append(10*log(PaseC[i]/10**-3,10))

for i in range(0,len(FS)):
    PS.append(10*log(PaseS[i]/10**-3,10))

for i in range(0,len(FE)):
    PE.append(10*log(PaseE[i]/10**-3,10))

for i in range(0,len(FO)):
    PO.append(10*log(PaseO[i]/10**-3,10))

plt.figure(1)
plt.plot(FL,PL,FC,PC,FS,PS,FE,PE)
plt.xlabel("Frequency (Hz)")
plt.ylabel("P[ase] (dBm)")
plt.legend(["L-band","C-Band","S-Band","E-band"])
plt.grid()


''' PLOT DA MODELAGEM DA ATENUAÇÃO
plt.figure(2)
plt.plot(F,Banda.getSlotsAttenuation(1))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Pase (dBm)")
plt.legend([""])
plt.grid()
'''

plt.show()