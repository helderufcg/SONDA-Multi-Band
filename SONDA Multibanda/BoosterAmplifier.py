from BandConstants import h, BRef
from UnitConversion import db_to_abs

"""
The BoosterAmplifier class represents a booster amplifier. In the considered
architecture it is on the node's exit.

This amplifier compensates for the loss on the SSS device in the node's exit.
"""

class BoosterAmplifier:

    def __init__(self):
        pass
    
    def Gain(self, MX_Loss, DX_Loss): 
        #self.gain = SSS_loss
        self.gain = DX_Loss * (MX_Loss**2)
        return self.gain

    def Noise(self, l, MX_Loss, DX_Loss, frequency, noise_figure):    
        # This is the ASE Noise Modelling
        noise = (db_to_abs(noise_figure) * h * frequency * BRef * l * (self.Gain(MX_Loss, DX_Loss) - 1))/MX_Loss
        return noise