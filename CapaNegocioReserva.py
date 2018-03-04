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
        if self.cdr.bajaReserva(r.id_reserva):
            return True
        else:
            return False

    def buscar(self, id):
        r = self.cdr.buscarReserva(id)
        if r == None:
            return None
        else:
            return r

    def modificar(self, r):
        self.cdr.modificarReserva(r)




