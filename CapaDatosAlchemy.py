from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base() #--- clase padre para definir las tablas

class Vuelo(Base):
    __tablename__ = 'Vuelo'
    nro_vuelo = Column(Integer, primary_key=True)
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
    __tablename__ = 'Reserva'
    vuelo_nro_vuelo = Column(Integer, ForeignKey('Vuelo.nro_vuelo'), primary_key=True )
    vuelo_dia_hora_salida = Column(String,ForeignKey('Vuelo.dia_hora_salida'), primary_key=True)
    cliente_dni = Column(String, ForeignKey("Cliente.dni"), primary_key=True)
    fecha = Column(String)
    cliente = relationship(Cliente)
    vuelo = relationship(Vuelo, foreign_keys=[vuelo_nro_vuelo])


#engine = create_engine('sqlite:///sqlalchemy_base.db', echo=True)
#Base.metadata.bind = engine

#---- creamos una sesión para admin datos
#DBSession = sessionmaker()
#DBSession.bind = engine
#session = DBSession()

class CapaDatosReserva():
    def __init__(self):
        engine = create_engine('sqlite:///sqlalchemy_base.db', echo=True)
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def altaReserva(self, r):
        self.session.add(r)
        self.session.commit()

    def mostrarReservas(self):
        return self.session.query(Reserva).all()

    def bajaReserva(self, nro_vuelo, dia_hora_salida, dni):
        self.session.query(Reserva).filter(Reserva.cliente_dni==dni and Reserva.vuelo_dia_hora_salida==dia_hora_salida and Reserva.vuelo_nro_vuelo== nro_vuelo).delete()
        self.session.commit()

    def buscarReserva(self, nro_vuelo, dia_hora_salida, dni):
        return self.session.query(Reserva).filter(Reserva.cliente_dni==dni and Reserva.vuelo_dia_hora_salida==dia_hora_salida and Reserva.vuelo_nro_vuelo== nro_vuelo).first()

    def modificarReserva(self,r):
        return self.session.query(Reserva).filter(Reserva.cliente_dni==r.cliente_dni and Reserva.vuelo_dia_hora_salida== r.dia_hora_salida and Reserva.vuelo_nro_vuelo== r.vuelo_nro_vuelo).first()
        reserva.vuelo_dia_hora_salida = r.dia_hora_salida
        reserva.vuelo_nro_vuelo = r.vuelo_nro_vuelo
        reserva.cliente_dni = r.cliente_dni
        reserva.fecha = r.fecha
        self.session.commit()

class CapaDatosVuelo():

    def __init__(self):
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
        vuelo.nro_vuelo = v.nro_vuelo
        vuelo.dia_hora_salida=v.dia_hora_salida
        vuelo.dia_hora_llegada = v.dia_hora_llegada
        vuelo.aerolinea=v.aerolinea
        vuelo.destino=v.destino
        vuelo.capacidad=v.capacidad
        self.session.commit()


class CapaDatosCliente():

    def __init__(self):
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
        self.session.query(Cliente).filter(Cliente.dni==dni).delete()
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
        return self.session.query(Cliente).count().filter(Cliente.dni == dni)


