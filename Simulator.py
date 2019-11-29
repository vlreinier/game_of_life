from World import *
import random

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None, rules='B3/S23', start_age=0):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0

        if world == None:
            self.world = World(20)
        else:
            self.world = world

        self.birth_neighbours = Simulator.get_rules_on_index(rules, 0)
        self.survival_neighbours = Simulator.get_rules_on_index(rules, 1)
        self.start_age = start_age

        if len(rules.split('/')) == 3:
            self.mode = 'decay of age'
            self.max_age = Simulator.get_rules_on_index(rules, 2)[0]
            self.world.world[self.world.world == 1] = self.start_age
        else:
            self.mode = 'standard'


    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """

        self.generation += 1

        # iterating over all cells to run rules on every cell
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

    def life_rules(self, x, y) -> int:
        """Calculates state for current cell by checking some if statements and comparing to rules"""
        current_age = self.world.get(x, y)

        if self.mode == 'decay of age':
            alive_neighbours = sum([1 for i in self.world.get_neighbours(x, y) if i > 0])
            fertile_ages = list(range(2, self.max_age-1))

            # birth
            if current_age in fertile_ages and alive_neighbours in self.birth_neighbours:
                next_age = current_age+1
            # survival
            elif current_age and alive_neighbours in self.survival_neighbours:
                next_age = current_age
            # death
            else:
                next_age = current_age-1
        else:
            alive_neighbours = self.world.get_neighbours(x, y).count(1)

            # birth
            if not current_age and alive_neighbours in self.birth_neighbours:
                next_age = 1
            # survival
            elif current_age and alive_neighbours in self.survival_neighbours:
                next_age = 1
            # death
            else:
                next_age = 0

        # age can not be negative
        if next_age < 0:
            next_age = 0

        return next_age

    @staticmethod
    def get_rules_on_index(rules, index) -> List[int]:
        """Splits rule string into birth and survival int lists"""
        return [int(i) for i in rules.split('/')[index] if i.isdigit()]