import random
#Practica 1
#Ejercicio1
def max(a,b,c):
        if ((a>b)and(a>c)):
            return a
        elif((b>a)and(b>c)):
            return b
        else:
            return c
#print(max(1,16,7))

#Ejercicio3
def longuitud(cade):
    a= len(cade)
    return a

#print(longuitud('perro'))

#Ejercicio5
def multi(list):
    a=1
    for i in list:
        a = a* i
    return a

lista=[1,2,3,4,5]
#print(multi(lista))

#Ejercicio6
def inversa(cade):
    if len(cade) == 1:
        return cade
    else:
        return (cade[-1] + inversa(cade[:-1]))

cadena='Pepino'
#print(inversa(cadena))

#Ejercicio8
def compara(lista1,lista2):
    for i in lista1:
        for j in lista2:
            if (i == j):
                return True
    else:
        return False

lista1=[0,1,3,5,7,9]
lista2=[2,4,6,8,10,7]
#print(compara(lista1,lista2))

#Ejercicio9
def generar_n_caracteres(cade,cant) :
    return cade*cant

caract='t'
n=3
#print(generar_n_caracteres(caract,n))

#Ejercicio10

def maslarga(list):
    a = 1
    for i in list:
        if (len(i) > a):
            larga = i
    return larga

lista=['a','be','cer','mipija']
#print(maslarga(lista))

#Ejercicio11
#print("Ejercicio 11: Determinar la cantidad de digitos de un numero ingresado")
#num = input("Escriba un numero: ")
cont=0

"""for i in num:
   if (i>="0" and i<="9") :
       cont = cont + 1
"""

#print ("La cantidad de digitos es: ",cont)

#Ejercicio12

numero=4
a=0
for i in range(numero+1):
    a = a + i

#print(a)

#Practica2
#Ejercicio1
"""
class Rectangulo():
    def __init__(self, x, y):
        self.base = x
        self.altu = y

    def area(self, x, y):
        print("El area es: ",x * y)


r = Rectangulo(2,4)
#r.area(2,4)

import math

class Circulo():
    def __init__(self):
        self.radio = 4

    def area(self):

        self.radio = 6

        print((self.radio**2) * math.pi)

    def perimetro(self):
        print((self.radio * math.pi))

cir = Circulo()
cir.area()
cir.perimetro()

class Circulo():
    def __init__(self,rad):
        self.radio = rad

    def area(self,rad):
        self.area = rad * rad * pi
        print("El area del circulo con radio",rad,"es:",self.area)

    def perimetro(self,rad):
        self.perime = rad * 2 * 3.141592
        print("El perimeto del circulo con radio",rad,"es:",self.perime)

rad = int(input("Ingrese el radio del circulo:"))

circu = Circulo(rad)
circu.area (rad)
circu.perimetro(rad)
"""

class Persona():
    def __init__(self, nom, edad, sexo, peso, altura):
        self.nombre= nom
        self.edad= edad
        self.sexo=sexo
        self.peso= peso
        self.altura= altura
        self.dni= self.generar_dni()

    def es_mayor_edad(self):
        if(self.edad>=18):
            return True
        else: return False

    def print_data(self):
        print("nombre:{0}, edad: {1}, sexo: {2}, peso{3}, altura: {4}, dni:{5}".format(self.nombre, self.edad, self.sexo, self.peso, self.altura, self.dni))

    def generar_dni(self):
        return random.randint(0,99999999)



class Estudiante(Persona):
    def __init__(self,nomb,edad,sexo,peso,altura,carrera,año,cantidad,cantaprob):
        Persona.nombre=nomb
        Persona.edad= edad
        Persona.sexo= sexo
        Persona.peso= peso
        Persona.altura= altura
        self.carrera=carrera
        self.año=año
        self.cantidad=cantidad
        self.cantaprob=cantaprob

    def avance(self):
        return (self.cantaprob * 100)/self.cantidad
    def edad_ingreso(self):
      import datetime
      return self.edad - (datetime.datetime.now().year - self.añoIngreso)

pedro = Estudiante("Pedro",21,"H",89,178,"ISI",2012,34,22)
julia = Estudiante("Julia",23,"M",67,156,"IM",2013,34,15)
julia2 = Estudiante("Julia",23,"M",67,156,"IM",2013,34,15)
julia3 = Estudiante("Julia",23,"M",67,156,"IM",2013,34,15)


def ej5(list):
    d = {'ISI':0,'IM':0}
    for i in list:
        if i.carrera in d.keys():
            d[i.carrera] +=1
        else:
            d[i.carrera ]=1

    return d

lista=[pedro,julia,julia2,julia3]
print(ej5(lista))














