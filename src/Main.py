'''
Created on Feb 27, 2018

@author: Felipe Rosero, Adrian Freire
'''
#Librerias
from __future__ import unicode_literals #Para error UTF-8
from __future__ import division
from PyQt4 import QtGui,QtCore
from random import randint, uniform
from PyQt4.Qt import QTimer, QMessageBox
from builtins import int
from MainWin import Ui_MainWindow
from EscenariosWin import Ui_EscenariosWin
from EscgWin import Ui_EscgWin
from IntubacionWin import Ui_Intubacion

import socket
import pickle
import pygame
import os
import threading
import RcpWin
import time as tm
import sys
import numpy as np
import pyqtgraph as pg
import ctypes #Get sistem metrics
from mock.mock import self

class tabla(QtGui.QDialog):
    def __init__(self,vd,vt):
        QtGui.QDialog.__init__(self)
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.setWindowTitle("Detalle de compresiones")        
        self.setModal(True)
        self.resize(270,400)
        self.setMinimumSize(270, 400)
       
        #Creacion de la tablla        
        tabla=QtGui.QTableWidget(self)
        tabla.setGeometry(QtCore.QRect(10,10,250,380))
        tabla.setStyleSheet("border-color: rgb(0, 0, 0);")
        tabla.setRowCount(len(vd))
        tabla.setColumnCount(2)
        #Add Header
        Encabezado=["Compresion","Tiempo"]
        val=vd
        valt=vt
        tabla.setHorizontalHeaderLabels(Encabezado)
        #Llenar tabla
        for i in range (0,len(val),1):
            tabla.setItem(i,0, QtGui.QTableWidgetItem(str(val[i])))
            tabla.setItem(i,1, QtGui.QTableWidgetItem(str(valt[i])+" s"))
            if(val[i]<5):
                tabla.item(i,0).setBackground(QtGui.QColor(255,255,0,120))
                tabla.item(i,1).setBackground(QtGui.QColor(255,255,0,120))
            elif(val[i]>=5 and val[i]<=6):
                tabla.item(i,0).setBackground(QtGui.QColor(0,255,0,120))
                tabla.item(i,1).setBackground(QtGui.QColor(0,255,0,120))
            else:
                tabla.item(i,0).setBackground(QtGui.QColor(255,0,0,70))
                tabla.item(i,1).setBackground(QtGui.QColor(255,0,0,70))

class cuadro(QtGui.QDialog):
    def __init__(self,num_comp,num_insuf,vec_etapa,frecuencia,f):
        QtGui.QDialog.__init__(self)
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.setWindowTitle("Datos de RCP")        
        self.setModal(True)
        self.resize(400,400)
        self.setMinimumSize(400, 400)
        print(vec_etapa)
        layout = QtGui.QHBoxLayout()
        textEdit = QtGui.QTextEdit()
        textEdit.setReadOnly(True)
        layout.addWidget(textEdit)
        self.setLayout(layout)
        
        #Llenar resultados
        textEdit.setTextColor(QtGui.QColor(255,0,0))
        textEdit.setFontPointSize(17)
        textEdit.setFontWeight(200)
        textEdit.setText("                 Resultados") 
        textEdit.setTextColor(QtGui.QColor(231,10,115))
        textEdit.setFontPointSize(11)
        textEdit.setFontWeight(1)
        textEdit.append("\nHubo un total de %s compresiones"%(str(num_comp)))
        textEdit.append("Hubieron %s etapas de insufalciones"%(str(num_insuf)))
        textEdit.append("")
    
        
        coninsu=0
        textEdit.setTextColor(QtGui.QColor(0,0,255))
        try:
            for i in range(1,f+1):
                print(i)
                if(i==1):
                    textEdit.append("%s Etapa: %s compresiones"%(str(i),str(vec_etapa[i]))) #primer tramo
                    if(coninsu<num_insuf):
                        textEdit.append("Insuflación")
                        coninsu+=1
                else:
                    textEdit.append("%s Etapa: %s compresiones"%(str(i),str(vec_etapa[i]-vec_etapa[i-1])))
                    if(coninsu<num_insuf):
                        textEdit.append("Insuflación")
                        coninsu+=1        
        except: pass
        
        textEdit.append("")
        textEdit.append("La frecuencia fué de %s compresiones por minuto"%(str(frecuencia)))
        textEdit.append("\n\n")
        textEdit.setTextColor(QtGui.QColor(5,173,27))
        textEdit.setFontPointSize(12)
        textEdit.setFontUnderline(True)
        if(frecuencia>=100): textEdit.append("Su práctica de RCP fué CORRECTA")
        elif(frecuencia>=70 and frecuencia<100):textEdit.append("Su práctica de RCP fué ACEPTABLE")
        else: textEdit.append("Su práctica de RCP fué INCORRECTA")
               
    
class recursos():
    def cargar_audio(self):
        #Inicializar sonidos
        path=os.path.normpath(os.getcwd() + os.sep + os.pardir).replace('\\','/')+"/Resources"
        pygame.init()
        pygame.display.set_mode((100,100))
        self._beep=pygame.mixer.Sound(path+"/Beepshort.wav")
        self.flatline=pygame.mixer.Sound(path+"/Flatlineshort.wav")
        pygame.mixer.Sound.set_volume(self._beep,1)
        self.caud=0

