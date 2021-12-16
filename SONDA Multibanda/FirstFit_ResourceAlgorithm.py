import numpy as np

global n_slots
n_slots = 32

"""
The FirstFit class represents the First Fit spectrum assignment algorithm.
It tries to allocate the requisition on the first block of slots that are 
capable of containing the requisition.
"""

class FirstFit:

    def __init__(self):  
        pass

    def VerifyContiguity(self, vector):
        if np.size(vector) > 1: 
            for i in range(np.size(vector)-1): 
                if (vector[i+1] - vector[i]) > 1:
                    contiguity = 0                          
                    break
                else:
                    contiguity = 1
            return contiguity        
        else:            
            return 1

    def FirstFit(self, N, T, route, required_slots):
        aux = [1]*n_slots
        dimension = (len(route)-1, n_slots)
        FFlists = np.zeros(shape=dimension, dtype=np.uint8)
    
        # checking which slots are available on each link of the route
        for r in range(len(route)-1): 
            rcurr = route[r]
            rnext = route[r+1]
            for s in range(n_slots):
                FFlists[r][s] = N[rcurr][rnext][s]    
        
        # checking which slots are available on all links of the route
        for r in range(len(route)-1):
            result = np.logical_and(aux, FFlists[r])           
            aux = result
            
        slots_vector = []    
        # applying first-fit to the resulting list
        for s in range(n_slots-required_slots+1):
            for slot in range(s, s+required_slots, 1):
                if result[slot]: 
                    slots_vector.append(slot)               
            if self.VerifyContiguity(slots_vector) and np.size(slots_vector) == required_slots:            
                break           
            else:
                slots_vector.clear()           

        return slots_vector
