import pyglet
import pyglet.math
from freegames import vector
from math import sin, cos

# Window
win = pyglet.window.Window(500, 500, "Pendulum")

# Bob
bob = pyglet.math.Vec2(250, 250)

# Arm
origin = pyglet.math.Vec2(250, 250)
l = 100
angle = 45
avel = 0
acc = 0

# Update
def update(dt):
    global angle, avel, acc

    win.clear()

    bob = pyglet.math.Vec2(origin.x + l * sin(angle), origin.y - l * cos(angle))

    pyglet.shapes.Line(origin.x, origin.y, bob.x, bob.y).draw()
    pyglet.shapes.Circle(bob.x, bob.y, 15, color=(234,23,12)).draw()

    acc = -0.01 * sin(angle)

    angle += avel
    avel += acc

    avel *= 0.99

pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()
