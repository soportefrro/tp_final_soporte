from CapaDatosAlchemy import CapaDatosVuelo

class CNVuelo():
    def __init__(self):
        self.cdv=CapaDatosVuelo()

    def altavuelo(self, v):
        self.cdv.altaVuelo(v)
        return True

    def todosvuelo(self):
        return self.cdv.mostrarVuelos()

    def borrar(self, v):
        if self.cdv.bajaVuelo(v.nro_vuelo,v.dia_hora_salida):
            return True
        else:
            return False

    def buscar(self, nro_vuelo,dia_hora_salida):
        v = self.cdv.buscarVuelo(nro_vuelo,dia_hora_salida)
        if v == None:
            return None
        else:
            return v

    def modificar(self, v):
        self.cdv.modificar(v)




