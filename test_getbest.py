from getbest import *
import unittest

class TestGetBest(unittest.TestCase):

    def test_getCols_function(self):
        f = open("bestdat0.csv", "r")
        num_col, mark_col = getCols(f)

        # Check correct column indices 
        self.assertEqual(num_col, 1)
        self.assertEqual(mark_col, 2)

        f.close()

    def test_findTop_function(self):
        f = open("bestdat0.csv", "r")
        num_col, mark_col = getCols(f)

        # Find top student 
        best_idx, best = findTop(f, num_col, mark_col)

        # Check correct top student and mark
        self.assertEqual(best, 90)
        self.assertEqual(best_idx, "167381")

        f.close()

if __name__ == '__main__':
    unittest.main()  # run all tests