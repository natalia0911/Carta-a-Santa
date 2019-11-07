# Elaborado por: Javier Rivera Madrigal y Natalia Vargas Reyes
# Fecha de creación: 31/10/2019 4:00 PM
# Ultima modificación: 06/11/2019 7:00 PM
# Version 3.7.2

# Importacion de librerias

#XML
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree

#GUI
from tkinter import *
import tkinter.ttk as t #usar algunos widgets como el cbx

#Utilidades
from faker import Faker #Usar perfiles Falsos
import random
import pickle
import webbrowser

# Globales
global juguetes
juguetes = []

# Definicion de clases
class Ninno:
     
    def __init__(self,pnombre):
        """
        Funcion: Constructor de clase.
        Entrada: Nombre, string
        Salida:  .
        """
        self.nombre = pnombre
        self.apellidos = ''
        self.edad = 0
        self.sexo = ''
        self.juguetes = []
        
    def obtenerNombre(self):
        """
        Funcion: Da el nombre del objeto
        Entrada: Ninguna.
        Salida:  el nombre del objeto
        """
        return self.nombre
    
    
    def guardarApellidos(self, papellidos):
        """
        Funcion: Da los apellidos del objeto.
        Entrada: Ninguna.
        Salida:  el nombre del objeto
        """
        self.apellidos = papellidos
        
    def obtenerApellidos(self):
        """
        Funcion: Da los apellidos del objeto.
        Entrada: Ninguna.
        Salida:  el nombre del objeto
        """
        return self.apellidos
    
        
    def guardarEdad(self,pedad):
        """
        Funcion:  Cambia la edad del objeto
        Entrada: edad, entero
        Salida: Ninguna.
        """
        self.edad = pedad
    
    def obtenerEdad(self):
        """
        Funcion: Da la edad del objeto
        Entrada: Ninguna.
        Salida:  self.edad
        """
        return self.edad
     
    def guardarSexo(self,psexo):
        """
        Funcion:  Guarda el sexo del objeto
        Entrada: El sexo, string
        Salida: Ninguna.
        """
        self.sexo = psexo
    
    def obtenerSexo(self):
        """
        Funcion: Da el sexo del objeto
        Entrada: Ninguna.
        Salida:  El sexo del objeto, string
        """
        return self.sexo

    def guardarJuguetes(self,pjuguetes):
        """
        Funcion: Guarda los objetos del ninno
        Entrada: Una lista con juguetes
        Salida: Ninguna.
        """
        self.juguetes = pjuguetes

    def obtenerJuguetes(self):
        """
        Funcion: Da los juguetes del objeto
        Entrada: Ninguna.
        Salida:  Una lista con juguetes
        """
        return self.juguetes
    
    def mostrar(self):
        """
        Funcion: Muestra todos los atributos
        Entrada: Ninguna.
        Salida: Todos los atributos.
        """
        print("\nNombre: ",self.nombre,"\nApellidos:", self.apellidos,"\nEdad: ",self.edad,"\nSexo: ",self.sexo,
              "\nJuguetes: ",self.juguetes)


# Definicion de Funciones
def guardarEntxt(plista):
    """
    Funcion: Guarda la lista creada o modificada, en el txt.
    Entradas: plista.
    Salidas: Ninguna, error en caso de fallo al guardar.
    """
    try:
        archivo=open("objetos.txt","wb") 
        pickle.dump(plista, archivo)
        archivo.close()
    except:
        print("Error al guardar en el archivo.")
    return True


def mostrarTxt():
    """
    Funcion: Crear una lista con la información del archivo leído.
    Entradas: Ninguna.
    Salidas: lista.
    """
    lista=[]
    try:
        archivo=open("objetos.txt","rb") 
        lista=pickle.load(archivo) 
        archivo.close()
    except:
       lista =[] #Para continuar y asignarle algo a todosPerfiles
    return lista


def leerXml():
    """
    Funcion: Lee el archivo xml y lo guarda en un diccionario
    Entrada: Ninguna.
    Salida:  .
    """
    #btnGenerarCartas.config(state='normal')
    tree = ElementTree()
    tree = ET.parse("juguetes.xml")
    root = tree.getroot()
     

    for child in root:
        juguetes.append([child.get("ID"),child[0].text.rstrip('\n'),child[1].text.rstrip('\n')])
        
    #print(juguetes) #VER JUGUETES
    print("Inventario cargado con éxito")


    return juguetes

