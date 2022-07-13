import matplotlib.pyplot as plt
import numpy as np
from sympy import true
from BandSelection import *

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
Load = np.arange(500,1001,50)

PB22 = [0.019532775998124852, 0.030827090847436726, 0.04421061939077767,
        0.054860653938994954, 0.06405329233922624, 0.07905138339920949,
        0.09260116677470136, 0.10607828577490187, 0.11873664212776062,
        0.12810658467845248, 0.135464643727987]

PB21 = [0.009143609531298575, 0.01881255173451727, 0.03036652394400413,
        0.04114379757251594, 0.0519318653926049, 0.06208480784751971,
        0.07346459006758742, 0.08579272477693892, 0.09614460148062687,
        0.10264832683227264, 0.1177301624676242]

PB20 = [0.0032732474214993436, 0.009202510444849354, 0.019482543640897756,
        0.031142946122703206, 0.03999360102383619, 0.05044136191677175,
        0.05928736586233474, 0.0713368526180625, 0.08167932696234582,
        0.09336196433572963, 0.10184336490477645]

PB19 = [0.000939720677425842, 0.003574121927595438, 0.009548180116869724,
        0.01992269992429374, 0.029239766081871343, 0.03892868265337901,
        0.049907670809003345, 0.05933309600094933, 0.06691201070592172,
        0.07716644802839726, 0.09053870529651425]

plt.figure(1)
plt.plot(Load, PB22, marker='o', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "blue") 
plt.plot(Load, PB21, marker='o', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "Orange")                  
plt.plot(Load, PB20, marker='o', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "green")
plt.plot(Load, PB19, marker='o', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "red")
plt.yscale('log')
plt.xlabel("Carga na rede (Erlangs)")
plt.ylabel("Probabilidade de Bloqueio")
plt.legend([r"$\alpha$ = $0.22$ dB/km ",r"$\alpha$ = $0.21$ dB/km",r"$\alpha$ = $0.20$ dB/km",r"$\alpha$ = $0.19$ dB/km"])
plt.grid(true)
plt.show()
