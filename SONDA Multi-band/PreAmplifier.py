from BandConstants import h, BRef
from UnitConversion import db_to_abs

"""
The PreAmplifier class represents a Pre-Amplifier.

In the current architecture such amplifier is on the node's entrance. It
compensates for the loss in the precedent fiber segment and for the loss in
the succedent switching element (either a SSS or a Splitter).
"""

class PreAmplifier:

    def __init__(self):
        pass

    def Gain(self, SSS_Loss, MX_Loss, DX_Loss):
        self.gain = SSS_Loss * MX_Loss * (SSS_Loss**2)
        return self.gain

    def Noise(self, l, SSS_Loss, MX_Loss, DX_Loss, frequency, noise_figure):    
        # This is the ASE Noise Modelling
        noise = (db_to_abs(noise_figure) * h * frequency * BRef * l * (self.Gain(SSS_Loss, MX_Loss, DX_Loss) - 1))/(SSS_Loss*MX_Loss*DX_Loss)
        return noise