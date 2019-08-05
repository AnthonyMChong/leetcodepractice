import unittest
from condense_a_string import condenseString

class TestCondenseString( unittest.TestCase ):

    def test_String(self):
        self.assertEqual (condenseString("S s S S ssss sss") , "SsSSsssssss")
        pass


if __name__ == '__main__':
    unittest.main()