#############################################################################################          
class Vrcp(QtGui.QDialog,RcpWin.Ui_RCPwin,recursos):
    def __init__(self,ip):
        QtGui.QDialog.__init__(self)
        pg.setConfigOption('background', 'k')
        pg.setConfigOption('foreground', 'w')
        self.setupUi(self) 
        self.ip=ip 
        self.w=QtGui.QWidget()    
        self.graphicsView.plotItem.showGrid(True,True,0.4)   
        self.graphicsView.setYRange(0,3,padding=0.05) #Rango de eje Y
        
        #Espaciado eje X
        ax = self.graphicsView.getAxis('bottom')  
        ax.setTickSpacing(0.2,0.04)
        ax.setStyle(showValues=False)
        #Espaciado Eje Y
        ay = self.graphicsView.getAxis('left')
        ay.setTickSpacing(0.5,0.1)
        ay.setStyle(showValues=0)            
        #Definir ancho y color de la linea plot    
        self.pen=pg.mkPen(width=3) 
        self.pen.setColor(QtGui.QColor(0,255,0))        
        pg.setConfigOptions(antialias=True) 
        #Contadores de boton inicio y detener
        self.condet=0
        self.conini=0    
        self.lm=0   #Estado de inicio toma datos
        
        with open("sinusoidal.txt",'rb') as fp:
            self.sinusoidal= pickle.load(fp)
            
        self.conec()
        self.t1=threading.Thread(name="Hilo1",target=self.tiempo)
        self.t2=threading.Thread(name="Hilo2",target=self.receive_data)
        
    
        #Inicio del programa
        self.btninicio.clicked.connect(self.callgraficar)
        self.btndetener.clicked.connect(self.detener)
        self.btninstrucciones.clicked.connect(self.instrucciones) 
        self.btnmenu.clicked.connect(self.cerrar)
        self.btnresultados.clicked.connect(self.resultado)
        self.btndetalle.clicked.connect(self.detalle)                  
        
    def conec(self):        
        self.scli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = self.ip
        PORT = 10700
        try:
            self.scli.connect((HOST, PORT))     
            print('Conectado al servidor')
            self.scli.send("RCP".encode())
            self.scli.recv(100)            
        except:
            print("Servidor aún no encontrado")
            QMessageBox.critical(self.w,"Problemas con servidor", "Ocurrió un problema con el servidor (Revise la conexión)"
                                        , QMessageBox.Ok)
            sys.exit(app.exec_())
                                                            
    # ----------------------- Metodos para lectura de datos --------------------------------
      
    def callToma_datos(self):
        print("ENTROOOOOOOOO")
        self.det=0
        self.btninicio.setEnabled(False)
        self.tinicialrcp=self.seg
        self.tfinalrcp= self.tinicialrcp+120       
        self.Toma_datos()
    
    def Toma_datos(self):
        self.valtablac=[]
        self.valtablat=[]
        self.compresiones=[]
        self.tcompresiones=[]
        self.frecuencia=0
        self.fre=0
        self.posi=-1
        self.plotter()
            
    def plotter(self):
        self.data =[0]             
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)
        self.timer.start(100)
            
    def updater(self):      
        if(self.det==0 and self.seg<self.tfinalrcp):
            self.graphicsView.setXRange(0,50,padding=0.00)
            self.line= self.data1 #Datos
            if(self.line>=80 and self.line<=530):
                distancia=round(2076.0/(self.line-11),1)
            else: distancia=0
            
            disfinal=round(14-distancia,1)
            if(disfinal<=1):disfinal=0 #eliminar ruido
            
            #Obtener distancia de compresio--->Procesamiento             
            self.compresiones.append(disfinal)
            self.tcompresiones.append(self.seg)
            #Plot    
            self.data.append(round(float(disfinal/2.5),1))#(self.data1)
            if(len(self.data)>=50):
                self.data=[self.data[49]]
                
            self.graphicsView.plot(self.data,pen=self.pen,clear=True)                
    
            #Color del ProgressBar 
            self.medidor.setValue(disfinal*10)
            if(self.medidor.value()>=0 and self.medidor.value()<=40):
                self.medidor.setStyleSheet("::chunk {background-color:rgb(0,240,0)}")              
            elif(self.medidor.value()>40 and self.medidor.value()<=60):
                self.medidor.setStyleSheet("::chunk {"
                            "background-color: "
                            "qlineargradient(y0: 0, y2: 1," 
                            "stop: 0 yellow, stop: 0.3 yellow,"
                            "stop: 1 rgb(0,240,0))}")            
            elif(self.medidor.value()>60 and self.medidor.value()<=100):
                self.medidor.setStyleSheet("::chunk {"
                            "background-color: "
                            "qlineargradient(y0: 0, y2: 1,"
                            "stop: 0 red, stop: 0.2 red, "
                            "stop: 0.4 yellow, stop: 1 yellow"
                            ")}")
        
            
            try: #Error lectura del primer valor pos[-1]=pos[1]
                if(self.compresiones[self.posi-1]<self.compresiones[self.posi]>=self.compresiones[self.posi+1]):
                    self.fre+=1
                if(self.compresiones[self.posi-1]==self.compresiones[self.posi]<self.compresiones[self.posi+1]):
                    self.fre-=1
                    
                    self.frecuencia=int((60*self.fre)/(self.seg-self.tinicialrcp+1))
                    self.lbfrecuencia.setText(str(self.frecuencia)+" C/min")
            except: pass

            self.posi+=1   
        
        #Presentacion de resultados    
        else:
            self.timer.stop()
            conh=0
            conl=[0] #Numero de compresiones por tramo
            self.insuflacion=0
            act=1
            for i in range(1,len(self.compresiones)-1,1):
                if(self.compresiones[i]==0):
                        conh+=1
                        if(conh>=20 and act==1):
                            self.insuflacion+=1
                            conl.append(len(self.valtablac))
                            act=0                 
                else: 
                    conh=0
                    act=1              
                if(self.compresiones[i-1]<self.compresiones[i]>=self.compresiones[i+1]): #Es posible enganar 
                    self.valtablac.append(self.compresiones[i])
                    self.valtablat.append(self.tcompresiones[i])
                if(self.compresiones[i-1]==self.compresiones[i]<self.compresiones[i+1]): #Es posible enganar 
                    self.valtablac.pop(-1)
                    self.valtablat.pop(-1)      
            
            f=self.insuflacion
            if(conl[-1]<len(self.valtablac)):
                f=f+1;
                conl.append(len(self.valtablac))
                
            self.ff=f
      
            for i in range(1,f+1):
                if(i==1):print("%d etapa: %d compresiones"%(i,conl[i])) #primer tramo
                else:print("%d etapa: %d compresiones"%(i,conl[i]-conl[i-1])) 
            self.vecconl=conl
            
            print("Reloj detenido")
            self.scli.send('SALIR'.encode())
            self.estadot=False
            QMessageBox.information(self.w, "Programa finalizado", "La ejecución del programa a terminado", buttons=QMessageBox.Ok)
            self.btndetalle.setEnabled(True)
            self.btnresultados.setEnabled(True)
            if(self.frecuencia>=100): self.lbresultado.setText("RCP Correcto")
            elif(self.frecuencia>=70 and self.frecuencia<100):self.lbresultado.setText("RCP Aceptable")
            else: self.lbresultado.setText("RCP Incorrecto")
                
    def resultado(self):
        objcd=cuadro(len(self.valtablac),self.insuflacion,self.vecconl,self.frecuencia,self.ff)
        objcd.exec_()
    
    def detalle(self):
        objtb=tabla(self.valtablac,self.valtablat)
        objtb.exec_()
    #--------------------------------------------------------------------------------    
    
    #---------------------Metodo para Graficar ECG sinusoidal------------------------    
    def callgraficar(self):
        self.det=0 #Boton detener  
        self.conini+=1  
                
        #Generacion de Valores de fibrilacion
        if(self.condet==0 and self.conini==1):      
            self.tot=[]   
            self.xg=[]
            self.valx=0
            self.valysinus=0
            self.valyfv=0              
            self.estadot=True
            
            self.scli.send("START".encode())
            self.t1.start() #Inicializo una unica vez el Hilo Tiempo
            self.t2.start() #Recivir datos
                 
        xv=np.arange(1,6.3,0.1)
        self.fv=(0.89+(np.sin(xv/2)-np.sin(randint(2,8)*xv/2)-np.cos(7*xv/2)+np.sin((xv/2)-2.5)-np.cos(9*(xv/2)-2))/4)
       
        self.cargar_audio()
        self.btndetener.setEnabled(True) 
        
        #Llamada al metodo
        self.tim= QTimer()      
        self.tim.timeout.connect(self.graficar)
        self.tim.start(10)
        
    def graficar(self):
        if(self.det==0):            
            if(self.seg<=10):                          
                self.tot.append(self.sinusoidal[self.valysinus])
                self.xg.append(self.valx/100) #Ancho --> 100=0.01  10=0.1                    
                                
                if self.sinusoidal[self.valysinus]==2.4095:  
                    self._beep.play()            
                    self.scli.send('P'.encode()) #Enviar seal de pulso
                               
                if(len(self.tot)>500):
                    del self.tot[0:300]
                    del self.xg[0:300]
       
                self.graphicsView.setXRange(self.xg[-1]-1,self.xg[-1]+1,padding=0.0)  
                self.graphicsView.plot(self.xg,self.tot,pen=self.pen,clear=True)                
                self.valysinus = (self.valysinus + 1) % len(self.sinusoidal)
                                                 
