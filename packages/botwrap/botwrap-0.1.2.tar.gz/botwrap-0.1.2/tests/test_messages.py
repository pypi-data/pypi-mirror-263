##Path of module being tested C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\messages.py
##Path of test C:\Users\jamig\OneDrive\Desktop\botwrap\tests\test_messages.py

import unittest
from openaiwrapper.messages import MessageManager
from unittest.mock import patch, MagicMock

class TestMessageManager(unittest.TestCase):
    def setUp(self):
        self.mock_api_client = MagicMock()
        self.message_manager = MessageManager(api_client=self.mock_api_client)

    @patch('openaiwrapper.messages.logging.Logger.error')
    def test_create_message(self, mock_log_error):
        thread_id = "test_thread"
        content = "Test message"
        role = "user"
        self.message_manager.create(thread_id=thread_id, content=content, role=role)
        self.mock_api_client.make_api_call.assert_called_once_with(
            f"threads/{thread_id}/messages",
            method="POST",
            data={"content": content, "role": role}
        )

    @patch('openaiwrapper.messages.logging.Logger.error')
    def test_retrieve_message(self, mock_log_error):
        thread_id = "test_thread"
        message_id = "test_message"
        self.message_manager.retrieve(thread_id=thread_id, message_id=message_id)
        self.mock_api_client.make_api_call.assert_called_once_with(
            f"threads/{thread_id}/messages/{message_id}",
            method="GET"
        )

    @patch('openaiwrapper.messages.logging.Logger.error')
    def test_delete_message(self, mock_log_error):
        thread_id = "test_thread"
        message_id = "test_message"
        self.message_manager.delete(thread_id=thread_id, message_id=message_id)
        self.mock_api_client.make_api_call.assert_called_once_with(
            f"threads/{thread_id}/messages/{message_id}",
            method="DELETE"
        )

    @patch('openaiwrapper.messages.logging.Logger.error')
    def test_list_messages(self, mock_log_error):
        thread_id = "test_thread"
        self.message_manager.list(thread_id=thread_id)
        self.mock_api_client.make_api_call.assert_called_once_with(
            f"threads/{thread_id}/messages",
            method="GET",
            params={}
        )

    def test_create_message_with_empty_content_raises_value_error(self):  # Improved method name
        thread_id = "test_thread"
        content = " "
        with self.assertRaises(ValueError):
            self.message_manager.create(thread_id=thread_id, content=content)

    def test_create_message_with_invalid_role_raises_value_error(self):  # Improved method name
        thread_id = "test_thread"
        content = "Valid content"
        role = "invalid_role"
        with self.assertRaises(ValueError):
            self.message_manager.create(thread_id=thread_id, content=content, role=role)

if __name__ == '__main__':
    unittest.main()
