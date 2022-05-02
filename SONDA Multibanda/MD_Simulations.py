import matplotlib.pyplot as plt
from Data_MD import MD22, MD21, MD20, MD19
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


'''
C22 = [MD22.count(64), MD22.count(16), MD22.count(4)]
C21 = [MD21.count(64), MD21.count(16), MD21.count(4)]
C20 = [MD20.count(64), MD20.count(16), MD20.count(4)]
C19 = [MD19.count(64), MD19.count(16), MD19.count(4)]
'''
'''
plt.subfigure(141)
plt.hist(MD22, bins = 'auto')
plt.ylabel("Número de chamadas")
plt.xlabel("Formatos de modulação (X-QAM)")
plt.legend("Número de chamadas com a modulação X-QAM")
plt.axis([4,64])

plt.subfigure(142)
plt.hist(MD21, bins = 'auto')
plt.ylabel("Número de chamadas")
plt.xlabel("Formatos de modulação (X-QAM)")
plt.legend("Número de chamadas com a modulação X-QAM")
plt.axis([4,64])

plt.subfigure(143)
plt.hist(MD20, bins = 'auto')
plt.ylabel("Número de chamadas")
plt.xlabel("Formatos de modulação (X-QAM)")
plt.legend("Número de chamadas com a modulação X-QAM")
plt.axis([4,64])

plt.subfigure(144)
plt.hist(MD19, bins = 'auto')
plt.ylabel("Número de chamadas")
plt.xlabel("Formatos de modulação (X-QAM)")
plt.legend("Número de chamadas com a modulação X-QAM")
plt.axis([4,64])
'''

'''
#, labels = ["4QAM","16QAM","64QAM"]
plt.subplot(221)
plt.hist(MD22,bins=50,histtype="step")
plt.legend(["Modulação (X-QAM)"])
plt.xlabel
plt.grid(False)

plt.subplot(222)
plt.hist(MD21,bins=10)

plt.subplot(223)
plt.hist(MD20)

plt.subplot(224)
plt.hist(MD19)
'''




'''
plt.subplot(221)
plt.pie(C22, autopct="%1.2f%%",shadow=True,startangle=90,wedgeprops = {'linewidth':1,'edgecolor':"k"},radius=1.2,pctdistance=0.67,labels=["64QAM","16QAM","4QAM"])
plt.title(r"$\bf\alpha$ = 0,22 dB/km",fontsize = 11,fontweight="bold",pad=12)


plt.subplot(222)
plt.pie(C21, autopct="%1.2f%%",shadow=True,startangle=90,wedgeprops = {'linewidth':1,'edgecolor':"k"},radius=1.2,pctdistance=0.67,labels=["64QAM","16QAM","4QAM"])
plt.title(r"$\bf\alpha$ = 0,21 dB/km",fontsize = 11,fontweight="bold",pad=12)


plt.subplot(223)
plt.pie(C20, autopct="%1.2f%%",shadow=True,startangle=90,wedgeprops = {'linewidth':1,'edgecolor':"k"},radius=1.2,pctdistance=0.67,labels=["64QAM","16QAM","4QAM"])
plt.title(r"$\bf\alpha$ = 0,20 dB/km",fontsize = 11,fontweight="bold",pad=12)


plt.subplot(224)
plt.pie(C19, autopct="%1.2f%%",shadow=True,startangle=90,wedgeprops = {'linewidth':1,'edgecolor':"k"},radius=1.2,pctdistance=0.67,labels=["64QAM","16QAM","4QAM"])
plt.title(r"$\bf\alpha$ = 0,19 dB/km",fontsize = 11,fontweight="bold",pad=12)

'''
plt.show()