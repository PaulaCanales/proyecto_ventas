# -*- coding: utf-8 -*-
import sqlite3
from PySide import QtGui
from UI_Form_Cli import Ui_Form
from Ui_Cliente import Ui_Cliente
import model

class FormCliente(QtGui.QDialog):

    def __init__(self, parent=None, rut=None):
        """
        Formulario para crear y editar cliente.
        Si se recibe la var rut
        entonces se está en modo de edición.
        """
        super(FormCliente, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        if rut is None:
            self.ui.aceptar.clicked.connect(self.crear_cliente)
        else:
            self.colocar_datos(rut)
            self.ui.aceptar.clicked.connect(self.edita_cliente)

    def colocar_datos(self, rut):
        """
        Coloca los datos del cliente en los widgets
        para su edición
        """
        cliente = model.obtener_nombre(rut)
        self.ui.rut.setText(str(cliente["rut"]))
        self.ui.nombre.setText(cliente["nombres"])
        self.ui.apellido.setText(cliente["apellidos"])
        self.ui.correo.setText(cliente["correo"])
        self.ui.rut.setEnabled(False)

    def edita_cliente(self): 
        """
        Edita los datos del cliente
        """
        rut, nombres, apellidos, correo = self.obtener_datos() 
        
        try: 
            model.editar_cliente(rut, nombres, apellidos, correo)
            # Invocar la función del modelo que permite editar 
            self.accepted.emit() 
            msgBox = QtGui.QMessageBox() 
            msgBox.setText(u"El cliente ha sido editado.") 
            msgBox.exec_() 
            self.close() 
            print "Editar" 
        except sqlite3.Error as e: 
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"Error!")
            msgBox.exec_() 

    def obtener_datos(self):
        """
        Obtiene los datos colocados por el usuario
        en el formulario
        """
        rut = self.ui.rut.text()
        nombres = self.ui.nombre.text()
        apellidos = self.ui.apellido.text()
        correo = self.ui.correo.text()
        return (rut, nombres, apellidos, correo)

    def crear_cliente(self):
        """
        Se crea un nuevo cliente a partir de los datos
        ingresados en el formulario 
        """
        rut, nombres, apellidos, correo = self.obtener_datos()
        try:
            model.crear_cliente(rut, nombres, apellidos, correo)
            self.accepted.emit()
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"El cliente ha sido creado.")
            msgBox.exec_()
            self.close()
        except sqlite3.Error as e:
            
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"Error Rut invalido!!")
            msgBox.exec_() 
        
        
            

	

