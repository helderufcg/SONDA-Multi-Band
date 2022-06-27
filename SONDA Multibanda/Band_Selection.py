from BandConstants import *
from BandData import *
from scipy.interpolate import interp1d

Ag652A = interp1d(DataFrequency_A, DataAtenuation_A, kind = 'cubic') #Attenuation OH peak fiber
Ag652D = interp1d(DataFrequency_D, DataAtenuation_D, kind = 'cubic') #Attenuation dry fiber

NF_L = interp1d(DataFreq_L, DataNF_L, kind = "cubic")
NF_C = interp1d(DataFreq_C, DataNF_C, kind = "cubic")
NF_S = interp1d(DataFreq_S, DataNF_S, kind = "cubic")

class Band_Selection:
    def __init__(self):
        pass
    
    def getNoiseFigureAmplifier_C(self, Freq):
        noise_figure = NF_C(Freq)
        return noise_figure
    
    def getSlotsAttenuation(self,fiber,Freq):
        if fiber == 1:
            A = Ag652A(Freq)
            return A
        elif fiber == 2:
            A = Ag652D(Freq)
            return A
        else:
            return 0
