from Calc import calculator
import unittest

class TestOperationsMethods(unittest.TestCase):
    def test_InitCalc(self):
        c = calculator()
        self.assertFalse(c == None)
        self.assertTrue(len(c.op_dic.keys()) == 4,"should be 4")
    
    def test_calcSimpleNum(self):
        c = calculator()
        self.assertEqual(c.calc("12") ,12,"Should be 12")
        self.assertEqual(c.calc("12.3") ,12.3,"Should be 12.3")

    def test_SingleOperaation(self):
        c = calculator()
        self.assertEqual(c.calc("1+2") ,3,"Should be 3")
        self.assertEqual(c.calc("1-2") ,-1,"Should be -1")
        self.assertEqual(c.calc("1*2") ,2,"Should be 2")
        self.assertEqual(c.calc("1/2") ,0.5,"Should be 0.5")

    def test_MultipleSameOperaation(self):
        c = calculator()
        self.assertEqual(c.calc("1+2+3") ,6,    "Should be 6")
        self.assertEqual(c.calc("1-2-2") ,-3,   "Should be -3")
        self.assertEqual(c.calc("1*2*3") ,6,    "Should be 6")
        self.assertEqual(c.calc("1/2/2") ,0.25, "Should be 0.25")
    
    def test_MultipleSamePrcdns(self):
        c = calculator()
        self.assertEqual(c.calc("1+2-3") ,0,    "Should be 6")
        self.assertEqual(c.calc("1*3/3") ,1,    "Should be 6")
    
    def test_MultipleDiffPrcdns(self):
        c = calculator()
        self.assertEqual(c.calc("1+2*3") ,7,    "Should be 6")
        self.assertEqual(c.calc("2*3+3") ,9,    "Should be 6")
    
    def test_Complex(self):
        c = calculator()
        self.assertEqual(c.calc("1+2+3*4/5+30-11"), 24.4,   "should be 24.4")
        self.assertEqual(c.calc("60/8+9/3*4-11"),   8.5,    "should be 8.5")
    
    def test_invalidExpression(self):
        c = calculator()
        self.assertEqual(c.calc("1++"), None,   "should be None")
