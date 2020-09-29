# calcular si un año es bisiesto, tiene que ser divisible entre 4 y soloo 1ntre 100 si también lo es entre 400

def bisiesto(x):
    if x%4==0:
        x= "Es bisiesto"
    elif x%100==0 and x&400==0:
        x= "ES bisiesto"
    else:
        x= "No es bisiesto"
    return x

año= bisiesto(2020)

print(año)

def menormayor(x, y):
    if x>y:
        mayor= x
    elif x==y:
        mayor= "Son iguales"
    else:
        mayor= y

    return mayor

numero= menormayor(5,7)
print("El número mayor es:", numero)

def absoluto(x):
    if x<0:
        absoluto= x* -1
    else:
        absoluto= x
    return absoluto

absoluto= absoluto(-34)
print("El número absoluto es: ", absoluto)