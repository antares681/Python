class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest

class WorkerTests(unittest.TestCase):
    #TEST 1
    def test_worker_is_initialized_correctly(self):
        #arrange and act
        worker = Worker('Test', 100, 10)
        #Assert
        self.assertEqual('Test', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy, msg='Energy should be equal to the energu on init')
        self.assertEqual(0, worker.money)

    #TEST 2
    def test_worker_energy_increased_after_rest(self):
        #arrange
        worker = Worker ('Test', 100, 10)
        #act
        worker.rest()
        self.assertEqual(11, worker.energy)

    # TEST 3
    def test_worker_works_with_negative_energy_raises(self):
        # arrange
        worker = Worker('Test', 100, 0)
        # act
        with self.assertRaises(Exception) as ex:
            worker.work()

        #assertion
        self.assertEqual('Not enough energy.', str(ex.exception))

    #TEST 4
    def test_worker_salary_properly_increased(self):
        #arrange
        worker = Worker('Test', 100, 10)
        #act
        worker.work()
        #assert
        self.assertEqual(100, worker.money)

    #TEST 5
    def test_worker_energy_properly_decreased(self):
        # arrange
        worker = Worker('Test', 100, 10)
        # act
        worker.work()
        # assert
        self.assertEqual(9, worker.energy)

    #TEST 6
    def test_get_info_return_proper_string_and_values(self):
        # arrange
        worker = Worker('Test', 100, 10)
        # act
        worker.get_info()
        #assert
        self.assertEqual(f'Test has saved 0 money.', f'{worker.name} has saved {worker.money} money.')

if __name__ == "__main__":
    unittest.main()
