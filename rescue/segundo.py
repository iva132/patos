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

    # Definimos la distancia maxima
    if cont <= movimientos[0]: # 140
        # Llamamos a la funcion correspondiente para movernos y le envimos el contador y el numero de pasos limite para que los imprima
        adelante(cont, movimientos[0])
        # Si el contador a llegado al limite de pasos ejecutamos lo siguiente
        if cont == movimientos[0]:
            # Llamamos a la funcion que va sumar el numero del limite y el sigiente moviminto para que los sume y los almacene en la lista en un nuevo elemento siendo el nuvo limite para la siguiente condicion
            suma(0, giroA)
    
    # Definimos la distancia maxima
    elif cont <= movimientos[1]: # 250
        derecha(cont, movimientos[1])
        if cont == movimientos[1]:
            suma(1, adelanteA + adelanteM)
    
    # Definimos la distancia maxima
    elif cont <= movimientos[2]: # 480
        adelante(cont, movimientos[2])
        if cont == movimientos[2]:
            suma(2, giro)
    
    # Definimos la distancia maxima
    elif cont <= movimientos[3]: # 515
        izquierda(cont, movimientos[3]) 
        if cont == movimientos[3]:
            suma(2, adelanteM)

    ####### parte 2 #######
            
    # Definimos la distancia maxima
    elif cont <= movimientos[4]: # 515
        adelante(cont)
        if cont == movimientos[4]:
            suma(2, giro)

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
        alto(cont)
        print("Estos fueron los movimientos", movimientos)
        break

    cont += 1