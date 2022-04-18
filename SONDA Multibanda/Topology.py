import numpy as np

# topo01

adj01 = np.array([[0, 4, 3, 2],  #distâncias entre os nós
                  [4, 0, 5, 7],
                  [3, 5, 0, 14],
                  [2, 7, 14, 0]
                 ])

links01 = [	(0,1), (0,2), (0,3),   # 0 #links entre os nós
			      (1,0), (1,2), (1,3),   # 1
			      (2,0), (2,1), (2,3),   # 2
			      (3,0), (3,1), (3,2)    # 3
		      ]                  

# Top1

adjTop1 = np.array([[0, 730, 340, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [730, 0, 0, 690, 620, 1830, 0, 0, 0, 0, 0, 0],
                    [340, 0, 0, 540, 0, 0, 0, 740, 0, 0, 0, 0],
                    [0, 690, 540, 0, 0, 0, 0, 0, 200, 0, 0, 0],
                    [0, 620, 0, 0, 0, 0, 870, 0, 0, 840, 0, 0],
                    [0, 1830, 0, 0, 0, 0, 370, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 870, 370, 0, 0, 0, 0, 1100, 0],
                    [0, 0, 740, 0, 0, 0, 0, 0, 280, 0, 0, 180],
                    [0, 0, 0, 200, 0, 0, 0, 280, 0, 440, 0, 160],
                    [0, 0, 0, 0, 840, 0, 0, 0, 440, 0, 830, 500],
                    [0, 0, 0, 0, 0, 0, 1100, 0, 0, 830, 0, 1330],
                    [0, 0, 0, 0, 0, 0, 0, 180, 160, 500, 1330, 0]
                   ])                   

linksTop1 = [ (0,1), (0,2),                       # 0
			        (1,0), (1,3), (1,4), (1,5),         # 1
			        (2,0), (2,3), (2,7),                # 2
			        (3,1), (3,2), (3,8),                # 3
              (4,1), (4,6), (4,9),                # 4
              (5,1), (5,6),                       # 5
              (6,4), (6,5), (6,10),               # 6
              (7,2), (7,8), (7,11),               # 7
              (8,3), (8,7), (8,9), (8,11),        # 8
              (9,4), (9,8), (9,10), (9,11),       # 9
              (10,6), (10,9), (10,11),            # 10
              (11,7), (11,8), (11,9), (11,10)     # 11
		        ]             

#European        

adjEuropean = np.array([[0, 462, 0, 1067, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [462, 0, 690, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 690, 0, 540, 0, 514, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1067, 0, 540, 0, 259, 0, 0, 0, 0, 0, 0, 0, 0, 552, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 259, 0, 393, 0, 0, 0, 0, 0, 0, 474, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 514, 0, 393, 0, 747, 0, 0, 594, 0, 600, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 747, 0, 834, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 834, 0, 760, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 760, 0, 796, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 594, 0, 0, 796, 0, 507, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 507, 0, 218, 0, 0, 0, 0, 0, 0, 0, 0, 327, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 600, 0, 0, 0, 0, 218, 0, 271, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 474, 0, 0, 0, 0, 0, 0, 271, 0, 592, 0, 0, 0, 0, 0, 456, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 552, 0, 0, 0, 0, 0, 0, 0, 0, 592, 0, 381, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 381, 0, 540, 0, 0, 775, 757, 0, 420, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 540, 0, 722, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 722, 0, 623, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 623, 0, 1123, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 775, 0, 0, 1123, 0, 0, 0, 0, 0, 819, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 456, 0, 757, 0, 0, 0, 0, 0, 522, 0, 534, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 327, 0, 0, 0, 0, 0, 0, 0, 0, 522, 0, 0, 0, 0, 0, 0, 720, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 420, 0, 0, 0, 0, 0, 0, 0, 376, 668, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 534, 0, 376, 0, 0, 0, 400, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 819, 0, 0, 668, 0, 0, 474, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 474, 0, 551, 0, 1209],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 400, 0, 551, 0, 783, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 720, 0, 0, 0, 0, 783, 0, 1500],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1209, 0, 1500, 0]
                       ])