def generarCartas():
    """
    Funcion: Genera las listas de objetos con la información de los niños.
    Entrada: Ninguna.
    Salida:  .
    """
    fake = Faker()
    
    for i in range(10):
        
        listJuguetes = []
        perfiles=fake.simple_profile()
        cantJuguetes = random.randint(1,3)
            
        for i in perfiles:
            if i =='name':
                perfil=perfiles[i].split(' ')
                nuevoNino= Ninno(perfil[0])
                
                perfil[1]+=' '+fake.last_name()
                nuevoNino.guardarApellidos(perfil[1])
                
                
            if i =='sex':
                perfil.append(perfiles[i])
                nuevoNino.guardarSexo(perfiles[i])
                edad=random.randint(0,12)
                perfil.append(edad)
                perfil.append(listJuguetes)
                nuevoNino.guardarEdad(edad)
                
        for j in range(cantJuguetes):
            jugueteRandom = random.randint(0,len(juguetes)-1)
            if juguetes[jugueteRandom][1] not in listJuguetes:
                listJuguetes.append(juguetes[jugueteRandom][1])
                nuevoNino.guardarJuguetes(listJuguetes)
                
        todosPerfiles.append(nuevoNino)
        nuevoNino.mostrar()
        
    guardarEntxt(todosPerfiles)
        
    #print(todosPerfiles)#VER OBJETOS

    return ''
def crearReporteDosJuguetes():
    """
    Función: Crea un archivo html
    Entrada: Ninguna
    Salida:  abre un archivo en el buscador
    """
    reporte= open("Reporte2juguetes.html","w")
    reporte.write("<html>\n")
    escribirReporteDosJuguetes(reporte)
    reporte.write("</html>\n")
    reporte.close
    url = "file:///C:/Users/javir/Desktop/TEC%20Javi/Progra/Tarea%20Programada%20%233/Reporte2juguetes.html"
    return webbrowser.open(url,new=2)
    
def escribirReporteDosJuguetes(reporte):
    """
    Función: Escribe la tabla del reporte de 2 juguetes o mas
    Entrada: reporte de HTML
    Salida: .
    """
    
    color = "#e33217"
    reporte.write("<head>\n")
    reporte.write("<title>Reporte de juguetes</title>\n")
    reporte.write("</head>\n")
    reporte.write("<style type='text/css'> table,th,td{border:1px solid black;border-collapse:collapse;}th,td{padding:10px;}h2{text-align: center</style>")
    reporte.write("<body>\n")
    reporte.write("<h1>Niños con dos juguetes o más</h1>\n")
    reporte.write("</body>\n")
    reporte.write("<TABLE style='width:100%'\n")
    reporte.write("<TR>\n")
    reporte.write("<TH>Nombre </TH>\n")
    reporte.write("<TH>Edad </TH>\n")
    reporte.write("<TH>Lista de Juguetes </TH>\n")
    reporte.write("<TH>Sexo </TH>\n")
    reporte.write("</TR>\n")
    #reporte.write("<FONT FACE=arial>")
    for ninno in todosPerfiles:
        if len(ninno.obtenerJuguetes())>=2:
            reporte.write("<TR BGCOLOR="+color+">\n")
            reporte.write("<TD align=center>"+ninno.obtenerNombre()+" "+ninno.obtenerApellidos()+"</TD>\n")
            reporte.write("<TD align=center>"+str(ninno.obtenerEdad())+"</TD>\n")
            reporte.write("<TD align=center>")
            for juguete in ninno.obtenerJuguetes():
                if  juguete != ninno.obtenerJuguetes()[-1]:
                    reporte.write(juguete+", ")
                else:
                     reporte.write(juguete)
            reporte.write("</TD>\n")
            if ninno.obtenerSexo() == "M":
                reporte.write("<TD align=center>"+"Masculino"+"</TD>\n")
            else:
                reporte.write("<TD align=center>"+"Femenino"+"</TD>\n")
            reporte.write("</TR>\n")
            if color=="#e33217":    #Hace que el color cambie en cada fila
                color="#2ed92e"
            else:
                color="#e33217"
    #reporte.write("</FONT>")
    return

