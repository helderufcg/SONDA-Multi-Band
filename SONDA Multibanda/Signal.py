from BandSelection import Band_Selection
from SSS_MX_DX import SSS_MX_DX
from Fiber import Fiber
from BoosterAmplifier import BoosterAmplifier
from InLineAmplifier import InLineAmplifier
from PreAmplifier import PreAmplifier

sss_mx_dx = SSS_MX_DX()
booster_amplifier = BoosterAmplifier()
inline_amplifier = InLineAmplifier()
pre_amplifier = PreAmplifier()
Band = Band_Selection()

sss_loss = sss_mx_dx.SSS_loss
mx_loss  = sss_mx_dx.MX_loss
dx_loss  = sss_mx_dx.DX_loss

"""
The Signal class represents a signal that propagates through the network.
"""

class Signal:

    def __init__(self, input_power = 0.001, input_OSNR = 1000):

        """
	    :param input_power: input power of the network transmitters, in Watts.
	    :param input_OSNR: input OSNR of the network.  
        """

        self.input_power = input_power
        self.input_OSNR = input_OSNR    

    def Summation(self, A, route, damp, fiber, frequency):
        ni = []
        
        #noise_figure = 5
        # Variable option below
        noise_figure = Band.getNoiseFigureAmplifier(frequency)
        
        l = len(route)-1
        np = pre_amplifier.Noise(l, sss_loss, mx_loss, dx_loss, frequency, noise_figure)
        nb = booster_amplifier.Noise(l, mx_loss, dx_loss, frequency, noise_figure)
        
        for i in range(len(route)-1):
            dij = A[route[i]][route[i+1]]
            namp = inline_amplifier.NumberOfInlineAmplifiers(dij, damp)
            ni.append(inline_amplifier.Noise(fiber.FiberLoss(dij), namp, mx_loss, dx_loss, frequency, noise_figure))
        
        summation = nb + sum(ni) + np
        return summation
   
    def ModulationFormat(self, modulation_format):    
        return modulation_format    
    
    def InputPower(self):    
        return self.input_power

    def InputNoisePower(self):    
        input_noise_power = self.input_power/self.input_OSNR 
        return input_noise_power

    def OutputNoisePower(self, A, route, damp, fiber, frequency):
        #output_noise_power = self.InputNoisePower() + self.Summation(A, route, damp, fiber, frequency)    
        output_noise_power = self.InputNoisePower() + sss_loss*self.Summation(A, route, damp, fiber, frequency)
        return output_noise_power

    def OutputOSNR(self, A, route, damp, fiber_type, frequency):
        fiber = Fiber(fiber_type, frequency)       
        output_OSNR = self.input_power/(self.OutputNoisePower(A, route, damp, fiber, frequency))
        return output_OSNR