linksEuropean = [ (0, 1), (0, 3),                                     # 0 
                  (1, 0), (1, 2),                                     # 1
                  (2, 1), (2, 3), (2, 5),                             # 2
                  (3, 0), (3, 2), (3, 4), (3, 13),                    # 3 
                  (4, 3), (4, 5), (4, 12),                            # 4 
                  (5, 2), (5, 4), (5, 6), (5, 9), (5, 11),            # 5
                  (6, 5), (6, 7),                                     # 6
                  (7, 6), (7, 8),                                     # 7
                  (8, 7), (8, 9),                                     # 8
                  (9, 5), (9, 8), (9, 10),                            # 9
                  (10, 9), (10, 11), (10, 20),                        # 10
                  (11, 5), (11, 10), (11, 12),                        # 11
                  (12, 4), (12, 11), (12, 13), (12, 19),              # 12
                  (13, 3), (13, 12), (13, 14),                        # 13
                  (14, 13), (14, 15), (14, 18), (14, 19), (14, 21),   # 14
                  (15, 14), (15, 16),                                 # 15
                  (16, 15), (16, 17),                                 # 16
                  (17, 16), (17, 18),                                 # 17 
                  (18, 14), (18, 17), (18, 23),                       # 18
                  (19, 12), (19, 14), (19, 20), (19, 22),             # 19
                  (20, 10), (20, 19), (20, 26),                       # 20
                  (21, 14), (21, 22), (21, 23),                       # 21
                  (22, 19), (22, 21), (22, 25),                       # 22
                  (23, 18), (23, 21), (23, 24),                       # 23
                  (24, 23), (24, 25), (24, 27),                       # 24
                  (25, 22), (25, 24), (25, 26),                       # 25
                  (26, 20), (26, 25), (26, 27),                       # 26
                  (27, 24), (27, 26)                                  # 27
                ] 

# German                

adjGerman = np.array([[0, 36, 0, 37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],          
                      [36, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 41, 0, 88, 0, 0, 0, 0, 182, 0, 0, 0, 0, 0, 0, 0, 0],
                      [37, 0, 88, 0, 278, 0, 0, 208, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 278, 0, 144, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 144, 0, 144, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 144, 0, 157, 0, 306, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 208, 0, 120, 157, 0, 316, 298, 258, 0, 0, 0, 0, 0, 0],
                      [0, 0, 182, 0, 0, 0, 0, 316, 0, 0, 353, 224, 85, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 306, 298, 0, 0, 174, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 258, 353, 174, 0, 275, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 224, 0, 275, 0, 0, 0, 187, 0, 179],
                      [0, 0, 0, 0, 0, 0, 0, 0, 85, 0, 0, 0, 0, 64, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 74, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 187, 0, 74, 0, 86, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 0, 143],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 179, 0, 0, 0, 143, 0]
                     ])            

linksGerman = [ (0, 1), (0, 3),                                     # 0
                (1, 0), (1, 2),                                     # 1  
                (2, 1), (2, 3), (2, 8),                             # 2
                (3, 0), (3, 2), (3, 4), (3, 7),                     # 3
                (4, 3), (4, 5),                                     # 4
                (5, 4), (5, 6), (5, 7),                             # 5
                (6, 5), (6, 7), (6, 9),                             # 6
                (7, 3), (7, 5), (7, 6), (7, 8), (7, 9), (7, 10),    # 7
                (8, 2), (8, 7), (8, 10), (8, 11), (8, 12),          # 8
                (9, 6), (9, 7), (9, 10),                            # 9
                (10, 7), (10, 8), (10, 9), (10, 11),                # 10
                (11, 8), (11, 10), (11, 14), (11, 16),              # 11  
                (12, 8), (12, 13),                                  # 12
                (13, 12), (13, 14),                                 # 13
                (14, 11), (14, 13), (14, 15),                       # 14   
                (15, 14), (15, 16),                                 # 15 
                (16, 11), (16, 15)                                  # 16  
              ]

