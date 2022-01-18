from PhysicalConstants import h, FreqC, BRef
from UnitConversion import db_to_abs

"""
The BoosterAmplifier class represents a booster amplifier. In the considered
architecture it is on the node's exit.

This amplifier compensates for the loss on the SSS device in the node's exit.
"""

class BoosterAmplifier: #Amplificador de potência (Nó inicial)

    def __init__(self, noise_figure = db_to_abs(5)):

        """
        :param noise_figure: the amplifier noise factor.
        """                

        self.noise_figure = noise_figure 

    def Gain(self, SSS_loss): 
        self.gain = SSS_loss #PERDA SSS (5db)
        return self.gain

    #Dependente da frequência
    def Noise(self, SSS_loss):
        # This is the ASE Noise Modelling
        noise = self.noise_figure * h * FreqC * BRef * (self.Gain(SSS_loss) - 1)
        return noise