#--------------------------------FIbrilacion Ventircular----------------------------                
            if(self.seg>10 and self.seg<=30):
                self.tot.append(self.fv[self.valyfv])
                self.xg.append(self.valx/100)  
                                                  
                #If algo empieza rcp                                 
                if self.lm==1:
                    self.tim.stop()
                    self.callToma_datos()
                                                                                    
                if(len(self.tot)>500):
                    del self.tot[0:300]
                    del self.xg[0:300]                   
                    
                self.graphicsView.setXRange(self.xg[-1]-1,self.xg[-1]+1,padding=0.0)  
                self.graphicsView.plot(self.xg,self.tot,pen=self.pen,clear=True)
                
                if(self.valyfv==len(self.fv)-1):
                    xv=np.arange(1,6.3,0.1)
                    self.fv=(0.89+(np.sin(xv/2)-np.sin(randint(2,8)*xv/2)-np.cos(7*xv/2)
                                   +np.sin((xv/2)-2.5)-np.cos(9*(xv/2)-2))/4) 
                                     
                self.valyfv = (self.valyfv + 1) % len(self.fv)
                               
            if(self.seg>30 and self.seg<40):
                if(self.caud==0): self.flatline.play();self.caud=2;
                self.tot.append(self.tot[-1])
                self.xg.append(self.valx/100) #Ancho --> 100=0.01  10=0.1
           
                if(len(self.tot)>500):
                    del self.tot[0:300]
                    del self.xg[0:300]
               
                self.graphicsView.setXRange(self.xg[-1]-1,self.xg[-1]+1,padding=0.0)  
                self.graphicsView.plot(self.xg,self.tot,pen=self.pen,clear=True)
            
            self.valx+=1
            if(self.seg>40):
                self.detener()
                self.tim.stop()
                                                    
#----------------------------------------------------------------------------------                
    #Imprimir tiempo
    def tiempo(self):
        mi=-1
        sec=60
        self.seg=0
        while self.estadot: 
            if(self.det==0):                      
                if sec%60==0: 
                    mi=mi+1
                    sec=sec-60              
                if(sec<60 and mi==0):
                    self.lbtiempo.setText(str(sec)+" s")
                else:               
                    self.lbtiempo.setText("%d min %d s" %(mi,sec))
                                     
                sec+=1
                self.seg+=1
                tm.sleep(1)  
        
    #Leer datos
    def receive_data(self):
        while (self.estadot):
            data=self.scli.recv(3)
            self.data1=int(data.decode())                                   
            if(self.seg>10 and self.data1>=177): 
                self.lm=1
                   
    #------------------------------------------------------------------------------------   
    
    def detener(self):
        print("Detener ",self.condet)
        self.det=1
        self.condet+=1
        try:
            self.flatline.stop()
        except: pass
    
    def instrucciones(self,event):
        objinstruc=QMessageBox.question(self, "Instrucciones RCP", "Al presionar en el boton inicio el progrma empezara y constara de los siguientes aspectos:\n"
                                        "Por 10 segundos se desarrollara normalmente una onda sinusoidal, "
                                        "entonces la onda empezara a fibrilar y tendra 15 segundos para empezar a realizar las compresiones"
                                        "caso contrario existira una asistolia por 10 segundos y el programa finalizara",QMessageBox.Ok)
        try:
            if (objinstruc==QMessageBox.Ok): event.accept()
        except:
            pass
    
    def cerrar(self):
        self.close()
        
    def closeEvent(self,event):
        self.scli.send('SALIR'.encode())
        self.scli.close()
        self.estadot=False
            
        try: self.tim.stop(); 
        except: pass 
        try: self.timer.stop(); 
        except: pass 
        pygame.display.quit()

 
###################################################################################################
class Vescg(QtGui.QDialog,Ui_EscgWin,recursos):
    def __init__(self,parent,ip):
        QtGui.QDialog.__init__(self,parent)       
        self.setupUi(self)
        self.ip=ip
        self.w=QtGui.QWidget()
        self.aplicarcp=0
        
        pg.setConfigOption('background', 'k')# Background del Plot
        pg.setConfigOption('foreground', 'w')
        pg.setConfigOptions(antialias=True)
        self.pen=pg.mkPen(QtGui.QColor(0,255,0),width=2)
        self.graphicsView.plotItem.showGrid(True,True,0.4)  
        self.graphicsView.setYRange(0,3,padding=0.0)    
        
        #Espaciado eje X
        ax = self.graphicsView.getAxis('bottom')  
        ax.setTickSpacing(0.2,0.04)
        ax.setStyle(showValues=False)
        #Espaciado Eje Y
        ay = self.graphicsView.getAxis('left')
        ay.setTickSpacing(0.5,0.1)
        ay.setStyle(showValues=0)
        
        
        self.cargar_audio() #Cargar audio
        self.conec()
        self.cargarondas() #Cargar Ondas
        
        self.estadot=True
        self.seg=0
        self.tfinalrcp=0
        
        self.t1=threading.Thread(name="Hilo1",target=self.tiempo)#, args=(10,)
        self.t2=threading.Thread(name="Hilo2",target=self.receive_data)
        
           
    def conec(self):        
        self.scli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = self.ip
        PORT = 10700
        try:
            self.scli.connect((HOST, PORT))     
            print('Conectado al servidor')
            self.scli.send("EC".encode())
            saludo=self.scli.recv(100)
            print(saludo)
            
        except:
            print("Servidor aún no encontrado")
            QMessageBox.critical(self.w,"Problemas con servidor", "Ocurrió un problema con el servidor (Revise la conexión)"
                                        , QMessageBox.Ok)
            sys.exit(app.exec_())

    def receive_data(self):
        while (self.estadot):
            try:
                data=self.scli.recv(3)
                self.data1=int(data.decode())                                  
                if(self.aplicarcp==5 and self.data1>=177): 
                    self.lm=1
            except:
                pass


