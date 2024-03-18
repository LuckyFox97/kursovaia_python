import unittest
from main_proj.main import base_json

class TestMainFunctions(unittest.TestCase):

    def test_base_json(self):
        data = base_json()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, dict)

if __name__ == '__main__':
    unittest.main()
