import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from src.weather import WeatherDataFetcher

class TestWeatherDataFetcher(unittest.TestCase):
    """Test suite for the WeatherDataFetcher class."""

    @classmethod
    def setUpClass(cls):
        print("Setting up...")
        cls.fetcher = WeatherDataFetcher()
    
    @classmethod
    def tearDownClass(cls):
        print("Tearing down...")
        cls.fetcher = None
    
    def setUp(self):
        print("Setting up...")
        self.fetcher.database = {}
    
    def tearDown(self):
        print("Tearing down...")
        self.fetcher.database = {}

    @patch("src.weather.requests.get")
    def test_fetch_weather_success(self, mock_get):
        """Test the fetch_weather method with a successful response."""
        # Arrange
        city = "New York"
        data = {"current_condition": [{"temp_C": "20"}]}
        mock_response = Mock()
        self.fetcher.database = data
        mock_response.json.return_value = data
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # fetch_weather now returns the data from the mock response instead of the API
        # like {"current_condition": [{"temp_C": "20"}]}
        result = self.fetcher.fetch_weather(city)

        # Assert
        self.assertEqual(result, data)