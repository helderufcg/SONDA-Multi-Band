from CallGenerator import Call
from RoutingWavelengthAssignment import n_slots, RWA
import random
from prettytable import PrettyTable
import pandas as pd

'''
The Simulation_NetworkLoad class is the simulation that varies the
network load and analyses the effect on the call blocking probability.

This simulation varies the network load, and analyzes the network performance
in terms of predefined metrics, such as call blocking probability,
or slot blocking probability.
'''

class Simulation_NetworkLoad:

    def __init__(self):
        pass

    def NewLoad(self, percentage, load):
        random.seed()
        param_01 = 1-(percentage/200)
        param_02 = 1+(percentage/200) 
        new_load = random.uniform(load*param_01, load*param_02)
        return new_load

    def FixedCalls(self, load, n_calls, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise, damp):
        call = Call(n_nodes, load, 1)                
        rwa = RWA()           
        count_block = 0
        number = 1            

        random.seed(0)
        for gen in range(n_calls):
            src_node = call.Src()
            dst_node = call.Dst()
            bit_rate = call.BitRate()        
            interarrival_time = call.InterarrivalTime()
            duration_time = call.DurationTime()

            count_block += rwa.RWA(A, N, T, src_node, dst_node, duration_time, bit_rate, network_type, wavelength_bandwidth, consider_ase_noise, damp, number)
                            
            # update all channels that are still in use
            for link in links:
                i, j = link
                for s in range(n_slots):
                    # dijkstra + first-fit
                    if T[i][j][s] > interarrival_time:
                        T[i][j][s] -= interarrival_time
                    else:
                        T[i][j][s] = 0
                        if not N[i][j][s]:
                            N[i][j][s] = 1 # free channel 

        blocked = count_block/n_calls
        return load, blocked  

    def FixedBlockages(self, load, n_blockages, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise, damp):
        call = Call(n_nodes, load, 1) 
        rwa = RWA()           
        n_calls = 0
        count_block = 0
        number = 1  
         
        random.seed(0)  
        while count_block < n_blockages:
            src_node = call.Src()
            dst_node = call.Dst()
            bit_rate = call.BitRate()        
            interarrival_time = call.InterarrivalTime()
            duration_time = call.DurationTime()                                           

            count_block += rwa.RWA(A, N, T, src_node, dst_node, duration_time, bit_rate, network_type, wavelength_bandwidth, consider_ase_noise, damp, number)
                            
            # update all channels that are still in use
            for link in links:
                i, j = link
                for s in range(n_slots):
                    # dijkstra + first-fit
                    if T[i][j][s] > interarrival_time:
                        T[i][j][s] -= interarrival_time
                    else:
                        T[i][j][s] = 0
                        if not N[i][j][s]:
                            N[i][j][s] = 1 # free channel 
                            
            n_calls += 1

        blocked = count_block/n_calls
        return load, blocked

    def LoadVariation(self, percentage, load, n_calls, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise, damp):
        rwa = RWA()           
        count_block = 0     
        new_load = []
        number = 1 

        for gen in range(n_calls):
            new_load.append(self.NewLoad(percentage, load))

        random.seed(0)
        for gen in range(n_calls):
            call = Call(n_nodes, new_load[gen], 1)
            src_node = call.Src()
            dst_node = call.Dst()
            bit_rate = call.BitRate()
            interarrival_time = call.InterarrivalTime()
            duration_time = call.DurationTime()

            count_block += rwa.RWA(A, N, T, src_node, dst_node, duration_time, bit_rate, network_type, wavelength_bandwidth, consider_ase_noise, damp, number)
                            
            # update all channels that are still in use
            for link in links:
                i, j = link
                for s in range(n_slots):
                    # dijkstra + first-fit
                    if T[i][j][s] > interarrival_time:
                        T[i][j][s] -= interarrival_time
                    else:
                        T[i][j][s] = 0
                        if not N[i][j][s]:
                            N[i][j][s] = 1 # free channel 

        blocked = count_block/n_calls
        return percentage, blocked 

    def BERVariation(self, load, n_calls, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise, damp):
        call = Call(n_nodes, load, 1)
        rwa = RWA()           
        n_calls01 = 0
        n_calls02 = 0
        n_calls03 = 0
        n_calls04 = 0
        n_blockages01 = 0
        n_blockages02 = 0
        n_blockages03 = 0
        n_blockages04 = 0
        count_block = 0
        count = [0]*n_calls
        
        random.seed(0)
        for gen in range(n_calls):
            number = random.randint(1, 100)
            src_node = call.Src()
            dst_node = call.Dst()
            bit_rate = call.BitRate()
            interarrival_time = call.InterarrivalTime()
            duration_time = call.DurationTime()

            count_block += rwa.RWA(A, N, T, src_node, dst_node, duration_time, bit_rate, network_type, wavelength_bandwidth, consider_ase_noise, damp, number)
            count[gen] = count_block
            
            if number > 0 and number <= 25:
                n_calls01 += 1
                if (count[gen]-count[gen-1]):
                    n_blockages01 += 1
            elif number > 25 and number <= 50:   
                n_calls02 += 1
                if (count[gen]-count[gen-1]):
                    n_blockages02 += 1
            elif number > 50 and number <= 75:    
                n_calls03 += 1 
                if (count[gen]-count[gen-1]):
                    n_blockages03 += 1
            else:    
                n_calls04 += 1
                if (count[gen]-count[gen-1]):
                    n_blockages04 += 1

            # update all channels that are still in use
            for link in links:
                i, j = link
                for s in range(n_slots):
                    # dijkstra + first-fit
                    if T[i][j][s] > interarrival_time:
                        T[i][j][s] -= interarrival_time
                    else:
                        T[i][j][s] = 0
                        if not N[i][j][s]:
                            N[i][j][s] = 1 # free channel 

        blocked = count_block/n_calls
        return load, blocked, n_calls01, n_blockages01, n_calls02, n_blockages02, n_calls03, n_blockages03, n_calls04, n_blockages04 

    def ShowResults(self, load_bp, simulation_type):
        results = PrettyTable()
        if simulation_type == 1 or simulation_type == 2:
            results.field_names = ['Load', 'Blocking probability']
            for i, j in load_bp:        
                results.add_row([i, j])
        elif simulation_type == 3:    
            results.field_names = ['Load variation (%)', 'Blocking probability']
            for i, j in load_bp:        
                results.add_row([i, j])
        else: 
            results.field_names = ['Load', 'Total bp', 'Calls (E-3)', 'Blockages (E-3)', 'Calls (E-6)', 'Blockages (E-6)', 'Calls (E-9)', 'Blockages (E-9)', 'Calls (E-12)', 'Blockages (E-12)']
            for i, j, k, l, m, n, o, p, q, r in load_bp:        
                results.add_row([i, j, k, l, m, n, o, p, q, r])
        return print(results)

    def SaveResults(self, load_bp):      
        load, BP = zip(*load_bp)
        with open('RESULTS.txt', 'a') as text_file:
                for item in BP:
                        text_file.write("%s " % item)
                text_file.write('\n') 
        df = pd.read_table('RESULTS.txt', delimiter=' ', index_col=False)
        df.to_excel('RESULTS.xlsx', 'Sheet1')
