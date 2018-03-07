from CapaDatosAlchemy import CapaDatosReserva

class CNReserva():
    def __init__(self):
        self.cdr=CapaDatosReserva()

    def altareserva(self, r):
        self.cdr.altaReserva(r)
        return True

    def todosreserva(self):
        return self.cdr.mostrarReservas()

    def borrar_reserva(self, nro_vuelo,dia_hora_salida,dni):
        if self.cdr.bajaReserva(nro_vuelo,dia_hora_salida,dni):
            return True
        else:
            return False

    def buscar(self, nro_vuelo,dia_hora_salida,dni):
        r = self.cdr.buscarReserva(nro_vuelo,dia_hora_salida,dni)
        if r == None:
            return None
        else:
            return r

    def modificar(self, r):
        if r.vuelo_nro_vuelo!='' and r.vuelo_dia_hora_salida!='' and r.cliente_dni!='' and r.fecha_reserva!='':
            self.cdr.modificarReserva(r)
        else :
            return False

