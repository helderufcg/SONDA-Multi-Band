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
    
    def Gain(self, SSS_loss): 
        self.gain = SSS_loss
        return self.gain

    def Noise(self, SSS_loss, frequency, noise_figure):    
        # This is the ASE Noise Modelling
        noise = db_to_abs(noise_figure) * h * frequency * BRef * (self.Gain(SSS_loss) - 1)
        return noise