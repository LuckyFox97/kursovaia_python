import unittest
from main_proj.main import masked_operation, base_json, description_operation

class TestMaskedOperation(unittest.TestCase):

    def test_masked_operation(self):
        data = masked_operation(base_json())  # Передаем результат выполнения функции base_json() в качестве аргумента
        self.assertIsInstance(data, str)
        self.assertTrue(len(data) > 0)

        lines = data.splitlines()
        self.assertTrue(len(lines) >= 7)

        for line in lines:
            if line.endswith('USD') or line.endswith('руб.'):
                self.assertTrue(True)
            else:
                self.assertFalse(False)


class TestDiscriptionOperation(unittest.TestCase):

    def test_discription_operation(self):
        data = description_operation()
        for operation in data:
            if 'description' in operation:
                self.assertTrue(True)
            else:
                self.assertFalse(False)



class TestBaseJson(unittest.TestCase):

    def test_base_json(self):
        data = base_json()
        self.assertIsInstance(data, list)
        for operation in data:
            self.assertIsInstance(operation, dict)



if __name__ == '__main__':
    unittest.main()