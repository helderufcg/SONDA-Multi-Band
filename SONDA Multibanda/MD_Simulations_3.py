
import matplotlib.pyplot as plt
from Data_MD_3 import MD00, MD01, MD10, MD11
import seaborn as sns

plt.subplot(1,7,1)
sns.countplot(MD00).set_ylim([0,100000])
plt.title(r'$\alpha$ = CTE | F = CTE')
plt.ylabel("Número de chamadas")
plt.xlabel("Formatos de modulação (X-QAM)")
plt.grid(True)

plt.subplot(1,7,3)
sns.countplot(MD01).set_ylim([0,100000])
plt.title(r'$\alpha$ = CTE | F = VAR')
plt.ylabel("Número de chamadas")
plt.xlabel("Formatos de modulação (X-QAM)")
plt.grid(True)

plt.subplot(1,7,5)
sns.countplot(MD10).set_ylim([0,100000])
plt.title(r'$\alpha$ = VAR | F = CTE')
plt.ylabel("Número de chamadas")
plt.xlabel("Formatos de modulação (X-QAM)")
plt.grid(True)

plt.subplot(1,7,7)
sns.countplot(MD11).set_ylim([0,100000])
plt.title(r'$\alpha$ = VAR | F = VAR')
plt.ylabel("Número de chamadas")
plt.xlabel("Formatos de modulação (X-QAM)")
plt.grid(True)

plt.show()