from PhysicalConstants import h, freq, BRef
from UnitConversion import db_to_abs

"""
The BoosterAmplifier class represents a booster amplifier. In the considered
architecture it is on the node's exit.

This amplifier compensates for the loss on the SSS device in the node's exit.
"""

class BoosterAmplifier:

    def __init__(self, noise_figure = db_to_abs(5)):

        """
        :param noise_figure: the amplifier noise factor.
        """                

        self.noise_figure = noise_figure 

    def Gain(self, SSS_loss): 
        self.gain = SSS_loss #DEFINIU-SE O GAMNHO DO AMPLIFICADOR IGUAL À PERDA SSS (5db)
        return self.gain

    def Noise(self, SSS_loss):    
        # This is the ASE Noise Modelling
        noise = self.noise_figure * h * freq * BRef * (self.Gain(SSS_loss) - 1)
        return noise