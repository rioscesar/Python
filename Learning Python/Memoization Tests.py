import unittest
from Memoization import fib

class MemoTests(unittest.TestCase):

    def setUp(self):
        self.fib_elems = ( (0,0), (1,1), (2,1) )
        print("setUp complete")
        
    def testCalc(self):
        for (i, val) in self.fib_elems:
            self.assertEqual(fib(i), val)

    def tearDown(self):
        self.fib_elems = None
        print("tearDown complete")

if __name__ == "__main__":
    unittest.main()