#-----------------------------------Conjunto de funciones para plot -----------------------------       
    def cargarondas(self):       #Revisar falla asignar valores
        with open("sinusoidal.txt",'rb') as fp:
            self.sinusoidal= pickle.load(fp)
            
        with open("bradisinusoidal.txt",'rb') as fp:
            self.bradisinusoidal=pickle.load(fp)  
            
        with open("TV.txt",'rb') as fp:
            self.TV=pickle.load(fp)
        
        with open("TSV.txt",'rb') as fp:
            self.TSV=pickle.load(fp)
            
        xv=np.arange(1,6.3,0.1)
        self.FV=(0.89+(np.sin(xv/2)-np.sin(randint(2,8)*xv/2)-np.cos(7*xv/2)+np.sin((xv/2)-2.5)-np.cos(9*(xv/2)-2))/10)
        
        
        xv=np.arange(1,3.2*randint(1,3),0.1)
        Ffa=[]
        Ffa.extend(0.89+(np.sin(xv*0.75)-np.sin(randint(2,8)*xv*0.75)-np.cos(7*xv*0.75)+np.sin((xv*0.75)-2.5)-np.cos(9*(xv*0.75)-2))/10)#53
        self.qrsfa=[0.9008,0.8873,1.422,2.087,1.651,0.7245,0.545,0.6893,0.8344,0.9325]#10 #4max #7min
        self.fauricular=[round(i,4) for i in Ffa]
        self.fauricular.extend(self.qrsfa)
        self.valmax=10
        
    def preinitval(self,vector):
        self.vecopc=vector
        print(self.vecopc)
        self.onda=[]
        self.t=[]
        self.resp=[]
        self.fresp=[]
        ti=0
        self.conasis=0
        self.t_fin_fl=[]
        for i in range(len(self.vecopc)-1):
            ti=ti+((self.vecopc[i][1]+1)*10)
            self.onda.append(self.vecopc[i][0]+1)
            self.t.append(ti)
            self.resp.append(self.vecopc[i][2])
            self.fresp.append(self.vecopc[i][3])
            if(self.onda[i]==2): #Opxion 2= asistolia
                self.t_fin_fl.append(ti)          
            
        data_resp=""
        data_fresp=""
        data_t=""
        for i in range(0,len(self.vecopc)-1):
            data_resp=data_resp+str(self.resp[i])+','
            data_fresp=data_fresp+str(self.fresp[i])+','
            data_t=data_t+str(self.t[i])+',' 
                 
        self.scli.send(data_resp.encode())
        print(self.scli.recv(100))
        self.scli.send(data_fresp.encode())
        print(self.scli.recv(100))
        self.scli.send(data_t.encode())  
        print(self.scli.recv(100))
         
        self.initval()

    def initval(self):
        self.valx=0
        self.valysinus=0
        self.valybrasinus=0
        self.valyasistolia=0.89
        self.valyTSV=0
        self.valyTV=0
        self.valyFV=0
        self.valyfauricular=0
        self.tot=[]
        self.posx=[]
        self.playfl=0
        
        tm.sleep(0.5)   
        self.scli.send("START".encode())#OJO
        
        self.t1.start()
        self.t2.start()
        self._exec()
        
    def _exec(self):
        
        if (self.seg<=self.t[0]):
            self.tim=QTimer() 
            self.tim.timeout.connect(self._exec)
            self.aplicarcp=self.onda[0]
            if (self.onda[0]==1):self.fsinusal()
            elif(self.onda[0]==2):self.fasistolia()
            elif(self.onda[0]==3):self.fbradisinusal()
            elif(self.onda[0]==4):self.fFauricular()
            elif(self.onda[0]==5):self.fFV()
            elif(self.onda[0]==6):self.fTV()
            elif(self.onda[0]==7):self.fTSV()
            
        try:
            if(self.seg>self.t[0] and self.seg<=self.t[1]):               
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[1]
                if (self.onda[1]==1):self.fsinusal()
                elif(self.onda[1]==2):self.fasistolia()
                elif(self.onda[1]==3):self.fbradisinusal()
                elif(self.onda[1]==4):self.fFauricular()
                elif(self.onda[1]==5):self.fFV()
                elif(self.onda[1]==6):self.fTV()
                elif(self.onda[1]==7):self.fTSV()
                       
        except: pass
        try:
            if(self.seg>self.t[1] and self.seg<=self.t[2]):
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[2]
                if (self.onda[2]==1):self.fsinusal()
                elif(self.onda[2]==2):self.fasistolia()
                elif(self.onda[2]==3):self.fbradisinusal()
                elif(self.onda[2]==4):self.fFauricular()
                elif(self.onda[2]==5):self.fFV()
                elif(self.onda[2]==6):self.fTV()
                elif(self.onda[2]==7):self.fTSV()
                
        except: pass
        try:
            if(self.seg>self.t[2] and self.seg<=self.t[3]):
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[3]
                if (self.onda[3]==1):self.fsinusal()
                elif(self.onda[3]==2):self.fasistolia()
                elif(self.onda[3]==3):self.fbradisinusal()
                elif(self.onda[3]==4):self.fFauricular()
                elif(self.onda[3]==5):self.fFV()
                elif(self.onda[3]==6):self.fTV()
                elif(self.onda[3]==7):self.fTSV()
        except: pass
        try:
            if(self.seg>self.t[3] and self.seg<=self.t[4]):
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[4]
                if (self.onda[4]==1):self.fsinusal()
                elif(self.onda[4]==2):self.fasistolia()
                elif(self.onda[4]==3):self.fbradisinusal()
                elif(self.onda[4]==4):self.fFauricular()
                elif(self.onda[4]==5):self.fFV()
                elif(self.onda[4]==6):self.fTV()
                elif(self.onda[4]==7):self.fTSV()
        except: pass
        try:
            if(self.seg>self.t[4] and self.seg<=self.t[5]):
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[5]
                if (self.onda[5]==1):self.fsinusal()
                elif(self.onda[5]==2):self.fasistolia()
                elif(self.onda[5]==3):self.fbradisinusal()
                elif(self.onda[5]==4):self.fFauricular()
                elif(self.onda[5]==5):self.fFV()
                elif(self.onda[5]==6):self.fTV()
                elif(self.onda[5]==7):self.fTSV()
        except: pass
        try:
            if(self.seg>self.t[5] and self.seg<=self.t[6]): 
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[6]
                if (self.onda[6]==1):self.fsinusal()
                elif(self.onda[6]==2):self.fasistolia()
                elif(self.onda[6]==3):self.fbradisinusal()
                elif(self.onda[6]==4):self.fFauricular()
                elif(self.onda[6]==5):self.fFV()
                elif(self.onda[6]==6):self.fTV()
                elif(self.onda[6]==7):self.fTSV()
        except: pass
        try:
            if(self.seg>self.t[6] and self.seg<=self.t[7]):
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[7]
                if (self.onda[7]==1):self.fsinusal()
                elif(self.onda[7]==2):self.fasistolia()
                elif(self.onda[7]==3):self.fbradisinusal()
                elif(self.onda[7]==4):self.fFauricular()
                elif(self.onda[7]==5):self.fFV()
                elif(self.onda[7]==6):self.fTV()
                elif(self.onda[7]==7):self.fTSV()
        except: pass
        try:
            if(self.seg>self.t[7] and self.seg<=self.t[8]): 
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[8]
                if (self.onda[8]==1):self.fsinusal()
                elif(self.onda[8]==2):self.fasistolia()
                elif(self.onda[8]==3):self.fbradisinusal()
                elif(self.onda[8]==4):self.fFauricular()
                elif(self.onda[8]==5):self.fFV()
                elif(self.onda[8]==6):self.fTV()
                elif(self.onda[8]==7):self.fTSV()
        except: pass
        try:
            if(self.seg>self.t[8] and self.seg<=self.t[9]): 
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[9]
                if (self.onda[9]==1):self.fsinusal()
                elif(self.onda[9]==2):self.fasistolia()
                elif(self.onda[9]==3):self.fbradisinusal()
                elif(self.onda[9]==4):self.fFauricular()
                elif(self.onda[9]==5):self.fFV()
                elif(self.onda[9]==6):self.fTV()
                elif(self.onda[9]==7):self.fTSV()
        except: pass
        try:
            if(self.seg>self.t[9] and self.seg<=self.t[10]):
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[10]
                if (self.onda[10]==1):self.fsinusal()
                elif(self.onda[10]==2):self.fasistolia()
                elif(self.onda[10]==3):self.fbradisinusal()
                elif(self.onda[10]==4):self.fFauricular()
                elif(self.onda[10]==5):self.fFV()
                elif(self.onda[10]==6):self.fTV()
                elif(self.onda[10]==7):self.fTSV()
        except: pass
        try:
            if(self.seg>self.t[10] and self.seg<=self.t[11]):
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[11]
                if (self.onda[11]==1):self.fsinusal()
                elif(self.onda[11]==2):self.fasistolia()
                elif(self.onda[11]==3):self.fbradisinusal()
                elif(self.onda[11]==4):self.fFauricular()
                elif(self.onda[11]==5):self.fFV()
                elif(self.onda[11]==6):self.fTV()
                elif(self.onda[11]==7):self.fTSV()
        except: pass
        try:
            if(self.seg>self.t[11] and self.seg<=self.t[12]):
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[12]
                if (self.onda[12]==1):self.fsinusal()
                elif(self.onda[12]==2):self.fasistolia()
                elif(self.onda[12]==3):self.fbradisinusal()
                elif(self.onda[12]==4):self.fFauricular()
                elif(self.onda[12]==5):self.fFV()
                elif(self.onda[12]==6):self.fTV()
                elif(self.onda[12]==7):self.fTSV()
        except: pass
        try:
            if(self.seg>self.t[12] and self.seg<=self.t[13]):
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[13]
                if (self.onda[13]==1):self.fsinusal()
                elif(self.onda[13]==2):self.fasistolia()
                elif(self.onda[13]==3):self.fbradisinusal()
                elif(self.onda[13]==4):self.fFauricular()
                elif(self.onda[13]==5):self.fFV()
                elif(self.onda[13]==6):self.fTV()
                elif(self.onda[13]==7):self.fTSV()
        except: pass
        try:
            if(self.seg>self.t[13] and self.seg<=self.t[14]):
                self.tim=QTimer() 
                self.tim.timeout.connect(self._exec)
                self.aplicarcp=self.onda[14]
                if (self.onda[14]==1):self.fsinusal()
                elif(self.onda[14]==2):self.fasistolia()
                elif(self.onda[14]==3):self.fbradisinusal()
                elif(self.onda[14]==4):self.fFauricular()
                elif(self.onda[14]==5):self.fFV()
                elif(self.onda[14]==6):self.fTV()
                elif(self.onda[14]==7):self.fTSV()
        except: pass
        self.valx+=1 #Siempre
    
    def fsinusal(self): 
        self.tim.start(1)      
        self.tot.append(self.sinusoidal[self.valysinus])
        self.posx.append(self.valx/100) #Ancho --> 100=0.01  10=0.1
        
        if self.sinusoidal[self.valysinus]==2.4095: 
            self._beep.play()            
            self.scli.send("P".encode())            
        
        if(len(self.tot)>500):
            del self.tot[0:300]
            del self.posx[0:300]
       
        self.graphicsView.setXRange(self.posx[-1]-1,self.posx[-1]+1,padding=0.0)  
        self.graphicsView.plot(self.posx,self.tot,pen=self.pen,clear=True)
        
        self.valysinus = (self.valysinus + 1) % len(self.sinusoidal) #Importante -->Valores de la onda 
        self.valyasistolia = self.tot[-1]
        
    def fasistolia(self): #Corregir
        self.tim.start(20)
        self.tot.append(self.valyasistolia)
        self.posx.append(self.valx/100) #Ancho --> 100=0.01  10=0.1
        
        if(self.playfl==0):
            self.flatline.play()
            self.playfl=1
            
        if(len(self.tot)>500):
            del self.tot[0:300]
            del self.posx[0:300]
       
        self.graphicsView.setXRange(self.posx[-1]-1,self.posx[-1]+1,padding=0.0)  
        self.graphicsView.plot(self.posx,self.tot,pen=self.pen,clear=True)
    
    def fbradisinusal(self):
        self.tim.start(10)
        self.tot.append(self.bradisinusoidal[self.valybrasinus])
        self.posx.append(self.valx/100) #Ancho --> 100=0.01  10=0.1
        
        if self.bradisinusoidal[self.valybrasinus]==2.087: 
            self._beep.play()
            self.scli.send("P".encode())
        
        if(len(self.tot)>500):
            del self.tot[0:300]
            del self.posx[0:300]
       
        self.graphicsView.setXRange(self.posx[-1]-1,self.posx[-1]+1,padding=0.0)  
        self.graphicsView.plot(self.posx,self.tot,pen=self.pen,clear=True)
        
        self.valybrasinus = (self.valybrasinus + 1) % len(self.bradisinusoidal) #Importante -->Valores de la onda 
        self.valyasistolia=self.tot[-1]
        
    def fFauricular(self):
        self.tim.start(15)
        self.tot.append(self.fauricular[self.valyfauricular])
        self.posx.append(self.valx/100)                    
                
        if self.fauricular[self.valyfauricular]==self.valmax or self.fauricular[self.valyfauricular]==2.087: 
            self._beep.play()
            self.scli.send("P".encode())
            
        if(len(self.tot)>500):
            del self.tot[0:300]
            del self.posx[0:300]
                    
        self.graphicsView.setXRange(self.posx[-1]-1,self.posx[-1]+1,padding=0.0)  
        self.graphicsView.plot(self.posx,self.tot,pen=self.pen,clear=True)
        
        valf=self.valyfauricular
        self.valyfauricular = (self.valyfauricular + 1) % len(self.fauricular)
        
        
        if(valf==len(self.fauricular)-1):
            xv=np.arange(1,3*randint(1,3),0.1)#3.2
            self.valmax=round(uniform(1.7,2.3),4)
            self.valmin=round(uniform(0.4,0.7),4)
            Ffa=[]
            Ffa.extend(0.89+(np.sin(xv*0.75)-np.sin(randint(2,8)*xv*0.75)-np.cos(7*xv*0.75)+np.sin((xv*0.75)-2.5)-np.cos(9*(xv*0.75)-2))/10)
            self.qrsfa=[0.9008,0.8873,1.422,self.valmax,1.651,0.7245,self.valmin,0.6893,0.8344,0.9325]
            self.fauricular=[round(i,4) for i in Ffa]
            self.fauricular.extend(self.qrsfa)
            
        self.valyasistolia=self.tot[-1]
         
    def fFV(self):
        self.tim.start(20)
        self.tot.append(self.FV[self.valyFV])
        self.posx.append(self.valx/100) 
                          
        if self.lm==1:
            self.tim.stop()
            self.callToma_datos()     
                    
        if(len(self.tot)>500):
            del self.tot[0:300]
            del self.posx[0:300]
                    
        self.graphicsView.setXRange(self.posx[-1]-1,self.posx[-1]+1,padding=0.0)  
        self.graphicsView.plot(self.posx,self.tot,pen=self.pen,clear=True)
                
        if(self.valyFV==len(self.FV)-1):
            xv=np.arange(1,6.3,0.1)
            self.FV=(0.89+(np.sin(xv/2)-np.sin(randint(2,8)*xv/2)-np.cos(7*xv/2)
                           +np.sin((xv/2)-2.5)-np.cos(9*(xv/2)-2))/10) 
                    
        self.valyFV = (self.valyFV + 1) % len(self.FV)
        self.valyasistolia=self.tot[-1]
        
        
    
    def fTV(self):
        self.tim.start(10)
        self.tot.append(self.TV[self.valyTV])
        self.posx.append(self.valx/100) #Ancho --> 100=0.01  10=0.1
        
        if self.TV[self.valyTV]==2.2673: 
            self._beep.play()
            self.scli.send("P".encode())
        
        if(len(self.tot)>500):
            del self.tot[0:300]
            del self.posx[0:300]
       
        self.graphicsView.setXRange(self.posx[-1]-1,self.posx[-1]+1,padding=0.0)  
        self.graphicsView.plot(self.posx,self.tot,pen=self.pen,clear=True)
        
        self.valyTV = (self.valyTV + 1) % len(self.TV) #Importante -->Valores de la onda 
        self.valyasistolia=self.tot[-1]
        
    def fTSV(self):
        self.tim.start(10)
        self.tot.append(self.TSV[self.valyTSV])
        self.posx.append(self.valx/100) #Ancho --> 100=0.01  10=0.1
        
        if self.TSV[self.valyTSV]==2.3807: 
            self._beep.play()
            self.scli.send("P".encode())
        
        if(len(self.tot)>500):
            del self.tot[0:300]
            del self.posx[0:300]
       
        self.graphicsView.setXRange(self.posx[-1]-1,self.posx[-1]+1,padding=0.0)  
        self.graphicsView.plot(self.posx,self.tot,pen=self.pen,clear=True)
        
        self.valyTSV = (self.valyTSV + 1) % len(self.TSV) #Importante -->Valores de la onda 
        self.valyasistolia=self.tot[-1]
        
    def tiempo(self):
        mi=-1
        sec=60
        self.seg=0
        print("FIn",self.t_fin_fl)          
        
        while self.estadot and (self.seg<=self.t[-1] or self.seg<=self.tfinalrcp): 
            #Elieminar flatline
            if(len(self.t_fin_fl)>self.conasis):
                if(self.seg==self.t_fin_fl[self.conasis]):
                    self.flatline.stop()
                    self.conasis+=1  
                    self.playfl=0
                                     
            if sec%60==0: 
                mi=mi+1
                sec=sec-60              
            if(sec<60 and mi==0):
                self.lbtiempo.setText(str(sec)+" s")
            else:               
                self.lbtiempo.setText("%d min %d s" %(mi,sec))               
            sec+=1
            self.seg+=1
            tm.sleep(1)
    
    def closeEvent(self,event):
        self.scli.send('SALIR'.encode())
        self.scli.close()
        self.estadot=False
        
        try: self.tim.stop(); 
        except: pass 
        try: self.timer.stop(); 
        except: pass
        try: self.flatline.stop()
        except:pass
        pygame.display.quit()
        self.parent().show()
        
