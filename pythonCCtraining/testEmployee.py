import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.mike = Employee('Mike', 'Ionov', 130_000)
        
    def test_give_default_raise(self):
        self.mike.give_raise()
        self.assertEqual(self.mike.salary, 135_000)

    def test_give_custom_raise(self):
        self.mike.give_raise(130_000)
        self.assertEqual(self.mike.salary, 260_000)

if __name__=="__main__":
    unittest.main()
