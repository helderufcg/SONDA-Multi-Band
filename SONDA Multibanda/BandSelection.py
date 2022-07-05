from BandConstants import *
from BandData import *
from scipy.interpolate import interp1d

"""
    Ag652X: G652-X fiber attenuation function.
    NF_X: X-Band noise figure function.  
"""

Ag652A = interp1d(DataFrequency_A, DataAtenuation_A, kind = 'cubic')
Ag652D = interp1d(DataFrequency_D, DataAtenuation_D, kind = 'cubic')

NF_L = interp1d(DataFreq_L, DataNF_L, kind = "cubic")
NF_C = interp1d(DataFreq_C, DataNF_C, kind = "cubic")
NF_S = interp1d(DataFreq_S, DataNF_S, kind = "cubic")

"""
The Band_Selection class represents the parameters dependent on the frequency and, consequently, on the band.
"""

class Band_Selection:
    
    def __init__(self):
        pass
    
    def getNoiseFigureAmplifier(self, frequency):
        if frequency <= FreqO and frequency > FreqE:
            noise_figure = 5
        elif frequency <= FreqE and frequency > FreqS:
            noise_figure = 5
        elif frequency <= FreqS and frequency > FreqC:
            noise_figure = NF_S(frequency)
        elif frequency <= FreqC and frequency > FreqL:
            noise_figure = NF_C(frequency)
        elif frequency <= FreqL and frequency > FreqU:
            noise_figure = NF_L(frequency)
        else:
            noise_figure = 10
        return noise_figure
    
    def getSlotsAttenuation(self, fiber_type, frequency):
        if fiber_type == 1:
            A = Ag652A(frequency)
            return A
        elif fiber_type == 2:
            A = Ag652D(frequency)
            return A
        else:
            return 0
        
    def getSlotFrequency(self, first_fit, N, T, route):
        slots = first_fit.FirstFit(N, T, route, 1)
        if slots == []:
            frequency = FreqC
        else:
            frequency = FreqC - BSlot*slots[0]
        return frequency