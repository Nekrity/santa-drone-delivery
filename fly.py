from djitellopy import Tello

# Uzdevums: Iziet trasi ar koda palidzību
# Noteikumi:
# - secīgi jaiziet cauri visiem vārtiem
# - jaapmeklē visas platformas
# - jaātgriezas atpakaļ
# - caur vārtiem drīkst līdot tikai taisni (ar kāmeru priekšā)

# Dokumentācija un piemēri
# https://github.com/damiafuentes/DJITelloPy/tree/master
# https://github.com/damiafuentes/DJITelloPy/blob/master/examples/simple.py

tello = Tello()

tello.connect()
tello.takeoff()
tello.rotate_clockwise(180)
tello.move_forward(121)
tello.land()

tello.takeoff()
tello.move_back(10)
tello.rotate_counter_clockwise(90)
tello.move_forward(90)
tello.rotate_clockwise(90)
tello.move_forward(75)
tello.rotate_clockwise(90)
tello.land()

tello.takeoff()
tello.move_forward(90)
tello.rotate_clockwise(90)
tello.move_forward(187)
tello.land()

#tello.set_speed(20)

#tello.move_left(100)
#tello.move_right(100)
#tello.move_forward(100)
#tello.move_back(100)

#tello.land()
#tello.takeoff()

#tello.rotate_clockwise(360)
#tello.rotate_counter_clockwise(360)

#tello.land()
