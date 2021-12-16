"""
    c: light's velocity.
    h: Planck's constant.
    l: light's wavelength.
    freq: light's frequency.
    BRef:  reference bandwidth.
    numPolarizations: is used to choose whether one or two polarizations are used to transmit the signal.
        
"""
 
c = 299792458 
h = 6.62606957E-34
l = 1550E-9 #COMPRIMENTO DE ONDA USADO -> BANDA C: 1550 NM
freq = 193.4E12 # c = l*f -> c/l = 193.4 THz
BRef = 12.5E9 #12.5 Gbps
BSlot = 12.5E9    
numPolarizations = 2
