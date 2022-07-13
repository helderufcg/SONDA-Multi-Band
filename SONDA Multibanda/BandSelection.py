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
            noise_figure = NFO
        elif frequency <= FreqE and frequency > FreqS:
            noise_figure = NFE
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
    
    def BandPrefer(self, band_control):
        bands = []
        if band_control[3]!=0:
            bands.append(3) # Prefer C-Band
        if band_control[4]!=0:
            bands.append(4) # Later, L-Band
        if band_control[2]!=0:
            bands.append(2) # Later, S-band
        if band_control[0]!=0:
            bands.append(0) # Later, O-band
        if band_control[1]!=0:
            bands.append(1) # Finally, E-band
        
        return bands
    
    def getSlotFrequency(self, first_fit, N, T, route, band_control, required_slots):
        Freq = (FreqO, FreqE, FreqS, FreqC, FreqEL)
        bands = self.BandPrefer(band_control)
        
        if bands == []:
            frequency = 194.91E12
        else:
            for band in bands:
                slots = first_fit.FirstFit(N, T, route, required_slots, band)
                
                if slots != []:
                    frequency = Freq[band] - BSlot*slots[0]
                    b = band
                    break  
                else:
                    frequency = 194.91E12
                    b = -1
                    
        return b, frequency