#---------------------------------------------------------------------------------------------        
    # ----------------------- Metodos para lectura de datos --------------------------------
      
    def callToma_datos(self):
        self.tinicialrcp=self.seg
        self.tfinalrcp= self.tinicialrcp+20 #+120      
        self.Toma_datos()
    
    def Toma_datos(self):
        self.valtablac=[]
        self.valtablat=[]
        self.compresiones=[]
        self.tcompresiones=[]
        self.frecuencia=0
        self.fre=0
        self.posi=-1
        self.plotter()
            
    def plotter(self):
        self.data =[0]             
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)
        self.timer.start(100)
            
    def updater(self):      
        if(self.seg<self.tfinalrcp):
            self.graphicsView.setXRange(0,50,padding=0.00)
            self.line= self.data1 #Datos
            if(self.line>=80 and self.line<=530):
                distancia=round(2076.0/(self.line-11),1)
            else: distancia=0
            
            disfinal=round(14-distancia,1)
            if(disfinal<=1):disfinal=0 #eliminar ruido
            
            #Obtener distancia de compresio--->Procesamiento             
            self.compresiones.append(disfinal)
            self.tcompresiones.append(self.seg)
            #Plot    
            self.data.append(round(float(disfinal/2.5),1))#(self.data1)
            if(len(self.data)>=50):
                self.data=[self.data[49]]
                
            self.graphicsView.plot(self.data,pen=self.pen,clear=True)    
            #print(disfinal,"      ",distancia,"       ",len(self.data))      
            
            
            #Color del ProgressBar 
            self.medidor.setValue(disfinal*10)
            if(self.medidor.value()>=0 and self.medidor.value()<=40):
                self.medidor.setStyleSheet("::chunk {background-color:rgb(0,240,0)}")              
            elif(self.medidor.value()>40 and self.medidor.value()<=60):
                self.medidor.setStyleSheet("::chunk {"
                            "background-color: "
                            "qlineargradient(y0: 0, y2: 1," 
                            "stop: 0 yellow, stop: 0.3 yellow,"
                            "stop: 1 rgb(0,240,0))}")            
            elif(self.medidor.value()>60 and self.medidor.value()<=100):
                self.medidor.setStyleSheet("::chunk {"
                            "background-color: "
                            "qlineargradient(y0: 0, y2: 1,"
                            "stop: 0 red, stop: 0.2 red, "
                            "stop: 0.4 yellow, stop: 1 yellow"
                            ")}")
        
            
            
            try: #Error lectura del primer valor pos[-1]=pos[1]
                if(self.compresiones[self.posi-1]<self.compresiones[self.posi]>=self.compresiones[self.posi+1]):
                    self.fre+=1
                if(self.compresiones[self.posi-1]==self.compresiones[self.posi]<self.compresiones[self.posi+1]):
                    self.fre-=1
                    self.frecuencia=int((60*self.fre)/(self.seg-self.tinicialrcp+1))
                    self.lbfrecuencia.setText(str(self.frecuencia)+" C/min")
            except: 
                pass
            
            self.posi+=1
            
        
        #Presentacion de resultados    
        else:
            self.timer.stop()
            conh=0
            conl=[0] #Numero de compresiones por tramo
            self.insuflacion=0
            act=1
            for i in range(1,len(self.compresiones)-1,1):
                if(self.compresiones[i]==0):
                        conh+=1
                        if(conh>=20 and act==1):
                            self.insuflacion+=1
                            conl.append(len(self.valtablac))
                            act=0                       
                else: 
                    conh=0
                    act=1              
                if(self.compresiones[i-1]<self.compresiones[i]>=self.compresiones[i+1]): #Es posible enganar 
                    self.valtablac.append(self.compresiones[i])
                    self.valtablat.append(self.tcompresiones[i])      
                if(self.compresiones[i-1]==self.compresiones[i]<self.compresiones[i+1]): #Es posible enganar 
                    self.valtablac.pop(-1)
                    self.valtablat.pop(-1)
            
            f=self.insuflacion
            if(conl[-1]<len(self.valtablac)):
                f=f+1;
                conl.append(len(self.valtablac))
 
            self.vecconl=conl
            
            print("Reloj detenido")
            self.estadot=False
            QMessageBox.information(self.w, "Programa finalizado", "La ejecución del programa a terminado", buttons=QMessageBox.Ok)
            """
            self.btndetalle.setEnabled(True)
            self.btnresultados.setEnabled(True)
            if(self.frecuencia>=100): self.lbresultado.setText("RCP Correcto")
            elif(self.frecuencia>=70 and self.frecuencia<100):self.lbresultado.setText("RCP Aceptable")
            else: self.lbresultado.setText("RCP Incorrecto")
                        
            self.scli.send('SALIR'.encode())
            """    
                            
    def resultado(self):
        objcd=cuadro(len(self.valtablac),self.insuflacion,self.vecconl,self.frecuencia)
        objcd.exec_()
    
    def detalle(self):
        objtb=tabla(self.valtablac,self.valtablat)
        objtb.exec_()
    #--------------------------------------------------------------------------------    
  



