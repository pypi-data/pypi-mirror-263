##Path C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\api_client.py
        
import requests
import logging
from requests.exceptions import HTTPError, RequestException
from time import sleep

# Define constants for readability
HTTP_SERVER_ERROR_START = 500
HTTP_SERVER_ERROR_END = 600
DEFAULT_RETRY_ATTEMPTS = 3
CONTENT_TYPE_JSON = 'application/json'

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class OpenAIRequestError(Exception):
    """Exception raised for errors in making API requests to OpenAI."""
    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class OpenAIAPIClient:
    def __init__(self, api_key: str, retry_attempts: int = DEFAULT_RETRY_ATTEMPTS):
        """Initializes an OpenAIAPIClient with an API key and configurable number of retry attempts.

        Args:
            api_key: API key for authenticating with OpenAI's services.
            retry_attempts: Number of times to retry a request after server errors (5xx).
        """
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1"
        self.retry_attempts = retry_attempts

    def _make_request(self, method: str, url: str, headers: dict, data: dict = None, files: dict = None, params: dict = None):
        """Internal function to make the actual request with retry logic.

        Args:
            method: The HTTP method to use ('GET', 'POST', etc.).
            url: The full URL for the request.
            headers: Headers to include in the request.
            data: Data to be sent in the body of the request.
            files: Files to be sent in the body of the request.
            params: URL parameters to be sent in the request.

        Returns:
            A dictionary containing the JSON response.

        Raises:
            OpenAIRequestError: An error occurred while making the API request.
        """
        headers["OpenAI-Beta"] = "assistants=v1"  # Add this line to include the required header
        for attempt in range(self.retry_attempts):
            try:
                if files:
                    headers.pop("Content-Type", None)  # Let requests handle multipart/form-data
                response = requests.request(method, url, headers=headers, json=data, files=files, params=params)
                response.raise_for_status()

                if CONTENT_TYPE_JSON in response.headers.get('Content-Type', ''):
                    return response.json()
                else:
                    raise OpenAIRequestError("Response content type is not JSON.", status_code=response.status_code)

            except HTTPError as e:
                if HTTP_SERVER_ERROR_START <= e.response.status_code < HTTP_SERVER_ERROR_END and attempt < self.retry_attempts - 1:
                    sleep(2 ** attempt)  # Exponential backoff
                else:
                    logger.error(f"HTTPError: {e.response.status_code}, Message: {e.response.text}")
                    raise OpenAIRequestError(e.response.text, status_code=e.response.status_code)
            except RequestException as e:
                logger.error(f"Request exception: {str(e)}")
                raise OpenAIRequestError(f"Failed to make a request to OpenAI API: {str(e)}", status_code=0)


    def make_api_call(self, endpoint: str, method: str = "GET", data: dict = None, files: dict = None, params: dict = None) -> dict:
        """Makes an API call to the specified endpoint.

        Args:
            endpoint: The endpoint of the API to interact with.
            method: The HTTP method to use ('GET', 'POST', etc.).
            data: Data to send in the body of the request.
            files: Files to send in the body of the request.
            params: URL parameters to send in the request.

        Returns:
            A dictionary containing the JSON response.

        Raises:
            OpenAIRequestError: An error occurred while making the API request.
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        if not files:
            headers["Content-Type"] = CONTENT_TYPE_JSON

        url = f"{self.base_url}/{endpoint}"

        return self._make_request(method, url, headers, data, files, params)