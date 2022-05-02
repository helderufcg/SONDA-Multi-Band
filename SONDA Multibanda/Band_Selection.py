from BandConstants import *
from BandData import *
import math
import numpy as np
from scipy.interpolate import interp1d

Ag652A = interp1d(amostra_freq, amostra_aten, kind='cubic') #Attenuation OH peak fiber
Ag652D = interp1d(amostra_freq_dry, amostra_aten_dry, kind='cubic') #Attenuation dry fiber

NF_L = interp1d(amostra_freq_l, amostra_nf_l, kind="cubic")
NF_C = interp1d(amostra_freq_c, amostra_nf_c, kind="cubic")
NF_S = interp1d(amostra_freq_s, amostra_nf_s, kind="cubic")

class Band_Selection:
    def __init__(self):
        pass
    
    def getNoiseFigureAmplifier_C(self, Freq):
        noise_figure = NF_C(Freq)
        return noise_figure
    
    def getSlotsAttenuation(self,fiber,Freq):
        if fiber == 1:
            A = Ag652D(Freq)
            return A
        elif fiber == 2:
            A = Ag652A(Freq)
            return A
        else:
            return 0

    def getSlotsAttenuation_O(self,fiber):
        slots_O = FO 
        if fiber == 1:
            AO = Ag652D(slots_O)
            return AO
        else:
            AO = Ag652A(slots_O)
            return AO

    def getSlotsAttenuation_E(self,fiber):
        slots_E = FE 
        if fiber == 1:
            AE = Ag652D(slots_E)
            return AE
        else:
            AE = Ag652A(slots_E)
            return AE

    def getSlotsAttenuation_S(self,fiber):
        slots_S = FS 
        if fiber == 1:
            AS = Ag652D(slots_S)
            return AS
        else:
            AS = Ag652A(slots_S)
            return AS
    
    def getSlotsAttenuation_C(self,fiber):
        slots_C = FC 
        if fiber == 1:
            AC = Ag652D(slots_C)
            return AC
        else:
            AC = Ag652A(slots_C)
            return AC

    def getSlotsAttenuation_L(self,fiber):
        slots_L = FL 
        if fiber == 1:
            AL = Ag652D(slots_L)
            return AL
        else:
            AL = Ag652A(slots_L)
            return AL
    