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

    def Gain(self, fiber_loss, namp, SSS_loss):
        self.gain = (fiber_loss**(1/(1+namp))) * SSS_loss
        return self.gain

    def Noise(self, fiber_loss, namp, SSS_loss, frequency, noise_figure):    
        # This is the ASE Noise Modelling
        noise = db_to_abs(noise_figure) * h * frequency * BRef * (self.Gain(fiber_loss, namp, SSS_loss) - 1)
        return noise