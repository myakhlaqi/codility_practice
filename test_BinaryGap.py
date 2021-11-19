import unittest
import BinaryGap


class TestBinaryGap(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(BinaryGap.solution(529),4,"Passed")
        self.assertEqual(BinaryGap.solution(9),2,"Passed")
        self.assertEqual(BinaryGap.solution(20),1,"Passed")
        self.assertEqual(BinaryGap.solution(5),1,"Passed")
        self.assertEqual(BinaryGap.solution(0),0,"Passed")
        self.assertEqual(BinaryGap.solution(15),0,"Passed")
        self.assertEqual(BinaryGap.solution(1041),5,"Passed")
        self.assertEqual(BinaryGap.solution(32),0,"Passed")
        
        


if __name__ == '__main__':
    unittest.main()