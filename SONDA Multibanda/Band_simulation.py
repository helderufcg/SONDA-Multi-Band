from turtle import width
import matplotlib.pyplot as plt
import numpy as np
from sympy import true
from Band_Selection import *

Band = Band_Selection()

NFl = NF_L(FL)
NFc = NF_C(FC)
#NFs = NF_S(FS)

LL = c/FL
LC = c/FC
LS = c/FS

'''
plt.figure(1)
plt.plot(FL, NFl, 'r-', linewidth=2)
plt.plot(FC, NFc, 'r-', linewidth=2)
plt.plot(FS, NFs, 'y-', linewidth=2)
plt.axis([184E12,206E12,3,9])
plt.legend(["Banda L", "Banda C","Banda S"])
plt.xlabel("Frequência (Hz)")
plt.ylabel("Fator de ruído (dB)")
plt.grid(true)
'''

plt.figure(2)
#plt.plot(LL, NFl, 'r-', linewidth=2)
plt.plot(LC, NFc, 'g-', linewidth=2)
#plt.plot(LS, NFs, 'y-', linewidth=2)
plt.axis([1530E-9,1565E-9,4,5])
plt.legend(["Banda C", "Banda L","Banda S"])
plt.xlabel("Comprimento de onda (m)")
plt.ylabel("Fator de ruído (dB)")
plt.grid(true)

plt.show()







'''
Load = np.arange(70,300,10)

PB22 = [0.0001, 0.00049, 0.00113, 0.00224,
        0.00391, 0.00634, 0.00911, 0.01273,
        0.01612, 0.01977, 0.02473, 0.02881,
        0.03356, 0.03862, 0.04279, 0.04856,
        0.05313, 0.0587, 0.06316, 0.06779,
        0.07354, 0.07727, 0.0822]

PB21 = [4e-05, 0.00021, 0.00059, 0.00147,
        0.00273, 0.00434, 0.00655, 0.00904,
        0.01187, 0.01555, 0.01938, 0.02353,
        0.02797, 0.03234, 0.03663, 0.04127,
        0.04668, 0.05062, 0.05718, 0.06162,
        0.06592, 0.07109, 0.07534]

PB20 = [1e-05, 2e-05, 0.00016, 0.00062,
        0.00109, 0.00231, 0.00387, 0.00573,
        0.00844, 0.01131, 0.0154, 0.01962,
        0.02343, 0.02802, 0.03236, 0.03684,
        0.04127, 0.04707, 0.05203, 0.05771,
        0.0626, 0.06625, 0.07101]

PB19 = [0.0, 1E-5, 2E-5, 0.00016, 0.00042,
       0.00082, 0.00179, 0.00278, 0.00436,
       0.00665, 0.00962, 0.0133, 0.01713,
       0.02117, 0.02525, 0.02997, 0.03443,
       0.03928, 0.0449, 0.04956, 0.05478,
       0.05999, 0.06516]

plt.figure(1)
plt.plot(Load, PB22, marker='o', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "blue") 
plt.plot(Load, PB21, marker='o', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "Orange")                  
plt.plot(Load, PB20, marker='o', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "green")
plt.plot(Load, PB19, marker='o', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "red")
plt.yscale('log')
plt.xlabel("Carga na rede (Erlangs)")
plt.ylabel("Probabilidade de Bloqueio")
plt.legend([r"$\alpha$ = $0.22$ dB/km ",r"$\alpha$ = $0.21$ dB/km",r"$\alpha$ = $0.20$ dB/km",r"$\alpha$ = $0.1912$ dB/km"])
plt.grid(true)
plt.show()
'''