import unittest
from main_proj.main import OperationsProcessor

class TestMainProj(unittest.TestCase):
    def test_mark_account_number(self):
        op = OperationsProcessor()
        self.assertEqual(op.mask_card('Счет 35383033474447895560'), 'Счет 5560')

    def test_mark_card_number(self):
        op = OperationsProcessor()
        self.assertEqual(op.mask_card('Maestro 1596837868705199'), 'Maestro 1596 83** **** 5199')
        self.assertEqual(op.mask_card('Visa Classic 1596837868705199'), 'Visa Classic 1596 83** **** 5199')


if __name__ == '__main__':
    unittest.main()
