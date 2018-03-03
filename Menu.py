from tkinter import *
from tkinter import ttk
from CapaUsuarioVuelo import CUVuelo
from CapaUsuario import CUCliente



class Menu():
   def __init__(self):
       self.ventana = Tk()
       self.tree = ttk.Treeview(self.ventana)

   def interfaz(self):
       vp=Frame(self.ventana)
       vp.grid(column=0, row=0,  sticky=(N, S, E, W))

       self.ventana.title("Menu")
       self.ventana.resizable
       self.ventana.geometry('200x225')

       self.tree.grid(row=1,column=1,columnspan=3,rowspan = 7,sticky=(N, S, E, W))

       botonA = Button(self.ventana, text="  Vuelos  ", command=lambda: self.vuelos(),background="#DAE4E3")
       botonA.grid(row=2,column=2,sticky=(N, S, E, W))

       botonB = Button(self.ventana,text="  Clientes  ", command= lambda: self.clientes(),background="#DAE4E3" )
       botonB.grid(row=4,column=2,columnspan=1,sticky=(N, S, E, W))

       botonM = Button(self.ventana,text="  Reservas  ", command=lambda: self.reservas(),background="#DAE4E3")
       botonM.grid(row=6,column=2,sticky=(N, S, E, W))

       self.ventana.mainloop()

   def vuelos (self):
       cuv = CUVuelo()
       cuv.interfaz()

   def clientes (self):
       cuc = CUCliente()
       cuc.interfaz()

cu = Menu()
cu.interfaz()