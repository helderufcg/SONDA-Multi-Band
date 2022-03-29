import numpy as np

c = 299792458  #Speed of light (m/s)
BSlot = 12.5E9 #Slot Reference bandwidth (Hz)

#Starting wavelength (nm)
LenO = 1260E-9
LenE = 1360E-9
LenS = 1460E-9
LenC = 1530E-9
LenL = 1565E-9
LenU = 1625E-9

#Starting frequency (Hz)
FreqO = 237.93E12
FreqE = 220.44E12
FreqS = 205.34E12
FreqC = 195.94E12
FreqL = 191.56E12
FreqU = 184.49E12

#BandWidth (Hz)
BandO = 17.500E12
BandE = 15.098E12
BandS = 9.395E12
BandC = 4.382E12
BandL = 7.073E12

#Noise Figure
NFO = 7     #dB PDFA
NFE = 6     #dB BDFA
NFS = 7     #dB TDFA
NFC = 5.5   #dB EDFA
NFL = 6     #dB EDFA

#FSUs array of each band
F  = np.arange(FreqO,FreqU,-BSlot)
FO = np.arange(FreqO,FreqE,-BSlot)
FE = np.arange(FreqE,FreqS,-BSlot)
FS = np.arange(FreqS,FreqC,-BSlot)
FC = np.arange(FreqC,FreqL,-BSlot)
FL = np.arange(FreqL,FreqU,-BSlot)
