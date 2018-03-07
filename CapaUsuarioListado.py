from tkinter import *
from tkinter import ttk
from CapaNegocioReserva import CNReserva
from CapaDatosAlchemy import CapaDatosReserva
from CapaNegocioVuelo import CNVuelo

class CUListado():
   def __init__(self):
       self.ventana = Tk()
       self.tree = ttk.Treeview(self.ventana)

   def interfaz(self):
       vp=Frame(self.ventana)
       vp.grid(column=0, row=0,  sticky=(N, S, E, W))

       self.ventana.title("Menu")
       self.ventana.resizable
       self.ventana.geometry('200x225')

       self.tree.grid(row=1,column=1,columnspan=3,rowspan = 9,sticky=(N, S, E, W))

       botonA = Button(self.ventana, text="  Reservas  ", command=lambda: self.todasreservas(),background="#b0b9e5",activebackground="#99a6e5",cursor="hand2")
       botonA.grid(row=2,column=2,sticky=(N, S, E, W))

       botonB = Button(self.ventana,text="  Reservas por cliente  ", command= lambda: self.reservasxcliente(),background="#b0b9e5",activebackground="#99a6e5",cursor="hand2")
       botonB.grid(row=4,column=2,columnspan=1,sticky=(N, S, E, W))

       botonM = Button(self.ventana,text="  Capacidad por vuelo  ", command=lambda: self.mostrarcapacidad(),background="#b0b9e5",activebackground="#99a6e5",cursor="hand2")
       botonM.grid(row=6,column=2,sticky=(N, S, E, W))

       self.ventana.mainloop()

   def todasreservas(self):
        self.cnr = CNReserva()

        self.ventana2 = Tk()
        self.tree2 = ttk.Treeview(self.ventana2)

        vp2=Frame(self.ventana2)
        vp2.grid(column=0, row=0,  sticky=(N, S, E, W))

        self.ventana2.title("Todas reservas")
        self.tree2["columns"]=("vuelo_dia_hora_salida","cliente_dni","fecha_reserva")
        self.tree2.column("#0", width=50)
        self.tree2.column("vuelo_dia_hora_salida", width=100)
        self.tree2.column("cliente_dni", width=100)
        self.tree2.column("fecha_reserva", width=100)


        self.tree2.heading("#0", text="Nro Vuelo")
        self.tree2.heading("vuelo_dia_hora_salida", text="Salida")
        self.tree2.heading("cliente_dni", text="DNI Cliente")
        self.tree2.heading("fecha_reserva", text="Fecha Reserva")

        lista= self.cnr.todosreserva()
        for i in range(len(lista)):
               self.tree2.insert("", lista[i].vuelo_nro_vuelo,text=lista[i].vuelo_nro_vuelo, values=(lista[i].vuelo_dia_hora_salida,lista[i].cliente_dni,lista[i].fecha_reserva))

        self.ventana2.title("ABM Reservas")
        self.ventana2.resizable
        self.ventana2.geometry('650x400')
        self.ventana2.columnconfigure(0,weight=0)
        self.ventana2.columnconfigure(1,weight=1)
        self.ventana2.columnconfigure(2,weight=1)
        self.ventana2.rowconfigure(1,weight=1)

        self.tree2.grid(row=1,column=0,columnspan=3,rowspan = 1,sticky=(N, S, E, W))

        self.ventana2.mainloop()

   def reservasxcliente(self):

       tl=Toplevel()
       tl.title("Listar por cliente")

       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

       self.dni=StringVar()

       botonbusca = Button(tl, text="Buscar",command=lambda: self.confirmaBusqueda())
       botonbusca.grid(column=2, row=3)

       etiquetanombre=Label(vp, text= "Dni: ")
       etiquetanombre.grid(column=0, row=0)
       entradanombre=Entry(vp, width= 20, textvariable= self.dni)
       entradanombre.grid(column=1, row=0)

   def confirmaBusqueda(self):
        #self.cn = CNCliente()
        self.cdr = CapaDatosReserva()
        a=self.dni.get()

        #Cliente= self.cn.buscaxDni(a)
        self.ventana2 = Tk()
        self.tree2 = ttk.Treeview(self.ventana2)

        vp2=Frame(self.ventana2)
        vp2.grid(column=0, row=0,  sticky=(N, S, E, W))

        self.ventana2.title("Todas reservas")
        self.tree2["columns"]=("vuelo_dia_hora_salida","cliente_dni","fecha_reserva")
        self.tree2.column("#0", width=50)
        self.tree2.column("vuelo_dia_hora_salida", width=100)
        self.tree2.column("cliente_dni", width=100)
        self.tree2.column("fecha_reserva", width=100)


        self.tree2.heading("#0", text="Nro Vuelo")
        self.tree2.heading("vuelo_dia_hora_salida", text="Salida")
        self.tree2.heading("cliente_dni", text="DNI Cliente")
        self.tree2.heading("fecha_reserva", text="Fecha Reserva")

        lista= self.cdr.reservasxcliente(a)
        for i in range(len(lista)):
              self.tree2.insert("", lista[i].nro_vuelo,text=lista[i].nro_vuelo, values=(lista[i].dia_hora_salida,lista[i].dia_hora_llegada,lista[i].aerolinea,lista[i].destino,lista[i].capacidad,lista[i].precio))

        self.ventana2.title("ABM Reservas")
        self.ventana2.resizable
        self.ventana2.geometry('650x400')
        self.ventana2.columnconfigure(0,weight=0)
        self.ventana2.columnconfigure(1,weight=1)
        self.ventana2.columnconfigure(2,weight=1)
        self.ventana2.rowconfigure(1,weight=1)

        self.tree2.grid(row=1,column=0,columnspan=3,rowspan = 1,sticky=(N, S, E, W))

        self.ventana2.mainloop()

   def mostrarcapacidad(self):
       self.cnv = CNVuelo()
       self.ventana2 = Tk()
       self.tree2 = ttk.Treeview(self.ventana2)
       vp=Frame(self.ventana2)
       vp.grid(column=0, row=0,  sticky=(N, S, E, W))

       self.tree2["columns"]=("dia_hora_salida","capacidad")
       self.tree2.column("#0", width=50)
       self.tree2.column("dia_hora_salida", width=150)
       self.tree2.column("capacidad", width=100)


       self.tree2.heading("#0", text="Nro vuelo")
       self.tree2.heading("dia_hora_salida", text="Salida")
       self.tree2.heading("capacidad", text="Capacidad")


       lista= self.cnv.todosvuelo()
       for i in range(len(lista)):
              self.tree.insert("", lista[i].nro_vuelo,text=lista[i].nro_vuelo, values=(lista[i].dia_hora_salida,lista[i].capacidad))

       #Configuracion de la ventana:
       self.ventana2.title("ABM Vuelos")
       self.ventana2.resizable
       self.ventana2.geometry('800x400')
       self.ventana2.columnconfigure(0,weight=0)
       self.ventana2.columnconfigure(1,weight=1)
       self.ventana2.rowconfigure(1,weight=1)

       self.tree2.grid(row=1,column=1,columnspan=3,rowspan = 1,sticky=(N, S, E, W))
       self.ventana2.mainloop()
