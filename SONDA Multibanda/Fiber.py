from UnitConversion import db_to_abs
from Band_Selection import Band_Selection

Banda = Band_Selection()

"""
The Fiber class represents a Fiber segment.
"""

class Fiber:

    def __init__(self, freq, fiber_type):
        
        """
        :param alpha_fiber: fiber loss coefficient, measured in dB per kilometer
        """
        alpha_fiber = 0.22
        # Variable option below
        #alpha_fiber = Banda.getSlotsAttenuation(fiber_type,freq)
        
        self.alpha_fiber = alpha_fiber

    def FiberLoss(self, dij):
        fiber_loss = db_to_abs(self.alpha_fiber * dij)
        return fiber_loss