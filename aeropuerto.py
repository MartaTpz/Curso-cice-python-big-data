from math import cos,radians,sin,pow,asin,sqrt


def distance(lat1, long1, lat2, long2):
    radius = 6371
    lat1 = radians(lat1)
    long1 = radians(long1)
    lat2 = radians(lat2)
    long2 = radians(long2)
    dlat = lat2 - lat1
    dlong = long1 - long2
    a = pow(sin(dlat / 2), 2) + cos(lat1) * cos(lat2) * pow(sin(dlong / 2), 2)
    distance = 2 * radius * asin(sqrt(a))
    return distance
class aeropuerto():
    def __init__(self, aident, anombre, apais, alatitud=0, alongitud=0):
        self.__ident= aident
        self.__nombre= anombre
        self.__pais= apais
        self.__latitud= alatitud
        self.__longitud= alongitud
    def cambiarcoordenadas(self, latitud, longitud):
        self.__latitud= latitud
        self.__longitud= longitud
    def getNombre(self):
        return self.__nombre
    def getId(self):
        return self.__ident
    def __repr__(self):
        return "%d - %s - %s" % (self.__ident, self.__nombre, self.__pais)

    def distancia(self, aero2):
        return distance(self.__latitud, self.__longitud, aero2.__latitud, aero2.__longitud)
ae1= aeropuerto(507, 'Heatrow', 'United Kingdom')
ae2= aeropuerto(30, 'Campbell River', 'Canadá')
ae1.cambiarcoordenadas(10, -25.3)
ae2.cambiarcoordenadas(100, 100)
print('La distancia del aeropuerto %s a %s es %.3f' % (ae1.getNombre(), ae2.getNombre(), ae1.distancia(ae2)))