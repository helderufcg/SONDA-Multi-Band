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
        
    def getSlotFrequency(self, first_fit, N, T, route, band_control, rs):
        bands = []
        Freq = (FreqO, FreqE, FreqS, FreqC, FreqEL) # FreqEL representa a frequência efetiva me que o primeiro slot da banda L é contemplado pelo amplificador
        
        if band_control[3]!=0:
            bands.append(3)
        if band_control[4]!=0:
            bands.append(4)
        if band_control[2]!=0:
            bands.append(2)
        
        if bands == []:
            frequency = 194.91E12
        else:
            for band in bands: #3 bands: C(3)->L(4)->S(2)
                slots = first_fit.FirstFit(N, T, route, rs, band)
                if slots != []:
                    frequency = Freq[band] - BSlot*slots[0]
                    b = band
                    break
                else:
                    frequency = 194.91E12
                    
        return b, frequency