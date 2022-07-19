from cmath import e
from UnitConversion import db_to_neper
from Band import Band

Banda = Band()

"""
The Fiber class represents a Fiber segment.
"""

class Fiber:

    def __init__(self, fiber_type, frequency):
        
        """
        :param alpha_fiber: fiber loss coefficient, measured in dB per kilometer
        """
        #self.alpha_fiber = 0.22
        # Variable option below
        self.alpha_fiber = Banda.SlotsAttenuation(fiber_type, frequency)

    def FiberLoss(self, dij):
        return e**(-db_to_neper(self.alpha_fiber)*dij)