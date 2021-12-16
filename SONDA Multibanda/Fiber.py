from UnitConversion import db_to_abs

"""
The Fiber class represents a Fiber segment.
"""

class Fiber:

    def __init__(self, alpha_fiber = 0.22):
        
        """
        :param alpha_fiber: fiber loss coefficient, measured in dB per kilometer
        """

        self.alpha_fiber = alpha_fiber
        
    def FiberLoss(self, dij):     
        fiber_loss = db_to_abs(self.alpha_fiber * dij)
        return fiber_loss