from mars_rovers_app.direction import Direction
from mars_rovers_app.mars_rover import MarsRover
from unittest import TestCase
import unittest

import mars_rovers_app


class TestRoversTests(TestCase):

    def test_rover1_should_return_the_current_position(self):
        rover1 = MarsRover(1, 2, Direction.N)
        rover1.move([5, 5], "LMLMLMLMM")

        result = "{} {} {}".format(str(rover1.x), str(
            rover1.y), rover1._direction.name)
        expected = "1 3 N"
        self.assertEqual(expected, result)

    def test_rover2_should_return_the_current_position(self):
        rover2 = MarsRover(3, 3, Direction.E)
        rover2.move([5, 5], "MMRMMRMRRM")

        result = "{} {} {}".format(str(rover2.x), str(
            rover2.y), rover2._direction.name)
        expected = "5 1 E"
        self.assertEqual(expected, result)