class Vescenarios(QtGui.QDialog,Ui_EscenariosWin,recursos):
    def __init__(self,ip):
        QtGui.QDialog.__init__(self)     
        self.setupUi(self)
        self.setModal(True) 
        self.ip=ip
        self.vecopc=[0]
        self.filt=0
        self.hl=0
        self.Tabla.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.Tabla.setRowCount(15)   
        self.w=QtGui.QWidget() 
        self.cbpatologias.setFocus()
        
        self.sbmodificar.valueChanged.connect(self.modtabla)
        self.btnanadir.clicked.connect(self.lltabla)     
        self.btncambiar.clicked.connect(self.chtabla)
        self.btnremover.clicked.connect(self.remtabla)
        self.btnguardar.clicked.connect(self.save)
        self.btncargar.clicked.connect(self.file_open)
        self.btninicio.clicked.connect(self.iniciar)
        
              
    def iniciar(self):
        self.hide()
        objvescg=Vescg(self,self.ip)
        objvescg.preinitval(self.vecopc)
        objvescg.exec_()
        
#-----------------------------------Conjnto Funcionalidad--------------------------------------            
    def hlfm(self):
        if(self.filt>=1):
            self.frame.setEnabled(True)
            self.btninicio.setEnabled(True)
        else: 
            self.frame.setEnabled(False)
            self.btninicio.setEnabled(False)
            
        self.Tabla.resizeColumnsToContents()
        self.Tabla.resizeRowsToContents()
        
    def lltabla(self):
        if(self.filt<=14):
            self.Tabla.selectRow(self.filt)
            self.Tabla.setItem(self.filt,0,QtGui.QTableWidgetItem(self.cbpatologias.currentText()))
            self.Tabla.setItem(self.filt,1,QtGui.QTableWidgetItem(self.cbtiempo.currentText()))
            self.Tabla.setItem(self.filt,2,QtGui.QTableWidgetItem(self.cbrespiracion.currentText()))
            print(self.cbpatologias.currentIndex())
            if(self.cbpatologias.currentIndex()==4):
                self.sbfrespiracion.setMinimum(0)
                self.sbfrespiracion.setValue(0)
                
            self.Tabla.setItem(self.filt,3,QtGui.QTableWidgetItem(str(self.sbfrespiracion.value())))
            self.vecopc[self.filt]=[self.cbpatologias.currentIndex(),self.cbtiempo.currentIndex(),
                                    self.cbrespiracion.currentIndex(),self.sbfrespiracion.value()]
            self.vecopc.append(0)
            self.filt+=1
            self.sbfrespiracion.setMinimum(20)
            
        else:
            QMessageBox.information(self.w, "Limite maximo", "El limite maximo de ritmos cardiacos se de 15", QMessageBox.Ok)   
            if(QMessageBox.Ok): pass
              
        self.hlfm()
        self.sbmodificar.setMaximum(self.filt)
    
    def modtabla(self): 
        self.hl=self.sbmodificar.value()-1
        self.valtomod=self.vecopc[self.hl]
             
        self.cbpatologias.setCurrentIndex(self.valtomod[0])
        self.cbtiempo.setCurrentIndex(self.valtomod[1])
        self.cbrespiracion.setCurrentIndex(self.valtomod[2])
        self.sbfrespiracion.setValue(self.valtomod[3])
        self.Tabla.selectRow(self.hl)
        
    def chtabla(self):        
        self.Tabla.setItem(self.hl,0,QtGui.QTableWidgetItem(self.cbpatologias.currentText()))
        self.Tabla.setItem(self.hl,1,QtGui.QTableWidgetItem(self.cbtiempo.currentText()))
        self.Tabla.setItem(self.hl,2,QtGui.QTableWidgetItem(self.cbrespiracion.currentText()))
        self.Tabla.setItem(self.hl,3,QtGui.QTableWidgetItem(str(self.sbfrespiracion.value())))
        self.vecopc[self.hl]=[self.cbpatologias.currentIndex(),self.cbtiempo.currentIndex(),
                                self.cbrespiracion.currentIndex(),self.sbfrespiracion.value()]
                
        self.Tabla.selectRow(self.hl)
        self.hlfm()
        
    def remtabla(self):
        self.Tabla.removeRow(self.hl)
        self.vecopc.remove(self.vecopc[self.hl])
        self.Tabla.setRowCount(15)      
        self.filt=len(self.vecopc)-1
        if(self.filt>=1): self.sbmodificar.setMaximum(len(self.vecopc)-1)            
        self.hlfm()        
           
    def save(self):
        files_types = "hlmf(*.hlmf)"
        name = QtGui.QFileDialog.getSaveFileName(self, 'Guardar', '', files_types)   
        try:  
            with open(name,'wb') as fp: pickle.dump(self.vecopc, fp)
        except FileNotFoundError: pass

    def file_open(self):                    
        name = QtGui.QFileDialog.getOpenFileName(self, 'Abrir','',"hlmf(*.hlmf)")
        try:
            with open(name,'rb') as fp: self.vecopc= pickle.load(fp)
        except FileNotFoundError: pass
        
        try:
            self.Tabla.setRowCount(0);
            self.Tabla.setRowCount(15);
            
        except:
            pass

        self.filt=len(self.vecopc)-1
        for i in range(len(self.vecopc)-1):            
            self.Tabla.setItem(i,0,QtGui.QTableWidgetItem(self.cbpatologias.itemText(self.vecopc[i][0])))
            self.Tabla.setItem(i,1,QtGui.QTableWidgetItem(self.cbtiempo.itemText(self.vecopc[i][1])))
            self.Tabla.setItem(i,2,QtGui.QTableWidgetItem(self.cbrespiracion.itemText(self.vecopc[i][2])))
            self.Tabla.setItem(i,3,QtGui.QTableWidgetItem(str(self.vecopc[i][3])))
        
        self.sbmodificar.setMaximum(self.filt)       
        self.hlfm()
