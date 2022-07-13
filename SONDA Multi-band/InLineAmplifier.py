from BandConstants import h, BRef 
from UnitConversion import db_to_abs
import math

"""
The InLineAmplifier class represents an In-Line Amplifier.

Those amplifiers are scattered through the fiber. Each amplifier compensates
for the loss in the precedent fiber segment.
"""


class InLineAmplifier:

    def __init__(self):
        pass

    def NumberOfInlineAmplifiers(self, dij, damp):

        """
        :param dij: physical length of the optical fiber between nodes i and j.
        :param damp: the desired physical distance between the in line amplifiers.
        """

        #namp = math.ceil((dij/damp) - 1)
        namp = math.ceil((dij/damp))
        return namp

    def Noise(self, FiberLoss, namp, MX_Loss, DX_Loss, frequency, noise_figure):        
        # This is the ASE Noise Modelling        
        #noise = self.NumberOfInlineAmplifiers(dij, damp) * db_to_abs(noise_figure) * h * frequency * BRef * (1 - (fiber_loss**(-1/(1 + self.NumberOfInlineAmplifiers(dij, damp)))))
        noise = db_to_abs(noise_figure) * h * frequency * BRef * (namp * ((FiberLoss**(1/namp)) * MX_Loss * DX_Loss - 1))/MX_Loss
        return noise