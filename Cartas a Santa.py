# Elaborado por: Javier Rivera Madrigal y Natalia Vargas Reyes
# Fecha de creación: 31/10/2019
# Ultima modificación:
# Version 3.7.2

# Importacion de librerias

#XML
import xml.etree.ElementTree as ET

from xml.etree.ElementTree import ElementTree

#GUI

from tkinter import *

import tkinter.ttk as t #usar algunos widgets como el cbx


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
    juguetes = list(diccionario.values())
    print(juguetes)
    print("Inventario cargado con exito")

 
def ventanaInicial():
    """
    Función: Coloca los widgets del frame1 y el frame1 en la ventana principal.
    Entradas: Ninguna.
    Salidas: Ninguna.
    """
    lblLogo.place(x=650,y=400)
    lblLogo2.place(x=60,y=200)
    
    frame1.grid(row=0,column=0, rowspan=19, columnspan=24, sticky=(E,W,N,S))
    franja1.grid(row=0,column=0, rowspan=4, columnspan=24, sticky=(E,W,N,S))
    lblTitulo1.place(x=250,y=35)
    
    btnCargar.grid(row=6,column=9, rowspan=2, columnspan=6, sticky=(E,W,N,S))
    btnGenerarCartas.grid(row=9,column=9, rowspan=2, columnspan=6, sticky=(E,W,N,S)) # El botón es cargado
    btnReportes.grid(row=12,column=9, rowspan=2, columnspan=6, sticky=(E,W,N,S)) # El botón es cargado
    btnSalir.grid(row=15,column=9, rowspan=2, columnspan=6, sticky=(E,W,N,S)) 
  
    frame2.grid_remove()
    frame3.grid_remove()
    frame4.grid_remove()
    
    return ''

def ventanaReportes():
    """
    Función: Coloca los widgets del frame2 y el frame2 en la ventana principal.
    Entradas: Ninguna.
    Salidas: Ninguna.
    """
    lblLogo3.place(x=690,y=490)
    frame2.grid(row=0,column=0, rowspan=19, columnspan=24, sticky=(E,W,N,S))
    franja2.grid(row=0,column=0, rowspan=3, columnspan=24, sticky=(E,W,N,S))
    lblTitulo2.place(x=320,y=35)

    btnSolicitantes.grid(row=4,column=9, rowspan=2, columnspan=6, sticky=(E,W,N,S))
    btn2Juguetes.grid(row=7,column=9, rowspan=2, columnspan=6, sticky=(E,W,N,S))
    btnInventario.grid(row=10,column=9, rowspan=2, columnspan=6, sticky=(E,W,N,S))
    btnListaSexo.grid(row=13,column=9, rowspan=2, columnspan=6, sticky=(E,W,N,S))
    btnCarta.grid(row=16,column=9, rowspan=2, columnspan=6, sticky=(E,W,N,S))
    btnAtras.place(x=40,y=25)

    frame1.grid_remove()
    frame3.grid_remove()
    frame4.grid_remove()

    return ''

def ventanaSolicitantes():
    """
    Función: Coloca los widgets del frame3 y el frame3 en la ventana principal.
    Entradas: Ninguna.
    Salidas: Ninguna.
    """
    
    lblLogo4.place(x=690,y=490)
    frame3.grid(row=0,column=0, rowspan=19, columnspan=24, sticky=(E,W,N,S))
    franja3.grid(row=0,column=0, rowspan=3, columnspan=24, sticky=(E,W,N,S))
    lblTitulo3.place(x=240,y=35)

    lblJuguete.grid(row=6, column=11, rowspan=1, columnspan=3, sticky=(E,W,N,S))
    cbxJuguetes.grid(row=8,column=11, rowspan=1, columnspan=3, sticky=(E,W,N,S))
    btnMostrar.grid(row=15,column=11, rowspan=1, columnspan=3, sticky=(E,W,N,S))
    btnAtras2.place(x=40,y=25)
     
    frame1.grid_remove()
    frame2.grid_remove()
    frame4.grid_remove()


def ventanaCarta():
    """
    Función: Coloca los widgets del frame4 y el frame4 en la ventana principal.
    Entradas: Ninguna.
    Salidas: Ninguna.
    """
    
    lblLogo5.place(x=690,y=440)
    frame4.grid(row=0,column=0, rowspan=19, columnspan=24, sticky=(E,W,N,S))
    franja4.grid(row=0,column=0, rowspan=3, columnspan=24, sticky=(E,W,N,S))
    lblTitulo4.place(x=360,y=35)

    lblJuguete.grid(row=6, column=11, rowspan=1, columnspan=3, sticky=(E,W,N,S))
    cbxNombres.grid(row=8,column=11, rowspan=1, columnspan=3, sticky=(E,W,N,S))
    btnMostrar2.grid(row=15,column=11, rowspan=1, columnspan=3, sticky=(E,W,N,S))
    btnAtras3.place(x=40,y=25)
     
    frame1.grid_remove()
    frame2.grid_remove()
    frame3.grid_remove()

    
def salir():
    """
    Función: Cierra la ventana.
    Entradas: Ninguna.
    Salidas: Ninguna.
    """
    
    ventana1.destroy()
    return ''



#☻♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥☻#

ventana1=Tk() #creacion del objeto ventana
ventana1.title("Sistema de Cartas para Santa")
ventana1.iconbitmap("tree.ico")
ventana1.resizable(0,0)
#---------------Se crean filas y columnas en la ventana---------------#
for i in range(0, 24):   #se crean 4 columnas.
    ventana1.columnconfigure(i, weight=1)
for i in range(0, 19):  #se crean 8 filas.
    ventana1.rowconfigure(i, weight=1)
    
