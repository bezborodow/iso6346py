import unittest
import src.iso6346 as iso6346


class TestIso6346(unittest.TestCase):


    def test_checkdigit(self):
        self.assertEqual(iso6346.checkdigit('ZEPU0037255'), 5,
                         'Incorrect checkdigit.')


if __name__ == '__main__':
    unittest.main()