#-------------------------------------------------------------------------------------------------


###################################################################################################
class Vintubacion(QtGui.QDialog,Ui_Intubacion):
    def __init__(self,ip):
        QtGui.QDialog.__init__(self)       
        self.setupUi(self)      
        self.label_2.raise_() #Traquea
        self.label_3.raise_() #Esofago
        self.label_2.setStyleSheet("background-color:rgb(0,255,0,0);""border-radius:11px;")
        self.label_3.setStyleSheet("background-color:rgb(255,0,0,0);""border-radius:11px;")
        self.ip=ip
        self.w=QtGui.QWidget()
        self.estado=True
        self.x=""
        
        self.conec()
        self.t1=threading.Thread(name="Hilo1",target=self.receive_data)
        self.t1.start()
        
        self.pushButton.clicked.connect(lambda: self.scli.send("OPEN".encode()))
        self.pushButton_2.clicked.connect(lambda: self.scli.send(bytes("CLOSE",'UTF-8')))
        
        self.tim=QTimer()
        self.tim.timeout.connect(self._exec)
        self.tim.start(70)
        
    def conec(self):        
        self.scli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = self.ip
        PORT = 10700
        try:
            self.scli.connect((HOST, PORT))     
            print('Conectado al servidor')
            self.scli.send("INTU".encode())
            self.scli.recv(100)
            
        except:
            print("Servidor aún no encontrado")
            QMessageBox.critical(self.w,"Problemas con servidor", "Ocurrió un problema con el servidor (Revise la conexión)"
                                        , QMessageBox.Ok)
            sys.exit(app.exec_())
            
    def receive_data(self):     
        while (self.estado):
            try:
                data=self.scli.recv(20)
                self.x=data.decode()
            except: pass
            
    def _exec(self):
        if(self.x=="INTC"):
            self.label_2.setStyleSheet("background-color:rgb(0,255,0);""border-radius:11px;")
            self.label_3.setStyleSheet("background-color:rgb(255,0,0,0);""border-radius:11px;")
            self.lbfrecuencia.setText("<html><head/><body><p align=\"center\">"
                                      "<span style=\" font-size:11pt; font-weight:600;\">"
                                      "Intubación Correcta</span></p></body></html>")
        elif(self.x=="INTIC"):   
            self.label_2.setStyleSheet("background-color:rgb(0,255,0,0);""border-radius:11px;")
            self.label_3.setStyleSheet("background-color:rgb(255,0,0);""border-radius:11px;")
            self.lbfrecuencia.setText("<html><head/><body><p align=\"center\">"
                                      "<span style=\" font-size:11pt; font-weight:600;\">"
                                      "Intubación Incorrecta</span></p></body></html>")
        else:
            self.label_2.setStyleSheet("background-color:rgb(0,255,0,0);""border-radius:11px;")
            self.label_3.setStyleSheet("background-color:rgb(255,0,0,0);""border-radius:11px;")
            self.lbfrecuencia.setText("<html><head/><body><p align=\"center\">"
                                      "<span style=\" font-size:11pt; font-weight:600;\">"
                                      "Sin Intubación</span></p></body></html>")
        
    def closeEvent(self,event):
        self.tim.stop()   
        self.scli.send('SALIR'.encode())
        self.estado=False
        self.scli.close()
                   