# NSFNet              

adjNSFNet = np.array([[0, 1136, 1702, 0, 0, 0, 0, 2838, 0, 0, 0, 0, 0, 0],
                      [1136, 0, 683, 959, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1702, 683, 0, 0, 0, 2049, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 959, 0, 0, 573, 0, 0, 0, 0, 0, 2349, 0, 0, 0],
                      [0, 0, 0, 573, 0, 1450, 732, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 2049, 0, 1450, 0, 0, 0, 0, 1128, 0, 0, 0, 1976],
                      [0, 0, 0, 0, 732, 0, 0, 718, 0, 0, 0, 0, 0, 0],
                      [2838, 0, 0, 0, 0, 0, 718, 0, 706, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 706, 0, 839, 0, 366, 451, 0],
                      [0, 0, 0, 0, 0, 1128, 0, 0, 839, 0, 0, 0, 0, 0],
                      [0, 0, 0, 2349, 0, 0, 0, 0, 0, 0, 0, 596, 789, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 366, 0, 596, 0, 0, 385],
                      [0, 0, 0, 0, 0, 0, 0, 0, 451, 0, 789, 0, 0, 246],
                      [0, 0, 0, 0, 0, 1976, 0, 0, 0, 0, 0, 385, 246, 0]
                     ])             

linksNSFNet = [ (0, 1), (0, 2), (0, 7),               # 0
                (1, 0), (1, 2), (1, 3),               # 1
                (2, 0), (2, 1), (2, 5),               # 2
                (3, 1), (3, 4), (3, 10),              # 3
                (4, 3), (4, 5), (4, 6),               # 4
                (5, 2), (5, 4), (5, 9), (5, 13),      # 5
                (6, 4), (6, 7),                       # 6
                (7, 0), (7, 6), (7, 8),               # 7
                (8, 7), (8, 9), (8, 11), (8, 12),     # 8
                (9, 5), (9, 8),                       # 9
                (10, 3), (10, 11), (10, 12),          # 10
                (11, 8), (11, 10), (11, 13),          # 11
                (12, 8), (12, 10), (12, 13),          # 12 
                (13, 5), (13, 11), (13, 12)           # 13
              ]  

# PacificBell              

