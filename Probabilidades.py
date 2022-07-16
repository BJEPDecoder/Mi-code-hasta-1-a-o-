import random # importamos random 
pro = (random.randrange(1, 3)) # damos la variable pro acortando probabilidad
print(pro) # borrar era para reviso 
print("Jugamos a las probabilidades, vale")  # explicacion 
print("Si yo le doy del 1, al 3 pierdes pero si fallo ganas") # explicacion
print("escoje un numero del 1  al 3") # intrucciones
 
res = input("") # incertar

if int(pro) == int(res): # calculo si le da
  print("Perdiste")
  
  
else:                       # calculo si falla
    if int(pro) > int(res): 
        print("Ganaste")
    else:
        print("Ganaste")
