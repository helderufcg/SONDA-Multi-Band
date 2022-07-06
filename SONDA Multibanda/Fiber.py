from cmath import e, exp
from UnitConversion import db_to_abs, db_to_neper
from BandSelection import Band_Selection

Banda = Band_Selection()

"""
The Fiber class represents a Fiber segment.
"""

class Fiber:

    def __init__(self, fiber_type, frequency):
        
        """
        :param alpha_fiber: fiber loss coefficient, measured in dB per kilometer
        """
        #alpha_fiber = 0.22
        # Variable option below
        alpha_fiber = Banda.getSlotsAttenuation(fiber_type, frequency)
        
        self.alpha_fiber = alpha_fiber

    def FiberLoss(self, dij):
        #fiber_loss = db_to_abs(self.alpha_fiber * dij)
        fiber_loss = e**(-db_to_neper(self.alpha_fiber)*dij)
        return fiber_loss