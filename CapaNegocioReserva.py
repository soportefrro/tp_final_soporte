from CapaDatosAlchemy import CapaDatosReserva

class CNReserva():
    def __init__(self):
        self.cdr=CapaDatosReserva()

    def altareserva(self, r):
        self.cdr.altaReserva(r)
        return True

    def todosreserva(self):
        return self.cdr.mostrarReservas()

    def borrar_reserva(self, r):
        if self.cdr.bajaReserva(r.vuelo_nro_vuelo, r.vuelo_dia_hora_salida, r.cliente_dni):
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
        self.cdr.modificar(r)




