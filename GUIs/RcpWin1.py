# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Mio\Espe\Tesis\Interfaz\Interfaz_RCP\GUIs\RcpWin.ui'
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

class Ui_RCPwin(object):
    def setupUi(self, RCPwin):
        RCPwin.setObjectName(_fromUtf8("RCPwin"))
        RCPwin.resize(840, 620)
        RCPwin.setMinimumSize(QtCore.QSize(840, 620))
        RCPwin.setMaximumSize(QtCore.QSize(840, 620))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/Icono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RCPwin.setWindowIcon(icon)
        RCPwin.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(201, 210, 255, 255), stop:1 rgba(0, 0, 255, 255));"))
        self.btninstrucciones = QtGui.QPushButton(RCPwin)
        self.btninstrucciones.setGeometry(QtCore.QRect(510, 500, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btninstrucciones.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/Instrucciones.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btninstrucciones.setIcon(icon1)
        self.btninstrucciones.setIconSize(QtCore.QSize(40, 40))
        self.btninstrucciones.setObjectName(_fromUtf8("btninstrucciones"))
        self.graphicsView = PlotWidget(RCPwin)
        self.graphicsView.setGeometry(QtCore.QRect(150, 50, 401, 261))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label = QtGui.QLabel(RCPwin)
        self.label.setGeometry(QtCore.QRect(150, 330, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.medidor = QtGui.QProgressBar(RCPwin)
        self.medidor.setGeometry(QtCore.QRect(610, 90, 31, 221))
        self.medidor.setProperty("value", 24)
        self.medidor.setOrientation(QtCore.Qt.Vertical)
        self.medidor.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.medidor.setObjectName(_fromUtf8("medidor"))
        self.verticalSlider = QtGui.QSlider(RCPwin)
        self.verticalSlider.setGeometry(QtCore.QRect(700, 150, 22, 160))
        self.verticalSlider.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
""))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.label_2 = QtGui.QLabel(RCPwin)
        self.label_2.setGeometry(QtCore.QRect(150, 360, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btninicio = QtGui.QPushButton(RCPwin)
        self.btninicio.setGeometry(QtCore.QRect(110, 500, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btninicio.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/FIRST AID.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btninicio.setIcon(icon2)
        self.btninicio.setIconSize(QtCore.QSize(40, 40))
        self.btninicio.setObjectName(_fromUtf8("btninicio"))
        self.btnmenu = QtGui.QPushButton(RCPwin)
        self.btnmenu.setGeometry(QtCore.QRect(690, 500, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnmenu.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/BRIGHTS HOME.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnmenu.setIcon(icon3)
        self.btnmenu.setIconSize(QtCore.QSize(40, 40))
        self.btnmenu.setObjectName(_fromUtf8("btnmenu"))
        self.btndetener = QtGui.QPushButton(RCPwin)
        self.btndetener.setGeometry(QtCore.QRect(240, 500, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btndetener.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/BRIGHTS STOP.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btndetener.setIcon(icon4)
        self.btndetener.setIconSize(QtCore.QSize(40, 40))
        self.btndetener.setObjectName(_fromUtf8("btndetener"))
        self.label_3 = QtGui.QLabel(RCPwin)
        self.label_3.setGeometry(QtCore.QRect(150, 420, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lbfrecuencia = QtGui.QLabel(RCPwin)
        self.lbfrecuencia.setGeometry(QtCore.QRect(240, 330, 141, 21))
        self.lbfrecuencia.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0)"))
        self.lbfrecuencia.setText(_fromUtf8(""))
        self.lbfrecuencia.setObjectName(_fromUtf8("lbfrecuencia"))
        self.lbtiempo = QtGui.QLabel(RCPwin)
        self.lbtiempo.setGeometry(QtCore.QRect(240, 360, 141, 21))
        self.lbtiempo.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lbtiempo.setText(_fromUtf8(""))
        self.lbtiempo.setObjectName(_fromUtf8("lbtiempo"))
        self.lbresultado = QtGui.QLabel(RCPwin)
        self.lbresultado.setGeometry(QtCore.QRect(240, 420, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbresultado.setFont(font)
        self.lbresultado.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);color:rgb(255,0,0);"))
        self.lbresultado.setText(_fromUtf8(""))
        self.lbresultado.setObjectName(_fromUtf8("lbresultado"))
        self.medidor_2 = QtGui.QProgressBar(RCPwin)
        self.medidor_2.setGeometry(QtCore.QRect(580, 90, 31, 221))
        self.medidor_2.setProperty("value", 100)
        self.medidor_2.setOrientation(QtCore.Qt.Vertical)
        self.medidor_2.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.medidor_2.setObjectName(_fromUtf8("medidor_2"))

        self.retranslateUi(RCPwin)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.medidor.setValue)
        QtCore.QMetaObject.connectSlotsByName(RCPwin)

    def retranslateUi(self, RCPwin):
        RCPwin.setWindowTitle(_translate("RCPwin", "Simulador de RCP", None))
        self.btninstrucciones.setText(_translate("RCPwin", "Instrucciones", None))
        self.label.setText(_translate("RCPwin", "Frecuencia:", None))
        self.label_2.setText(_translate("RCPwin", "Tiempo:", None))
        self.btninicio.setText(_translate("RCPwin", "Inicio", None))
        self.btnmenu.setText(_translate("RCPwin", "Menú", None))
        self.btndetener.setText(_translate("RCPwin", "Detener", None))
        self.label_3.setText(_translate("RCPwin", "Resultado:", None))

from pyqtgraph import PlotWidget
import Iconos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    RCPwin = QtGui.QDialog()
    ui = Ui_RCPwin()
    ui.setupUi(RCPwin)
    RCPwin.show()
    sys.exit(app.exec_())

