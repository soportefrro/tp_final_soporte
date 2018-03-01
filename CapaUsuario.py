from CapaNegocioSocio import CNSocio
from tkinter import *
from tkinter import ttk
from Entidades import Socio

class CUSocio():

    def __init__(self):
        self.cn = CNSocio()
        self.ventana = Tk()
        self.tree = ttk.Treeview(self.ventana)

    def interfaz(self):

        vp=Frame(self.ventana)
        vp.grid(column=0, row=0,  sticky=(N, S, E, W))

        self.tree["columns"]=("dni","nombre","apellido")
        self.tree.column("#0", width=25)
        self.tree.column("nombre", width=100)
        self.tree.column("apellido", width=100)
        self.tree.column("dni", width=100)

        self.tree.heading("#0", text="Id")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("apellido", text="Apellido")
        self.tree.heading("dni", text="DNI")

        for i in self.cn.todos():
            self.tree.insert("",i[0],text=i[0],values=(i[1],i[2],i[3]))

        #Configuracion de la ventana:
        self.ventana.title("ABM Socios")
        self.ventana.resizable
        self.ventana.geometry('500x400')
        self.ventana.columnconfigure(0,weight=0)
        self.ventana.columnconfigure(1,weight=1)
        self.ventana.columnconfigure(2,weight=1)
        self.ventana.rowconfigure(1,weight=1)

        self.tree.grid(row=1,column=1,columnspan=5,rowspan = 1,sticky=(N, S, E, W))

        botonA = Button(self.ventana, text=" Alta  ", command=lambda: self.alta(),background="#ADF5A9")
        botonA.grid(row=5,column=1,sticky=(N, S, E, W))

        botonB = Button(self.ventana,text="  Baja  ", command= lambda: self.baja(),background="#F5A9A9" )
        botonB.grid(row=5,column=2,columnspan=1,sticky=(N, S, E, W))

        botonM = Button(self.ventana,text="  Modificacion  ", command=lambda: self.modificar(),background="#7EB0EA")
        botonM.grid(row=5,column=3,sticky=(N, S, E, W))

        botonAct = Button(self.ventana,text="  Refrescar  ", command=lambda: self.refresh())
        botonAct.grid(row=5,column=4,sticky=(N, S, E, W))

        self.ventana.mainloop()

    def confirmaModificar(self, id):
        a=self.nombre.get()
        b=self.apellido.get()
        c=self.dni.get()

        socio= Socio(id, c, a, b)
        print(socio)
        retorno= self.cn.modificar2(socio)

        if retorno == False:
            # ventana de error
            tl=Toplevel()
            tl.title("ERROR")
            vp=Frame(tl)
            vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
            etique=Label(vp, text="Error en la modificación del socio")
            etique.grid(column=1, row=1)
            botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
            botoncerrar.grid(column=1, row=2)

        else:
            # ventana de confirmación
            tl=Toplevel()
            tl.title("Socio modificado")
            vp=Frame(tl)
            vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
            etique=Label(vp, text="El socio ha sido modificado")
            etique.grid(column=1, row=1)
            botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
            botoncerrar.grid(column=1, row=2)
            self.refresh()


    def confirmaAlta(self):
        a=self.nombre.get()
        b=self.apellido.get()
        c=int(self.dni.get())

        s= Socio(0, c, a, b)
        print(s)
        print(self.cn.alta(s))

        tl=Toplevel()
        tl.title("Socio agregado")
        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
        etique=Label(vp, text="El socio ha sido agregado")
        etique.grid(column=1, row=1)
        botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
        botoncerrar.grid(column=1, row=2)
        self.refresh()

    def alta(self):
        tl=Toplevel()
        self.ventana.title("Formulario nuevo socio")

        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

        self.nombre=StringVar()
        self.dni=StringVar()
        self.apellido= StringVar()
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


    def modificar(self):
        tl=Toplevel()
        self.ventana.title("Formulario modifica socio")

        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

        posicion=self.tree.selection()
        indice=self.tree.item(posicion, "text")

        #busca el socio y setea los valores en los entry
        soc=self.cn.buscaxId(indice)

        self.nombre=StringVar()
        self.dni=StringVar()
        self.apellido= StringVar()
        self.nombre.set(soc[2])
        self.dni.set(int(soc[1]))
        self.apellido.set(soc[3])

        botonmodifica = Button(tl, text="Modificar",command=lambda: self.confirmaModificar(indice))
        botonmodifica.grid(column=2, row=3)


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

    def baja(self):
        #import pdb; pdb.set_trace()
        posicion=self.tree.selection()
        indice=self.tree.item(posicion, "text")
        soc = self.cn.buscaxId(indice)
        s = Socio(int(soc[0]),int(soc[1]),soc[2],soc[3])
        #s.idsocio = soc[0]
        #s.dni = int(soc[1])
        #s.nombre = soc[2]
        #s.apellido = soc[3]
        print(self.cn.borrar(s))

        tl=Toplevel()
        tl.title("Socio borrado")
        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
        etique=Label(vp, text="El socio ha sido borrado")
        etique.grid(column=1, row=1)
        botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
        botoncerrar.grid(column=1, row=2)
        self.refresh()

    def refresh(self):
        [self.tree.delete(c) for c in self.tree.get_children()]

        for i in self.cn.todos():
            self.tree.insert("",i[0],text=i[0],values=(i[1],i[2],i[3]))




cu = CUSocio()
cu.interfaz()

