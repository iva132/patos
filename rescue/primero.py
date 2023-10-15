try:
    from controller import Robot
except:
    print("Las librerias no estan instaladas")

# creamos el un objeto de la clase robot
robot = Robot()

# Definimos la velocidad que se va mover el robot
velocidad = 4

# Definoimos la variable que va contar lo0s pasos
pasos = 0

# Definimos la velocidad de ejecucion
timeStep = 32

# Denimos las ruedas del robot
ruedaIzquierada = robot.getDevice("wheel1 motor")
ruedaDerecha = robot.getDevice("wheel2 motor")

# Definimos la posion inicial del robot
ruedaIzquierada.setPosition(float("inf"))
ruedaDerecha.setPosition(float("inf"))

# Definimos el programa principal
while robot.step(timeStep) != -1:
    if pasos <= 140:
        print(pasos)
        print("-----adelante-----")
        ruedaIzquierada.setVelocity(velocidad)
        ruedaDerecha.setVelocity(velocidad)
    
    elif pasos <= 250:
        print(pasos)
        print("-----derecha-----")
        ruedaIzquierada.setVelocity(velocidad)
        ruedaDerecha.setVelocity(velocidad * -1)
    
    elif pasos <= 480:
        print(pasos)
        print("-----adelante-----")
        ruedaIzquierada.setVelocity(velocidad)
        ruedaDerecha.setVelocity(velocidad )
    
    elif pasos <= 515:
        print(pasos)
        print("-----izquierda-----")
        ruedaIzquierada.setVelocity(velocidad * -1)
        ruedaDerecha.setVelocity(velocidad)
    
    else:
        print("-----paro-----")
        ruedaIzquierada.setVelocity(0)
        ruedaDerecha.setVelocity(0)
        break

    pasos += 1