def reporteInventario():
    """
    Función: Escribe la tabla del reporte de inventario de los juguetes.
    Entrada: .
    Salida: .
    """
    
    reporte= open("Inventario.html","w")
    reporte.write("<html>\n")
   
    color = "#9FF781"
    reporte.write("<head>\n")
    reporte.write("<title>Inventario de juguetes</title>\n")
    reporte.write("</head>\n")
    reporte.write("<style type='text/css'> table,th,td{border:1px solid black;border-collapse:collapse;}th,td{padding:10px;}h2{text-align: center</style>")
    reporte.write("<body>\n")
    reporte.write("<h1>Inventario de juguetes</h1>\n")
    reporte.write("</body>\n")
    reporte.write("<TABLE style='width:100%'\n")
    reporte.write("<TR>\n")
    reporte.write("<TH>ID del juguete</TH>\n")
    reporte.write("<TH>Nombre</TH>\n")
    reporte.write("<TH>Descripción</TH>\n")
    reporte.write("<TH>Imagen</TH>\n")
    reporte.write("</TR>\n")
    #padding-left: 20px;
    for juguete in juguetes:
        
        reporte.write("<TR BGCOLOR="+color+">\n")
        reporte.write("<TD align=center>"+juguete[0]+"</TD>\n")
        reporte.write("<TD align=center>"+juguete[1]+"</TD>\n")
        reporte.write("<TD align=center>"+juguete[2]+"</TD>\n")
        if juguete[1]=="Carro con prepulsión":
            reporte.write("<TD align=center><img src='https://www.tailoy.com.pe/media/catalog/product/cache/1/image/640x/"+\
                          "9df78eab33525d08d6e5fb8d27136e95/2/6/26976-2.jpg' alt='Barbie' style='width:100px;height:100px;'></TD>\n")

        elif juguete[1]=="Barbie de nieve":
            reporte.write("<TD align=center><img src='https://unrinconenmivitrina.files.wordpress.com/2017/03/barbie-snow.jpg?w=474'+\
                          alt='Barbie' style='width:100px;height:100px;'></TD>\n")

        elif juguete[1]=="Barbie de nieve":
            reporte.write("<TD align=center><img src='https://www.tailoy.com.pe/media/catalog/product/cache/1/image/640x/"+\
                          "9df78eab33525d08d6e5fb8d27136e95/2/6/26976-2.jpg' alt='Barbie' style='width:100px;height:100px;'></TD>\n")

        elif juguete[1]=="Barbie enfermera":
            reporte.write("<TD align=center><img src='https://irion.cl/wp-content/uploads/2019/08/mat_fwk89_ghw34_c-600x600.jpg'+\
                            alt='Barbie' style='width:100px;height:100px;'></TD>\n")

        elif juguete[1]=="Barbie programadora":
            reporte.write("<TD align=center><img src='https://live.staticflickr.com/5504/30528801791_cf6c67d638_b.jpg'+\
                          alt='Barbie' style='width:100px;height:100px;'></TD>\n")

        elif juguete[1]=="Peluche Pooh":
            reporte.write("<TD align=center><img src='https://ae01.alicdn.com/kf/HTB1Adj1XPvuK1Rjy0Faq6x2aVXat/Disney-"+\
                          "Winnie-The-Pooh-Hand-Puppet-Plush-Toy-Pooh-Stuffed-Plush-Dolls-Toys-Birthday-Gifts-For.jpg' alt='Barbie' style='width:100px;height:100px;'></TD>\n")

        elif juguete[1]=="Figura de acción Batman":
            reporte.write("<TD align=center><img src='https://s3.amazonaws.com/media.toynk.com/html/media/import/Jan2019/MEZ-76994-CA.jpg'+\
                          alt='Barbie' style='width:100px;height:100px;'></TD>\n")

        elif juguete[1]=="Peluche Dango":
            reporte.write("<TD align=center><img src='https://ae01.alicdn.com/kf/HTB1L1BhdwoQMeJjy0Foq6AShVXag/CLANNAD-Dango-juguetes"+\
                          "-de-peluche-Daikazoku-Furukawa-Nagisa-Dango-coj-n-de-peluche-familiar-Cosplay-para.jpg' alt='Barbie' style='width:100px;height:100px;'></TD>\n")

        elif juguete[1]=="Funko Naruto shippuden":
            reporte.write("<TD align=center><img src='https://www.tooys.mx/pub/media/catalog/product/cache"+\
                          "/89d4a95274a31fe8bdfcc437494b2c9e/n/a/naruto-sage-funko.jpg' alt='Barbie' style='width:100px;height:100px;'></TD>\n")

        elif juguete[1]=="Bebé paco":
            reporte.write("<TD align=center><img src='https://images-na.ssl-images-amazon.com/images/I/81KwXkLgZcL._SL1500_.jpg'+\
                          alt='Barbie' style='width:100px;height:100px;'></TD>\n")

        elif juguete[1]=="Computadora de juguete":
            reporte.write("<TD align=center><img src='https://childrens.com.ar/app/uploads/imagenes/productos/grandes/f1_21009.jpg'+\
                          alt='Barbie' style='width:100px;height:100px;'></TD>\n")

        elif juguete[1]=="Libro El principito":
            reporte.write("<TD align=center><img src='https://www.sanborns.com.mx/imagenes-sanborns-ii/1200/9786124076633.jpg'+\
                          alt='Barbie' style='width:100px;height:100px;'></TD>\n")
        else:
            reporte.write("<TD align=center><img src='http://www.libreriacuesta.com/content/images/thumbs/default-image_550.png'+\
                          alt='Barbie' style='width:100px;height:100px;'></TD>\n")


        reporte.write("</TR>\n")
        
        if color=="#9FF781":    #Hace que el color cambie en cada fila
            color="#8181F7"
        else:
            color="#9FF781"
                
    reporte.write("</html>\n")
    reporte.close
    return 


