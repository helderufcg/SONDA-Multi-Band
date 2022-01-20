from PhysicalConstants import *
import math
import numpy as np

Ag652 = 1.108*10**(-2)

def w(f0):
    return Ag652*math.exp(f0)
op = np.vectorize(w)

class BandSelection:
    def __init__(self):
        pass
    
    #Retorna a largura de banda
    
    def getBandwidthO(self):
        result = c * ((1/LO) - (1/LE))
        return(result)

    def getBandwidthE(self):
        result = c * ((1/LE) - (1/LS))
        return(result)

    def getBandwidthS(self):
        result = c * ((1/LS) - (1/LC))
        return(result)

    def getBandwidthC(self):
        result = c * ((1/LC) - (1/LL))
        return(result)

    def getBandwidthL(self):
        result = c * ((1/LL) - (1/LU))
        return(result)

    #Slots com sua respectiva atenuação
    #Fibra ITU-T G652

    def getSlots_O_G652(self):
        slots_O = np.arange(FreqO,FreqE,-BSlot)
        atenuaO=op((slots_O*4582E-9)/c)
        return atenuaO

    def getSlots_E_G652(self):
        slots_E = np.arange(FreqE,FreqS,-BSlot)
        atenuaO=op((slots_E*4582E-9)/c)
        return atenuaO

    def getSlots_S_G652(self):
        slots_S = np.arange(FreqS,FreqC,-BSlot)
        atenuaO=op((slots_S*4582E-9)/c)
        return atenuaO

    def getSlots_C_G652(self):
        slots_C = np.arange(FreqC,FreqL,-BSlot)
        atenuaO=op((slots_C*4582E-9)/c)
        return atenuaO

    def getSlots_L_G652(self):
        slots_L = np.arange(FreqL,FreqU,-BSlot)
        atenuaO=op((slots_L*4582E-9)/c)
        return atenuaO

    #Fibra Convencional

    
