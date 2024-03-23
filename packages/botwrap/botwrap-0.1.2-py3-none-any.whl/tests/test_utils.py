##Path of module being tested C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\utils.py
##Path of test C:\Users\jamig\OneDrive\Desktop\botwrap\tests\test_utils.py

import unittest
from unittest.mock import patch, MagicMock  # Ensure patch is imported
from requests.models import Response
from openaiwrapper.exceptions import OpenAIRequestError
from openaiwrapper import utils
from datetime import datetime


class TestUtils(unittest.TestCase):

    def test_log_api_call(self):
        # This test would verify that logging occurs, which might require a more intricate setup to capture log outputs.
        pass

    @patch.object(utils, 'Response', autospec=True)
    def test_handle_http_error_with_valid_json(self, mock_response):
        mock_response.json.return_value = {'error': {'message': 'Test error message'}}
        mock_response.status_code = 400
        with self.assertRaises(OpenAIRequestError) as context:
            utils.handle_http_error(mock_response)
        self.assertEqual(context.exception.message, 'Test error message')
        self.assertEqual(context.exception.status_code, 400)

    @patch.object(utils, 'Response', autospec=True)
    def test_handle_http_error_with_invalid_json(self, mock_response):
        mock_response.json.side_effect = ValueError
        mock_response.status_code = 400
        with self.assertRaises(OpenAIRequestError) as context:
            utils.handle_http_error(mock_response)
        self.assertEqual(context.exception.message, 'Failed to decode JSON response.')
        self.assertEqual(context.exception.status_code, 400)

    def test_validate_response_content_type_with_expected_type(self):
        mock_response = MagicMock(spec=Response)
        mock_response.headers = {'Content-Type': 'application/json'}
        try:
            utils.validate_response_content_type(mock_response, 'application/json')
        except ValueError:
            self.fail("validate_response_content_type raised ValueError unexpectedly!")

    def test_validate_response_content_type_with_unexpected_type(self):
        mock_response = MagicMock(spec=Response)
        mock_response.headers = {'Content-Type': 'text/html'}
        with self.assertRaises(ValueError):
            utils.validate_response_content_type(mock_response, 'application/json')

    def test_format_data_for_request(self):
        data = {'key1': 'value1', 'key2': None}
        expected = {'key1': 'value1'}
        result = utils.format_data_for_request(data)
        self.assertEqual(result, expected)

    def test_validate_list_of_dicts_with_required_keys(self):
        items = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value1', 'key2': 'value2'}]
        required_keys = ['key1', 'key2']
        self.assertTrue(utils.validate_list_of_dicts(items, required_keys))

    def test_validate_list_of_dicts_missing_required_keys(self):
        items = [{'key1': 'value1'}, {'key1': 'value1', 'key2': 'value2'}]
        required_keys = ['key1', 'key2']
        self.assertFalse(utils.validate_list_of_dicts(items, required_keys))

    def test_datetime_to_iso(self):
        dt = datetime(2020, 1, 1)
        expected = '2020-01-01T00:00:00'
        result = utils.datetime_to_iso(dt)
        self.assertEqual(result, expected)

    def test_sanitize_input(self):
        input_string = ' test string '
        expected = 'test string'
        result = utils.sanitize_input(input_string)
        self.assertEqual(result, expected)

    def test_fetch_all_pages(self):
        def mock_fetch_page_function(page_token=None, **params):
            if page_token == 'token_1':
                return [{'item': 2}], None
            return [{'item': 1}], 'token_1'

        result = utils.fetch_all_pages(mock_fetch_page_function)
        expected = [{'item': 1}, {'item': 2}]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
