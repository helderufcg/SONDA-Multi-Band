import numpy as np

"""
    c: Light's velocity.
    h: Planck's constant.
    LenX: Starting light's wavelength of the X-Band.
    FreqX: Starting light's frequency of the X-Band.
    FreqCX: Central light's frequency of the X-Band.
    BX: Bandwidth of each X-Band.
    FX: FSUs array of each X-Band.
    FEX: Effective FSUs array of each X-Band (Referring to the slots covered by the amplifier)
    NFX: Constante noise figure of each X-Band.
    BSlot: Slot reference bandwidth
    BRef:  Reference bandwidth.
    numPolarizations: Is used to choose whether one or two polarizations are used to transmit the signal.     
"""

c = 299792458
h = 6.62606957E-34
BRef = 12.5E9
BSlot = 12.5E9
numPolarizations = 2

LenO = 1260E-9
LenE = 1360E-9
LenS = 1460E-9
LenC = 1530E-9
LenL = 1565E-9
LenU = 1625E-9

FreqO = 237.93E12
FreqE = 220.44E12
FreqS = 205.34E12
FreqC = 195.94E12
FreqL = 191.56E12
FreqU = 184.49E12

FreqCO = 228.85E12
FreqCE = 212.62E12
FreqCS = 200.53E12
FreqCC = 193.41E12
FreqCL = 187.96E12

BO = 17.500E12
BE = 15.098E12
BS = 9.395E12
BC = 4.382E12
BL = 7.073E12

NFO = 7
NFE = 6
NFS = 7
NFC = 5.5
NFL = 6

F  = np.arange(FreqO,FreqU,-BSlot)
FO = np.arange(FreqO,FreqE,-BSlot)
FE = np.arange(FreqE,FreqS,-BSlot)
FS = np.arange(FreqS,FreqC,-BSlot)
FC = np.arange(FreqC,FreqL,-BSlot)
FL = np.arange(FreqL,FreqU,-BSlot)

FES = np.arange(FreqS,197.2184E12,-BSlot)
FEL = np.arange(190.9292E12,185.8263E12,-BSlot)

FreqEL = 190.93E12

"""
    Effective S-Band Slots: 650
    Effective C-Band Slots: 351
    Effective L-Band Slots: 409
"""