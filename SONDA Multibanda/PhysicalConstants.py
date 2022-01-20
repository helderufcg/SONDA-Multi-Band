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

#Comprimento de onda inicial

LO = 1260E-9 #1260 nm BANDA O
LE = 1360E-9 #1360 nm BANDA S
LS = 1460E-9 #1460 nm BANDA S
LC = 1530E-9 #1530 nm BANDA C
LL = 1565E-9 #1565 nm BANDA L
LU = 1625E-9 #1625 nm BANDA U

#Frequência inicial

FreqO = 237.93E12 #237.93 THz BANDA O
FreqE = 220.44E12 #220.44 THz BANDA E
FreqS = 205.34E12 #205.34 THz BANDA S
FreqC = 195.94E12 #195.94 THz BANDA C
FreqL = 191.56E12 #191.56 THz BANDA L
FreqU = 184.49E12 #184.49 THz BANDA U

#Tamanho da banda, em THz

BandO = 17.500E12
BandE = 15.098E12
BandS = 9.395E12
BandC = 4.382E12
BandL = 7.073E12

BRef = 12.5E9 #12.5 Gbps
BSlot = 12.5E9 #Tamanho espectral do slot

numPolarizations = 2