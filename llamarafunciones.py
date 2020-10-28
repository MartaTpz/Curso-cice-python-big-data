ciudades= ['  madrid', 'BaRceloNa', 'SEVilla']

def formatear(lista):
    resultado= []
    for ciudad in lista:
        nueva_ciudad= ciudad.strip()
        nueva_ciudad= nueva_ciudad.title()
        resultado.append(nueva_ciudad)
    return resultado
print(formatear(ciudades))

ff= map(str.upper, ciudades)
print(ciudades(ff))


ala= lambda x, lista: x*lista
print (ala(3, ciudades))