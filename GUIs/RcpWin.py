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
        RCPwin.resize(720, 560)
        RCPwin.setMinimumSize(QtCore.QSize(720, 560))
        RCPwin.setMaximumSize(QtCore.QSize(840, 620))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/Icono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RCPwin.setWindowIcon(icon)
        RCPwin.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 50, 48, 255), stop:1 rgba(97, 91, 88, 255));\n"
""))
        self.btninstrucciones = QtGui.QPushButton(RCPwin)
        self.btninstrucciones.setGeometry(QtCore.QRect(380, 490, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btninstrucciones.setFont(font)
        self.btninstrucciones.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(194, 251, 21);\n"
"border: 1px solid;\n"
"border-radius:10px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/Instrucciones.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btninstrucciones.setIcon(icon1)
        self.btninstrucciones.setIconSize(QtCore.QSize(40, 40))
        self.btninstrucciones.setObjectName(_fromUtf8("btninstrucciones"))
        self.graphicsView = PlotWidget(RCPwin)
        self.graphicsView.setGeometry(QtCore.QRect(120, 40, 401, 261))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label = QtGui.QLabel(RCPwin)
        self.label.setGeometry(QtCore.QRect(120, 330, 111, 21))
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
        self.medidor.setGeometry(QtCore.QRect(560, 40, 31, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.medidor.setFont(font)
        self.medidor.setStyleSheet(_fromUtf8("\n"
"border:1px solid;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);"))
        self.medidor.setProperty("value", 0)
        self.medidor.setOrientation(QtCore.Qt.Vertical)
        self.medidor.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.medidor.setObjectName(_fromUtf8("medidor"))
        self.label_2 = QtGui.QLabel(RCPwin)
        self.label_2.setGeometry(QtCore.QRect(120, 370, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btninicio = QtGui.QPushButton(RCPwin)
        self.btninicio.setEnabled(True)
        self.btninicio.setGeometry(QtCore.QRect(20, 490, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btninicio.setFont(font)
        self.btninicio.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(194, 251, 21);\n"
"border: 1px solid;\n"
"border-radius:10px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/FIRST AID.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btninicio.setIcon(icon2)
        self.btninicio.setIconSize(QtCore.QSize(40, 40))
        self.btninicio.setObjectName(_fromUtf8("btninicio"))
        self.btnmenu = QtGui.QPushButton(RCPwin)
        self.btnmenu.setGeometry(QtCore.QRect(550, 490, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnmenu.setFont(font)
        self.btnmenu.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(194, 251, 21);\n"
"border: 1px solid;\n"
"border-radius:10px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/BRIGHTS HOME.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnmenu.setIcon(icon3)
        self.btnmenu.setIconSize(QtCore.QSize(40, 40))
        self.btnmenu.setObjectName(_fromUtf8("btnmenu"))
        self.btndetener = QtGui.QPushButton(RCPwin)
        self.btndetener.setEnabled(False)
        self.btndetener.setGeometry(QtCore.QRect(190, 490, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btndetener.setFont(font)
        self.btndetener.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(194, 251, 21);\n"
"border: 1px solid;\n"
"border-radius:10px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }\n"
""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btndetener.setIcon(icon4)
        self.btndetener.setIconSize(QtCore.QSize(40, 40))
        self.btndetener.setObjectName(_fromUtf8("btndetener"))
        self.label_3 = QtGui.QLabel(RCPwin)
        self.label_3.setGeometry(QtCore.QRect(120, 410, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lbfrecuencia = QtGui.QLabel(RCPwin)
        self.lbfrecuencia.setEnabled(True)
        self.lbfrecuencia.setGeometry(QtCore.QRect(260, 330, 141, 21))
        self.lbfrecuencia.setStyleSheet(_fromUtf8("QLabel{ \n"
"background-color: rgb(244, 255, 167);\n"
"color: rgb(0, 0, 0);\n"
"border:1px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"}\n"
"QLabel:hover{ background-color: white; }"))
        self.lbfrecuencia.setText(_fromUtf8(""))
        self.lbfrecuencia.setObjectName(_fromUtf8("lbfrecuencia"))
        self.lbtiempo = QtGui.QLabel(RCPwin)
        self.lbtiempo.setGeometry(QtCore.QRect(260, 370, 141, 21))
        self.lbtiempo.setStyleSheet(_fromUtf8("QLabel{ \n"
"background-color: rgb(244, 255, 167);\n"
"color: rgb(0, 0, 0);\n"
"border:1px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"}\n"
"QLabel:hover{ background-color: white; }"))
        self.lbtiempo.setText(_fromUtf8(""))
        self.lbtiempo.setObjectName(_fromUtf8("lbtiempo"))
        self.lbresultado = QtGui.QLabel(RCPwin)
        self.lbresultado.setGeometry(QtCore.QRect(260, 410, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbresultado.setFont(font)
        self.lbresultado.setStyleSheet(_fromUtf8("QLabel{ \n"
"background-color:rgb(244, 255, 167);\n"
"color: rgb(0, 0, 0);\n"
"border:1px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"}\n"
"QLabel:hover{ background-color: white; }"))
        self.lbresultado.setText(_fromUtf8(""))
        self.lbresultado.setObjectName(_fromUtf8("lbresultado"))
        self.btnresultados = QtGui.QPushButton(RCPwin)
        self.btnresultados.setEnabled(False)
        self.btnresultados.setGeometry(QtCore.QRect(410, 410, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnresultados.setFont(font)
        self.btnresultados.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(255, 164, 16);\n"
"border: 1px solid;\n"
"border-radius:5px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/res1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnresultados.setIcon(icon5)
        self.btnresultados.setIconSize(QtCore.QSize(15, 15))
        self.btnresultados.setObjectName(_fromUtf8("btnresultados"))
        self.btndetalle = QtGui.QPushButton(RCPwin)
        self.btndetalle.setEnabled(False)
        self.btndetalle.setGeometry(QtCore.QRect(520, 410, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btndetalle.setFont(font)
        self.btndetalle.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(255, 164, 16);\n"
"border: 1px solid;\n"
"border-radius:5px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        self.btndetalle.setIcon(icon5)
        self.btndetalle.setIconSize(QtCore.QSize(15, 15))
        self.btndetalle.setObjectName(_fromUtf8("btndetalle"))

        self.retranslateUi(RCPwin)
        QtCore.QMetaObject.connectSlotsByName(RCPwin)

    def retranslateUi(self, RCPwin):
        RCPwin.setWindowTitle(_translate("RCPwin", "Simulador de RCP", None))
        self.btninstrucciones.setText(_translate("RCPwin", "Instrucciones", None))
        self.label.setText(_translate("RCPwin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Frecuencia:</span></p></body></html>", None))
        self.label_2.setText(_translate("RCPwin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Tiempo:</span></p></body></html>", None))
        self.btninicio.setText(_translate("RCPwin", "Inicio", None))
        self.btnmenu.setText(_translate("RCPwin", "Menú", None))
        self.btndetener.setText(_translate("RCPwin", "Detener", None))
        self.label_3.setText(_translate("RCPwin", "<html><head/><body><p><span style=\" font-size:14pt; color:#fbfbfb;\">Resultado:</span></p></body></html>", None))
        self.btnresultados.setText(_translate("RCPwin", "Resultados", None))
        self.btndetalle.setText(_translate("RCPwin", "Detalle", None))

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

