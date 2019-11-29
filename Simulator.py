from World import *
import random

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None, rules='B3/S23'):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if len(rules.split('/')) == 3:
            self.mode = 'decay of age'
        else:
            self.mode = 'standard'
        self.birth_neighbours, self.survival_neighbours = Simulator.split_rules(rules)
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
                self.world.set(x, y, self.life_rules(self.world.get(x, y), self.world.get_neighbours(x, y).count(1)))

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

    @staticmethod
    def get_rules(rules) -> List[int]:
        """Splits rule string into birth and survival int lists"""
        rules = rules.split('/')

        if len(rules) ==
        birth_neighbours = [int(i) for i in rules.split('/')[index] if i.isdigit()]
        survival_neighbours = [int(i) for i in rules.split('/')[1] if i.isdigit()]
        return birth_neighbours, survival_neighbours

    def life_rules(self, current_state, alive_neighbours) -> int:
        """Calculates state for current cell by checking some if statements and comparing to rules"""
        if self.mode == 'decay of age':
            # birth
            if current_state in [2, 3, 4] and alive_neighbours in self.birth_neighbours:
                return +1
            # survival
            if current_state == 6 and alive_neighbours in self.survival_neighbours:
                return current_state
            # death
            else:
                return -1
        else:
            # birth
            if not current_state and alive_neighbours in self.birth_neighbours:
                return 1
            # survival
            if current_state and alive_neighbours in self.survival_neighbours:
                return 1
            # death
            else:
                return 0


    # def life_rules_OLD(self, x, y):
    #     current_state = self.world.get(x, y)
    #     alive_neighbours = self.world.get_neighbours(x, y).count(1)
    #     if current_state == 1 and alive_neighbours < 2:
    #         return 0
    #     elif current_state == 1 and alive_neighbours > 3:
    #         return 0
    #     elif current_state == 1 and (alive_neighbours == 3 or alive_neighbours == 2):
    #         return 1
    #     elif current_state == 0 and alive_neighbours == 3:
    #
    #         return 1
    #     else:
    #         return 0