# Elaborado por: Javier Rivera Madrigal
# Fecha de creación: 31/10/2019
# Ultima modificación:
# Version 3.7.2

# Importacion de librerias

#XML
import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import ElementTree
 


# Globales
diccionario = {}

# Definicion de clases

# Definicion de Funciones

def leerXml():
    """
    Funcion: Lee el archivo xml y lo guarda en un diccionario
    Entrada: .
    Salida:  .
    
    """
    tree = ElementTree()
    tree = ET.parse("juguetes.xml")
    root = tree.getroot()

    for child in root:
        diccionario[child.get("ID")]=[child[0].text,child[1].text]
        
 
