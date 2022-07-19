from BandConstants import FreqO, FreqE, FreqS, FreqC, FreqEL, FreqL, FreqU, BSlot, NFO, NFE
from scipy.interpolate import interp1d

"""
    Ag652X: G652-X fiber attenuation function.
    NF_X: X-Band noise figure function.  
"""



"""
The Band_Selection class represents the parameters dependent on the frequency and, consequently, on the band.
"""

class Band:
    
    def __init__(self):
        
        # Fiber G652.A
        self.DataAtenuation_A = [4.0243E-01, 3.9287E-01, 3.7936E-01,
                     3.6754E-01, 3.5065E-01, 3.3602E-01,
                     3.2363E-01, 3.2138E-01, 3.1632E-01,
                     3.2420E-01, 3.3545E-01, 3.5403E-01,
                     3.8048E-01, 4.4634E-01, 7.1482E-01,
                     9.3039E-01, 9.9118E-01, 9.9174E-01,
                     9.3208E-01, 7.8213E-01, 6.2757E-01,
                     4.8574E-01, 3.9343E-01, 3.4615E-01,
                     3.0084E-01, 2.7748E-01, 2.5756E-01,
                     2.5491E-01, 2.4754E-01, 2.4506E-01,
                     2.3521E-01, 2.3521E-01, 2.2784E-01,
                     2.2536E-01, 2.2041E-01, 2.1782E-01,
                     2.1551E-01, 2.0808E-01, 2.0803E-01,
                     2.0797E-01, 2.0791E-01, 2.0566E-01,
                     2.0870E-01, 2.1309E-01, 2.1343E-01,
                     2.1377E-01, 2.1557E-01, 2.2249E-01,
                     2.2536E-01, 2.2784E-01]

        self.DataFrequency_A = [2.3793E+14, 2.3605E+14, 2.3421E+14,
                   2.3239E+14, 2.3060E+14, 2.2884E+14,
                   2.2711E+14, 2.2540E+14, 2.2372E+14,
                   2.2206E+14, 2.2124E+14, 2.2043E+14,
                   2.1962E+14, 2.1882E+14, 2.1803E+14,
                   2.1724E+14, 2.1645E+14, 2.1567E+14,
                   2.1490E+14, 2.1413E+14, 2.1337E+14,
                   2.1261E+14, 2.1186E+14, 2.1112E+14,
                   2.1038E+14, 2.0964E+14, 2.0891E+14,
                   2.0818E+14, 2.0746E+14, 2.0675E+14,
                   2.0604E+14, 2.0533E+14, 2.0394E+14,
                   2.0256E+14, 2.0120E+14, 1.9986E+14,
                   1.9853E+14, 1.9723E+14, 1.9594E+14,
                   1.9467E+14, 1.9341E+14, 1.9217E+14,
                   1.9156E+14, 1.9095E+14, 1.8974E+14,
                   1.8854E+14, 1.8737E+14, 1.8620E+14,
                   1.8505E+14, 1.8448E+14]

        # Fiber G652.D
        self.DataAtenuation_D = [3.8229E-01, 3.7171E-01, 3.5865E-01,
                     3.4407E-01, 3.3073E-01, 3.1835E-01,
                     3.0771E-01, 3.0039E-01, 2.8947E-01,
                     2.8118E-01, 2.7311E-01, 2.6583E-01,
                     2.5491E-01, 2.5309E-01, 2.4133E-01,
                     2.3669E-01, 2.3488E-01, 2.2760E-01,
                     2.2214E-01, 2.1486E-01, 2.0940E-01,
                     2.0576E-01, 2.0062E-01, 1.9665E-01,
                     2.0211E-01, 1.9665E-01, 1.9120E-01,
                     1.8755E-01, 1.9123E-01, 1.9120E-01,
                     1.9114E-01, 1.9120E-01, 1.9123E-01,
                     1.9234E-01, 1.9840E-01, 2.0211E-01,
                     2.0394E-01, 2.0759E-01]

        self.DataFrequency_D = [2.3793E+14, 2.3606E+14, 2.3421E+14,
                   2.3240E+14, 2.3061E+14, 2.2885E+14,
                   2.2712E+14, 2.2541E+14, 2.2373E+14,
                   2.2207E+14, 2.2044E+14, 2.1883E+14,
                   2.1724E+14, 2.1568E+14, 2.1414E+14,
                   2.1262E+14, 2.1112E+14, 2.0965E+14,
                   2.0819E+14, 2.0675E+14, 2.0534E+14,
                   2.0394E+14, 2.0256E+14, 2.0120E+14,
                   1.9986E+14, 1.9854E+14, 1.9723E+14,
                   1.9594E+14, 1.9467E+14, 1.9341E+14,
                   1.9217E+14, 1.9156E+14, 1.8974E+14,
                   1.8855E+14, 1.8737E+14, 1.8621E+14,
                   1.8506E+14, 1.8449E+14]
        
        # L-Band noise figure
        self.DataNF_L = [4.5607, 4.5704, 4.5783,
                    4.5864, 4.5943, 4.5991,
                    4.6055, 4.6149, 4.6248,
                    4.6335, 4.6428, 4.6483,
                    4.6560, 4.6683, 4.6795,
                    4.6868, 4.7050, 4.7215,
                    4.7509, 4.7813, 4.8164,
                    4.9181]

        self.DataFreq_L = [185.8263E12, 186.0383E12, 186.2765E12,
                    186.5361E12, 186.7810E12, 187.0138E12,
                    187.2481E12, 187.4966E12, 187.7465E12,
                    187.9783E12, 188.2217E12, 188.4643E12,
                    188.7094E12, 188.9498E12, 189.1905E12,
                    189.4367E12, 189.6788E12, 189.9199E12,
                    190.1663E12, 190.4076E12, 190.6474E12,
                    190.9292E12]

        # C-Band noise figure
        self.DataNF_C = [4.3497, 4.3428, 4.3292,
                    4.3207, 4.3091, 4.2961,
                    4.2916, 4.2818, 4.2638,
                    4.2639, 4.2478, 4.2363,
                    4.2327, 4.2275, 4.2229,
                    4.2144, 4.2113, 4.1985,
                    4.1824, 4.1620, 4.1466,
                    4.1453]

        self.DataFreq_C = [191.2973E+12, 191.5300E+12, 191.7622E+12,
                    191.9916E+12, 192.2231E+12, 192.4542E+12,
                    192.6854E+12, 192.9159E+12, 193.1471E+12,
                    193.3768E+12, 193.6089E+12, 193.8390E+12,
                    193.9928E+12, 194.2224E+12, 194.4564E+12,
                    194.6857E+12, 194.9155E+12, 195.1457E+12,
                    195.3757E+12, 195.6108E+12, 195.8370E+12,
                    196.0304E+12]

        # S-Band noise figure
        self.DataNF_S = [7.8142, 7.6818, 7.5467,
                    7.4133, 7.1494, 7.0787,
                    6.8133, 6.7463, 6.5491,
                    6.2754, 6.2098, 6.0771,
                    5.9419, 5.9450, 5.9449,
                    5.9458, 6.0138, 6.0114,
                    6.0145, 6.0144, 6.0144,
                    6.0111, 6.0145, 6.0810,
                    6.0776, 6.0783, 6.0763,
                    6.0776, 6.1488, 6.2111,
                    6.3435, 6.0080, 6.1435,
                    6.0754, 6.2783, 6.2421,
                    6.1739, 6.3416, 6.1404,
                    6.3438, 6.4682, 6.6768,
                    6.6773, 6.8124, 6.8112,
                    6.9428, 6.9444, 7.0098,
                    7.2098, 7.2780, 7.5457,
                    7.5457, 7.8117]

        self.DataFreq_S = [197.2184E12, 197.2833E12, 197.3661E12,
                    197.4899E12, 197.6670E12, 197.7675E12,
                    197.9163E12, 198.0821E12, 198.2494E12,
                    198.3586E12, 198.5278E12, 198.6821E12,
                    198.9004E12, 199.0187E12, 199.2680E12,
                    199.4224E12, 199.5725E12, 199.6900E12,
                    199.8561E12, 200.0259E12, 200.1971E12,
                    200.3396E12, 200.5487E12, 200.7333E12,
                    200.8345E12, 200.9481E12, 201.0475E12,
                    201.1789E12, 201.3328E12, 201.4427E12,
                    201.6028E12, 202.0074E12, 202.1793E12,
                    202.3252E12, 202.5358E12, 202.8512E12,
                    203.1916E12, 203.4751E12, 203.7075E12,
                    203.9537E12, 204.2180E12, 204.5365E12,
                    204.6547E12, 204.8115E12, 205.0335E12,
                    205.1215E12, 205.4240E12, 205.6169E12,
                    205.7810E12, 205.9887E12, 206.2294E12,
                    206.4545E12, 206.7866E12]

    
    def NoiseFigureAmplifier(self, frequency):
        if frequency <= FreqO and frequency > FreqE:
            noise_figure = NFO
        elif frequency <= FreqE and frequency > FreqS:
            noise_figure = NFE
        elif frequency <= FreqS and frequency > FreqC:
            NF_S = interp1d(self.DataFreq_S, self.DataNF_S, kind = "cubic")
            noise_figure = NF_S(frequency)
        elif frequency <= FreqC and frequency > FreqL:
            NF_C = interp1d(self.DataFreq_C, self.DataNF_C, kind = "cubic")
            noise_figure = NF_C(frequency)
        elif frequency <= FreqL and frequency > FreqU:
            NF_L = interp1d(self.DataFreq_L, self.DataNF_L, kind = "cubic")
            noise_figure = NF_L(frequency)
        else:
            raise ValueError('Frequency is out of range of amplifiers.')
        return noise_figure
    
    
    def SlotsAttenuation(self, fiber_type, frequency):
        if fiber_type == 1:
            Ag652A = interp1d(self.DataFrequency_A, self.DataAtenuation_A, kind = 'cubic')
            return Ag652A(frequency)
        else:
            Ag652D = interp1d(self.DataFrequency_D, self.DataAtenuation_D, kind = 'cubic')
            return Ag652D(frequency)
              
    
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
    
    def RequiredSlotFrequency(self, first_fit, N, T, route, band_control, required_slots):
        Freq = (FreqO, FreqE, FreqS, FreqC, FreqEL)
        bands = self.BandPrefer(band_control)
        
        if bands == []:
            b = -1
            frequency = 0
        else:
            for band in bands:
                slots = first_fit.FirstFit(N, T, route, required_slots, band)
                
                if slots != []:
                    frequency = Freq[band] - BSlot*slots[0]
                    b = band
                    break  
                else:
                    b = -1
                    frequency = 0
                    
        return b, frequency