#---------------Solo es para ver las rayitas de la ventana-------------#
f=24
c=19
for k in range(0, f+1):
    frame= Frame(ventana1, width=1, height=650, bg="#424242")
    frame.grid(row= 0, column=k, rowspan=f, sticky= "NW")
for k in range(0, c+1):
    frame= Frame(ventana1, width=850, height=1, bg="#424242")
    frame.grid(row= k, column=0, columnspan=c, sticky= "NW")




#------------------------WIDGETS DE VENTANAINICIAL---------------#
frame1 = Frame(ventana1, bg= '#FFFFFF')
for i in range(0, 24):
    frame1.columnconfigure(i, weight=1)
for i in range(0, 19):
    frame1.rowconfigure(i, weight=1)

franja1 = Frame(frame1, bg= '#088A4B')


#state='disabled',
lblTitulo1=Label(franja1, text='Cartas a Santa', fg="#FFFFFF", font=('Super Mario 256', 26),bg='#088A4B')

btnReportes=Button(frame1,text="Reportes",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",\
                       bg="#DF0101",command=lambda:ventanaReportes())
btnGenerarCartas=Button(frame1,text="Generar Cartas",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",\
                       bg="#DF0101")#,command=lambda: 
btnCargar=Button(frame1,text="Cargar Inventario",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",bg="#DF0101",command=lambda:leerXml())

btnSalir=Button(frame1,text="Salir",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",bg="#DF0101",command=lambda:salir())

    
logo=PhotoImage(file="santa-claus.png")
lblLogo=Label(frame1,image=logo, bg='#FFFFFF')
logo2=PhotoImage(file="elf.png")
lblLogo2=Label(frame1,image=logo2, bg='#FFFFFF') 


#------------------------WIDGETS DE VENTANAREPORTES---------------#
frame2 = Frame(ventana1, bg= '#FFFFFF')
for i in range(0, 24):
    frame2.columnconfigure(i, weight=1)
for i in range(0, 19):
    frame2.rowconfigure(i, weight=1)

franja2 = Frame(frame2, bg= '#088A4B')


lblTitulo2=Label(franja2, text='Reportes', fg="#FFFFFF", font=('Super Mario 256', 26),bg='#088A4B')

btnSolicitantes=Button(frame2,text="Solicitantes por juguete",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF", \
                       bg="#DF0101",command=lambda:ventanaSolicitantes())
btn2Juguetes=Button(frame2,text="Interesados en 2 juguetes o más",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",\
                       bg="#DF0101")
btnInventario=Button(frame2,text="Inventario",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",bg="#DF0101")

btnListaSexo=Button(frame2,text="Lista Solicitantes según sexo",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",bg="#DF0101")

btnCarta=Button(frame2,text="Carta de un niño",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",bg="#DF0101",\
                command=lambda:ventanaCarta())

btnAtras=Button(franja2,text="Atrás",font= ('Super Mario 256', 10, 'bold'), fg="#FFFFFF",bg="#DF0101",command=lambda:ventanaInicial())

logo3=PhotoImage(file="regalo.png")
lblLogo3=Label(frame2,image=logo3, bg='#FFFFFF')


#------------------------WIDGETS DE VENTANASOLICITANTES---------------#
frame3 = Frame(ventana1, bg= '#FFFFFF')
for i in range(0, 24):
    frame3.columnconfigure(i, weight=1)
for i in range(0, 19):
    frame3.rowconfigure(i, weight=1)

franja3 = Frame(frame3, bg= '#088A4B')

lblTitulo3=Label(franja3, text='Solicitantes por juguete', fg="#FFFFFF", font=('Super Mario 256', 20),bg='#088A4B')
lblJuguete=Label(frame3, text="Seleccione el juguete: ", fg='#0A0A2A', font=('Super Mario 256', 12),bg="#FFFFFF")

cbxJuguetes=t.Combobox(frame3, values=("Juguete1"))
#cbxJuguetes.bind("<<ComboboxSelected>>",funcion a llamar)

btnMostrar=Button(frame3,text="Mostrar",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",bg="#DF0101",state='disabled')
btnAtras2=Button(franja3,text="Atrás",font= ('Super Mario 256', 10, 'bold'), fg="#FFFFFF",bg="#DF0101",\
                 command=lambda:ventanaReportes())

logo4=PhotoImage(file="sack.png")
lblLogo4=Label(frame3,image=logo4, bg='#FFFFFF')


#------------------------WIDGETS DE VENTANACARTA---------------#
frame4 = Frame(ventana1, bg= '#FFFFFF')
for i in range(0, 24):
    frame4.columnconfigure(i, weight=1)
for i in range(0, 19):
    frame4.rowconfigure(i, weight=1)

franja4 = Frame(frame4, bg= '#088A4B')

lblTitulo4=Label(franja4, text='Carta', fg="#FFFFFF", font=('Super Mario 256', 26),bg='#088A4B')
lblJuguete=Label(frame4, text="Seleccione el nombre: ", fg='#0A0A2A', font=('Super Mario 256', 12),bg="#FFFFFF")

cbxNombres=t.Combobox(frame4, values=("Nombre1"))
#cbxNombres.bind("<<ComboboxSelected>>",funcion a llamar)

btnMostrar2=Button(frame4,text="Mostrar",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",bg="#DF0101",state='disabled')
btnAtras3=Button(franja4,text="Atrás",font= ('Super Mario 256', 10, 'bold'), fg="#FFFFFF",bg="#DF0101",\
                 command=lambda:ventanaReportes())
logo5=PhotoImage(file="card.png")
lblLogo5=Label(frame4,image=logo5, bg='#FFFFFF')


#ventanaCarta()
#ventanaSolicitantes()
#ventanaReportes()
ventanaInicial()
ventana1.mainloop()
