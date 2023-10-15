try:
    from controller import Robot
except:
    print("no esta la libreria instalada")

timeStep = 32
velocidad_max = 6.28

robot = Robot()

rueda_izquierada = robot.getMotor("left weel motor")
rueda_derecha = robot.getMotor("right weel motor")

rueda_izquierada.setVelocity(velocidad_max)
rueda_derecha.setVelocity(velocidad_max)

rueda_izquierada.setPosition(float("inf"))
rueda_derecha.setPosition(float("inf"))

while robot.step(timeStep) != -1:
    pass