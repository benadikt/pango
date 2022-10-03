from src.operations import *
import unittest


class TestOperationsMethods(unittest.TestCase):
    def test_add(self):
        tmp = Add()
        self.assertEqual(tmp.symbol() ,"+","should be +")
        self.assertEqual(tmp.m_precedence ,1,"should be 1")
        self.assertEqual(tmp.calc(3,4) ,7,"should be 7")
    
    def test_sub(self):
        tmp = Subtract()
        self.assertEqual(tmp.symbol() ,"-","should be -")
        self.assertEqual(tmp.m_precedence ,1,"should be 1")
        self.assertEqual(tmp.calc(3,4) ,-1,"should be -1")
    
    def test_mul(self):
        tmp = Multiply()
        self.assertEqual(tmp.symbol() ,"*","should be *")
        self.assertEqual(tmp.m_precedence ,2,"should be 2")
        self.assertEqual(tmp.calc(3,4) ,12,"should be 12")
    
    def test_divide(self):
        tmp = Divide()
        self.assertEqual(tmp.symbol() ,"/","should be /")
        self.assertEqual(tmp.m_precedence ,2,"should be 2")
        self.assertEqual(tmp.calc(3,4) ,0.75,"should be 0.75")

if __name__ == '__main__':
    unittest.main()