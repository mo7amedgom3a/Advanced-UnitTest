import unittest
from unittest.mock import patch, Mock
from src.api_client import fetch_data_from_api

class TestMyModule(unittest.TestCase):
    @patch('src.api_client.requests.get')
    def test_get_data_from_api(self, mock_get):
        """"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': 'Hello from API'}
        mock_get.return_value = mock_response

        status,result  = fetch_data_from_api('https://jsonplaceholder.typicode.com/posts')

        self.assertEqual(result, {'data': 'Hello from API'})
        self.assertEqual(status, 200)
        mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts')

if __name__ == '__main__':
    unittest.main()