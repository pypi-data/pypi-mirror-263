##Path C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\threads.py

import logging

class ThreadManager:
    def __init__(self, api_client):
        self.api_client = api_client
        self.logger = logging.getLogger(__name__)

    def _validate_thread_id(self, thread_id):
        if not thread_id:
            raise ValueError("Thread ID must be provided and cannot be empty.")

    def create(self, **kwargs):
        """Creates a new thread."""
        self.logger.info("Creating new thread")
        return self.api_client.make_api_call("threads", method="POST", data=kwargs)

    def retrieve(self, thread_id):
        """Retrieves a specific thread by ID."""
        self._validate_thread_id(thread_id)
        self.logger.info(f"Retrieving thread with ID: {thread_id}")
        return self.api_client.make_api_call(f"threads/{thread_id}", method="GET")

    def update(self, thread_id, **kwargs):
        """Updates a specific thread."""
        self._validate_thread_id(thread_id)
        self.logger.info(f"Updating thread with ID: {thread_id}")
        return self.api_client.make_api_call(f"threads/{thread_id}", method="PATCH", data=kwargs)

    def delete(self, thread_id):
        """Deletes a specific thread by ID."""
        self._validate_thread_id(thread_id)
        self.logger.info(f"Deleting thread with ID: {thread_id}")
        return self.api_client.make_api_call(f"threads/{thread_id}", method="DELETE")

    def list(self, **kwargs):
        """Lists all threads, with optional filtering parameters."""
        self.logger.info("Listing all threads")
        return self.api_client.make_api_call("threads", method="GET", params=kwargs)

    # Example of a utility method
    def list_all_threads(self):
        """Utility method to fetch and return all threads, handling pagination automatically."""
        all_threads = []
        page = self.list()
        all_threads.extend(page.get('data', []))
        
        while page.get('pagination', {}).get('has_more', False):
            next_page_token = page.get('pagination', {}).get('next_page_token')
            page = self.list(after=next_page_token)
            all_threads.extend(page.get('data', []))
        
        return all_threads