# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Mio\Espe\Tesis\Interfaz\Interfaz_RCP\GUIs\PatologiaWin.ui'
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

class Ui_Patologia(object):
    def setupUi(self, Patologia):
        Patologia.setObjectName(_fromUtf8("Patologia"))
        Patologia.resize(840, 620)
        Patologia.setMinimumSize(QtCore.QSize(840, 620))
        Patologia.setMaximumSize(QtCore.QSize(840, 620))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/Icono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Patologia.setWindowIcon(icon)
        Patologia.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.btntaquicardiav = QtGui.QPushButton(Patologia)
        self.btntaquicardiav.setGeometry(QtCore.QRect(50, 120, 151, 23))
        self.btntaquicardiav.setObjectName(_fromUtf8("btntaquicardiav"))
        self.graphicsViewp = PlotWidget(Patologia)
        self.graphicsViewp.setGeometry(QtCore.QRect(300, 50, 451, 321))
        self.graphicsViewp.setObjectName(_fromUtf8("graphicsViewp"))
        self.btnbradicardia = QtGui.QPushButton(Patologia)
        self.btnbradicardia.setGeometry(QtCore.QRect(50, 70, 151, 23))
        self.btnbradicardia.setObjectName(_fromUtf8("btnbradicardia"))
        self.btntaquicardiasv = QtGui.QPushButton(Patologia)
        self.btntaquicardiasv.setGeometry(QtCore.QRect(50, 170, 151, 23))
        self.btntaquicardiasv.setObjectName(_fromUtf8("btntaquicardiasv"))
        self.pushButton_4 = QtGui.QPushButton(Patologia)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 220, 151, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Patologia)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 280, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Patologia)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 330, 75, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.btninstrucciones = QtGui.QPushButton(Patologia)
        self.btninstrucciones.setGeometry(QtCore.QRect(510, 540, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btninstrucciones.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/Instrucciones.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btninstrucciones.setIcon(icon1)
        self.btninstrucciones.setIconSize(QtCore.QSize(40, 40))
        self.btninstrucciones.setObjectName(_fromUtf8("btninstrucciones"))
        self.btndetener = QtGui.QPushButton(Patologia)
        self.btndetener.setGeometry(QtCore.QRect(240, 540, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btndetener.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/BRIGHTS STOP.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btndetener.setIcon(icon2)
        self.btndetener.setIconSize(QtCore.QSize(40, 40))
        self.btndetener.setObjectName(_fromUtf8("btndetener"))
        self.btnmenu = QtGui.QPushButton(Patologia)
        self.btnmenu.setGeometry(QtCore.QRect(690, 540, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnmenu.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/BRIGHTS HOME.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnmenu.setIcon(icon3)
        self.btnmenu.setIconSize(QtCore.QSize(40, 40))
        self.btnmenu.setObjectName(_fromUtf8("btnmenu"))

        self.retranslateUi(Patologia)
        QtCore.QMetaObject.connectSlotsByName(Patologia)

    def retranslateUi(self, Patologia):
        Patologia.setWindowTitle(_translate("Patologia", "Patologias", None))
        self.btntaquicardiav.setText(_translate("Patologia", "Taquicardia Ventricular", None))
        self.btnbradicardia.setText(_translate("Patologia", "Bradicardia Sinusoidal", None))
        self.btntaquicardiasv.setText(_translate("Patologia", "Taquicardia Supraventricular", None))
        self.pushButton_4.setText(_translate("Patologia", "Bradicardia Sinusal", None))
        self.pushButton_5.setText(_translate("Patologia", "PushButton", None))
        self.pushButton_6.setText(_translate("Patologia", "PushButton", None))
        self.btninstrucciones.setText(_translate("Patologia", "Instrucciones", None))
        self.btndetener.setText(_translate("Patologia", "Detener", None))
        self.btnmenu.setText(_translate("Patologia", "Menú", None))

from pyqtgraph import PlotWidget
import Iconos

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Patologia = QtGui.QDialog()
    ui = Ui_Patologia()
    ui.setupUi(Patologia)
    Patologia.show()
    sys.exit(app.exec_())