def reporteSolicitantesJuguete():
    """
    Función: Escribe la tabla del reporte de solicitantes por juguete.
    Entrada: reporte de HTML
    Salida: .
    """
    jugueteSeleccionado=cbxJuguetes.get()
    print(jugueteSeleccionado)

    reporte= open("SolicitantesJuguete.html","w")
    reporte.write("<html>\n")
   
    color = "#9FF781"
    reporte.write("<head>\n")
    reporte.write("<title>Reporte de juguetes</title>\n")
    reporte.write("</head>\n")
    reporte.write("<style type='text/css'> table,th,td{border:1px solid black;border-collapse:collapse;}th,td{padding:10px;}h2{text-align: center</style>")
    reporte.write("<body>\n")
    reporte.write("<h1>Solicitantes por juguete: "+jugueteSeleccionado+".</h1>\n")
    reporte.write("</body>\n")
    reporte.write("<TABLE style='width:100%'\n")
    reporte.write("<TR>\n")
    reporte.write("<TH>Nombre completo</TH>\n")
    reporte.write("<TH>Edad</TH>\n")
    reporte.write("</TR>\n")
    
    
    for ninno in todosPerfiles:
        if jugueteSeleccionado in ninno.obtenerJuguetes():
            reporte.write("<TR BGCOLOR="+color+">\n")
            reporte.write("<TD align=center>"+ninno.obtenerNombre()+" "+ninno.obtenerApellidos()+"</TD>\n")
            reporte.write("<TD align=center>"+str(ninno.obtenerEdad())+"</TD>\n")
            reporte.write("</TR>\n")
            
            if color=="#9FF781":    #Hace que el color cambie en cada fila
                color="#8181F7"
            else:
                color="#9FF781"
                
    reporte.write("</html>\n")
    reporte.close
    return 

def tomarJuguete(event):
    """
    Función: Funcion del evento del comboBox cbxJuguetes,toma el valor seleccionado.
    Entradas: El evento.
    Salidas: Llama a mostrarSolicitantesJuguete(jugueteSeleccionado).
    """
    jugueteSeleccionado=cbxJuguetes.get()
    btnMostrar.config(state='normal')
    print(jugueteSeleccionado)
    return 

