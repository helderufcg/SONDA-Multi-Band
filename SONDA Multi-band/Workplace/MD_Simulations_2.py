import matplotlib.pyplot as plt
from Data_MD_2 import MD22, MD21, MD20, MD19
import seaborn as sns

plt.subplot(1,7,1)
sns.countplot(MD22).set_ylim([0,100000])
plt.title(r'$\alpha$ = 0,22 dB')
plt.ylabel("Número de chamadas")
plt.xlabel("Formatos de modulação (X-QAM)")
plt.grid(True)

plt.subplot(1,7,3)
sns.countplot(MD21).set_ylim([0,100000])
plt.title(r'$\alpha$ = 0,21 dB')
plt.ylabel("Número de chamadas")
plt.xlabel("Formatos de modulação (X-QAM)")
plt.grid(True)

plt.subplot(1,7,5)
sns.countplot(MD20).set_ylim([0,100000])
plt.title(r'$\alpha$ = 0,20 dB')
plt.ylabel("Número de chamadas")
plt.xlabel("Formatos de modulação (X-QAM)")
plt.grid(True)

plt.subplot(1,7,7)
sns.countplot(MD19).set_ylim([0,100000])
plt.title(r'$\alpha$ = 0,19 dB')
plt.ylabel("Número de chamadas")
plt.xlabel("Formatos de modulação (X-QAM)")
plt.grid(True)

plt.show()