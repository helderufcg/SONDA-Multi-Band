"""
    c: light's velocity.
    h: Planck's constant.
    L: light's wavelength.
    Freq: light's frequency. -> Frequências centrais das grades
    BRef:  reference bandwidth.
    numPolarizations: is used to choose whether one or two polarizations are used to transmit the signal.
        
"""

c = 299792458 
h = 6.62606957E-34

FcentralO = 228.85E12 #P/ 1310nm
FcentralE = 212.62E12 #P/ 1410nm
FcentralS = 200.53E12 #P/ 1495nm
FcentralC = 193.41E12 #P/ 1550nm
FcentralL = 187.96E12 #P/ 1595nm

Fcentral  = 207.83E12 #P/ 1442.5nm

BRef = 12.5E9 
BSlot = 12.5E9 

numPolarizations = 2