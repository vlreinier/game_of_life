from World import *
import random

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """

        self.generation += 1

        # game of life rules
        for x in range(len(self.world.world)):
            for y in range(len(self.world.world[x])):
                self.world.set(x, y, self.life_rules(x, y))

        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world

    def life_rules(self, x, y):
        current_state = self.world.get(x, y)
        alive_neighbours = self.world.get_neighbours(x, y).count(1)
        if current_state == 1 and alive_neighbours < 2:
            return 0
        elif current_state == 1 and alive_neighbours > 3:
            return 0
        elif current_state == 1 and (alive_neighbours == 3 or alive_neighbours == 2):
            return 1
        elif current_state == 0 and alive_neighbours == 3:

            return 1
        else:
            return 0