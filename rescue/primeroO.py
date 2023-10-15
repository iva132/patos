try:
    from controller import Robot
except:
    print("Las librerias no estan instaladas")

# creamos el un objeto de la clase robot
robot = Robot()

# Denimos las ruedas del robot
ruedaIzquierada = robot.getDevice("wheel1 motor")
ruedaDerecha = robot.getDevice("wheel2 motor")

# Definimos la posion inicial del robot
ruedaIzquierada.setPosition(float("inf"))
ruedaDerecha.setPosition(float("inf"))

# Definimos la velocidad que se va mover el robot
velocidad = 4

# Definoimos la variable que va contar los pasos
cont = 0

# Definimos la velocidad de ejecucion
timeStep =32

# Girar 180° arena
giroA = 110
# Girar 180
giro = 35
# Girar medio 90°
giroM = 17
# Adelante largo con arena
adelanteA = 140
# Adelante medio
adelanteM = 90
# Adelante corto
adelanteC = 50

def adelante(cont, limite):
    longitud=len("adelante")
    print(cont, " " * longitud, limite)
    print("-----adelante-----")
    ruedaIzquierada.setVelocity(velocidad)
    ruedaDerecha.setVelocity(velocidad)

def derecha(cont, limite):
    longitud=len("derecha")
    print(cont, " " * longitud, limite)
    print("-----derecha-----")
    ruedaIzquierada.setVelocity(velocidad)
    ruedaDerecha.setVelocity(velocidad * -1)

def izquierda(cont, limite):
    longitud=len("izquierda")
    print(cont, " " * longitud, limite)
    print("-----izquierda-----")
    ruedaIzquierada.setVelocity(velocidad * -1)
    ruedaDerecha.setVelocity(velocidad)

def alto(limite):
    print(" " *5  ,limite )
    print("-----paro-----")
    ruedaIzquierada.setVelocity(0)
    ruedaDerecha.setVelocity(0)
    print("El progrma finaliso")


movimientos = [adelanteA]

def suma(ind, adicional):
    global movimientos
    num=movimientos[ind]
    numero=num+adicional
    movimientos.append(numero)

# Definimos el programa principal
while robot.step(timeStep) != -1:

    if cont <= movimientos[0]:
        adelante(cont, movimientos[0])
        if cont == movimientos[0]:
            suma(0, giroA)
    
    elif cont <= movimientos[1]:
        derecha(cont, movimientos[1])
        if cont == movimientos[1]:
            suma(1, adelanteA + adelanteM)
    
    elif cont <= movimientos[2]:
        adelante(cont, movimientos[2])
        if cont == movimientos[2]:
            suma(2, giro)
    
    elif cont <= movimientos[3]:
        izquierda(cont, movimientos[3]) 

    else:
        alto(cont)
        print("Estos fueron los movimientos", movimientos)
        break

    cont += 1