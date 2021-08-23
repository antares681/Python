class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')
    self.sleepy = False


import unittest
from unittest import TestCase

class CatTests(TestCase):
  def setUp(self):
    self.cat = Cat('Gosho')

  def test_eating_cat_size_increasing(self):
    self.cat.eat()
    self.assertEqual(1,self.cat.size)

  def test_cat_is_fed_after_eating(self):
      self.cat.eat()
      self.assertEqual(True, self.cat.fed)

  def test_cat_cannot_eat_fed(self):
    with self.assertRaises(Exception) as ex:
      self.cat.fed = True
      self.cat.eat()
    self.assertEqual('Already fed.', str(ex.exception))

  def test_cat_cannot_sleep_if_not_fed(self):
    with self.assertRaises(Exception) as ex:
      self.cat.sleepy = False
      self.cat.sleep()
    self.assertEqual('Cannot sleep while hungry', str(ex.exception))

  def test_cat_if_sleepy(self):
    self.cat.eat()
    self.assertTrue(self.cat.sleepy)
    self.cat.sleep()
    self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()