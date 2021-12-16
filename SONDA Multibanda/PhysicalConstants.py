"""
    c: light's velocity.
    h: Planck's constant.
    l: light's wavelength.
    freq: light's frequency. -> Frequências centrais das grades
    BRef:  reference bandwidth.
    numPolarizations: is used to choose whether one or two polarizations are used to transmit the signal.
        
"""

c = 299792458 
h = 6.62606957E-34

lS  = 1510E-9 #1510 nm BANDA S 
lSC = 1530E-9 #1530 nm BANDA S+C
lC  = 1550E-9 #1550 nm BANDA C
lCL = 1570E-9 #1570 nm BANDA C+L
lL  = 1590E-9 #1590 nm BANDA L

lO  = 1270E-9 #1270 nm BANDA O

freqS  = 198.54E12 #198.54 THz BANDA S
freqSC = 195.94E12 #195.94 THz BANDA S+C
freqC  = 193.41E12 #193.41 THz BANDA C
freqCL = 190.95E12 #190.95 THz BANDA C+L
freqL  = 188.55E12 #188.55 THz BANDA L

freqO = 236.06E12 #236.06 THz BANDA O

BRef = 12.5E9 #12.5 Gbps
BSlot = 12.5E9

numPolarizations = 2
