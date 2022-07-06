import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import numpy as np
from RoutingWavelengthAssignment import *

"""
The Grafics class implements methods to generate grafics.
"""

class Grafics:

    def __init__(self):  
        pass

    @staticmethod
    def plot_blocking_probability(load_bp):
        sorted_load_bp = sorted(load_bp)
        load, BP = zip(*sorted_load_bp)
        
        plt.plot(load, BP, marker='s', markersize = 8, markeredgewidth = 5, markerfacecolor = 'w', linewidth = 5, label = 'Dijkstra + First Fit')
        plt.yscale('log')
        plt.xlabel('Carga na rede (Erlangs)')
        plt.ylabel('Probabilidade de bloqueio')
        plt.legend()
        plt.grid(True)
        plt.show()
        plt.figure(1)

    @staticmethod
    def plot_boxplot(columns):    
        dados = pd.read_excel(r"D:\PIBIC 2019 - 2020\SONDA\RESULTS.xlsx")
        bp = dados.boxplot(column=columns, 
                        boxprops=dict(linestyle='-', linewidth=5),
                        flierprops=dict(linestyle='-', linewidth=5),
                        medianprops=dict(linestyle='-', linewidth=5),
                        whiskerprops=dict(linestyle='-', linewidth=5),
                        capprops=dict(linestyle='-', linewidth=5), 
                        showmeans=True,
                        meanprops=dict(marker='x', markersize = 12, markeredgewidth = 3),
                        showfliers=False, grid=True, rot=0)

        plt.yscale('log')        
        bp.set_xlabel('Variação de carga na rede (%)')
        bp.set_ylabel('Probabilidade de bloqueio')
        plt.show()

    def autolabel(self, rects, percentages, ax):
        # attach a text label above each bar in *rects*, displaying its height
        for rect, label in zip(rects, percentages):
            height = rect.get_height()
            ax.annotate(str('{0:.2f}%'.format(label)).replace('.', ','),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points", rotation = 90,
                        ha='center', va='bottom')   

    def plot_BER_variation(self, load_bp, n_calls): 
        load, blocked, n_calls01, n_blockages01, n_calls02, n_blockages02, n_calls03, n_blockages03, n_calls04, n_blockages04 = zip(*load_bp)
        pb01 = []
        pb02 = []
        pb03 = []
        pb04 = []
        for i in range(len(load)):
            pb01.append(n_blockages01[i]/n_calls)
            pb02.append(n_blockages02[i]/n_calls)
            pb03.append(n_blockages03[i]/n_calls)
            pb04.append(n_blockages04[i]/n_calls)
        barw = 0.15
        r1 = np.arange(len(load))
        r2 = [x + barw for x in r1]
        r3 = [x + barw for x in r2]
        r4 = [x + barw for x in r3]
        ax = plt.subplot(111)
        rects01 = ax.bar(r1, pb01, width = barw, label = r'BER = $10^{-3}$')
        rects02 = ax.bar(r2, pb02, width = barw, label = r'BER = $10^{-6}$')
        rects03 = ax.bar(r3, pb03, width = barw, label = r'BER = $10^{-9}$')
        rects04 = ax.bar(r4, pb04, width = barw, label = r'BER = $10^{-12}$')
        percentage01 = []
        percentage02 = []
        percentage03 = []
        percentage04 = []
        for j in range(len(load)): 
            percentage01.append(pb01[j]*100)
            percentage02.append(pb02[j]*100)
            percentage03.append(pb03[j]*100)
            percentage04.append(pb04[j]*100)
        plt.yscale('log')
        plt.xlabel('Carga na rede (Erlangs)')
        plt.xticks([r + barw for r in range(len(load))], load)
        plt.ylabel('Probabilidade de bloqueio')
        plt.legend(loc = 4)
        self.autolabel(rects01, percentage01, ax)
        self.autolabel(rects02, percentage02, ax)
        self.autolabel(rects03, percentage03, ax)
        self.autolabel(rects04, percentage04, ax)
        plt.show()

    @staticmethod
    def plot_topology(A):
        G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
        layout = nx.spring_layout(G)
        nx.draw(G, layout)
        # draw nodes, edges and labels
        nx.draw_networkx_nodes(G, layout, node_size=500, node_color='blue', alpha=0.3)
        nx.draw_networkx_edges(G, layout, width=2, alpha=0.3, edge_color='green')
        nx.draw_networkx_labels(G, layout, font_size=10, font_family='sans-serif')
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)
        plt.figure(2)