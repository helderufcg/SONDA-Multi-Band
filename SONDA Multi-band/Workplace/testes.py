import numpy as np
import matplotlib.pyplot as plt

Load = np.arange(500,1001,50)

#Atenuação CTE e NF CTE
PB1 = [0.019532775998124852, 0.030827090847436726, 0.04421061939077767,
       0.054860653938994954, 0.06405329233922624, 0.07905138339920949,
       0.09260116677470136, 0.10607828577490187, 0.11873664212776062,
       0.12810658467845248, 0.135464643727987]

#Atenuação CTE e NF VAR
PB2 = [0.008085316257145399, 0.017542936336684033, 0.02873315518777117,
       0.03994726960412256, 0.05070479667376534, 0.06002761270184285,
       0.07220216606498195, 0.08289124668435013, 0.0904895484571532,
       0.10414496979795876, 0.11771630370806356]

#Atenuação VAR e NF CTE
PB3 = [0.0007701567345970578, 0.0033466082125765536, 0.008998713184014686,
       0.018726591760299626, 0.028740587457607634, 0.037520636349992496,
       0.050261359067149174, 0.058913632614587014, 0.0666045024643666,
       0.07828401440425865, 0.08654262224145391]

#Atenuação VAR e NF VAR
PB4 = [0.0002218009482877743, 0.0012583396460038908, 0.003972873221642624,
       0.01000050002500125, 0.02000880387370443, 0.02894356005788712,
       0.038887808671981335, 0.04680114194786353, 0.0552761041401802,
       0.06393044367727913, 0.074855902387903283]

plt.figure(1)
plt.plot(Load, PB1, marker='s', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "blue") 
plt.plot(Load, PB2, marker='o', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "Orange")                  
plt.plot(Load, PB3, marker='^', markersize = 5, markeredgewidth = 2, markerfacecolor = 'w', linewidth = 3, color = "green")
plt.plot(Load, PB4, marker='d', markersize = 5, markeredgewidth = 2, markerfacecolor = 'w', linewidth = 3, color = "red")
plt.yscale('log')
plt.xlabel("Carga na rede (Erlangs)")
plt.ylabel("Probabilidade de Bloqueio")
plt.legend([r"$\alpha$ = CTE | F = CTE",r"$\alpha$ = CTE | F = VAR",r"$\alpha$ = VAR | F = CTE",r"$\alpha$ = VAR | F = VAR"])
plt.grid(True)
plt.show()