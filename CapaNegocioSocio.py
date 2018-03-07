
from CapaDatosAlchemy import CapaDatosCliente


class CNCliente():
   global cd
   cd = CapaDatosCliente()

   def alta(self,s):
    if (self.buscaxDni(s.dni)):
        return False
    else:
        if s.nombre!='' and s.apellido!='' and s.mail!='' and s.telefono!='' and s.sexo!='':
            cd.altaCliente(s)
            return True



   def borrar(self,s):
       #if self.validaDni(s) and cd.buscaDni(s.dni):
           cd.bajaCliente(s.dni)
           # return True
           #else:
            #   return False #No pudo borrar
       #else:
        #return False #No cumple con las condiciones


   def modificar(self,s):
       if s.dni!='' and s.nombre!='' and s.apellido!='' and s.mail!='' and s.telefono!='' and s.sexo!='':
           cd.modificarCliente(s)
           return True
       else:
           return False

   """def modificar2(self,s):

       if(self.validaNombre(s)==True):
        socioModif = cd.modificar2(s)
        return socioModif
       else:
        return False"""

   def buscaxDni(self,dni):
       if (dni != ''):
           socEnco = cd.buscarxDni(dni)
           if socEnco == None:
               return False #No existe es Id.
           else: return socEnco


   def todos(self):
       return cd.mostrarClientes()  #La ui debe mostrarlos


   def validaDni(self, s):
       if(s.dni != '' and isinstance(s.dni,int)):
           return True #Esto es bueno
       else: return False


   def validaNombre(self,s):
       if(isinstance(s.nombre,str) and isinstance(s.apellido,str) and len(s.nombre)<25 and len(s.apellido)<25 and len(s.nombre)>3 and len(s.apellido)>3):
           return True #Esto es bueno
       else:
           return False
"""
   def anterior(self,id):
       socEnco = cd.anterior(id)
       if (socEnco==False):
           return cd.primero()
       else:
           return socEnco #En la ui se muestra asi: print("El socio anterior es: \n""ID:", socEnco[0], "\nDNI:", socEnco[1], "\nNOMBRE:", socEnco[2], "\nAPELLIDO:", socEnco[3])


   def siguiente(self,id):
       socEnco = cd.proximo(id)
       if (socEnco == False):
           return cd.ultimo()
       else:
           return socEnco  #print("El socio siguiente es: \n""ID:", socEnco[0], "\nDNI:", socEnco[1], "\nNOMBRE:", socEnco[2], "\nAPELLIDO:", socEnco[3]). Esto va en ui


   def primero(self):
       socEnco = cd.primero()
       if (socEnco == False):
           return False #No existen socios entonces no puede devolver el primero
       else:
           return socEnco #print("El primer socio es: \n""ID:", socEnco[0], "\nDNI:", socEnco[1], "\nNOMBRE:", socEnco[2], "\nAPELLIDO:", socEnco[3]). Esto va en ui


   def ultimo(self):
       socEnco = cd.ultimo()
       if (socEnco == False):
           return False #"No existe" el ultimo socio, no habría ninguno
       else:
           return socEnco  #print("El ultimo socio es: \n""ID:", socEnco[0], "\nDNI:", socEnco[1], "\nNOMBRE:", socEnco[2], "\nAPELLIDO:", socEnco[3]). En ui
"""


