import pyglet
from pyglet import window
import pyglet.math
from freegames import vector
from math import sin, cos

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bob = pyglet.math.Vec2(250, 250)
        self.origin = pyglet.math.Vec2(250, 250)
        self.l = 100

        self.angle = 45
        self.avel = 0
        self.acc = 0

    def update(self, dt):
        self.clear()

        self.bob = pyglet.math.Vec2(self.origin.x + self.l * sin(self.angle),
                self.origin.y - self.l * cos(self.angle))
        self.acc = -0.01 * sin(self.angle)

        self.angle += self.avel
        self.avel += self.acc

        self.avel *= 0.99

    def on_draw(self):
        pyglet.shapes.Line(self.origin.x, self.origin.y, self.bob.x, self.bob.y).draw()
        pyglet.shapes.Circle(self.bob.x, self.bob.y, 15, color=(34, 45, 120)).draw()

    def on_mouse_press(self, x, y, button, modifiers):
        self.origin = pyglet.math.Vec2(x, y)

win = Window(500, 500, "Pendulum")

pyglet.clock.schedule_interval(win.update, 1/60)
pyglet.app.run()
