from tkinter import *
def agreganumero(numero):
   valor.set(valor.get()+numero)
   #Todo lo siguiente es para volver a habilitar los operadores
   botonsuma.config(state=NORMAL)
   botonresta.config(state=NORMAL)
   botonmulti.config(state=NORMAL)
   botondivi.config(state=NORMAL)
   botonigual.config(state=NORMAL)

def agregaoperador(operador):
   valor.set(valor.get()+operador)
   #todo lo siguiente es para deshabilitarlos cuando el ultimo boton presionado fue un operador
   botonsuma.config(state=DISABLED)
   botonresta.config(state=DISABLED)
   botonmulti.config(state=DISABLED)
   botondivi.config(state=DISABLED)
   botonigual.config(state=DISABLED)

def calcula():
   try:
       valor.set(eval(valor.get()))
   except:
       valor.set("Error")

def borra():
   valor.set("")

ventana = Tk()
valor = StringVar()

#Creo el cuadro de texto y botones aca porque necesito que TODOS los metodos puedan acceder a ellos
txtbox = Entry(ventana,textvariable=valor,bd=5,justify=RIGHT)
txtbox.grid(row=1,column=1,columnspan=4,sticky=(N, S, E, W))
ventana.title("Calculadora")
ventana.resizable
ventana.geometry('300x350')
ventana.columnconfigure(0,weight=0)
ventana.columnconfigure(1,weight=1)
ventana.columnconfigure(2,weight=1)
ventana.columnconfigure(3,weight=1)
ventana.columnconfigure(4,weight=1)
ventana.columnconfigure(5,weight=0)
ventana.rowconfigure(0,weight=0)
ventana.rowconfigure(1,weight=1)
ventana.rowconfigure(2,weight=1)
ventana.rowconfigure(3,weight=1)
ventana.rowconfigure(4,weight=1)
ventana.rowconfigure(5,weight=1)


boton1 = Button(ventana,text="  1  ", command=lambda: agreganumero("1"))
boton1.grid(row=2,column=1,sticky=(N, S, E, W))
boton2 = Button(ventana,text="  2  ", command=lambda: agreganumero("2"))
boton2.grid(row=2,column=2,sticky=(N, S, E, W))
boton3 = Button(ventana,text="  3  ", command=lambda: agreganumero("3"))
boton3.grid(row=2,column=3,sticky=(N, S, E, W))

boton4 = Button(ventana,text="  4  ", command=lambda: agreganumero("4"))
boton4.grid(row=3,column=1,sticky=(N, S, E, W))
boton5 = Button(ventana,text="  5  ", command=lambda: agreganumero("5"))
boton5.grid(row=3,column=2,sticky=(N, S, E, W))
boton6 = Button(ventana,text="  6  ", command=lambda: agreganumero("6"))
boton6.grid(row=3,column=3,sticky=(N, S, E, W))

boton7 = Button(ventana,text="  7  ", command=lambda: agreganumero("7"))
boton7.grid(row=4,column=1,sticky=(N, S, E, W))
boton8 = Button(ventana,text="  8  ", command=lambda: agreganumero("8"))
boton8.grid(row=4,column=2,sticky=(N, S, E, W))
boton9 = Button(ventana,text="  9  ", command=lambda: agreganumero("9"))
boton9.grid(row=4,column=3,sticky=(N, S, E, W))

boton0 = Button(ventana,text="  0  ", command=lambda: agreganumero("0") )
boton0.grid(row=5,column=2,columnspan=1,sticky=(N, S, E, W))


botonsuma = Button(ventana,text="  +  ", command=lambda: agregaoperador("+"),background="#A9A9F5",relief=RIDGE)
botonsuma.grid(row=2,column=4,sticky=(N, S, E, W))
botonresta = Button(ventana,text="  -  ", command=lambda: agregaoperador("-"),background="#A9A9F5",relief=RIDGE)
botonresta.grid(row=3,column=4,sticky=(N, S, E, W))
botonmulti = Button(ventana,text="  *  ", command=lambda: agregaoperador("*"),background="#A9A9F5",relief=RIDGE)
botonmulti.grid(row=4,column=4,sticky=(N, S, E, W))
botondivi = Button(ventana,text="  /  ", command=lambda: agregaoperador("/"),background="#A9A9F5",relief=RIDGE)
botondivi.grid(row=5,column=4,sticky=(N, S, E, W))
botonigual = Button(ventana,text="  =  ", command=lambda: calcula(),background="#BCF5A9",relief=RIDGE)
botonigual.grid(row=5,column=3,sticky=(N, S, E, W))
botonC = Button(ventana, text=" C  ", command=lambda: borra(),background="#F5A9A9",relief=RIDGE)
botonC.grid(row=5,column=1,sticky=(N, S, E, W))

ventana.mainloop()

