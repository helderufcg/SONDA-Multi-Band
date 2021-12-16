from UnitConversion import db_to_abs

"""
The SSS class represents a spectrum selective switch.
"""

class SSS:

    def __init__(self, SSS_loss = db_to_abs(5)):
        
        """
        :param SSS_loss: the loss of a SSS. Is considered constant for all the SSS devices.
        """

        self.SSS_loss = SSS_loss
        
    def SSSLoss(self):        
        return self.SSS_loss 