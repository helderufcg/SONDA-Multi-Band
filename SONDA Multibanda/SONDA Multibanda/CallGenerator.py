import random

"""
CallGenerator class implements methods to continuously generate calls.

Currently, the origin and destination node are chosen with an uniform
distribution and the call duration and arrival times are chosen with
exponential distributions, the former with parameter mu and the latter
with parameter 1/h.   
"""

class Call:

    def __init__(self, n_nodes, H, mu):
        
        """
        :param n_nodes: number of nodes.
        :param H: parameter for the call interarrival time exponential distribution.
        :param mu: parameter for the call duration time exponential distribution.
        """
        
        self.n_nodes = n_nodes
        self.H = H
        self.mu = mu
     
    def Src(self):
        nodes = range(0, self.n_nodes, 1)        
        self.src_node = nodes[random.randint(0, (len(nodes)-1))]            # Randomly assign src node from list
        return self.src_node

    def Dst(self):
        nodes = range(0, self.n_nodes, 1)  
        self.dst_node = nodes[random.randint(0, (len(nodes)-1))]
        while(self.dst_node == self.src_node):                              # Ensure dst node is not equal to source
            self.dst_node = nodes[random.randint(0, (len(nodes)-1))]        # Randomly assign dest node from list         
        return self.dst_node
       
    def BitRate(self):
        bit_rates = [10E9, 40E9, 100E9, 160E9, 400E9]
        bit_rate = bit_rates[random.randint(0, (len(bit_rates)-1))]         # Randomly assign bit rate
        # Continuous option below
        # bit_rate = random.randint(10E9, 400E9)
        return bit_rate 

    def InterarrivalTime(self):
        interarrival_time = random.expovariate(self.H)                      # Randomly assign interarrival time
        while (interarrival_time == 0):  
            interarrival_time = random.expovariate(self.H) 
        return interarrival_time

    def DurationTime(self):
        duration_time = random.expovariate(1/self.mu)                       # Randomly assign duration time
        while (duration_time == 0):  
            duration_time = random.expovariate(1/self.mu)  
        return duration_time  
