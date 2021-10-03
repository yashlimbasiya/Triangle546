

import unittest

from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    
    def testInvalidInputA(self):
    	self.assertEqual(classifyTriangle(2,230,332),'InvalidInput')   
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 3, 7),'NotATriangle') 
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')     
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(7, 8, 9),'Scalene')
    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 3, 5),'Isosceles')
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(4, 8, 1),'NotATriangle')

    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