adjPacificBell = np.array([[0, 0, 650, 585, 650, 780, 975, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],          
                           [0, 0, 0, 520, 585, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [650, 0, 0, 0, 0, 0, 0, 390, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [585, 520, 0, 0, 0, 0, 0, 0, 910, 650, 0, 0, 650, 0, 0, 650, 0],
                           [650, 585, 0, 0, 0, 0, 0, 0, 780, 0, 0, 0, 0, 585, 0, 650, 0],
                           [780, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 975, 0, 0],
                           [975, 0, 0, 0, 0, 0, 0, 715, 0, 650, 650, 0, 0, 0, 0, 0, 0],
                           [0, 0, 390, 0, 0, 0, 715, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 910, 780, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 650, 0, 0, 650, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 650, 0, 0, 0, 0, 650, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 650, 0, 585, 0, 0, 0, 0],
                           [0, 0, 0, 650, 0, 0, 0, 0, 0, 0, 0, 585, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 585, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 585],
                           [0, 0, 0, 0, 0, 975, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 585],
                           [0, 0, 0, 650, 650, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 585, 585, 0, 0]
                          ])

linksPacificBell = [ (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),               # 0
                     (1, 3), (1, 4),                                       # 1
                     (2, 0), (2, 7),                                       # 2
                     (3, 0), (3, 1), (3, 8), (3, 9), (3, 12), (3, 15),    # 3
                     (4, 0), (4, 1), (4, 8), (4, 13), (4, 15),             # 4 
                     (5, 0), (5, 14),                                      # 5 
                     (6, 0), (6, 7), (6, 9), (6, 10),                     # 6
                     (7, 2), (7, 6),                                       # 7
                     (8, 3), (8, 4),                                       # 8
                     (9, 3), (9, 6),                                     # 9 
                     (10, 6), (10, 11),                                    # 10
                     (11, 10), (11, 12),                                   # 11
                     (12, 3), (12, 11),                                    # 12 
                     (13, 4), (13, 16),                                    # 13
                     (14, 5), (14, 16),                                    # 14
                     (15, 3), (15, 4),                                     # 15
                     (16, 13), (16, 14)                                    # 16 
                   ]                    

# USBackbone

adjUSBackbone = np.array([[0, 800, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [800, 0, 1100, 0, 0, 950, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 1100, 0, 250, 800, 0, 1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 250, 0, 800, 0, 850, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 800, 800, 0, 0, 0, 1200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1000, 950, 0, 0, 0, 0, 1000, 0, 1200, 0, 1900, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 1000, 850, 0, 1000, 0, 1150, 1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1200, 0, 1150, 0, 0, 900, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1200, 1000, 0, 0, 1000, 1400, 1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 900, 1000, 0, 0, 0, 950, 850, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1900, 0, 0, 1400, 0, 0, 900, 0, 0, 1300, 0, 0, 0, 2600, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 10000, 0, 900, 0, 900, 0, 0, 1000, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 950, 0, 900, 0, 650, 0, 0, 1100, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 850, 0, 0, 650, 0, 0, 0, 0, 1200, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1300, 0, 0, 0, 0, 0, 0, 0, 0, 1300, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 1000, 0, 0, 0, 1000, 800, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1100, 0, 0, 1000, 0, 800, 0, 0, 0, 850, 1000, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1200, 0, 0, 800, 0, 0, 0, 0, 0, 0, 900],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2600, 0, 0, 0, 0, 0, 0, 0, 0, 1200, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1300, 0, 0, 0, 1200, 0, 700, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0, 700, 0, 300, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 800, 850, 0, 0, 0, 300, 0, 600, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 600, 0, 900],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 900, 0, 0, 0, 0, 900, 0]
                         ])                

linksUSBackbone = [ (0, 1), (0, 5),                                      # 0    
                    (1, 0), (1, 2), (1, 5),                              # 1
                    (2, 1), (2, 3), (2, 4), (2, 6),                      # 2
                    (3, 2), (3, 4), (3, 6),                              # 3
                    (4, 2), (4, 3), (4, 7),                              # 4
                    (5, 0), (5, 1), (5, 6), (5, 8), (5, 10),             # 5
                    (6, 2), (6, 3), (6, 5), (6, 7), (6, 8),              # 6
                    (7, 4), (7, 6), (7, 9),                              # 7
                    (8, 5), (8, 6), (8, 9), (8, 10), (8, 11),            # 8
                    (9, 7), (9, 8), (9, 12), (9, 13),                    # 9
                    (10, 5), (10, 8), (10, 11), (10, 14), (10, 18),      # 10
                    (11, 8), (11, 10), (11, 12), (11, 15),               # 11
                    (12, 9), (12, 11), (12, 13), (12, 16),               # 12
                    (13, 9), (13, 12), (13, 17),                         # 13
                    (14, 10), (14, 19),                                  # 14 
                    (15, 11), (15, 16), (15, 20), (15, 21),              # 15
                    (16, 12), (16, 15), (16, 17), (16, 21), (16, 22),    # 16
                    (17, 13), (17, 16), (17, 23),                        # 17
                    (18, 10), (18, 19),                                  # 18
                    (19, 14), (19, 18), (19, 20),                        # 19
                    (20, 15), (20, 19), (20, 21),                        # 20
                    (21, 15), (21, 16), (21, 20), (21, 22),              # 21
                    (22, 16), (22, 21), (22, 23),                        # 22 
                    (23, 17), (23, 22)                                   # 23 
                  ]

# Italian

adjItalian = np.array([[0, 140, 110, 0, 210, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [140, 0, 110, 0, 0, 95, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [110, 110, 0, 90, 0, 0, 0, 95, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 90, 0, 85, 0, 0, 95, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [210, 0, 0, 85, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 95, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 90, 0, 0, 0, 90, 0, 130, 120, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 95, 95, 0, 0, 130, 0, 0, 55, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 120, 0, 0, 60, 0, 0, 190, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 150, 55, 60, 0, 0, 110, 180, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 200, 0, 0, 0, 0, 0, 130, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 110, 0, 0, 120, 170, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 190, 180, 0, 120, 0, 460, 180, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 130, 170, 0, 0, 0, 200, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 460, 0, 0, 0, 0, 0, 420, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180, 200, 0, 0, 210, 90, 310, 350, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 210, 0, 100, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 100, 0, 0, 0, 200],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 420, 310, 0, 0, 150, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 350, 0, 0, 150, 0, 210],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 0, 210, 0]
                        ])

linksItalian = [
                (0, 1), (0, 2), (0, 4),                                     #0
                (1, 0), (1, 2), (1, 5), (1, 6),                             #1
                (2, 0), (2, 1), (2, 3), (2, 7),                             #2
                (3, 2), (3, 4), (3, 7),                                     #3
                (4, 0), (4, 3),                                             #4
                (5, 1), (5, 6),                                             #5
                (6, 1), (6, 5), (6, 7), (6, 8), (6, 9),                     #6
                (7, 2), (7, 3), (7, 6), (7, 9), (7, 10),                    #7
                (8, 6), (8, 9), (8, 12),                                    #8
                (9, 6), (9, 7), (9, 8), (9, 11), (9, 12),                   #9
                (10, 7), (10, 13),                                          #10
                (11, 9), (11, 12), (11, 13),                                #11
                (12, 8), (12, 9), (12, 11), (12, 14), (12, 15),             #12
                (13, 10), (13, 11), (13, 15),                               #13
                (14, 12), (14, 18),                                         #14
                (15, 12), (15, 13), (15, 16), (15, 18), (15, 17), (15, 19), #15
                (16, 15), (16, 17),                                         #16
                (17, 15), (17, 16), (17, 20),                               #17
                (18, 14), (18, 15), (18, 19),                               #18
                (19, 15), (19, 18), (19, 20),                               #19
                (20, 17), (20, 19)                                          #20
                ]

# Finland

adjFinland = np.array([
                        [0, 73, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [73, 0, 0, 69, 62, 183, 0, 0, 0, 0, 0, 0,],
                        [34, 0, 0, 54, 0, 0, 0, 74, 0, 0, 0, 0],
                        [0, 69, 54, 0, 0, 0, 0, 0, 20, 0, 0, 0],
                        [0, 62, 0, 0, 0, 0, 87, 0, 0, 84, 0, 0],
                        [0, 183, 0, 0, 0, 0, 37, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 87, 37, 0, 0, 0, 0, 110, 0],
                        [0, 0, 74, 0, 0, 0, 0, 0, 28, 0, 0, 18],
                        [0, 0, 0, 20, 0, 0, 0, 28, 0, 44, 0, 16],
                        [0, 0, 0, 0, 84, 0, 0, 0, 44, 0, 83, 50],
                        [0, 0, 0, 0, 0, 0, 110, 0, 0, 83, 0, 133],
                        [0, 0, 0, 0, 0, 0, 0, 18, 16, 50, 133, 0]
                    ])

linksFinland = [
                (0, 1), (0, 2),
                (1, 0), (1, 3), (1, 4), (1, 5),
                (2, 0), (2, 3), (2, 7),
                (3, 1), (3, 2), (3, 8),
                (4, 1), (4, 6), (4, 9),
                (5, 1), (5, 6),
                (6, 4), (6, 5), (6, 11),
                (7, 2), (7, 8), (7, 11),
                (8, 3), (8, 7), (8, 9), (8, 11),
                (9, 4), (9, 8), (9, 10), (9, 11),
                (10, 6), (10, 9), (10, 11),
                (11, 7), (11, 8), (11, 9), (11, 10)
                ]

# Japanese

adjJapanese = np.array([
                        [0, 160, 240, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [160, 0, 0, 240, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [240, 0, 0, 0, 240, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 240, 0, 0, 80, 40, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 240, 80, 0, 40, 80, 0, 240, 0, 0, 0, 0, 0],
                        [0, 0, 0, 40, 40, 0, 0, 160, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 80, 0, 0, 80, 0, 0, 0, 240, 0, 0],
                        [0, 0, 0, 0, 0, 160, 80, 0, 0, 160, 0, 0, 0, 0],
                        [0, 0, 0, 0, 240, 0, 0, 0, 0, 0, 0, 240, 0, 240],
                        [0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 40, 40, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 0, 40, 320, 0],
                        [0, 0, 0, 0, 0, 0, 240, 0, 240, 40, 40, 0, 320, 240],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 320, 320, 0, 160],
                        [0, 0, 0, 0, 0, 0, 0, 0, 240, 0, 0, 240, 160, 0]
                        ])

linksJapanese = [
                (0, 1), (0, 2),
                (1, 0), (1, 3),
                (2, 0), (2, 4),
                (3, 1), (3, 4), (3, 5),
                (4, 2), (4, 3), (4, 5), (4, 6), (4, 8),
                (5, 3), (5, 4), (5, 7),
                (6, 4), (6, 7), (6, 11),
                (7, 5), (7, 6), (7, 9),
                (8, 4), (8, 11), (8, 13),
                (9, 7), (9, 10), (9, 11),
                (10, 9), (10, 11), (10, 12),
                (11, 6), (11, 8), (11, 9), (11, 12), (11, 13),
                (12, 10), (12, 11), (12, 13),
                (13, 8), (13, 11), (13, 12)
                ]


# Ipê

adjIpe = np.array([
                  [0, 731, 966, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   #TO
                  [731, 0, 0, 0, 179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 737, 0, 0, 0, 0, 0, 0],                 #GO
                  [966, 0, 0, 482, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   #PA
                  [0, 0, 482, 0, 0, 654, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   #MA
                  [0, 179, 0, 0, 0, 1686, 0, 0, 0, 0, 0, 622, 0, 0, 0, 0, 0, 0, 931, 0, 0, 0],              #DF
                  [0, 0, 0, 654, 1686, 0, 0, 435, 0, 629, 0, 1895, 2194, 0, 0, 0, 0, 0, 0, 0, 0, 0],        #CE
                  [0, 0, 0, 0, 0, 0, 0, 0, 115, 195, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   #PB2
                  [0, 0, 0, 0, 0, 435, 0, 0, 176, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   #RN
                  [0, 0, 0, 0, 0, 0, 115, 176, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   #PB1
                  [0, 0, 0, 0, 0, 629, 195, 0, 0, 0, 670, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 196],               #PE
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 670, 0, 987, 0, 0, 0, 0, 0, 0, 0, 837, 273, 0],               #BA
                  [0, 0, 0, 0, 622, 1895, 0, 0, 0, 987, 0, 0, 497, 0, 0, 0, 0, 0, 0, 0, 0, 0],              #MG
                  [0, 0, 0, 0, 0, 2194, 0, 0, 0, 0, 0, 497, 0, 336, 0, 0, 0, 491, 361, 0, 0, 0],            #SP
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 336, 0, 766, 0, 551, 0, 0, 0, 0, 0],                 #PR
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 766, 0, 566, 0, 0, 0, 0, 0, 0],                   #MS
                  [0, 737, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 566, 0, 0, 0, 0, 0, 0, 0],                   #MT
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 551, 0, 0, 0, 382, 0, 0, 0, 0],                   #RS
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 491, 0, 0, 0, 382, 0, 0, 0, 0, 0],                   #SC
                  [0, 0, 0, 0, 931, 0, 0, 0, 0, 0, 0, 0, 361, 0, 0, 0, 0, 0, 0, 411, 0, 0],                 #RJ
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 837, 0, 0, 0, 0, 0, 0, 0, 411, 0, 0, 0],                   #ES
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 273, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 209],                   #SE
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 196, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 209, 0]                    #AL
                  ])

linksIpe = [
            (0, 1), (0, 2),                                         #TO - GO, PA
            (1, 0), (1, 4), (1, 15),                                #GO - TO, DF, MT
            (2, 0), (2, 3),                                         #PA - TO, MA
            (3, 2), (3, 5),                                         #MA - PA, CE
            (4, 1), (4, 5), (4, 11), (4, 18),                       #DF - GO, CE, MG, RJ
            (5, 3), (5, 4), (5, 7), (5, 9), (5, 11), (5, 12),       #CE - MA, DF, RN, PE, MG, SP
            (6, 8), (6, 9),                                         #PB2 - PB1, PE
            (7, 5), (7, 8),                                         #RN - CE, PB1
            (8, 6), (8, 7),                                         #PB1 - RN, PB2
            (9, 5), (9, 6), (9, 10), (9, 21),                       #PE - CE, PB2, BA, AL
            (10, 9), (10, 11), (10, 19), (10, 20),                  #BA - PE, MG, ES, SE
            (11, 4), (11, 5), (11, 10), (11, 12),                   #MG - CE, DF, BA, SP
            (12, 5), (12, 11), (12, 13), (12, 17), (12, 18),        #SP - CE, MG, PR, SC, RJ
            (13, 12), (13, 14), (13, 16),                           #PR - SP, MS, RS
            (14, 13), (14, 15),                                     #MS - PR, MT
            (15, 1), (15, 14),                                      #MT - GO, MS
            (16, 13), (16, 17),                                     #RS - PR, SC
            (17, 16), (17, 12),                                     #SC - SP, RS
            (18, 4), (18, 12), (18, 19),                            #RJ - DF, SP, ES
            (19, 10), (19, 18),                                     #ES - RJ, BA
            (20, 10), (20, 21),                                     #SE - BA, AL
            (21, 9), (21, 20)                                       #AL - PE, SE
        ]

# Abilane

linksAbilene = [
    (0, 1), (0, 4),
    (1, 0), (1, 2),
    (2,1), (2,3), (2,6),
    (3,2), (3,4),
    (4, 0), (4,5), (4,3),
    (5, 4), (5, 6), (5, 9),
    (6, 5), (6, 2), (6, 7),
    (7, 6), (7, 8),
    (8, 7), (8, 10), (8, 9),
    (9, 5), (9, 8), (9, 10),
    (10, 9), (10, 8)
]

adjAbilene = np.array([
    [0, 520, 0, 0, 610, 0, 0, 0, 0, 0, 0], #1-0
    [520, 0, 420, 0, 0, 0, 0, 0, 0, 0, 0], #2-1
    [0, 420, 0, 270, 0, 0, 270, 0, 0, 0, 0], #3-2
    [0, 0, 270, 0, 420, 0, 0, 0, 0, 0, 0], #4-3
    [610, 0, 0, 420, 0, 210, 0, 0, 0, 0, 0], #5-4
    [0, 0, 0, 0, 210, 0, 280, 0, 0, 430, 0], #6-5
    [0, 0, 0, 0, 0, 280, 0, 460, 0, 0, 0], #7-6
    [0, 0, 0, 0, 0, 0, 460, 0, 470, 0, 0], #8-7
    [0, 0, 0, 0, 0, 0, 0, 470, 0, 340, 420], #9-8
    [0, 0, 0, 0, 0, 430, 0, 0, 340, 0, 420], #10-9
    [0, 0, 0, 0, 0, 0, 0, 0, 420, 420, 0] #11-10
    ])

from GUI_SondaPaginaChamadas import Ui_OtherWindow

