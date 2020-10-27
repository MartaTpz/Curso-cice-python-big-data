fichero = open("cuna.txt")
"""for linea in fichero:
    print (linea)"""
lineas= fichero.readlines()
primeralinea= lineas[0].rstrip()


arco= open("nuevo.txt", 'w')
for i, linea in  enumerate(lineas):
    if i%2==0:
        arco.write(str(i)+''+linea)
arco.close()
arco_mas= open('nuevo.txt', 'a')
arco_mas.write('\n is the final cutdown')
arco_mas.close()

