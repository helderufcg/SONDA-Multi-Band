# ----------- Sonda Classes gerais ------------
import sys

from PyQt5.QtWidgets import QMainWindow

from Topology import *
from RoutingWavelengthAssignment import RWA
from Simulation_NetworkLoad import Simulation_NetworkLoad
from Grafics import Grafics
import multiprocessing as mp
import time

# ----------- Interface Gráfica ------------
from GUI_SondaMainWindow import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow

# ---------------- matplotlib ----------------
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import matplotlib
matplotlib.use('QT5Agg')

# ----------- banco de dados, para Linux apague a linha de código que diz port=3308 ------------
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="sonda",
    #port=3308
)

cursor = banco.cursor()

# ----------- classe para interface gráfica ------------

class GUI(Ui_MainWindow):

    def __init__(self, window):
        self.setupUi(window)
        self.SimulateButton.clicked.connect(self.simulation) #  ao clicar, irá executar a função
        self.ExitButton.clicked.connect(self.exit)  #  sai do programa

        self.num_mintl.setValidator(QtGui.QIntValidator(1,9999)) #  restrição de entrada apenas numeros inteiros
        self.num_maxtl.setValidator(QtGui.QIntValidator(1,9999)) #  restrição de entrada apenas numeros inteiros
        self.num_step.setValidator(QtGui.QIntValidator(1,999)) #  restrição de entrada apenas numeros inteiros
        self.num_calls.setValidator(QtGui.QIntValidator(1,100000000)) # restrição de entrada apenas numeros inteiros
        self.numbloqueios_lineEdit.setValidator(QtGui.QIntValidator(1,1000000000)) # restrição de entrada apenas numeros inteiros
        self.wavelenght_lineEdit.setValidator(QtGui.QIntValidator(0,999999999)) # restrição de entrada apenas numeros inteiros

        self.dist_amplificador_lineEdit.setValidator(QtGui.QDoubleValidator()) # restrição de entrada para numeros com precisão dupla
        self.BER_lineEdit.setValidator(QtGui.QIntValidator())

        # toolbar

    # --------------- sair do programa ---------------
    def exit(self):
        sys.exit()

    # --------------- simulação probabilidade de bloqueio ---------------
    def simulation(self):

        try:
            # --------------- seleção de topologias ---------------
            if self.SimpleTopology.isChecked():
                topologia = "Simple Topology"
                n_nodes = len(adj01)
                A = adj01
                links = links01

            elif self.Topology1.isChecked():
                topologia = "Topology 1"
                n_nodes = len(adjTop1)
                A = adjTop1
                links = linksTop1

            elif self.European.isChecked():
                topologia = "European"
                n_nodes = len(adjEuropean)
                A = adjEuropean
                links = linksEuropean

            elif self.German.isChecked():
                topologia = "German"
                n_nodes = len(adjGerman)
                A = adjGerman
                links = linksGerman

            elif self.NSFnet.isChecked():
                topologia = "NSFNet"
                n_nodes = len(adjNSFNet)
                A = adjNSFNet
                links = linksNSFNet

            elif self.PacificBell.isChecked():
                topologia = "PacificBell"
                n_nodes = len(adjPacificBell)
                A = adjPacificBell
                links = linksPacificBell

            elif self.UsBackbone.isChecked():
                topologia = "UsBackbone"
                n_nodes = len(adjUSBackbone)
                A = adjUSBackbone
                links = linksUSBackbone

            elif self.italy_radioButton.isChecked():
                topologia = "Italian"
                n_nodes = len(adjItalian)
                A = adjItalian
                links = linksItalian

            elif self.Japan_radioButton.isChecked():
                topologia = "Japan"
                n_nodes = len(adjJapanese)
                A = adjJapanese
                links = linksJapanese

            elif self.Finland_radioButton.isChecked():
                topologia = "Finland"
                n_nodes = len(adjFinland)
                A = adjFinland
                links = linksFinland

            elif self.Ipe_radioButton.isChecked():
                topologia = "Ipê"
                n_nodes = len(adjIpe)
                A = adjIpe
                links = linksIpe

            elif self.Abilene_radioButton.isChecked():
                topologia = "Abilene"
                n_nodes = len(adjAbilene)
                A = adjAbilene
                links = linksAbilene

            else:
                self.carga_textBrowser.setText('selecione uma das topologias disponíveis')

            # --------------- seleção de redes ---------------
            n_fibers = 1
            n_cores = 1
            n_modes = 1

            if self.WDMButton.isChecked():
                rede = "WDM"
                network_type = 1
                wavelength_bandwidth = int(self.wavelenght_lineEdit.text())

                consider_ase_noise = 0
                distancia_amplificador = 0.0

            elif self.EONButton.isChecked():
                rede = "EON"
                network_type = 2
                wavelength_bandwidth = None

                # --------------- se o botão de ruído ASE está selecionado ou não ---------------
                if self.Sim_ruidoASE.isChecked():
                    distancia_amplificador = float(self.dist_amplificador_lineEdit.text())
                    consider_ase_noise = 1

                elif self.Nao_ruidoASE.isChecked():
                    distancia_amplificador = float(self.dist_amplificador_lineEdit.text())
                    consider_ase_noise = 0

                else:
                    self.carga_textBrowser.setText('Por favor, selecione todas as opções de forma correta')

            else:
                self.carga_textBrowser.setText('selecione uma das redes disponíveis')

            # --------------- Tipo de simulação, parametros e chamada da simulação ------------------
            rwa = RWA()
            slots, times = rwa.Generate(n_nodes, links)
            N = slots.copy()
            T = times.copy()
            simulation = Simulation_NetworkLoad()
            grafics = Grafics()
            load_bp = []
            pool = mp.Pool(mp.cpu_count())

            # --------------- carga mínima, máxima e o passo ---------------
            min_traffic_load = int(self.num_mintl.text())
            max_traffic_load = int(self.num_maxtl.text())
            traffic_load_step = int(self.num_step.text())

            # --------------- se o usuário preferir a simulação com o numero de chamadas ---------------
            if self.chamadas_radioButton.isChecked():
                n_calls = int(self.num_calls.text())  # Refers to the number of simulated calls in the program
                t1 = time.time()

                t1 = time.time()
                for load in range(min_traffic_load, max_traffic_load, traffic_load_step):
                    r = pool.apply_async(simulation.FixedCalls, args=(
                    load, n_calls, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise,
                    distancia_amplificador), callback=load_bp.append)
                pool.close()
                pool.join()
                t2 = time.time()

                # --------------- exibição dos resultados ---------------
                self.carga_textBrowser.setText(str(load_bp))
                self.tempo_textBrowser.setText(str(t2 - t1))
                grafics.plot_topology(A)
                grafics.plot_blocking_probability(load_bp)

                # --------------- inserindo os resultados no banco de dados ---------------
                try:
                    cursor = banco.cursor()
                    comando_SQL = "INSERT INTO simulacao (topologia, rede, fibra, modos, nucleo, mintrafego, maxtrafego, passo, " \
                                      "distamplificador, chamadas, probabilidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

                    dados = (topologia, rede, n_fibers, n_modes, n_cores, min_traffic_load, max_traffic_load, traffic_load_step,
                                 distancia_amplificador, n_calls, str(load_bp))
                    cursor.execute(comando_SQL, dados)
                    banco.commit()
                    print(cursor.rowcount, "salvo no banco de dados!")

                except mysql.connector.Error as error:
                    print("falha ao salvar no banco de dados {}".format(error))

            # --------------- se o usuário preferir a simulação com o numero de bloqueios ---------------
            elif self.bloqueios_radioButton.isChecked():
                n_blockages = int(self.numbloqueios_lineEdit.text())

                t1 = time.time()
                for load in range(min_traffic_load, max_traffic_load, traffic_load_step):
                    r = pool.apply_async(simulation.FixedCalls, args=(
                        load, n_blockages, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise,
                        distancia_amplificador), callback=load_bp.append)
                pool.close()
                pool.join()
                t2 = time.time()

                # --------------- exibição dos resultados ---------------

                self.carga_textBrowser.setText(str(load_bp))
                self.tempo_textBrowser.setText(str(t2 - t1))
                grafics.plot_topology(A)
                grafics.plot_blocking_probability(load_bp)

                # --------------- inserindo os resultados no banco de dados ---------------
                try:
                    cursor = banco.cursor()
                    comando_SQL = "INSERT INTO simulacao_bloqueios (topologia, rede, fibra, modos, nucleo, mintrafego, maxtrafego, passo, " \
                                      "distamplificador, bloqueios, probabilidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

                    dados = (topologia, rede, n_fibers, n_modes, n_cores, min_traffic_load, max_traffic_load, traffic_load_step,
                                 distancia_amplificador, n_blockages, str(load_bp))
                    cursor.execute(comando_SQL, dados)
                    banco.commit()
                    print(cursor.rowcount, "salvo no banco de dados!")

                except mysql.connector.Error as error:
                    print("falha ao salvar no banco de dados {}".format(error))

                # --------------- para a simulação 3: variação percentual na carga de tráfego da rede ----------

            elif self.porcentagem_radioButton.isChecked():
                n_calls = int(self.bloqueiopercentual_lineEdit.text())
                traffic_load = int(self.percentual_lineEdit.text())
                t1 = time.time()

                for percentage in range(min_traffic_load, max_traffic_load, traffic_load_step):
                    r = pool.apply_async(simulation.LoadVariation, args=(
                    percentage, traffic_load, n_calls, n_nodes, links, A, N, T, network_type, wavelength_bandwidth,
                    consider_ase_noise, distancia_amplificador), callback=load_bp.append)
                pool.close()
                pool.join()
                t2 = time.time()

                # --------------- exibição dos resultados ---------------

                self.carga_textBrowser.setText(str(load_bp))
                self.tempo_textBrowser.setText(str(t2 - t1))
                grafics.plot_topology(A)
                grafics.plot_blocking_probability(load_bp)

                # --------------- inserindo os resultados no banco de dados ---------------

                try:
                    cursor = banco.cursor()
                    comando_SQL = "INSERT INTO simulacao_porcentagem (topologia, rede, fibra, modos, nucleo, mintrafego, maxtrafego, passo, " \
                                  "distamplificador,chamadas, cargatrafego, probabilidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

                    dados = (
                    topologia, rede, n_fibers, n_modes, n_cores, min_traffic_load, max_traffic_load, traffic_load_step,
                    distancia_amplificador, n_calls, traffic_load, str(load_bp))
                    cursor.execute(comando_SQL, dados)
                    banco.commit()
                    print(cursor.rowcount, "salvo no banco de dados!")

                except mysql.connector.Error as error:
                    print("falha ao salvar no banco de dados {}".format(error))

            # --------------- para a simulação 4: variação BER ----------

            elif self.BER_radioButton.isChecked():
                n_calls = int(self.BER_lineEdit.text())

                t1 = time.time()
                for load in range(min_traffic_load, max_traffic_load, traffic_load_step):
                    r = pool.apply_async(simulation.BERVariation, args=(
                    load, n_calls, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise,
                    distancia_amplificador), callback=load_bp.append)
                pool.close()
                pool.join()
                t2 = time.time()

                # --------------- exibição dos resultados ---------------
                self.carga_textBrowser.setText(str(load_bp))
                self.tempo_textBrowser.setText(str(t2 - t1))
                grafics.plot_topology(A)
                grafics.plot_BER_variation(sorted(load_bp), n_calls)

                # --------------- inserindo os resultados no banco de dados ---------------

                try:
                    cursor = banco.cursor()
                    comando_SQL = "INSERT INTO simulacao_porcentagem (topologia, rede, fibra, modos, nucleo, mintrafego, maxtrafego, passo, " \
                                  "distamplificador,chamadas, probabilidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

                    dados = (
                    topologia, rede, n_fibers, n_modes, n_cores, min_traffic_load, max_traffic_load, traffic_load_step,
                    distancia_amplificador, n_calls, str(load_bp))
                    cursor.execute(comando_SQL, dados)
                    banco.commit()
                    print(cursor.rowcount, "salvo no banco de dados!")

                except mysql.connector.Error as error:
                    print("falha ao salvar no banco de dados {}".format(error))

            else:
                self.carga_textBrowser.setText('Erro! Por favor, informe os dados da simulação corretamente. Verifique '
                                               'se: \n 1 - a topologia desejada está selecionada; \n 2 - a rede desejada '
                                               'está selecionada; \n 3 - O tipo de simulação está selecionado; \n '
                                               '4 - os dados inseridos nos campos estão corretos.')

        # --------------- correção de erros ---------------

        except UnboundLocalError:
            self.carga_textBrowser.setText('Erro! Por favor, informe os dados da simulação corretamente. Verifique '
                                            'se: \n 1 - a topologia desejada está selecionada; \n 2 - a rede desejada '
                                            'está selecionada; \n 3 - O tipo de simulação está selecionado; \n '
                                            '4 - os dados inseridos nos campos estão corretos.')

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI(MainWindow)
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
