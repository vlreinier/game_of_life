from unittest import TestCase
from Simulator import *


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)

    def test_life_rules(self):
        """
        Tests functionality of life_rules function.
        """

        world = World(110, alive_cells=0)  # all cells are dead 0
        self.sim.set_world(world)  # set world in simulator object
        self.sim.world.set(0, 0, 1)  # set 2 cells alive
        self.sim.world.set(0, 1, 1)
        state = self.sim.life_rules(0, 1)  # check state
        self.assertEqual(state, 0)
        """ state must be zero since 'Elke levende cel met minder dan twee levende buren """
        """gaat dood (ook wel onderpopulatie of exposure genaamd);"""

        world = World(110, alive_cells=1)  # all cells are alive
        self.sim.set_world(world)  # set world in simulator object
        state = self.sim.life_rules(0, 0)  # return calculated state (0 or 1) for cell
        self.assertEqual(state, 0)
        """ state must be zero since all cells are alive (1)'Elke levende cel met meer dan drie levende buren """
        """gaat dood (ook wel overpopulatie of overcrowding genaamd);"""

        world = World(110, alive_cells=0)  # all cells are dead
        self.sim.set_world(world)  # set world in simulator object
        self.sim.world.set(0, 0, 1)
        self.sim.world.set(0, 1, 1)
        self.sim.world.set(0, 2, 1)
        state = self.sim.life_rules(0, 1)
        self.assertEqual(state, 1)  # checking for state alive with 2 alive neighbours
        self.sim.world.set(0, 1, 0)
        state = self.sim.life_rules(0, 1)
        self.assertEqual(state, 0)  # checking for state dead with 2 alive neighbours
        """ state must be zero since all cells are alive (1)'Elke cel met twee of drie levende buren overleeft, """
        """onveranderd naar de volgende generatie (survival);"""

        world = World(110, alive_cells=0)  # all cells are dead 0
        self.sim.set_world(world)  # set world in simulator object
        self.sim.world.set(0, 0, 1)  # set 2 cells alive
        self.sim.world.set(0, 1, 0)
        self.sim.world.set(0, 2, 1)
        self.sim.world.set(1, 1, 1)
        state = self.sim.life_rules(0, 1)  # check state
        self.assertEqual(state, 1)
        """ state must be zero since 'elke dode cel met precies drie levende buren komt tot leven """
        """(ook wel geboorte of birth genaamd)."""


test = TestSimulator()
test.setUp()
test.test_life_rules()
