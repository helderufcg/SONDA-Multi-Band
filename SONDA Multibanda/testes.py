import numpy as np
import matplotlib.pyplot as plt

Load = np.arange(70,300,20)

#Atenuação CTE e NF CTE
PB1 = [0.0009458482935005088, 0.004182298005462081, 0.009404152873909118,
       0.01675884028825205, 0.02624189781404991, 0.03764068204915873,
       0.04420475643179206, 0.05421229534858506, 0.06390593047034765,
       0.0730727073438071, 0.0821962847279303, 0.09550186228631459]

#Atenuação VAR e NF CTE
PB2 = [9.456102926276156e-05, 0.0006589290820986101, 0.0026699703099301534,
       0.0065055459779461994, 0.0121914050594331, 0.019726978615955182,
       0.027359781121751026, 0.03695764653706852, 0.046227810650887574,
       0.057501006267609685, 0.06430041152263374, 0.07594167679222358]

#Atenuação CTE e NF VAR
PB3 = [0.0003452853870044939, 0.0019268491007395246, 0.005994736621246545,
       0.01205734473154322, 0.020159258139300473, 0.02717391304347826,
       0.03888176056611843, 0.04578964238289299, 0.05810237638719424,
       0.06656460094521734, 0.07400281210686006, 0.08364001338240214]

#Atenuação VAR e NF VAR
PB4 = [2.2369755732333794e-05, 0.00023408420523847678, 0.0011470178682443516,
       0.003909120760558535, 0.008219020457141919, 0.015260186174271327,
       0.023299161230195712, 0.031562667676672033, 0.041786803727382894,
       0.05149330587023687, 0.061572563265808754, 0.07062645667066883]

plt.figure(1)
plt.plot(Load, PB1, marker='s', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "blue") 
plt.plot(Load, PB2, marker='o', markersize = 5, markeredgewidth = 3, markerfacecolor = 'w', linewidth = 3, color = "Orange")                  
plt.plot(Load, PB3, marker='^', markersize = 5, markeredgewidth = 2, markerfacecolor = 'w', linewidth = 3, color = "green")
plt.plot(Load, PB4, marker='d', markersize = 5, markeredgewidth = 2, markerfacecolor = 'w', linewidth = 3, color = "red")
plt.yscale('log')
plt.xlabel("Carga na rede (Erlangs)")
plt.ylabel("Probabilidade de Bloqueio")
plt.legend([r"$\alpha$ = CTE | F = CTE",r"$\alpha$ = VAR | F = CTE",r"$\alpha$ = CTE | F = VAR",r"$\alpha$ = VAR | F = VAR"])
plt.grid(True)
plt.show()