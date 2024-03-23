##Path C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\messages.py

import logging

class MessageManager:
    def __init__(self, api_client):
        self.api_client = api_client
        self.logger = logging.getLogger(__name__)

    def create(self, thread_id, content, role="user", **kwargs):
        """Sends a new message to a thread, validating inputs before sending."""
        if not content.strip():
            raise ValueError("Message content cannot be empty.")
        if role not in ["user", "assistant"]:
            raise ValueError("Role must be either 'user' or 'assistant'.")
        
        data = {"content": content, "role": role, **kwargs}
        try:
            return self.api_client.make_api_call(f"threads/{thread_id}/messages", method="POST", data=data)
        except Exception as e:
            self.logger.error(f"Failed to create message in thread {thread_id}: {e}")
            raise

    def retrieve(self, thread_id, message_id):
        """Retrieves a specific message by ID from a thread."""
        try:
            return self.api_client.make_api_call(f"threads/{thread_id}/messages/{message_id}", method="GET")
        except Exception as e:
            self.logger.error(f"Failed to retrieve message {message_id} from thread {thread_id}: {e}")
            raise

    def delete(self, thread_id, message_id):
        """Deletes a specific message by ID from a thread."""
        try:
            return self.api_client.make_api_call(f"threads/{thread_id}/messages/{message_id}", method="DELETE")
        except Exception as e:
            self.logger.error(f"Failed to delete message {message_id} from thread {thread_id}: {e}")
            raise

    def list(self, thread_id, **kwargs):
        """Lists all messages in a specific thread, supporting pagination."""
        try:
            return self.api_client.make_api_call(f"threads/{thread_id}/messages", method="GET", params=kwargs)
        except Exception as e:
            self.logger.error(f"Failed to list messages in thread {thread_id}: {e}")
            raise