from space_jam_function import space_jam
import unittest

class TestSpaceJam(unittest.TestCase):
    def test_first_case(self):
        self.assertEqual(space_jam('mlaiengineer'), 'M  L  A  I  E  N  G  I  N  E  E  R')

    def test_second_case(self):
        self.assertEqual(space_jam(' f r e!'), 'F  R  E  !')

if __name__ == '__main__':
    print("Running tests...")
    unittest.main()