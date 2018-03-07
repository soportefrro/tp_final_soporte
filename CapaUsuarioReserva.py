from CapaNegocioReserva import CNReserva
from CapaNegocioVuelo import CNVuelo
from CapaNegocioSocio import CNCliente
from tkinter import *
from tkinter import ttk
from CapaDatosAlchemy import Reserva
from CapaDatosAlchemy import Vuelo

class CUReserva():
   def __init__(self):
       self.cnr = CNReserva()
       self.ventana = Tk()
       self.tree = ttk.Treeview(self.ventana)


   def interfaz(self):

       vp=Frame(self.ventana)
       vp.grid(column=0, row=0,  sticky=(N, S, E, W))

       self.tree["columns"]=("vuelo_dia_hora_salida","cliente_dni","fecha_reserva")
       self.tree.column("#0", width=50)
       self.tree.column("vuelo_dia_hora_salida", width=100)
       self.tree.column("cliente_dni", width=100)
       self.tree.column("fecha_reserva", width=100)


       self.tree.heading("#0", text="Nro Vuelo")
       self.tree.heading("vuelo_dia_hora_salida", text="Salida")
       self.tree.heading("cliente_dni", text="DNI Cliente")
       self.tree.heading("fecha_reserva", text="Fecha Reserva")

       lista= self.cnr.todosreserva()
       for i in range(len(lista)):
              self.tree.insert("", lista[i].vuelo_nro_vuelo,text=lista[i].vuelo_nro_vuelo, values=(lista[i].vuelo_dia_hora_salida,lista[i].cliente_dni,lista[i].fecha_reserva))

       #Configuracion de la ventana:
       self.ventana.title("ABM Reservas")
       self.ventana.resizable
       self.ventana.geometry('650x400')
       self.ventana.columnconfigure(0,weight=0)
       self.ventana.columnconfigure(1,weight=1)
       self.ventana.columnconfigure(2,weight=1)
       self.ventana.columnconfigure(3,weight=1)
       self.ventana.columnconfigure(4,weight=1)
       self.ventana.rowconfigure(1,weight=1)

       self.tree.grid(row=1,column=1,columnspan=3,rowspan = 1,sticky=(N, S, E, W))

       botonA = Button(self.ventana, text=" Alta  ", command=lambda: self.alta(),background="#ADF5A9",cursor="hand2")
       botonA.grid(row=5,column=1,sticky=(N, S, E, W))

       botonB = Button(self.ventana,text="  Baja  ", command= lambda: self.baja(),background="#F5A9A9",cursor="hand2")
       botonB.grid(row=5,column=2,columnspan=1,sticky=(N, S, E, W))

       botonM = Button(self.ventana,text="  Modificacion  ", command=lambda: self.modificar(),background="#7EB0EA",cursor="hand2")
       botonM.grid(row=5,column=3,sticky=(N, S, E, W))

       self.ventana.mainloop()

   def confirmaAlta(self):
       a=self.vuelo_nro_vuelo.get()
       b=self.vuelo_dia_hora_salida.get()
       c=self.cliente_dni.get()
       d=self.fecha_reserva.get()


       reserva = Reserva(vuelo_nro_vuelo= a, vuelo_dia_hora_salida= b, cliente_dni= c,fecha_reserva =d)
       self.cnr.altareserva(reserva)

       tl=Toplevel()
       tl.title("Reserva hecha")
       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
       etique=Label(vp, text="La reserva se ha realizado con éxito")
       etique.grid(column=1, row=1)
       botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
       botoncerrar.grid(column=1, row=2)
       self.refresh()

   def alta(self):
       self.cnv = CNVuelo()

       self.ventana2 = Tk()
       self.tree2 = ttk.Treeview(self.ventana2)

       vp2=Frame(self.ventana2)
       vp2.grid(column=0, row=0,  sticky=(N, S, E, W))

       self.tree2["columns"]=("dia_hora_salida","dia_hora_llegada","aerolinea","destino","capacidad","precio")
       self.tree2.column("#0", width=75)
       self.tree2.column("dia_hora_salida", width=150)
       self.tree2.column("dia_hora_llegada", width=150)
       self.tree2.column("aerolinea", width=100)
       self.tree2.column("destino", width=100)
       self.tree2.column("capacidad", width=100)
       self.tree2.column("precio",width=100)

       self.tree2.heading("#0", text="Nro vuelo")
       self.tree2.heading("dia_hora_salida", text="Salida")
       self.tree2.heading("dia_hora_llegada", text="Llegada")
       self.tree2.heading("aerolinea", text="Aerolinea")
       self.tree2.heading("destino", text="Destino")
       self.tree2.heading("capacidad", text="Capacidad")
       self.tree2.heading("precio", text="Precio")

       lista= self.cnv.todosvuelo()
       for i in range(len(lista)):
              self.tree2.insert("", lista[i].nro_vuelo,text=lista[i].nro_vuelo, values=(lista[i].dia_hora_salida,lista[i].dia_hora_llegada,lista[i].aerolinea,lista[i].destino,lista[i].capacidad,lista[i].precio))

       self.ventana2.title("Lista de vuelos")
       self.ventana2.resizable
       self.ventana2.geometry('800x400')
       self.ventana2.columnconfigure(0,weight=0)
       self.ventana2.columnconfigure(1,weight=1)
       self.ventana2.columnconfigure(2,weight=1)
       self.ventana2.columnconfigure(3,weight=1)
       self.ventana2.columnconfigure(4,weight=1)
       self.ventana2.rowconfigure(1,weight=1)

       etiquetaseleccionar=Label(vp2, text= "Seleccione el Vuelo para el cual desea reservar")
       etiquetaseleccionar.grid(column=0, row=0)

       self.tree2.grid(row=1,column=0,columnspan=3,rowspan = 1,sticky=(N, S, E, W))

       botonA = Button(self.ventana2, text="Agregar", command=lambda: self.mapear(),background="#ADF5A9")
       botonA.grid(row=5,column=1,sticky=(N, S, E, W))

       self.ventana.mainloop()

   def mapear(self):

       posicion=self.tree2.selection()
       var1=self.tree2.item(posicion,"text")
       var2=self.tree2.item(posicion)['values'][0]
       self.alta2(var1,var2)


   def alta2(self,var1,var2):
       self.cn = CNCliente()
       self.ventana2 = Tk()
       self.tree2 = ttk.Treeview(self.ventana2)

       vp2=Frame(self.ventana2)
       vp2.grid(column=0, row=0,  sticky=(N, S, E, W))

       self.tree2["columns"]=("nombre","apellido","mail","telefono","sexo")
       self.tree2.column("#0", width=100)
       self.tree2.column("nombre", width=100)
       self.tree2.column("apellido", width=100)
       self.tree2.column("mail", width=150)
       self.tree2.column("telefono", width=100)
       self.tree2.column("sexo", width=100)


       self.tree2.heading("#0", text="DNI")
       self.tree2.heading("nombre", text="Nombre")
       self.tree2.heading("apellido", text="Apellido")
       self.tree2.heading("mail", text="E-Mail")
       self.tree2.heading("telefono", text="Telefono")
       self.tree2.heading("sexo", text="Sexo (M/F)")

       lista= self.cn.todos()
       for i in range(len(lista)):
              self.tree2.insert("", lista[i].dni,text=lista[i].dni, values=(lista[i].nombre,lista[i].apellido,lista[i].mail,lista[i].telefono,lista[i].sexo))

       self.ventana2.title("Lista de clientes")
       self.ventana2.resizable
       self.ventana2.geometry('800x400')
       self.ventana2.columnconfigure(0,weight=0)
       self.ventana2.columnconfigure(1,weight=1)
       self.ventana2.columnconfigure(2,weight=1)
       self.ventana2.columnconfigure(3,weight=1)
       self.ventana2.columnconfigure(4,weight=1)
       self.ventana2.rowconfigure(1,weight=1)

       etiquetaseleccionar=Label(vp2, text= "           Seleccione el Cliente que reserva")
       etiquetaseleccionar.grid(column=0, row=0)

       self.tree2.grid(row=1,column=0,columnspan=3,rowspan = 1,sticky=(N, S, E, W))


       botonA = Button(self.ventana2, text="Agregar", command=lambda: self.formuAlta(var1,var2),background="#ADF5A9")
       botonA.grid(row=5,column=1,sticky=(N, S, E, W))
       self.ventana.mainloop()


   def formuAlta(self,var1,var2):
       tl=Toplevel()
       self.ventana.title("Formulario nueva Reserva")

       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

       self.vuelo_nro_vuelo=IntVar()
       self.vuelo_dia_hora_salida= StringVar()
       self.cliente_dni=StringVar()
       self.cliente_nombre=StringVar()
       self.cliente_apellido=StringVar()
       self.fecha_reserva= StringVar()
       self.precio =IntVar()

       posicion=self.tree2.selection()
       var3=self.tree2.item(posicion,"text")

       v = self.cnv.buscar(var1,var2)
       self.vuelo_nro_vuelo.set(var1)
       self.vuelo_dia_hora_salida.set(var2)
       self.precio.set(v.precio)

       c= self.cn.buscaxDni(var3)
       self.cliente_dni.set(var3)
       self.cliente_nombre.set(c.nombre)
       self.cliente_apellido.set(c.apellido)

       botonagrega = Button(tl, text="Agregar",command=lambda: self.formuAlta2())
       botonagrega.grid(column=2, row=3)

       etiquetanombre=Label(vp, text= "Nro Vuelo")
       etiquetanombre.grid(column=0, row=6)
       entradanombre=Entry(vp, width= 20, textvariable= self.vuelo_nro_vuelo, state='disabled')
       entradanombre.grid(column=1, row=6)

       etiquetaapellido=Label(vp, text= "Salida")
       etiquetaapellido.grid(column=0, row=7)
       entradaapellido=Entry(vp, width= 20, textvariable= self.vuelo_dia_hora_salida, state='disabled')
       entradaapellido.grid(column=1, row=7)

       etiquetadni=Label(vp, text= "DNI")
       etiquetadni.grid(column=0, row=8)
       entradadni=Entry(vp, width= 20, textvariable= self.cliente_dni, state='disabled')
       entradadni.grid(column=1, row=8)

       etiquetadni=Label(vp, text= "Apellido")
       etiquetadni.grid(column=0, row=9)
       entradadni=Entry(vp, width= 20, textvariable= self.cliente_apellido, state='disabled')
       entradadni.grid(column=1, row=9)

       etiquetadni=Label(vp, text= "Nombre")
       etiquetadni.grid(column=0, row=10)
       entradadni=Entry(vp, width= 20, textvariable= self.cliente_nombre, state='disabled')
       entradadni.grid(column=1, row=10)

       etiquetadni=Label(vp, text= "fecha_reserva")
       etiquetadni.grid(column=0, row=11)
       entradadni=Entry(vp, width= 20, textvariable= self.fecha_reserva)
       entradadni.grid(column=1, row=11)

       etiquetadni=Label(vp, text= "precio")
       etiquetadni.grid(column=0, row=12)
       entradadni=Entry(vp, width= 20, textvariable= self.precio, state='disabled')
       entradadni.grid(column=1, row=12)


   def baja(self):
       posicion=self.tree.selection()
       var1=self.tree.item(posicion,"text")
       v = self.cnr.buscar(var1)  #Quiero mandarle dos parametros
       self.cnr.borrar_reserva(v)

       tl=Toplevel()
       tl.title("Reserva borrada")
       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
       etique=Label(vp, text="La reserva ha sido cancelada con éxito")
       etique.grid(column=1, row=1)
       botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
       botoncerrar.grid(column=1, row=2)
       self.refresh()

   def formuAlta2(self):

       a=self.vuelo_nro_vuelo.get()
       b=self.vuelo_dia_hora_salida.get()
       c=self.cliente_dni.get()
       d=self.fecha_reserva.get()

       reserva = Reserva(vuelo_nro_vuelo= a, vuelo_dia_hora_salida= b, cliente_dni= c,fecha_reserva =d)
       if self.cnr.altareserva(reserva):
           tl=Toplevel()
           tl.title("Reserva agregada")
           vp=Frame(tl)
           vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
           etique=Label(vp, text="La reserva ha sido agregada")
           etique.grid(column=1, row=1)
           botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
           botoncerrar.grid(column=1, row=2)
           self.refresh()
       else:
           tl=Toplevel()
           tl.title("ERROR")
           vp=Frame(tl)
           vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
           etique=Label(vp, text="Operación fallida. No queda lugar disponible en el vuelo seleccionado")
           etique.grid(column=1, row=1)
           botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
           botoncerrar.grid(column=1, row=2)
           self.refresh()

   def confirmaModificar(self,var1):

       c=self.destino.get()
       d=self.fecha.get()
       e=self.precio.get()

       r = Reserva(id_reserva= var1, destino= c,fecha=d,precio=e)

       if self.cnr.modificar(r):
           # ventana de confirmación
           tl=Toplevel()
           tl.title("Reserva modificada")
           vp=Frame(tl)
           vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
           etique=Label(vp, text="La reserva ha sido modificada con éxito")
           etique.grid(column=1, row=1)
           botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
           botoncerrar.grid(column=1, row=2)
           self.refresh()
       else:
            # ventana de error
           tl=Toplevel()
           tl.title("ERROR")
           vp=Frame(tl)
           vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
           etique=Label(vp, text="Operación fallida. Existen campos vacios o iguales a 0\n")
           etique.grid(column=1, row=1)
           botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
           botoncerrar.grid(column=1, row=2)
           self.refresh()

   def modificar(self):
       tl=Toplevel()
       self.ventana.title("Formulario modificar reserva")

       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

       self.id_reserva=IntVar()
       self.destino= StringVar()
       self.fecha=StringVar()
       self.precio= StringVar()

       posicion=self.tree.selection()
       var1=self.tree.item(posicion,"text")

       v = self.cnr.buscar(var1)
       self.id_reserva.set(var1)
       self.destino.set(v.destino)
       self.fecha.set(v.fecha)
       self.precio.set(v.precio)

       botonmodifica = Button(tl, text="Modificar",command=lambda: self.confirmaModificar(var1))
       botonmodifica.grid(column=2, row=3)


       etiquetanombre=Label(vp, text= "ID Reserva")
       etiquetanombre.grid(column=0, row=0)
       entradanombre=Entry(vp, width= 20, textvariable= self.id_reserva)
       entradanombre.grid(column=1, row=0)

       etiquetaapellido=Label(vp, text= "Destino")
       etiquetaapellido.grid(column=0, row=1)
       entradaapellido=Entry(vp, width= 20, textvariable= self.destino)
       entradaapellido.grid(column=1, row=1)

       etiquetadni=Label(vp, text= "Fecha")
       etiquetadni.grid(column=0, row=2)
       entradadni=Entry(vp, width= 20, textvariable= self.fecha)
       entradadni.grid(column=1, row=2)

       etiquetadni=Label(vp, text= "Precio")
       etiquetadni.grid(column=0, row=3)
       entradadni=Entry(vp, width= 20, textvariable= self.precio)
       entradadni.grid(column=1, row=3)


   def refresh(self):
       [self.tree.delete(c) for c in self.tree.get_children()]
       lista= self.cnr.todosreserva()
       for i in range(len(lista)):
              self.tree.insert("", lista[i].vuelo_nro_vuelo,text=lista[i].vuelo_nro_vuelo, values=(lista[i].vuelo_dia_hora_salida,lista[i].cliente_dni,lista[i].fecha_reserva))



