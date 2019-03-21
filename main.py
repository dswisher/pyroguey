"""The main bits."""

import time

from bearlibterminal import terminal
import esper

FPS = 60
SCREEN_WIDTH = 90
SCREEN_HEIGHT = 35


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Components

class Velocity:
    """Velocity component."""

    def __init__(self, x=0.0, y=0.0):
        """Constructor."""
        self.x = x
        self.y = y


class Renderable:
    """Renderable component."""

    def __init__(self, glyph, posx, posy):
        """Constructor."""
        self.glyph = glyph
        self.x = posx
        self.y = posy


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Processors
class MovementProcessor(esper.Processor):
    """Movement processor."""

    def __init__(self, minx, maxx, miny, maxy):
        """Constructor."""
        super().__init__()
        self.minx = minx
        self.maxx = maxx
        self.miny = miny
        self.maxy = maxy

    def process(self):
        """Process."""
        for ent, (vel, rend) in self.world.get_components(Velocity, Renderable):
            rend.x += vel.x
            rend.y += vel.y
            # An example of keeping the sprite inside screen boundaries. Basically,
            # adjust the position back inside screen boundaries if it tries to go outside:
            rend.x = max(self.minx, rend.x)
            rend.y = max(self.miny, rend.y)
            rend.x = min(self.maxx, rend.x)
            rend.y = min(self.maxy, rend.y)


class RenderProcessor(esper.Processor):
    """Render processor."""

    def __init__(self):
        """Constructor."""
        super().__init__()

    def process(self):
        """Process."""
        terminal.clear()
        for ent, rend in self.world.get_component(Renderable):
            terminal.put(rend.x, rend.y, rend.glyph)
        terminal.refresh()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Main program
def main():
    """Do the needful."""
    terminal.open()
    terminal.set("window.title='Pyroguey'; window.size={}x{};".format(SCREEN_WIDTH, SCREEN_HEIGHT))
    terminal.set('input.filter=[keyboard+]')    # for TK_KEY_RELEASED to work

    world = esper.World()
    player = world.create_entity()
    world.add_component(player, Velocity(x=0, y=0))
    world.add_component(player, Renderable('@', 10, 10))

    enemy = world.create_entity()
    world.add_component(enemy, Renderable('T', 20, 20))

    render_processor = RenderProcessor()
    movement_processor = MovementProcessor(minx=0, maxx=SCREEN_WIDTH - 1, miny=0, maxy=SCREEN_HEIGHT - 1)
    world.add_processor(render_processor)
    world.add_processor(movement_processor)

    # terminal.printf(1, 1, 'Hello, world!')
    while True:
        start_time = time.perf_counter()  # limit fps

        key = None
        if terminal.has_input():
            key = terminal.read()

        if key == terminal.TK_ESCAPE:
            break

        if key == terminal.TK_UP:
            world.component_for_entity(player, Velocity).y = -1
        if key == terminal.TK_DOWN:
            world.component_for_entity(player, Velocity).y = 1
        if key == terminal.TK_LEFT:
            world.component_for_entity(player, Velocity).x = -1
        if key == terminal.TK_RIGHT:
            world.component_for_entity(player, Velocity).x = 1

        if key == terminal.TK_UP | terminal.TK_KEY_RELEASED:
            world.component_for_entity(player, Velocity).y = 0
        if key == terminal.TK_DOWN | terminal.TK_KEY_RELEASED:
            world.component_for_entity(player, Velocity).y = 0
        if key == terminal.TK_LEFT | terminal.TK_KEY_RELEASED:
            world.component_for_entity(player, Velocity).x = 0
        if key == terminal.TK_RIGHT | terminal.TK_KEY_RELEASED:
            world.component_for_entity(player, Velocity).x = 0

        world.process()

        delta_time = (time.perf_counter() - start_time) * 1000
        terminal.delay(max(int(1000.0 / FPS - delta_time), 0))

        # terminal.clear()
        # terminal.put(x, y, '@')

        # terminal.refresh()

        # key = terminal.read()

        # if key == terminal.TK_ESCAPE:
        #     break
        # elif key == terminal.TK_UP:
        #     y -= 1
        # elif key == terminal.TK_DOWN:
        #     y += 1
        # elif key == terminal.TK_LEFT:
        #     x -= 1
        # elif key == terminal.TK_RIGHT:
        #     x += 1

    terminal.close()


if __name__ == '__main__':
    main()
