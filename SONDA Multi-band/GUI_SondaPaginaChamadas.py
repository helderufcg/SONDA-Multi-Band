# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_SondaPaginaChamadas.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb
import ast
from GUI_SondaPaginaBloqueios import Ui_AnotherWindow

def MyConverter(mydata):
    def cvt(data):
        try:
            return ast.literal_eval(data)
        except Exception:
            return str(data)

    return tuple(map(cvt, mydata))

class Ui_OtherWindow(object):

    def Load(self):
        db = mdb.connect('localhost', 'root', '', 'sonda', port=3308)

        cur = db.cursor()
        comando = "SELECT * FROM simulacao"
        cur.execute(comando)
        data = cur.fetchall()

        for row in data:
            self.addTable(MyConverter(row))

        cur.close()

    def addTable(self, columns):
        rowPosition = self.banco_tableWidget.rowCount()
        self.banco_tableWidget.insertRow(rowPosition)

        for i, column in enumerate(columns):
            self.banco_tableWidget.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(column)))

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AnotherWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Resultados Salvos: Chamadas")
        MainWindow.resize(803, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.banco_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.banco_tableWidget.setGeometry(QtCore.QRect(10, 0, 781, 501))
        self.banco_tableWidget.setRowCount(1)
        self.banco_tableWidget.setColumnCount(11)
        self.banco_tableWidget.setObjectName("banco_tableWidget")
        self.Ok_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Ok_pushButton.setGeometry(QtCore.QRect(260, 510, 111, 31))
        self.Ok_pushButton.setObjectName("Ok_pushButton")
        self.bloqueios_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Ok_pushButton.clicked.connect(self.Load) # carregar dados
        self.bloqueios_pushButton.setGeometry(QtCore.QRect(390, 510, 101, 31))
        self.bloqueios_pushButton.setObjectName("bloqueios_pushButton")
        self.bloqueios_pushButton.clicked.connect(self.openWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Ok_pushButton.setText(_translate("MainWindow", "Carregar Dados"))
        self.bloqueios_pushButton.setText(_translate("MainWindow", "Bloqueios"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
