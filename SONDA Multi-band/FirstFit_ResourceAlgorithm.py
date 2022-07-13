import numpy as np

"""
The FirstFit class represents the First Fit spectrum assignment algorithm.
It tries to allocate the requisition on the first block of slots that are 
capable of containing the requisition.
"""

class FirstFit:

    def __init__(self, band_control):
        self.band_control=band_control
        pass
    
    def n_slots(self, band):
        return self.band_control[band]
    
    def bands(self):
        return self.band_control
    
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

    def FirstFit(self, N, T, route, required_slots, band):
        aux = [1]*self.n_slots(band)
        dimension = (len(route)-1, self.n_slots(band))
        FFlists = np.zeros(shape=dimension, dtype=np.uint8)
    
        # checking which slots are available on each link of the route
        for r in range(len(route)-1): 
            rcurr = route[r] #r currenct
            rnext = route[r+1] 
            for s in range(self.n_slots(band)):
                FFlists[r][s] = N[band][rcurr][rnext][s]    
        
        # checking which slots are available on all links of the route
        for r in range(len(route)-1):
            result = np.logical_and(aux, FFlists[r])           
            aux = result 
            
        slots_vector = []    
        # applying first-fit to the resulting list
        for s in range(self.n_slots(band)-required_slots+1): 
            for slot in range(s, s+required_slots, 1): 
                if result[slot]:
                    slots_vector.append(slot)
            if self.VerifyContiguity(slots_vector) and np.size(slots_vector) == required_slots:            
                break
            else:
                slots_vector.clear()

        return slots_vector
