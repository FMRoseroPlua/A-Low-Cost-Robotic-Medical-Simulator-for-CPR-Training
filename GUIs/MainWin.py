# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Mio\Espe\Tesis\Interfaz\Interfaz_RCP\GUIs\MainWin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/Icono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 50, 48, 255), stop:1 rgba(97, 91, 88, 255));\n"
""))
        MainWindow.setWindowFilePath(_fromUtf8(""))
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(90, 390, 621, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("color: rgb(199, 199, 0);\n"
"border:5px solid;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btnescenarios = QtGui.QPushButton(self.groupBox)
        self.btnescenarios.setGeometry(QtCore.QRect(420, 40, 151, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnescenarios.setFont(font)
        self.btnescenarios.setAutoFillBackground(False)
        self.btnescenarios.setStyleSheet(_fromUtf8("QPushButton{\n"
"border: 1px solid;\n"
"border-radius:5px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color:rgb(0, 0, 0);\n"
"border-right-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }\n"
""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/patologias.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnescenarios.setIcon(icon1)
        self.btnescenarios.setIconSize(QtCore.QSize(40, 40))
        self.btnescenarios.setCheckable(False)
        self.btnescenarios.setChecked(False)
        self.btnescenarios.setAutoDefault(True)
        self.btnescenarios.setDefault(False)
        self.btnescenarios.setFlat(False)
        self.btnescenarios.setObjectName(_fromUtf8("btnescenarios"))
        self.btnintubacion = QtGui.QPushButton(self.groupBox)
        self.btnintubacion.setGeometry(QtCore.QRect(240, 40, 151, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnintubacion.setFont(font)
        self.btnintubacion.setStyleSheet(_fromUtf8("QPushButton{\n"
"border: 1px solid;\n"
"border-radius:5px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color:rgb(0, 0, 0);\n"
"border-right-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }\n"
""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/intubacion2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnintubacion.setIcon(icon2)
        self.btnintubacion.setIconSize(QtCore.QSize(40, 40))
        self.btnintubacion.setCheckable(False)
        self.btnintubacion.setAutoDefault(True)
        self.btnintubacion.setDefault(False)
        self.btnintubacion.setFlat(False)
        self.btnintubacion.setObjectName(_fromUtf8("btnintubacion"))
        self.btnrcp = QtGui.QPushButton(self.groupBox)
        self.btnrcp.setGeometry(QtCore.QRect(60, 40, 151, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnrcp.setFont(font)
        self.btnrcp.setStyleSheet(_fromUtf8("QPushButton{\n"
"border: 1px solid;\n"
"border-radius:5px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color:rgb(0, 0, 0);\n"
"border-right-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }\n"
""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/WTM 1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnrcp.setIcon(icon3)
        self.btnrcp.setIconSize(QtCore.QSize(40, 40))
        self.btnrcp.setCheckable(False)
        self.btnrcp.setDefault(False)
        self.btnrcp.setFlat(False)
        self.btnrcp.setObjectName(_fromUtf8("btnrcp"))
        self.btnip = QtGui.QPushButton(self.centralwidget)
        self.btnip.setEnabled(True)
        self.btnip.setGeometry(QtCore.QRect(700, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnip.setFont(font)
        self.btnip.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(230, 230, 230);\n"
"border: 1px solid;\n"
"border-radius:5px;\n"
"border-color:rgb(255, 255, 127); \n"
"border-bottom-color:rgb(0, 0, 0);\n"
"border-right-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }\n"
""))
        self.btnip.setObjectName(_fromUtf8("btnip"))
        self.teip = QtGui.QPlainTextEdit(self.centralwidget)
        self.teip.setEnabled(True)
        self.teip.setGeometry(QtCore.QRect(560, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.teip.setFont(font)
        self.teip.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.teip.setObjectName(_fromUtf8("teip"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 30, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color:rgb(255, 255, 255,0);\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 550, 461, 31))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255,0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 701, 171))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Palatino Linotype"))
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);\n"
"color:rgb(241, 214, 0);"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulador RCP Adulto", None))
        self.groupBox.setTitle(_translate("MainWindow", "Opciones", None))
        self.btnescenarios.setText(_translate("MainWindow", "Escenarios \n"
"Clínicos", None))
        self.btnintubacion.setText(_translate("MainWindow", "Intubación", None))
        self.btnrcp.setText(_translate("MainWindow", "RCP", None))
        self.btnip.setText(_translate("MainWindow", "Conectar", None))
        self.teip.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ej. 192.168.1.2</p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Ingresar IPV4 Raspberry", None))
        self.label_2.setText(_translate("MainWindow", "© Copyright: Todo derecho reservado a Felipe Miguel Rosero Plúa, Adrián Antonio Freire Fiallos", None))
        self.label_3.setText(_translate("MainWindow", "SIMULADOR DE  \n"
"REANIMACIÓN CARDIOPULMONAR  \n"
"EN ADULTOS", None))

import Iconos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

