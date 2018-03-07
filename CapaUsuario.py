from CapaNegocioSocio import CNCliente
from tkinter import *
from tkinter import ttk
from CapaDatosAlchemy import Cliente

class CUCliente():

   def __init__(self):
       self.cn = CNCliente()
       self.ventana = Tk()
       self.tree = ttk.Treeview(self.ventana)

   def interfaz(self):

       vp=Frame(self.ventana)
       vp.grid(column=0, row=0,  sticky=(N, S, E, W))

       self.tree["columns"]=("nombre","apellido", "mail", "telefono", "sexo")
       self.tree.column("#0", width=100)
       self.tree.column("nombre", width=100)
       self.tree.column("apellido", width=100)
       self.tree.column("mail", width=100)
       self.tree.column("telefono", width=100)
       self.tree.column("sexo", width=100)

       self.tree.heading("#0", text="Dni")
       self.tree.heading("nombre", text="Nombre")
       self.tree.heading("apellido", text="Apellido")
       self.tree.heading("mail", text="Mail")
       self.tree.heading("telefono", text="Telefono")
       self.tree.heading("sexo", text="Sexo")

      # for i in self.cn.todos():
       #    self.tree.insert("",i[0],text=i[0],values=(i[1],i[2],i[3]))

       lista= self.cn.todos()
       for i in range(len(lista)):
              self.tree.insert("", lista[i].dni,text=lista[i].dni, values=(lista[i].nombre,lista[i].apellido,lista[i].mail,lista[i].telefono,lista[i].sexo))

       #Configuracion de la ventana:
       self.ventana.title("ABM Clientes")
       self.ventana.resizable
       self.ventana.geometry('700x400')
       self.ventana.columnconfigure(0,weight=1)
       self.ventana.columnconfigure(1,weight=1)
       self.ventana.columnconfigure(2,weight=1)
       self.ventana.columnconfigure(3,weight=1)
       self.ventana.columnconfigure(4,weight=1)
       self.ventana.columnconfigure(5,weight=1)
       self.ventana.rowconfigure(1,weight=1)

       self.tree.grid(row=1,column=1,columnspan=6,rowspan = 1,sticky=(N, S, E, W))

       botonA = Button(self.ventana, text=" Alta  ", command=lambda: self.alta(),background="#ADF5A9",cursor="hand2")
       botonA.grid(row=5,column=1,columnspan=2,sticky=(N, S, E, W))

       botonB = Button(self.ventana,text="Baja", command= lambda: self.baja(),background="#F5A9A9",cursor="hand2")
       botonB.grid(row=5,column=3,columnspan=2,sticky=(N, S, E, W))

       botonM = Button(self.ventana,text="  Modificacion  ", command=lambda: self.modificar(),background="#7EB0EA",cursor="hand2")
       botonM.grid(row=5,column=5, columnspan=2,sticky=(N, S, E, W))

       """botonAct = Button(self.ventana,text="  Refrescar  ", command=lambda: self.refresh())
       botonAct.grid(row=5,column=4,sticky=(N, S, E, W))"""

       self.ventana.mainloop()

   def confirmaModificar(self, indice):

       a=self.nombre.get()
       b=self.apellido.get()
       d=self.mail.get()
       e=self.telefono.get()
       f=self.sexo.get()

       s= Cliente(dni= indice, nombre= a, apellido= b, mail= d, telefono= e, sexo=f)

       retorno= self.cn.modificar(s)

       if retorno == False:
           # ventana de error
           tl=Toplevel()
           tl.title("ERROR")
           vp=Frame(tl)
           vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
           etique=Label(vp, text="Operación fallida. Existen campos vacíos\n")
           etique.grid(column=1, row=1)
           botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
           botoncerrar.grid(column=1, row=2)
       else:
           # ventana de confirmación
           tl=Toplevel()
           tl.title("Cliente modificado")
           vp=Frame(tl)
           vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
           etique=Label(vp, text="El cliente ha sido modificado")
           etique.grid(column=1, row=1)
           botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
           botoncerrar.grid(column=1, row=2)
           self.refresh()


   def confirmaAlta(self):
       a=self.nombre.get()
       b=self.apellido.get()
       c=self.dni.get()
       d=self.mail.get()
       e=self.telefono.get()
       f=self.sexo.get()

       s= Cliente(dni= c, nombre= a, apellido= b, mail= d, telefono= e, sexo=f)

       if (self.cn.alta(s)):
           tl=Toplevel()
           tl.title("Cliente agregado")
           vp=Frame(tl)
           vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
           etique=Label(vp, text="El cliente ha sido agregado")
           etique.grid(column=1, row=1)
           botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
           botoncerrar.grid(column=1, row=2)
           self.refresh()
       else:
           tl=Toplevel()
           tl.title("ERROR")
           vp=Frame(tl)
           vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
           etique=Label(vp, text="El DNI ingresado ya existe o quedaron campos vacíos\n\nPor favor modifíquelos\n")
           etique.grid(column=1, row=1)
           botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
           botoncerrar.grid(column=1, row=2)
           self.refresh()


   def alta(self):
       tl=Toplevel()
       tl.title("Formulario nuevo cliente")

       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

       self.nombre=StringVar()
       self.dni=StringVar()
       self.apellido= StringVar()
       self.mail=StringVar()
       self.telefono=StringVar()
       self.sexo= StringVar()

       botonagrega = Button(tl, text="Agregar",command=lambda: self.confirmaAlta())
       botonagrega.grid(column=2, row=3)

       etiquetanombre=Label(vp, text= "Nombre: ")
       etiquetanombre.grid(column=0, row=0)
       entradanombre=Entry(vp, width= 20, textvariable= self.nombre)
       entradanombre.grid(column=1, row=0)

       etiquetaapellido=Label(vp, text= "Apellido: ")
       etiquetaapellido.grid(column=0, row=1)
       entradaapellido=Entry(vp, width= 20, textvariable= self.apellido)
       entradaapellido.grid(column=1, row=1)

       etiquetadni=Label(vp, text= "DNI: ")
       etiquetadni.grid(column=0, row=2)
       entradadni=Entry(vp, width= 20, textvariable= self.dni)
       entradadni.grid(column=1, row=2)

       etiquetadni=Label(vp, text= "Mail: ")
       etiquetadni.grid(column=0, row=3)
       entradadni=Entry(vp, width= 20, textvariable= self.mail)
       entradadni.grid(column=1, row=3)

       etiquetadni=Label(vp, text= "Telefono: ")
       etiquetadni.grid(column=0, row=4)
       entradadni=Entry(vp, width= 20, textvariable= self.telefono)
       entradadni.grid(column=1, row=4)

       etiquetadni=Label(vp, text= "Sexo: ")
       etiquetadni.grid(column=0, row=5)
       entradadni=Entry(vp, width= 20, textvariable= self.sexo)
       entradadni.grid(column=1, row=5)

   def modificar(self):
       tl=Toplevel()
       tl.title("Formulario modifica cliente")

       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

       posicion=self.tree.selection()
       indice=self.tree.item(posicion, "text")

       #busca el cliente y setea los valores en los entry
       soc=self.cn.buscaxDni(indice)

       self.nombre=StringVar()
       self.dni=StringVar()
       self.apellido= StringVar()
       self.telefono=StringVar()
       self.mail=StringVar()
       self.sexo= StringVar()

       self.nombre.set(soc.nombre)
       self.dni.set(soc.dni)
       self.apellido.set(soc.apellido)
       self.mail.set(soc.mail)
       self.telefono.set(soc.telefono)
       self.sexo.set(soc.sexo)

       botonmodifica = Button(tl, text="Modificar",command=lambda: self.confirmaModificar(indice))
       botonmodifica.grid(column=2, row=3)


       etiquetanombre=Label(vp, text= "Dni: ")
       etiquetanombre.grid(column=0, row=0)
       entradanombre=Entry(vp, width= 20, textvariable= self.dni,state='disabled')
       entradanombre.grid(column=1, row=0)

       etiquetaapellido=Label(vp, text= "Nombre: ")
       etiquetaapellido.grid(column=0, row=1)
       entradaapellido=Entry(vp, width= 20, textvariable= self.nombre)
       entradaapellido.grid(column=1, row=1)

       etiquetadni=Label(vp, text= "Apellido: ")
       etiquetadni.grid(column=0, row=2)
       entradadni=Entry(vp, width= 20, textvariable= self.apellido)
       entradadni.grid(column=1, row=2)

       etiquetadni=Label(vp, text= "Mail: ")
       etiquetadni.grid(column=0, row=3)
       entradadni=Entry(vp, width= 20, textvariable= self.mail)
       entradadni.grid(column=1, row=3)

       etiquetadni=Label(vp, text= "Telefono: ")
       etiquetadni.grid(column=0, row=4)
       entradadni=Entry(vp, width= 20, textvariable= self.telefono)
       entradadni.grid(column=1, row=4)

       etiquetadni=Label(vp, text= "Sexo: ")
       etiquetadni.grid(column=0, row=5)
       entradadni=Entry(vp, width= 20, textvariable= self.sexo)
       entradadni.grid(column=1, row=5)


   def baja(self):
       #import pdb; pdb.set_trace()
       posicion=self.tree.selection()
       indice=self.tree.item(posicion, "text")
       soc = self.cn.buscaxDni(indice)
       self.cn.borrar(soc)
       #s.idsocio = soc[0]
       #s.dni = int(soc[1])
       #s.nombre = soc[2]
       #s.apellido = soc[3]
       #print(self.cn.borrar(s))

       tl=Toplevel()
       tl.title("Cliente borrado")
       vp=Frame(tl)
       vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
       etique=Label(vp, text="El cliente ha sido borrado")
       etique.grid(column=1, row=1)
       botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
       botoncerrar.grid(column=1, row=2)
       self.refresh()

   def refresh(self):
       [self.tree.delete(c) for c in self.tree.get_children()]
       lista= self.cn.todos()
       for i in range(len(lista)):
              self.tree.insert("", lista[i].dni,text=lista[i].dni, values=(lista[i].nombre,lista[i].apellido,lista[i].mail,lista[i].telefono,lista[i].sexo))

      # for i in self.cn.todos():
         #  self.tree.insert("",i[0],text=i[0],values=(i[1],i[2],i[3]))





