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
        if r.id_reserva!='' and r.destino!='' and r.fecha!='' and r.precio!='':
            if int(r.precio)>0:
                self.cdr.modificarReserva(r)
                return True
        else:
            return False
