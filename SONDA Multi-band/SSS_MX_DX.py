from UnitConversion import db_to_abs

"""
The SSS_MX_DX class represents a Spectrum Selective Switch, Multiplexer and Demultiplexer.
"""

class SSS_MX_DX:

    def __init__(self, SSS_loss = db_to_abs(5), MX_loss = db_to_abs(5), DX_loss = db_to_abs(5)):
        
        """
        :param SSS_loss: the loss of a SSS. Is considered constant for all the SSS devices.
        :param MX_loss: the loss of a MX. Is considered constant for all the MX devices.
        :param DX_loss: the loss of a DX. Is considered constant for all the DX devices.
        """

        self.SSS_loss = SSS_loss
        self.MX_loss = MX_loss
        self.DX_loss = DX_loss
        
        
    def SSSLoss(self):        
        return self.SSS_loss 
    
    def MXLoss(self):        
        return self.MX_loss

    def DXLoss(self):        
        return self.DX_loss    