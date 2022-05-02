import math
from UnitConversion import db_to_abs
from PhysicalConstants import BRef, numPolarizations

"""
The Modulation class represents a modulation scheme.
"""

class Modulation:
       
    def __init__(self):          
        '''
        self.M = [1024, 512, 256, 128, 64, 32, 16, 8, 4]
        self.SNRb01 = [24.26, 21.80, 19.38, 17.04, 14.77, 12.59, 10.52, 8.58, 6.79]      # signal-noise per bit relation, in dB (BER E-3)
        self.SNRb02 = [28.50, 25.98, 23.51, 21.11, 18.78, 16.54, 14.40, 12.39, 10.53]    # signal-noise per bit relation, in dB (BER E-6)
        self.SNRb03 = [30.66, 28.12, 25.64, 23.22, 20.87, 18.61, 16.46, 14.43, 12.55]    # signal-noise per bit relation, in dB (BER E-9)
        self.SNRb04 = [32.11, 29.57, 27.08, 24.65, 22.29, 20.02, 17.86, 15.83, 13.93]    # signal-noise per bit relation, in dB (BER E-12)
        '''
        
        '''
        self.M = [64, 16, 4]
        self.SNRb01 = [14.77, 10.52, 6.79]
        '''
        
        self.M = [64, 32, 16, 8, 4]
        self.SNRb01 = [14.8 , 12.6, 10.5, 8.6, 6.8]
        

    def ThresholdOSNR(self, bit_rate, SNRb): 
        threshold_OSNR = (0.5 * (bit_rate) * db_to_abs(SNRb)) / BRef        
        return threshold_OSNR

    def RequiredSlots(self, bit_rate, b_slot, M):        
        required_slots = math.ceil(bit_rate / (b_slot * numPolarizations * math.log2(M)))
        return required_slots         
