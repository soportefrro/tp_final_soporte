from CapaNegocioVuelo import CNVuelo
from tkinter import *
from tkinter import ttk
from CapaDatosAlchemy import Vuelo


class CUVuelo():
   def __init__(self):
       self.cnv = CNVuelo()
       self.ventana = Tk()
       self.tree = ttk.Treeview(self.ventana)


   def interfaz(self):

       vp=Frame(self.ventana)
       vp.grid(column=0, row=0,  sticky=(N, S, E, W))

       self.tree["columns"]=("dia_hora_salida","dia_hora_llegada","aerolinea","destino","capacidad","precio")
       self.tree.column("#0", width=50)
       self.tree.column("dia_hora_salida", width=150)
       self.tree.column("dia_hora_llegada", width=150)
       self.tree.column("aerolinea", width=100)
       self.tree.column("destino", width=100)
       self.tree.column("capacidad", width=100)
       self.tree.column("precio", width=100)

       self.tree.heading("#0", text="Nro vuelo")
       self.tree.heading("dia_hora_salida", text="Salida")
       self.tree.heading("dia_hora_llegada", text="Llegada")
       self.tree.heading("aerolinea", text="Aerolinea")
       self.tree.heading("destino", text="Destino")
       self.tree.heading("capacidad", text="Capacidad")
       self.tree.heading("precio", text="Precio")

       lista= self.cnv.todosvuelo()
       for i in range(len(lista)):
              self.tree.insert("", lista[i].nro_vuelo,text=lista[i].nro_vuelo, values=(lista[i].dia_hora_salida,lista[i].dia_hora_llegada,lista[i].aerolinea,lista[i].destino,lista[i].capacidad,lista[i].precio))

       #Configuracion de la ventana:
       self.ventana.title("ABM Vuelos")
       self.ventana.resizable
       self.ventana.geometry('800x400')
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
       a=self.nro_vuelo.get()
       b=self.dia_hora_salida.get()
       c=self.dia_hora_llegada.get()
       d=self.aerolinea.get()
       e=self.destino.get()
       f=self.capacidad.get()
       g=self.precio.get()

       vuelo = Vuelo(nro_vuelo= a, dia_hora_salida= b, dia_hora_llegada= c,aerolinea =d,destino=e,capacidad=f,precio=g)
       self.cnv.altavuelo(vuelo)

       tl=Toplevel()
       tl.title("Vuelo agregado")
       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
       etique=Label(vp, text="El vuelo ha sido agregado")
       etique.grid(column=1, row=1)
       botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
       botoncerrar.grid(column=1, row=2)
       self.refresh()




   def alta(self):
       tl=Toplevel()
       self.ventana.title("Formulario nuevo Vuelo")

       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

       self.nro_vuelo=IntVar()
       self.dia_hora_salida= StringVar()
       self.dia_hora_llegada=StringVar()
       self.aerolinea= StringVar()
       self.destino= StringVar()
       self.capacidad= IntVar()
       self.precio = IntVar()

       botonagrega = Button(tl, text="Agregar",command=lambda: self.confirmaAlta())
       botonagrega.grid(column=2, row=3)

       etiquetanombre=Label(vp, text= "Nro Vuelo")
       etiquetanombre.grid(column=0, row=0)
       entradanombre=Entry(vp, width= 20, textvariable= self.nro_vuelo)
       entradanombre.grid(column=1, row=0)

       etiquetaapellido=Label(vp, text= "Salida")
       etiquetaapellido.grid(column=0, row=1)
       entradaapellido=Entry(vp, width= 20, textvariable= self.dia_hora_salida)
       entradaapellido.grid(column=1, row=1)

       etiquetadni=Label(vp, text= "Llegada")
       etiquetadni.grid(column=0, row=2)
       entradadni=Entry(vp, width= 20, textvariable= self.dia_hora_llegada)
       entradadni.grid(column=1, row=2)

       etiquetadni=Label(vp, text= "Aerolinea")
       etiquetadni.grid(column=0, row=3)
       entradadni=Entry(vp, width= 20, textvariable= self.aerolinea)
       entradadni.grid(column=1, row=3)

       etiquetadni=Label(vp, text= "destino")
       etiquetadni.grid(column=0, row=4)
       entradadni=Entry(vp, width= 20, textvariable= self.destino)
       entradadni.grid(column=1, row=4)

       etiquetadni=Label(vp, text= "capacidad")
       etiquetadni.grid(column=0, row=5)
       entradadni=Entry(vp, width= 20, textvariable= self.capacidad)
       entradadni.grid(column=1, row=5)

       etiquetadni=Label(vp, text= "precio")
       etiquetadni.grid(column=0, row=6)
       entradadni=Entry(vp, width= 20, textvariable= self.precio)
       entradadni.grid(column=1, row=6)



   def baja(self):
       posicion=self.tree.selection()
       var1=self.tree.item(posicion,"text")
       var2=self.tree.item(posicion) ['values'][0]
       v = self.cnv.buscar(var1,var2)  #Quiero mandarle dos parametros
       self.cnv.borrar(v)

       tl=Toplevel()
       tl.title("Vuelo borrado")
       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
       etique=Label(vp, text="El vuelo ha sido borrado")
       etique.grid(column=1, row=1)
       botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
       botoncerrar.grid(column=1, row=2)
       self.refresh()

   def confirmaModificar(self,var1,var2):

       c=self.dia_hora_llegada.get()
       d=self.aerolinea.get()
       e=self.destino.get()
       f=self.capacidad.get()
       g=self.precio.get()

       v = Vuelo(nro_vuelo= var1, dia_hora_salida= var2, dia_hora_llegada= c,aerolinea =d,destino=e,capacidad=f,precio=g)
       self.cnv.modificar(v)

       # ventana de confirmación
       tl=Toplevel()
       tl.title("Vuelo modificado")
       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
       etique=Label(vp, text="El vuelo ha sido modificado")
       etique.grid(column=1, row=1)
       botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
       botoncerrar.grid(column=1, row=2)

       self.refresh()
   def modificar(self):
       tl=Toplevel()
       self.ventana.title("Formulario nuevo Vuelo")

       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

       self.nro_vuelo=IntVar()
       self.dia_hora_salida= StringVar()
       self.dia_hora_llegada=StringVar()
       self.aerolinea= StringVar()
       self.destino= StringVar()
       self.capacidad= IntVar()
       self.precio = IntVar()

       posicion=self.tree.selection()
       var1=self.tree.item(posicion,"text")
       var2=self.tree.item(posicion)['values'][0]

       v = self.cnv.buscar(var1,var2)
       self.nro_vuelo.set(var1)
       self.dia_hora_salida.set(var2)
       self.dia_hora_llegada.set(v.dia_hora_llegada)
       self.aerolinea.set(v.aerolinea)
       self.destino.set(v.destino)
       self.capacidad.set(v.capacidad)
       self.precio.set(v.precio)

       botonmodifica = Button(tl, text="Modificar",command=lambda: self.confirmaModificar(var1,var2))
       botonmodifica.grid(column=2, row=3)


       etiquetanombre=Label(vp, text= "Nro Vuelo")
       etiquetanombre.grid(column=0, row=0)
       entradanombre=Entry(vp, width= 20, textvariable= self.nro_vuelo)
       entradanombre.grid(column=1, row=0)

       etiquetaapellido=Label(vp, text= "Salida")
       etiquetaapellido.grid(column=0, row=1)
       entradaapellido=Entry(vp, width= 20, textvariable= self.dia_hora_salida)
       entradaapellido.grid(column=1, row=1)

       etiquetadni=Label(vp, text= "Llegada")
       etiquetadni.grid(column=0, row=2)
       entradadni=Entry(vp, width= 20, textvariable= self.dia_hora_llegada)
       entradadni.grid(column=1, row=2)

       etiquetadni=Label(vp, text= "Aerolinea")
       etiquetadni.grid(column=0, row=3)
       entradadni=Entry(vp, width= 20, textvariable= self.aerolinea)
       entradadni.grid(column=1, row=3)

       etiquetadni=Label(vp, text= "destino")
       etiquetadni.grid(column=0, row=4)
       entradadni=Entry(vp, width= 20, textvariable= self.destino)
       entradadni.grid(column=1, row=4)

       etiquetadni=Label(vp, text= "capacidad")
       etiquetadni.grid(column=0, row=5)
       entradadni=Entry(vp, width= 20, textvariable= self.capacidad)
       entradadni.grid(column=1, row=5)

       etiquetadni=Label(vp, text= "precio")
       etiquetadni.grid(column=0, row=6)
       entradadni=Entry(vp, width= 20, textvariable= self.precio)
       entradadni.grid(column=1, row=6)

   def refresh(self):
       [self.tree.delete(c) for c in self.tree.get_children()]
       lista= self.cnv.todosvuelo()
       for i in range(len(lista)):
              self.tree.insert("", lista[i].nro_vuelo,text=lista[i].nro_vuelo, values=(lista[i].dia_hora_salida,lista[i].dia_hora_llegada,lista[i].aerolinea,lista[i].destino,lista[i].capacidad,lista[i].precio))





