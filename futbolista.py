from deportista import Deportista
from persona import Persona

class Futbolista(Persona,Deportista):
    listaFutbolistas = []
    def __init__(self,nombre, edad, altura, sexo, años, goles, tarjetas, pierna):
        Persona.__init__(self,nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", años)
        self._golesMarcados = goles
        self._tarjetasRojas = tarjetas
        self._piernaHabil = pierna
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self,goles):
        self._golesMarcados = goles

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self,tarjetas):
        self._tarjetasRojas = tarjetas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self,pierna):
        self._piernaHabil = pierna

    def __str__(self):
        return "Mi nombre es " + str(self.getNombre()) + " soy profesional en el deporte " + str(self.getDeporte()) + ". Tengo " + str(self.getEdad()) + " años de edad y llevo " + str(self.getAñosPracticando()) + " años en el deporte"
