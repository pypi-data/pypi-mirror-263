##Path C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\runs.py

import logging


class RunManager:
    def __init__(self, api_client):
        """Initializes the RunManager with an API client.

        Args:
            api_client: An instance of APIClient that handles making API calls.
        """
        self.api_client = api_client
        self.logger = logging.getLogger(__name__)

    def create(self, thread_id, assistant_id, **kwargs):
        """Creates a Run for a Thread with the specified Assistant.

        Args:
            thread_id: The ID of the thread to create a run for.
            assistant_id: The ID of the assistant to use for the run.
            **kwargs: Additional parameters for the run creation.

        Returns:
            A dictionary containing the response data from the API call.
        """
        data = {"assistant_id": assistant_id, **kwargs}
        try:
            return self.api_client.make_api_call(f"threads/{thread_id}/runs", method="POST", data=data)
        except Exception as e:
            self.logger.error(f"Failed to create run for thread {thread_id} with assistant {assistant_id}: {e}")
            raise

    def retrieve(self, thread_id, run_id):
        """Retrieves details of a specific Run.

        Args:
            thread_id: The ID of the thread the run belongs to.
            run_id: The ID of the run to retrieve.

        Returns:
            A dictionary containing the response data from the API call.
        """
        try:
            return self.api_client.make_api_call(f"threads/{thread_id}/runs/{run_id}", method="GET")
        except Exception as e:
            self.logger.error(f"Failed to retrieve run {run_id} from thread {thread_id}: {e}")
            raise

    def list(self, thread_id, **kwargs):
        """Lists all runs for a specific thread, supporting pagination.

        Args:
            thread_id: The ID of the thread to list runs for.
            **kwargs: Parameters for filtering or pagination.

        Returns:
            A tuple containing a list of runs and the next page token, if any.
        """
        try:
            response = self.api_client.make_api_call(f"threads/{thread_id}/runs", method="GET", params=kwargs)

            runs = response.get('data')
            next_page_token = response.get('pagination', {}).get('next_page_token')

            return runs, next_page_token
        except Exception as e:
            self.logger.error(f"Failed to list runs for thread {thread_id}: {e}")
            raise