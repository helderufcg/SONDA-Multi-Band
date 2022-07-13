# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_SondaPaginaBloqueios.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb
import ast

def MyConverter(mydata):
    def cvt(data):
        try:
            return ast.literal_eval(data)
        except Exception:
            return str(data)

    return tuple(map(cvt, mydata))

class Ui_AnotherWindow(object):

    def Load(self):
        db = mdb.connect('localhost', 'root', '', 'sonda', port=3308)

        cur = db.cursor()
        comando = "SELECT * FROM simulacao_bloqueios"
        cur.execute(comando)
        data = cur.fetchall()

        for row in data:
            self.addTable(MyConverter(row))

        cur.close()

    def addTable(self, columns):
        rowPosition = self.bloqueios_tableWidget.rowCount()
        self.bloqueios_tableWidget.insertRow(rowPosition)

        for i, column in enumerate(columns):
            self.bloqueios_tableWidget.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(column)))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Resultados Salvos: Bloqueios")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bloqueios_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.bloqueios_tableWidget.setGeometry(QtCore.QRect(15, 11, 771, 491))
        self.bloqueios_tableWidget.setRowCount(1)
        self.bloqueios_tableWidget.setColumnCount(11)
        self.bloqueios_tableWidget.setObjectName("bloqueios_tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 510, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Load)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Carregar Dados"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AnotherWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
