"""
Creado con Python3 y PyQt5
Calculadora de suma reversible
Creador: Jose Carlos Mar Rangel
"""

#suma de arreglo de numeros

import sys #Libreria necesaria para correr el GUI
from PyQt5.QtWidgets import QApplication #Crear la app
from interfaz import gui # gui de la app

if __name__ == '__main__': #Comprobar si este programa se esta ejecutando
    app = QApplication(sys.argv)
    metodogui = gui()
    app.exec_()