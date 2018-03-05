from CapaNegocioReserva import CNReserva
from tkinter import *
from tkinter import ttk
from CapaDatosAlchemy import Reserva


class CUReserva():
   def __init__(self):
       self.cnr = CNReserva()
       self.ventana = Tk()
       self.tree = ttk.Treeview(self.ventana)


   def interfaz(self):

       vp=Frame(self.ventana)
       vp.grid(column=0, row=0,  sticky=(N, S, E, W))

       self.tree["columns"]=("destino","fecha", "precio")
       self.tree.column("#0", width=50)
       self.tree.column("destino", width=150)
       self.tree.column("fecha", width=150)
       self.tree.column("precio", width=150)


       self.tree.heading("#0", text="ID Reserva")
       self.tree.heading("destino", text="Destino")
       self.tree.heading("fecha", text="Fecha Reserva")
       self.tree.heading("precio", text="Precio")


       lista= self.cnr.todosreserva()
       for i in range(len(lista)):
              self.tree.insert("", lista[i].id_reserva,text=lista[i].id_reserva, values=(lista[i].destino,lista[i].fecha,lista[i].precio))

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

       botonA = Button(self.ventana, text=" Alta  ", command=lambda: self.alta(),background="#ADF5A9")
       botonA.grid(row=5,column=1,sticky=(N, S, E, W))

       botonB = Button(self.ventana,text="  Baja  ", command= lambda: self.baja(),background="#F5A9A9" )
       botonB.grid(row=5,column=2,columnspan=1,sticky=(N, S, E, W))

       botonM = Button(self.ventana,text="  Modificacion  ", command=lambda: self.modificar(),background="#7EB0EA")
       botonM.grid(row=5,column=3,sticky=(N, S, E, W))

       self.ventana.mainloop()

   def confirmaAlta(self):
       a=self.id_reserva.get()
       b=self.destino.get()
       c=self.fecha.get()
       d=self.precio.get()


       reserva = Reserva(id_reserva= a, destino= b, fecha= c,precio =d)
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
       tl=Toplevel()
       self.ventana.title("Formulario nueva reserva")

       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

       self.id_reserva=IntVar()
       self.destino= StringVar()
       self.fecha=StringVar()
       self.precio= StringVar()


       botonagrega = Button(tl, text="Agregar",command=lambda: self.confirmaAlta())
       botonagrega.grid(column=2, row=3)

       etiquetanombre=Label(vp, text= "ID reserva")
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

   def confirmaModificar(self,var1):

       c=self.destino.get()
       d=self.fecha.get()
       e=self.precio.get()

       r = Reserva(id_reserva= var1, destino= c,fecha=d,precio=e)
       self.cnr.modificar(r)

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
              self.tree.insert("", lista[i].id_reserva,text=lista[i].id_reserva, values=(lista[i].destino,lista[i].fecha,lista[i].precio))



