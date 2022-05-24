
class Deportista:
    def __init__(self,deporte, años):
        self._deporte = deporte
        self._añosPracticados = años

    def getDeporte(self):
        return self._deporte

    def setDeporte(self, deporte):
        self._deporte = deporte

    def getAñosPracticados(self):
        return self._añosPracticados

    def setAñosPracticados(self, años):
        self._añosPracticados = años