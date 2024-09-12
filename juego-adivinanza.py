

import random


numero_secreto= random.randint(1,100)
cant_intentos= 0
cant_max_intentos= 5
adivinado = False

print("Bienvenidos al juego de adivinar el numero secreto")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("Gracias por participar")
        break
    
    entrada= input("Introduce un numero del 1 al 99: ")
    numero = int(entrada)
    
    if numero== numero_secreto:
        print("Felicitaciones ganaste el juego")
        adivinado = True
    elif numero< numero_secreto:
        print("El numero es mayor ")
    else:
        print("El numero es menor ") 
    
    cant_intentos+= 1



