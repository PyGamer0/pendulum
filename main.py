import pyglet
from freegames import vector
from math import sin, cos

# Window
win = pyglet.window.Window(500, 500, "Pendulum")

# Bob
bob = vector(250, 250)

# Arm
origin = vector(250, 350)
l = 100
angle = 45
avel = 0
acc = 0

# Update
def update(dt):
    global angle, avel, acc

    win.clear()

    bob.x = origin.x + l * sin(angle)
    bob.y = origin.y + -l * cos(angle)

    pyglet.shapes.Line(origin.x, origin.y, bob.x, bob.y).draw()
    pyglet.shapes.Circle(bob.x, bob.y, 15, color=(234,23,12)).draw()

    acc = -0.01 * sin(angle)

    angle += avel
    avel += acc

    avel *= 0.99

pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()
