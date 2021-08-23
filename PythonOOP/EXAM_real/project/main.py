from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist

import unittest
from unittest import TestCase, main

class AstrinautTestCase(TestCase):
    def test_init_inputs(self):
        a = Biologist('Ivan')
        self.assertEqual('Ivan',  a.name)
        # self.assertEqual(70,  a.oxygen)


if __name__ == '__main__':
    main()
