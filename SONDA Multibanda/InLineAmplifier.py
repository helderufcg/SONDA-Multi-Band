from BandConstants import h, BRef 
from UnitConversion import db_to_abs
import math

"""
The InLineAmplifier class represents an In-Line Amplifier.

Those amplifiers are scattered through the fiber. Each amplifier compensates
for the loss in the precedent fiber segment.

    def __init__(self, noise_figure = db_to_abs(5)):

        
        #:param noise_figure: the amplifier noise factor.
        
      
        self.noise_figure = noise_figure 

"""


class InLineAmplifier:

    def __init__(self):
        pass

    def NumberOfInlineAmplifiers(self, dij, damp):

        """
        :param dij: physical length of the optical fiber between nodes i and j.
        :param damp: the desired physical distance between the in line amplifiers.
        """

        namp = math.ceil((dij/damp) - 1)
        return namp

    def Noise(self, fiber_loss, dij, damp, freq, noise_figure):        
        # This is the ASE Noise Modelling        
        noise = self.NumberOfInlineAmplifiers(dij, damp) * db_to_abs(noise_figure) * h * freq * BRef * (1 - (fiber_loss**(-1/(1 + self.NumberOfInlineAmplifiers(dij, damp)))))
        return noise