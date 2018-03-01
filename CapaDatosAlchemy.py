from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base() #--- clase padre para definir las tablas

class Vuelo(Base):
    __tablename__ = 'Vuelo' #--- indispensable.
    nro_vuelo = Column(Integer, primary_key=True) #--- indispensable
    dia_hora_salida = Column(String, primary_key=True)
    dia_hora_llegada = Column(String)
    aerolinea = Column(String)
    destino = Column(String)
    capacidad = Column(Integer)

class Cliente(Base):
    __tablename__ = 'Cliente'
    dni = Column(String, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    mail = Column(String)
    telefono = Column(String)
    sexo = Column(String)

class Reserva(Base):
    __tablename__= 'Reserva'


#engine = create_engine('sqlite:///sqlalchemy_base.db', echo=True)
#Base.metadata.bind = engine

#---- creamos una sesión para admin datos
#DBSession = sessionmaker()
#DBSession.bind = engine
#session = DBSession()

class CapaDatosVuelo():

    def _init_(self):
        engine = create_engine('sqlite:///sqlalchemy_base.db', echo=True)
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def altaVuelo(self, v):
        self.session.add(v)
        self.session.commit()

    def mostrarVuelos(self):
        return self.session.query(Vuelo).all()

    def bajaVuelo(self, nro_vuelo, dia_hora_salida):
        self.session.query(Vuelo).filter(Vuelo.nro_vuelo==nro_vuelo and Vuelo.dia_hora_salida==dia_hora_salida).delete()
        self.session.commit()

    def buscarVuelo (self,nro_vuelo, dia_hora_salida):
        return self.session.query(Vuelo).filter(Vuelo.nro_vuelo==nro_vuelo and Vuelo.dia_hora_salida==dia_hora_salida).first()

    def modificar(self, v):
        vuelo = self.session.query(Vuelo).filter(Vuelo.nro_vuelo==v.nro_vuelo and Vuelo.dia_hora_salida==v.dia_hora_salida).first()
        vuelo.dia_hora_llegada = v.dia_hora_llegada
        vuelo.aerolinea=v.aerolinea
        vuelo.destino=v.destino
        vuelo.capacidad=v.capacidad
        self.session.commit()

    #def volver(self):
        #self.session.rollback()

    #def comitear(self):
       # self.session.commit()


class CapaDatosCliente():

    def init(self):
        engine = create_engine('sqlite:///sqlalchemy_base.db', echo=True)
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def altaCliente(self, c):
        self.session.add(c)
        self.session.commit()

    def mostrarClientes(self):
        return self.session.query(Cliente).all()

    def bajaCliente(self, dni):
        self.session.query(Cliente).filter(Vuelo.dni==dni).delete()
        self.session.commit()

    def modificarCliente(self, c):
        cli = self.session.query(Cliente).filter(Cliente.dni==c.dni).first()
        cli.dni = c.dni
        cli.nombre=c.nombre
        cli.apellido=c.apellido
        cli.telefono=c.telefono
        cli.mail= c.mail
        cli.sexo= c.sexo
        self.session.commit()

    def buscarxDni(self,dni):
        return self.session.query(Cliente).filter(Cliente.dni==dni).first()

    def buscaDni(self,dni):
        return self.session.query(Cliente).count().filter(Cliente.dni == dni) #ver si esta bien

    def validaCantidad(self):
        return self.session.query(Cliente).count()

    #def volver(self):
     #   self.session.rollback()

    #def comitear(self):
     #   self.session.commit()
