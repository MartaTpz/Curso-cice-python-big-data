
a=5 
if a>4:
    a+=1
    print('La variabke a vale', a)
# asignacion doble de variable e identación coherente
    
x, y= 0,0
if x>y:
         print(x, 'Es mayor que ', y)
elif x<y:
    print(y, 'Es mayor que', x)
else:
  print(x, 'Es igual que', y)
  
#función si no se puede hacer siempre devolver algo return none o lo que sea
import math  
def foo(x):
    if x>=0:
        return print(math.sqrt(x))
    else: 
        return print('No se puede hacer la raiz cuadrada de un numero negativo')

foo(997)
#Expresiones ternarias una variable que se asigna mediante una condición

x='fire' if 4>3 else 3
print(x)

#bucles for
lista=[1,2,3,4,5,6]

for elefante in lista:
    print(elefante)
    
for taco in range(10):
    print('taco')

suma=0
for taco in range(10):
    suma= suma+taco
    print('la suma de los elementos más la variable es',
         suma)
    
puntos=((1,2),(3,4),(5,6))
for x,y in puntos:
   
    print('la suma es',x+y)
    
for holi in range(10):
    if holi % 2 ==0:
        continue
    print(holi)
    
#diccionario
diccionario1={1:'uno', 2:'dos', 3:'tres', 4:'cuatro'}
for i in diccionario1.keys():
    print("clave",i)
for churro in diccionario1.values():
    print("valor",churro)
    