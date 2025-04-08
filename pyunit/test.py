import unittest
a = 2
b = 3
expectedResult = 6

def multiply(a, b):
    return a * b

class TestMathOperations(unittest.TestCase):
    def testMultiply(self):
        self.assertEqual(multiply(a, b), expectedResult)

if __name__ == "__main__":
    

    unittest.main()