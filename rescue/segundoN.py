try:
    from controller import Robot
except:
    print("Las librerias no estan instaladas")

# creamos el un objeto de la clase robot
robot = Robot()

# Definimos la velocidad que se va mover el robot
velocidad = 4

# Definoimos la variable que va contar los cont
cont = 0

# En esta variable vamos a hacer las sumas de los cont 
cont = 0

# Definimos la velocidad de ejecucion
timeStep = 32

# Denimos las ruedas del robot
ruedaIzquierada = robot.getDevice("wheel1 motor")
ruedaDerecha = robot.getDevice("wheel2 motor")

# Definimos la posion inicial del robot
ruedaIzquierada.setPosition(float("inf"))
ruedaDerecha.setPosition(float("inf"))

# Girar 180° = 55
# Girar medio 90° = 17
# Adelante medio = 70
# Adelante corto = 50

def adelante(cont):
    print(cont)
    print("-----adelante-----")
    ruedaIzquierada.setVelocity(velocidad)
    ruedaDerecha.setVelocity(velocidad)

def derecha(cont):
    print(cont)
    print("-----derecha-----")
    ruedaIzquierada.setVelocity(velocidad)
    ruedaDerecha.setVelocity(velocidad * -1)

def izquierda(cont):
    print(cont)
    print("-----izquierda-----")
    ruedaIzquierada.setVelocity(velocidad * -1)
    ruedaDerecha.setVelocity(velocidad)

def alto():
    print("-----paro-----")
    ruedaIzquierada.setVelocity(0)
    ruedaDerecha.setVelocity(0)
    print("El progrma finaliso")

# Definimos el programa principal
while robot.step(timeStep) != -1:

    if cont <= 140:
        adelante(cont)
    
    elif cont <= 250:
        derecha(cont)
    
    elif cont <= 480:
        adelante(cont)
    
    elif cont <= 515:
        izquierda(cont)

####### parte 2 #######
            
    elif cont <= 595:
        adelante(cont)

    elif cont <= 610:
        derecha(cont)

    elif cont <= 645:
        adelante(cont)
          
    elif cont <= 663:
        izquierda(cont)
     
    elif cont <= 714:
        adelante(cont)

    elif cont <= 731:
        derecha(cont)

    elif cont <= 781:
        adelante(cont)

    elif cont <= 798:
        izquierda(cont)

    elif cont <= 848:
        adelante(cont)
    
    elif cont <= 865:
        derecha(cont)

    elif cont <= 1002:
        adelante(cont)
    
    elif cont <= 1019:
        derecha(cont)

    elif cont <= 1080:
        adelante(cont)

    else:
        alto()
        break
    
    cont += 1