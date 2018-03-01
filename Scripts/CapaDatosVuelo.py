import pymysql

class ConectarBd():
 def conectar(self):
     try:
         global cur,conn
         d= dict()
         d['host']='localhost'
         d['port']=3306
         d['user']='root'
         d['passwd']='1234567'
         d['db']='prueba'

         self.conn= pymysql.connect(**d)     #Con self las transformo en propiedades de la clase conectarBD
         self.cur = self.conn.cursor()
         return 0
     except Exception as f:
         return 1    #Si no conecta retorna 1 para que otro metodo sepa que la base de datos no conecto



class CDVuelo ():
       def __init__(self):    #Instancio una conexion
        self.conexion = ConectarBd()
        a = self.conexion.conectar()
        print(a)

       def alta(self,vueloAlta):
        consul1="insert into vuelo (nro_vuelo,dia_hora_salida,dia_hora_llegada,aerolinea,id_destino,capacidad) values({0},{1},{2},{3},{4},{5})".format(repr(vueloAlta.nro_vuelo), repr(vueloAlta.dia_hora_salida),repr(vueloAlta.dia_hora_llegada),repr(vueloAlta.aerolinea),repr(vueloAlta.id_destino),repr(vueloAlta.capacidad))
        self.conexion.cur.execute(consul1)
        self.conexion.conn.commit()
        return self.conexion.cur.lastrowid


