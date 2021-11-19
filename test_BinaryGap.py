import unittest
import BinaryGapV2


class TestBinaryGap(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(BinaryGapV2.solution(529),4,"Passed")
        self.assertEqual(BinaryGapV2.solution(9),2,"Passed")
        self.assertEqual(BinaryGapV2.solution(20),1,"Passed")
        self.assertEqual(BinaryGapV2.solution(5),1,"Passed")
        self.assertEqual(BinaryGapV2.solution(0),0,"Passed")
        self.assertEqual(BinaryGapV2.solution(15),0,"Passed")
        self.assertEqual(BinaryGapV2.solution(1041),5,"Passed")
        self.assertEqual(BinaryGapV2.solution(32),0,"Passed")
        
        


if __name__ == '__main__':
    unittest.main()