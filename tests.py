import unittest
import src.iso6346 as iso6346


class TestIso6346(unittest.TestCase):


    def test_checkdigit(self):
        self.assertEqual(iso6346.checkdigit('ZEPU0037255'), 5,
                         'Incorrect checkdigit.')


    def test_validate(self):
        self.assertEqual(iso6346.validate('ZEPU0037255'), True,
                         'Incorrect validation, should pass.')


    def test_format(self):
        self.assertEqual(iso6346.format('ZEPU0037255'), 'ZEPU 003725 5',
                         'Incorrect format.')


    def test_format_box(self):
        self.assertEqual(iso6346.format('ZEPU0037255', box=True), 'ZEPU 003725 [5]',
                         'Incorrect format.')



    def test_normalise(self):
        self.assertEqual(iso6346.normalize(' ZEPU-003725 [5]'), 'ZEPU0037255',
                         'Incorrect normalisation.')


if __name__ == '__main__':
    unittest.main()
