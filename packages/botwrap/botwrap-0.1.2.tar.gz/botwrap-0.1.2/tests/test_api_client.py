##Path of module being tested C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\api_client.py
##Path of test C:\Users\jamig\OneDrive\Desktop\botwrap\tests\test_api_client.py
import unittest
from unittest.mock import patch, MagicMock
from requests.exceptions import HTTPError, RequestException

# Importing the OpenAIAPIClient and OpenAIRequestError from the correct path
from openaiwrapper.api_client import OpenAIAPIClient, OpenAIRequestError

class TestOpenAIAPIClient(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.client = OpenAIAPIClient(api_key=self.api_key)

    @patch('openaiwrapper.api_client.requests.request')
    def test_successful_api_call(self, mock_request):
        # Mocking the successful API response
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = None
        mock_response.json.return_value = {"success": True}
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_request.return_value = mock_response

        response = self.client.make_api_call('test', 'GET')
        self.assertEqual(response, {"success": True})

    @patch('openaiwrapper.api_client.requests.request')
    def test_http_error_with_retry_success(self, mock_request):
        # Create a response mock to represent an HTTP error response
        mock_error_response = MagicMock()
        mock_error_response.status_code = 500
        mock_error_response.headers = {'Content-Type': 'application/json'}
        # This part ensures that when `raise_for_status` is called, an HTTPError is raised with a mock response attached
        http_error = HTTPError()
        http_error.response = mock_error_response
        mock_error_response.raise_for_status.side_effect = http_error

        # Mocking a successful response following the error
        mock_success_response = MagicMock()
        mock_success_response.raise_for_status.side_effect = None
        mock_success_response.json.return_value = {"success": True}
        mock_success_response.status_code = 200
        mock_success_response.headers = {'Content-Type': 'application/json'}

        mock_request.side_effect = [http_error, mock_success_response]

        response = self.client.make_api_call('test', 'POST')
        self.assertEqual(response, {"success": True})

    @patch('openaiwrapper.api_client.requests.request')
    def test_non_json_response_error(self, mock_request):
        # Mocking a response with a non-JSON content-type
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = None
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'text/html'}
        mock_request.return_value = mock_response

        with self.assertRaises(OpenAIRequestError):
            self.client.make_api_call('test', 'GET')

    @patch('openaiwrapper.api_client.requests.request')
    def test_http_error_no_retry_failure(self, mock_request):
        # Mocking consecutive HTTP errors to test failure without retry
        mock_error_response = MagicMock()
        mock_error_response.raise_for_status.side_effect = HTTPError(response=MagicMock(status_code=500))
        mock_error_response.status_code = 500
        mock_request.side_effect = [mock_error_response, mock_error_response, mock_error_response]

        with self.assertRaises(OpenAIRequestError):
            self.client.make_api_call('test', 'POST')

    @patch('openaiwrapper.api_client.requests.request')
    def test_request_exception_handling(self, mock_request):
        # Mocking a RequestException
        mock_request.side_effect = RequestException("Connection error")

        with self.assertRaises(OpenAIRequestError):
            self.client.make_api_call('test', 'GET')

if __name__ == '__main__':
    unittest.main()
