import sys
# insert at 1, 0 is the script path (or '' in REPL)
#sys.path.insert(1, '../serviceA/folder')
from ScheduledRate import ScheduledRate
import unittest

class TestStringMethods(unittest.TestCase):
    def gggg(self):
        ScheduledRate(10,test_func)

    def test_func(self):
        return 1

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()