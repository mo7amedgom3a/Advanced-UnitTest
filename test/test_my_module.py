import unittest
from unittest.mock import patch
from src.my_module import get_data_from_module
from src.data_service import get_data

class TestMyModule(unittest.TestCase):

    @patch('src.my_module.get_data')
    def test_get_data_from_module(self, mock_get_data):
        mock_get_data.return_value = {'data': 'Hello from data service'}
        result = get_data_from_module()
        self.assertEqual(result, {'data': {'data': 'Hello from data service'}})
        mock_get_data.assert_called_once() # Check if the mock was called

if __name__ == '__main__':
    unittest.main()
