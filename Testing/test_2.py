# def add(v1,v2,extra=None):
#     if extra:
#         return False

#     if (type(v1) == str and type(v2) in [int,float]) or (type(v1) in [int,float] and type(v2) == str):
#         return "Invalid inputs"
#     return v1 + v2

# import unittest

# class AddTest(unittest.TestCase):
#     def test_add_with_two_int(self):
#         output = add(45,65)
#         self.assertEqual(output,110)

#     def test_add_with_two_str(self):
#         output = add("a","b")
#         self.assertEqual(output,"ab")

#     def test_add_with_one_int_second_str(self):
#         output = add("a",12.25)
#         self.assertEqual(output,"Invalid inputs")

#     def test_add_with_extra_args(self):
#         output = add(12,25,extra="Aniket")
#         self.assertFalse(output)

import unittest
class Calculations:
    def add(v1,v2):
        return v1 + v2

    def sub(v1,v2):
        return v1 - v2

    def mul(v1,v2):
        return v1 * v2

    def div(v1,v2):
        return v1 // v2


class CalculationTest(unittest.TestCase):  #test suite

    def setUp(self):
        print("Abc")
        self.val1 = 6
        self.val2 = 3

    @classmethod
    def setUpClass(cls):
        print("In setUp class")
        cls.Name = "Math Calculation"
        
    def test_add(self):
        result = Calculations.add(self.val1,self.val2)
        self.assertEqual(result,9)
        print(CalculationTest.Name,"-----------------")

    def test_sub(self):
        result = Calculations.sub(self.val1,self.val2)
        self.assertEqual(result,3)

    def test_mul(self):
        result = Calculations.mul(self.val1,self.val2)
        self.assertEqual(result,18)

    def test_div(self):
        result = Calculations.div(self.val1,self.val2)
        self.assertEqual(result,2)

    @classmethod
    def tearDownClass(cls):
        print("In tearDown class")
        del cls.Name


    def tearDown(self):
        print("xyz")
        del self.val1
        del self.val2





if __name__ == '__main__':
    unittest.main()                 #test runner
