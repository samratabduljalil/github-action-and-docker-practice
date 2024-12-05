import unittest
from sum_of_two_numbers import sum_numbers

class TestSumNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_numbers(3,5),8)






if __name__ == '__main__':
    unittest.main()        