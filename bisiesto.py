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