def math_operations(*args, **kwargs):

    int_args = list(args)

    while True:
        for k, v in kwargs.items():
            if not int_args:
                return kwargs
            if k == "a":
                kwargs[k] += abs(int_args[0])
            if k == "s":
                kwargs[k] -= abs(int_args[0])
            if k == "d":
                try:
                    kwargs[k] /= abs(int_args[0])
                except ZeroDivisionError:
                    continue
            if k == "m":
                kwargs[k] *= abs(int_args[0])
            int_args.pop(0)

# print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))

import unittest
class Tests(unittest.TestCase):
    def test(self):
        func = math_operations
        res = func(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15)
        self.assertEqual(res, {'a': 9, 's': 15, 'd': -3.0, 'm': -45})
if __name__ == '__main__':
    unittest.main()