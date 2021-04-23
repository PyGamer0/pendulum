import pyglet
from freegames import vector

class entity:
    def __init__(self, x, y, m):
        self.pos = vector(x, y)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)
        self.mass = m

    def apply_force(self, f):
        self.acc += f / self.mass

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self, r, c):
        shape = pyglet.shapes.Circle(self.pos.x, self.pos.y, r)
        shape.color = c
        shape.draw()

win = pyglet.window.Window(width=500, height=500)
e = entity(250, 250, 1)

def update(dt):
    e.update()

    # Gravity
    g = vector(0, -0.1)
    e.apply_force(g)

@win.event
def on_draw():
    win.clear()
    e.draw(25, (243, 122, 20))

pyglet.clock.schedule_interval(update, 1/120)
pyglet.app.run()