def mostrarSolicitantesJuguete():
    """
    Función: Funcion del evento del comboBox cbxJuguetes,toma el valor seleccionado.
    Entradas: El evento.
    Salidas: Llama a mostrarSolicitantesJuguete(jugueteSeleccionado).
    """
    global juguetes
    listaJuguetes = []
    for i in juguetes:
        listaJuguetes.append(i[1])

    cbxJuguetes["values"]=listaJuguetes
    return ''


def btnAceptarCantCartas():
    """
    Función: Acciones que suceden al precionar el boton aceptar tras haber ingreso la cantidad de cartas.
    Entradas: Ninguna.
    Salidas: Ninguna.
    """
    pass
def ventanitaCantCartas():
    """
    Función: Crea una pequeña ventana para pedir la cantidad de cartas a generar.
    Entradas: Ninguna.
    Salidas: Ninguna.
    """
    ventanita=Tk() #creacion del objeto ventana
    ventanita.title("Sistema de Cartas para Santa")
    ventanita.iconbitmap("tree.ico")
    ventanita.resizable(0,0)
    ventanita.config(bg='#FFFFFF')
    #---------------Se crean filas y columnas en la ventana---------------#
    for i in range(0, 19):   
        ventanita.columnconfigure(i, weight=1)
    for i in range(0, 19):  
        ventanita.rowconfigure(i, weight=1)
        
    #---------------Solo es para ver las rayitas de la ventana-------------#
    f=19
    c=19
    for k in range(0, f+1):
        frame= Frame(ventanita, width=1, height=250, bg='#FFFFFF')
        frame.grid(row= 0, column=k, rowspan=f, sticky= "NW")
    for k in range(0, c+1):
        frame= Frame(ventanita, width=330, height=1, bg='#FFFFFF')
        frame.grid(row= k, column=0, columnspan=c, sticky= "NW")

    lblCantidad=Label(ventanita, text='Cantidad de Cartas a generar: ', fg="#DF0101", font=('Super Mario 256', 10),bg='#FFFFFF')
    entradaC=StringVar()
    entradaC.set("") #Se declara la variable que permite el set y get del Entry
    entCantidad=Entry(ventanita, textvariable=entradaC)
    btnAceptar=Button(ventanita,text="Aceptar",font= ('Super Mario 256', 10, 'bold'), fg="#FFFFFF",\
                       bg="#DF0101")#,command=lambda:ventanaReportes()

    lblCantidad.grid(row=5,column=2, rowspan=1, columnspan=15, sticky=(E,W,N,S))
    entCantidad.grid(row=8,column=5, rowspan=1, columnspan=9, sticky=(E,W,N,S))
    btnAceptar.grid(row=13,column=7, rowspan=1, columnspan=5, sticky=(E,W,N,S))


    cantidad = entradaC.get()
    generarCartas()
    return ''

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
    mostrarSolicitantesJuguete()
    
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
# Globales 
juguetes = []
todosPerfiles = mostrarTxt()

#creacion del objeto ventana
ventana1=Tk()  
ventana1.title("Sistema de Cartas para Santa")
ventana1.iconbitmap("tree.ico")
ventana1.resizable(0,0)
#---------------Se crean filas y columnas en la ventana---------------#
for i in range(0, 24):   
    ventana1.columnconfigure(i, weight=1)
for i in range(0, 19):  
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
                       bg="#DF0101",state='disabled',command=lambda:ventanitaCantCartas())
btnCargar=Button(frame1,text="Cargar Inventario",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",bg="#DF0101",\
                 command=lambda:leerXml())

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
                       bg="#DF0101",command=lambda: crearReporteDosJuguetes())
btnInventario=Button(frame2,text="Inventario",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",bg="#DF0101",\
                     command=lambda: reporteInventario())

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

cbxJuguetes=t.Combobox(frame3, values=(""),state='readonly')
cbxJuguetes.bind("<<ComboboxSelected>>",tomarJuguete)

btnMostrar=Button(frame3,text="Mostrar",font= ('Super Mario 256', 12, 'bold'), fg="#FFFFFF",bg="#DF0101",state='disabled',\
                  command=lambda:reporteSolicitantesJuguete())
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

#ventanitaCantCartas()
#ventanaCarta()
#ventanaSolicitantes()
#ventanaReportes()
ventanaInicial()
ventana1.mainloop()
