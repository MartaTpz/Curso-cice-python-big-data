def repite():

    
    lista= [1,2,2,3,3,4,5,6,7,8,2,9]
  
  
    veces= lista.count(2)
   
    return veces
    
    
    
 
    
print(repite())

def porcentaje():
    lista= [1,2,2,3,3,4,5,6,7,8,2,9]
  
    total= len(lista)
    veces= lista.count(2)
    porcentaje= veces*100/total
    return porcentaje

print(porcentaje())