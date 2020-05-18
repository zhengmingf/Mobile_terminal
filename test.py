import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        # self.assertEqual('foo'.upper(), 'FOO')
        print(1)

    def test_isupper(self):
        # self.assertTrue('FOO'.isupper())
        # self.assertFalse('Foo'.isupper())
        self.test_isupper()
        # unittest.FunctionTestCase(self.test_upper)


if __name__ == '__main__':
    unittest.main()