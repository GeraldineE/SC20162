class Puntos(object):
    """ Representación de un punto en el plano, los atributos son x e y
        que representan los valores de las coordenadas cartesianas."""
    def __init__(self, x=0, y=0):
        "Constructor de Punto, x e y deben ser numéricos"
        self.x = x
        self.y = y