###################################################################################################
class Root(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnrcp.clicked.connect(self.callvrcp)
        self.ui.btnescenarios.clicked.connect(self.callvescenarios)
        self.ui.btnintubacion.clicked.connect(self.callvintubacion)
        #Manejar la Ventana        
        resolucion=ctypes.windll.user32 #Resolucion de la pantalla
        ancho=resolucion.GetSystemMetrics(0)
        alto=resolucion.GetSystemMetrics(1)
        posx=(ancho/2)-(self.frameSize().width()/2)
        posy=(alto/2)-(self.frameSize().height()/2)
        self.move(posx,posy) #Iniciar la ventana en el centro de la pantalla
        
        #Validacion IP
        self.ui.teip.setFocus()   
        self.ui.btnip.clicked.connect(self.validarip)
        self.v=1
        
             
    def validarip(self):
        self.ip=self.ui.teip.toPlainText()
        try:           
            self.ip1=self.ip.split(".")
            c=0
            for i in range(len(self.ip1)):
                if(int(self.ip1[i])<=255):c+=1
                else:
                    QMessageBox.information(QtGui.QWidget(),"Error IP","Valor máximo 255",QMessageBox.Ok)
                    break;
            if(c==4): 
                self.conec()
                if self.v==2:self.ui.groupBox.setEnabled(True)
                            
        except:
            QMessageBox.information(QtGui.QWidget(),"Error IP","El formato ingresado no es válido",QMessageBox.Ok)
            self.ui.groupBox.setEnabled(False)
            
    def conec(self):        
        self.scli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = self.ip
        PORT = 10700
        try:
            self.scli.settimeout(2)
            self.scli.connect((HOST, PORT))     
            print('Conectado al servidor')
            self.scli.send("F".encode())
            self.scli.recv(100)
            saludo=self.scli.recv(100)
            print(saludo.decode())
            self.v=2
            self.ui.btnip.setEnabled(False)
            self.ui.teip.setEnabled(False)
        except:
            print("Servidor aún no encontrado")
            self.v=1
            ms=QMessageBox.critical(QtGui.QWidget(),"Servidor no encontrado", "Verifique que la ip ingresada pertenezca a Raspberry\n"
                                           , QMessageBox.Ok,QMessageBox.Abort)
            if(ms==QMessageBox.Abort): 
                sys.exit(app.exec_())
               
                    
    def callvrcp(self):
        self.objvrcp=Vrcp(self.ip)
        self.objvrcp.exec_()  #Show no modal)
        try:
            del self.objintubacion
        except:
            pass
        try:
            del self.objescenarios
        except:
            pass
    
    def callvescenarios(self):
        self.objescenarios=Vescenarios(self.ip)
        self.objescenarios.exec_()
        try:
            del self.objvrcp
        except:
            pass
        try:
            del self.objintubacion
        except:
            pass
            
    def callvintubacion(self):
        self.objintubacion=Vintubacion(self.ip)
        self.objintubacion.exec_()
        try:
            del self.objvrcp
        except:
            pass
        try:
            del self.objescenarios
        except:
            pass

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv) #Instanciar
    objvprincipal = Vescenarios("192.168.1.5") #Creo un objeto demi clase principal
    objvprincipal.show()  #Mostrar ventana
    sys.exit(app.exec_()) #Ejecutar Aplicacion
    """
    #pasar datos a las ventanas de resultados
    vecd=[7,2,3,5,5,7,7]
    vect=[1,2,3,4,5,7,7] 
    objvprincipal = tabla(vecd,vect) #Creo un objeto de mi clase principal
    """