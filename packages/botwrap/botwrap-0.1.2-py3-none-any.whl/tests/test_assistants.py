##Path of module being tested C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\assistants.py
##Path of test C:\Users\jamig\OneDrive\Desktop\botwrap\tests\test_assistants.py

import unittest
from unittest.mock import patch, MagicMock
from openaiwrapper.assistants import AssistantManager


class TestAssistantManager(unittest.TestCase):
    def setUp(self):
        self.mock_api_client = MagicMock()
        self.assistant_manager = AssistantManager(api_client=self.mock_api_client)

    @patch('logging.Logger.info')
    def test_create_assistant(self, mock_log_info):
        self.assistant_manager.create(
            name="Test Assistant",
            instructions="Help users with their questions.",
            model="gpt-3.5-turbo",
            tools=[{"type": "retrieval"}]
        )
        self.mock_api_client.make_api_call.assert_called_once_with(
            "assistants",
            method="POST",
            data={
                "name": "Test Assistant",
                "instructions": "Help users with their questions.",
                "model": "gpt-3.5-turbo",
                "tools": [{"type": "retrieval"}]
            }
        )
        mock_log_info.assert_called()

    @patch('logging.Logger.info')
    def test_retrieve_assistant(self, mock_log_info):
        assistant_id = "test_id"
        self.assistant_manager.retrieve(assistant_id)
        self.mock_api_client.make_api_call.assert_called_once_with(
            f"assistants/{assistant_id}",
            method="GET"
        )
        mock_log_info.assert_called()

    @patch('logging.Logger.info')
    def test_update_assistant(self, mock_log_info):
        assistant_id = "test_id"
        self.assistant_manager.update(
            assistant_id,
            name="Updated Test Assistant"
        )
        self.mock_api_client.make_api_call.assert_called_once_with(
            f"assistants/{assistant_id}",
            method="PATCH",
            data={"name": "Updated Test Assistant"}
        )
        mock_log_info.assert_called()

    @patch('logging.Logger.info')
    def test_delete_assistant(self, mock_log_info):
        assistant_id = "test_id"
        self.assistant_manager.delete(assistant_id)
        self.mock_api_client.make_api_call.assert_called_once_with(
            f"assistants/{assistant_id}",
            method="DELETE"
        )
        mock_log_info.assert_called()

    @patch('logging.Logger.info')
    def test_list_assistants(self, mock_log_info):
        self.assistant_manager.list()
        self.mock_api_client.make_api_call.assert_called_once_with(
            "assistants",
            method="GET",
            params={}
        )
        mock_log_info.assert_called()

    def test_validate_tools_config(self):
        with self.assertRaises(ValueError):
            self.assistant_manager.create(
                name="Invalid Tools Assistant",
                instructions="This assistant has invalid tools config.",
                model="gpt-3.5-turbo",
                tools="Not a list of dictionaries"  # Incorrect tools format
            )

if __name__ == '__main__':
    unittest.main()