import os
from Fiber import Fiber
from PhysicalConstants import FcentralC
from Topology import *
from Band_Selection import *
from RoutingWavelengthAssignment import RWA
from Simulation_NetworkLoad import Simulation_NetworkLoad
from Grafics import Grafics
from FirstFit_ResourceAlgorithm import FirstFit
import multiprocessing as mp
import time

os.system('cls')

def main():
        '''
        with open('Modulations.txt','a') as text:
                text.write('[')
        '''
        # --------------- Simualtion Types ------------------
        '''
        print('\n1 - Network load variation with fixed number of calls  \n2 - Network load variation with fixed number of blockages \n3 - Percentage variation on the network traffic load \n4 - BER variation')
        simualtion_type = int(input('\n>>> Define a simulation to run: '))
        if simualtion_type == 1 or simualtion_type == 2 or simualtion_type == 3 or simualtion_type == 4:
                pass
        else:
                raise ValueError('Invalid simualtion type.')
        '''
        #Escolha automática do tipo de simulação
        simualtion_type = 1
        # --------------- Topologies ------------------
       

        '''
        print('\n1 - Simple topology \n2 - Topology 1 \n3 - European \n4 - German \n5 - NSFNet \n6 - PacificBell \n7 - US Backbone')       
        topology = int(input('\n>>> Select a network topology: '))
        if topology == 1:
                n_nodes = len(adj01)
                A = adj01
                links = links01
        elif topology == 2:
                n_nodes = len(adjTop1)
                A = adjTop1
                links = linksTop1        
        elif topology == 3:        
                n_nodes = len(adjEuropean)
                A = adjEuropean
                links = linksEuropean
        elif topology == 4:
                n_nodes = len(adjGerman) 
                A = adjGerman
                links = linksGerman
        elif topology == 5:
                n_nodes = len(adjNSFNet) 
                A = adjNSFNet
                links = linksNSFNet       
        elif topology == 6:
                n_nodes = len(adjPacificBell) 
                A = adjPacificBell
                links = linksPacificBell         
        elif topology == 7:
                n_nodes = len(adjUSBackbone)
                A = adjUSBackbone
                links = linksUSBackbone         
        else:
                raise ValueError('Invalid network topology.')
        '''
        #Escolha automática da topologia
        
        n_nodes = len(adjNSFNet) 
        A = adjNSFNet
        links = linksNSFNet
        '''
        n_nodes = len(adj01)
        A = adj01
        links = links01
        '''
        # --------------- Fiber selection ------------------
        '''
        print('\n1 - ITU-T G652-D \n2 - ITU-T G652-A ')       
        fiber_type = int(input('\n>>> Select fiber type: '))
        '''

        # --------------- Band selection ------------------
        #Escolha automática do tipo da fibra
        
        fiber_type = 1 #1 == G652-D ; 2 == G652-A
        cont = 1
        all_slots = 64
        band_selection = Band_Selection()
        control= [0, 0, 0, 0, 0]
        '''
        
        if fiber_type == 1 or fiber_type == 2:
                while(cont!=0):
                        print('All Slots:', all_slots)
                        print('\n| Banda O:',control[0],' | Banda E:',control[1],' | Banda S:',control[2],' | Banda C:',control[3],' | Banda L:',control[4])
                        print('\n1 - O-Band \n2 - E-Band \n3 - S-Band \n4 - C-Band \n5 - L-Band \n6 - Default \n7 - Clear \n8 - Close')
                        band = int(input('\n>>> Select the bands (One at a time): '))
                        print('\n')

                        if band == 1:
                                if control[0] == 0:
                                        all_slots = all_slots + len(band_selection.getSlotsAttenuation_O(fiber_type))
                                        control[0] = 1
                                else:
                                        raise ValueError('The band has already been selected.')
                        elif band ==2:
                                if control[1] == 0:
                                        all_slots = all_slots + len(band_selection.getSlotsAttenuation_E(fiber_type))
                                        control[1] = 1
                                else:
                                        raise ValueError('The band has already been selected.')
                        elif band ==3:
                                if control[2] == 0:
                                        all_slots = all_slots + len(band_selection.getSlotsAttenuation_S(fiber_type))
                                        control[2] = 1
                                else:
                                        raise ValueError('The band has already been selected.')        
                        elif band ==4:
                                if control[3] == 0:
                                        all_slots = all_slots + len(band_selection.getSlotsAttenuation_C(fiber_type))
                                        control[3] = 1
                                else:
                                        raise ValueError('The band has already been selected.')        
                        elif band ==5:
                                if control[4] == 0:
                                        all_slots = all_slots + len(band_selection.getSlotsAttenuation_L(fiber_type))
                                        control[4] = 1
                                else:
                                        raise ValueError('The band has already been selected.')        
                        elif band == 6:
                                all_slots = 32
                                control = [0, 0, 0, 1, 0]
                        elif band == 7:
                                all_slots = 0
                                control = [0, 0, 0, 0, 0]
                        elif band == 8:
                                cont = 0
                        else:
                                raise ValueError('Invalid band.')
        
        else:
                raise ValueError('Invalid fiber type.') #Falta implementar a modelagem para fibras com o pico d'água -> Fazer fit da função atenuação de cada banda
        '''
        # --------------- Network Types ------------------
        '''
        print('\n1 - WDM  \n2 - EON')    
        network_type = int(input('\n>>> Select a network type: '))
        if network_type == 1 or network_type == 2:
                if network_type == 1:
                        wavelength_bandwidth = int(input('\n>>> Enter the wavelength bandwidth in GHz: '))
                        if wavelength_bandwidth < 0:
                                raise ValueError('The wavelength bandwidth must be positive.')
                        consider_ase_noise = 0
                        damp = None                       
                else:        
                        wavelength_bandwidth = None
        else:
                raise ValueError('Invalid network type.')
        '''
        wavelength_bandwidth = None
        network_type = 2 #EON

        # --------------- Consider ASE ------------------
        '''
        consider_ase_noise = int(input('\n>>> Consider ASE noise? (0 - No | 1 - Yes): '))
        if consider_ase_noise == 0 or consider_ase_noise == 1:
                pass
        else:        
                raise ValueError('The option entered is invalid.')
        '''
        consider_ase_noise = 1 #ASE ativado

        # --------------- Network Types ------------------
        '''
        damp = float(input('\n>>> Enter the distance between inline amplifiers in Km: '))
        if damp < 0:
                raise ValueError('The distance between inline amplifiers must be positive.')
        '''
        damp = 70 #Distância entre os amplificadores de linha de 60Km    
        
        # --------------- Parameters and Simulation  ------------------
        first_fit = FirstFit(all_slots)
        rwa = RWA()
        slots, times = rwa.Generate(n_nodes, links, first_fit)
        N = slots.copy() #shallow copy da matriz de slots
        T = times.copy() #shallow copy da matriz de tráfego
        simulation = Simulation_NetworkLoad(all_slots, 193.4E12, fiber_type)
        grafics = Grafics()
        load_bp = []
        pool = mp.Pool(mp.cpu_count()) #cria um processo para cada núcleo e thread               

        # --------------- Simulation interval  ------------------
        '''
        if simualtion_type == 1 or simualtion_type == 2 or simualtion_type == 4:
                min_traffic_load = int(input('\n>>> Enter the min. traffic load: '))    
                if min_traffic_load < 0:
                        raise ValueError('Invalid network load.')
                max_traffic_load = int(input('\n>>> Enter the max. traffic load: '))
                if max_traffic_load < 0 or max_traffic_load < min_traffic_load:
                        raise ValueError('Invalid network load.')                
                traffic_load_step = int(input('\n>>> Enter the traffic load step: '))
                if traffic_load_step < 0:
                        raise ValueError('Invalid network load.')
        else:                 
                traffic_load = int(input('\n>>> Enter the traffic load: '))
                if traffic_load < 0:
                        raise ValueError('Invalid network load.')
                min_percentage = int(input('\n>>> Enter the min. percentage variation: '))
                if min_percentage < 0:
                        raise ValueError('Invalid percentage.')
                max_percentage = int(input('\n>>> Enter the max. percentage variation: '))
                if max_percentage < 0:
                        raise ValueError('Invalid percentage.')
                percentage_step = int(input('\n>>> Enter the percentage step: '))
                if percentage_step < 0:
                        raise ValueError('Invalid percentage.')
        '''
        min_traffic_load = 70
        max_traffic_load = 300
        traffic_load_step = 20
        """
        traffic_load = 5000
        min_percentage = 0.2
        max_percentage = 0.7
        percentage_step = 0.01
        """
        # --------------- Simulation interval  ------------------

        if simualtion_type == 1:
                
                '''
                n_calls = int(input('\n>>> Enter the number of calls: '))
                if n_calls < 0:
                        raise ValueError('Invalid number of calls.')
                print('\nSimulation in progress...\n')
                '''

                n_calls = 10000 #Número de chamadas
                print('\nSimulation in progress...\n')
                t1 = time.time()
                for load in range(min_traffic_load, max_traffic_load, traffic_load_step):
                        r = pool.apply_async(simulation.FixedCalls, args=(load, n_calls, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise, damp), callback=load_bp.append)
                pool.close()
                pool.join()
                t2 = time.time()
                grafics.plot_topology(A)
                grafics.plot_blocking_probability(load_bp)
                

        #----------------------------Testar depois-------------------------------------
        elif simualtion_type == 2:
                '''
                n_blockages = int(input('\n>>> Enter the number of blocked calls: '))        
                if n_blockages < 0:
                        raise ValueError('Invalid number of blockages.')
                '''
                n_blockages = 1000
                print('\nSimulation in progress...\n')
                t1 = time.time()
                for load in range(min_traffic_load, max_traffic_load, traffic_load_step):
                        r = pool.apply_async(simulation.FixedBlockages, args=(load, n_blockages, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise, damp), callback=load_bp.append)
                pool.close()
                pool.join()
                t2 = time.time()    
                grafics.plot_blocking_probability(load_bp)

        elif simualtion_type == 3:                  
                n_calls = int(input('\n>>> Enter the number of calls: '))
                print('\nSimulation in progress...\n')                
                t1 = time.time()
                for percentage in range(min_percentage, max_percentage, percentage_step):
                        r = pool.apply_async(simulation.LoadVariation, args=(percentage, traffic_load, n_calls, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise, damp), callback=load_bp.append)
                pool.close()
                pool.join()            
                t2 = time.time()
                # simulation.SaveResults(sorted(load_bp))

        else: 
                #n_calls = int(input('\n>>> Enter the number of calls: '))
                n_calls = 10000 #Número de chamadas
                print('\nSimulation in progress...\n')                
                t1 = time.time()
                for load in range(min_traffic_load, max_traffic_load, traffic_load_step):
                        r = pool.apply_async(simulation.BERVariation, args=(load, n_calls, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise, damp), callback=load_bp.append)
                pool.close()
                pool.join()            
                t2 = time.time()   
                grafics.plot_BER_variation(sorted(load_bp), n_calls)



        # --------------- Results ------------------

        simulation.ShowResults(sorted(load_bp), simualtion_type)
        print('\nTime taken =', t2-t1, 'seconds')
        '''
        with open('Modulations.txt','a') as text:
                text.write(']\n')
        '''        
if __name__ == '__main__':
    main()
