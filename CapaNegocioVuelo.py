from CapaDatosAlchemy import CapaDatosVuelo

class CNVuelo():
    def __init__(self):
        self.cdv=CapaDatosVuelo()

    def actualizaCap(self,a,b):
        v=self.cdv.buscarVuelo(a,b)
        self.cdv.actualizarCap(v)

    def altavuelo(self, v):
        if v.nro_vuelo!='' and v.dia_hora_salida!='' and v.dia_hora_llegada!='' and v.aerolinea!='' and v.destino!='' and v.capacidad!='' and v.precio!='':
            if int(v.capacidad)>0 and int(v.nro_vuelo) and (v.precio)>0:
                self.cdv.altaVuelo(v)
                return True
            else: return False

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
        if v.dia_hora_llegada!='' and v.aerolinea!='' and v.destino!='' and v.capacidad!='' and v.precio!='':
            if int(v.capacidad)>0 and int(v.precio)>0:
                self.cdv.modificar(v)
                return True
            else: return False
