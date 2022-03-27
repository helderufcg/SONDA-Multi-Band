from PhysicalConstants import BSlot
from Dijkstra_RoutingAlgorithm import Dijkstra
from FirstFit_ResourceAlgorithm import *
from Signal import Signal 
from Modulation import Modulation
import math

dijkstra = Dijkstra()
signal = Signal()
modulation = Modulation()
#first_fit = FirstFit()

"""
The RoutingWavelengthAssignment class contains the routing and
wavelength assignment operations that a call must endure before its
implementation.
"""

class RWA:

    def __init__(self):#, n_slots
        #self.n_slots = n_slots
        pass
   
    def Generate(self, n_nodes, links, first_fit):             
        # init slots availability matrix    
        dimension = (n_nodes, n_nodes, first_fit.get_N_slots())#self.n_slots
        slot = np.zeros(shape=dimension, dtype=np.uint8)
        for link in links:
            for s in range(first_fit.get_N_slots()): #self.n_slots
                slot_availability = 1
                slot[link[0]][link[1]][s] = slot_availability
                slot[link[1]][link[0]][s] = slot_availability

        # init traffic matrix
        dimension = (n_nodes, n_nodes, first_fit.get_N_slots()) #self.n_slots
        time = np.zeros(shape=dimension, dtype=np.float64)
        for link in links:
            for s in range(first_fit.get_N_slots()): #self.n_slots
                time[link[0]][link[1]][s] = 0
                time[link[1]][link[0]][s] = 0

        return slot, time

    def RWA(self, A, N, T, src_node, dst_node, holding_time, bit_rate, network_type, wavelength_bandwidth, consider_ase_noise, damp, number, first_fit):
        # defining the best route according to the dijkstra algorithm 
        #first_fit = FirstFit(self.n_slots) #att

        route = dijkstra.Dijkstra(A, src_node, dst_node)

        M = modulation.M
        if number > 0 and number <= 25:
            SNRb = modulation.SNRb01
        elif number > 25 and number <= 50:   
            SNRb = modulation.SNRb02
        elif number > 50 and number <= 75:    
            SNRb = modulation.SNRb03
        else:    
            SNRb = modulation.SNRb04
            
        if network_type == 1:
            required_slots = math.ceil((wavelength_bandwidth*10**9)/BSlot) #Bslot = 12.5 GHz
        else:            
            if consider_ase_noise == 0:
                required_slots = modulation.RequiredSlots(bit_rate, BSlot, M[0])
            else:                
                for i in range(9):
                    if signal.OutputOSNR(A, route, damp) > modulation.ThresholdOSNR(bit_rate, SNRb[i]):
                        required_slots = modulation.RequiredSlots(bit_rate, BSlot, M[i])
                        color = 0
                        break
                    else:
                        color = 1      
                if color:        
                    return 1              
        
        # defining the slots to be alocated First_fit.get_N_slots()
        slots_vector = first_fit.FirstFit(N, T, route, required_slots)        

        if slots_vector:        
            # if the resulting slot vector is not contiguous         
            if not first_fit.VerifyContiguity(slots_vector): 
                return 1  # blocked 

            # if all specifications are answered, allocate resources on the links of the route    
            for r in range(len(route)-1):
                rcurr = route[r]
                rnext = route[r+1]
                for i in range(required_slots):
                    N[rcurr][rnext][slots_vector[i]] = 0
                    T[rcurr][rnext][slots_vector[i]] = holding_time

            return 0  # allocated
        else:
            return 1  # blocked
