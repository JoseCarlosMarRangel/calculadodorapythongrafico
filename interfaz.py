#Importaciones
#import sys #cargar librerias necesarias para funcionar
from PyQt5.QtWidgets import(QGridLayout, QStyleFactory, QWidget, QPushButton, QLineEdit,
                            QVBoxLayout)
from PyQt5.QtCore import *
from sistema import convertir


arraynum = []

class gui(QWidget):

    
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Sistema de ecuaciones')
        self.show()
        
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Reversible")
        self.setLayout(QVBoxLayout())
        self.keypad()
        self.setStyle(QStyleFactory.create("Fusion"))
        self.show()
    
    def suma(self):
        arraynum = self.numinicial.text()
        #b= [int(x) for x in arraynum.split(',')]
        #print(b)
        self.resultado = convertir(arraynum)
        #print(arraynum)
        
    def igual(self):
        self.numinicial.setText(str(self.resultado))
            
    def limpiar(self):
        y= ''
        self.numinicial.setText(y)
        
    def keypad(self):
        container = QWidget()
        container.setLayout(QGridLayout())
        
        #botones
        self.numinicial = QLineEdit()
        btn_result = QPushButton("=", clicked=self.igual)
        btn_clear = QPushButton("C", clicked=self.limpiar)
        btn_plus = QPushButton("+", clicked= self.suma)
        
        #añadir botones al layout
        container.layout().addWidget(self.numinicial, 0, 0, 1, 4)
        container.layout().addWidget(btn_result, 1, 0,1,2)
        container.layout().addWidget(btn_clear, 1, 2,1,2)
        container.layout().addWidget(btn_plus, 2, 0,1,4)    
        self.layout().addWidget(container)