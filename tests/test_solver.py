import sys
sys.path.append("..")
import unittest
from src import solver

# test = [[9,0,0,4,0,0,0,0,0],
#         [0,0,8,0,2,9,4,0,0],
#         [0,0,7,8,0,0,0,0,3],
#         [1,7,0,5,0,0,0,4,0],
#         [0,0,0,0,9,8,0,0,7],
#         [8,5,0,0,0,7,6,0,0],
#         [6,0,3,9,0,1,0,0,0],
#         [0,0,0,0,0,0,0,0,9],
#         [4,0,0,2,0,0,0,8,0]]



class MyTestCase(unittest.TestCase):
    def test_check_line(self):
        self.assertTrue(solver.check_if_number_in_line(4,0))
        self.assertTrue(solver.check_if_number_in_line(9,0))
        self.assertFalse(solver.check_if_number_in_line(1,0))
        self.assertFalse(solver.check_if_number_in_line(2,0))

    def test_check_column(self):
        self.assertTrue(solver.check_if_number_in_column(4,3))
        self.assertTrue(solver.check_if_number_in_column(9,0))
        self.assertTrue(solver.check_if_number_in_column(1,0))
        self.assertFalse(solver.check_if_number_in_column(1,1))
        self.assertFalse(solver.check_if_number_in_column(2,0))

    def test_check_square(self):
        self.assertTrue(solver.check_if_number_in_square(9,0))
        self.assertTrue(solver.check_if_number_in_square(8,0))
        self.assertTrue(solver.check_if_number_in_square(7,0))
        self.assertTrue(solver.check_if_number_in_square(9, 4))
        self.assertTrue(solver.check_if_number_in_square(8, 4))
        self.assertTrue(solver.check_if_number_in_square(7, 4))
        self.assertTrue(solver.check_if_number_in_square(5, 4))
        self.assertFalse(solver.check_if_number_in_square(1,1))
        self.assertFalse(solver.check_if_number_in_square(9,3))

# test = [[9,0,0,4,0,0,0,0,0],
#         [0,0,8,0,2,9,4,0,0],
#         [0,0,7,8,0,0,0,0,3],
#         [1,7,0,5,0,0,0,4,0],
#         [0,0,0,0,9,8,0,0,7],
#         [8,5,0,0,0,7,6,0,0],
#         [6,0,3,9,0,1,0,0,0],
#         [0,0,0,0,0,0,0,0,9],
#         [4,0,0,2,0,0,0,8,0]]


if __name__ == '__main__':
    unittest.main()
