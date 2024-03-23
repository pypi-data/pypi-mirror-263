##Path C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\utils.py

import logging
from typing import Any, Dict, List
from requests.models import Response
from datetime import datetime
from .exceptions import OpenAIRequestError

# Set up logging
logger = logging.getLogger(__name__)

def log_api_call(method: str, url: str, data: Dict[str, Any] = None, status_code: int = None, duration: float = None) -> None:
    """Logs details of an API call including the request method, URL, optional data, status code, and duration."""
    logger.info(f"API Request - Method: {method}, URL: {url}, Status Code: {status_code}, Duration: {duration} seconds, Data: {data if data else 'No Data'}")

def handle_http_error(response: Response) -> None:
    """Handles HTTP errors by raising an OpenAIRequestError with detailed message."""
    try:
        json_response = response.json()
        error_message = json_response.get('error', {}).get('message', 'No error message provided.')
    except ValueError:  # JSON decoding failed
        error_message = "Failed to decode JSON response."
    raise OpenAIRequestError(message=error_message, status_code=response.status_code)

def handle_api_error(response: Dict[str, Any]) -> None:
    """Logs and raises API errors in a consistent format."""
    error_message = response.get('error', {}).get('message', 'Unknown error.')
    error_type = response.get('error', {}).get('type', 'APIError')
    logger.error(f"{error_type}: {error_message}")
    raise Exception(f"{error_type}: {error_message}")

def validate_response_content_type(response: Response, expected_content_type: str) -> None:
    """Validates the Content-Type of the response."""
    content_type = response.headers.get('Content-Type', '')
    if expected_content_type not in content_type:
        raise ValueError(f"Unexpected Content-Type: {content_type}, expected {expected_content_type}.")

def format_data_for_request(data: Dict[str, Any]) -> Dict[str, Any]:
    """Formats data to be sent in an API request."""
    formatted_data = {k: v for k, v in data.items() if v is not None}
    return formatted_data

def validate_list_of_dicts(items: List[Dict[str, Any]], required_keys: List[str]) -> bool:
    """Validates that each dictionary in a list contains all required keys."""
    return all(all(key in item for key in required_keys) for item in items)

def datetime_to_iso(dt: datetime) -> str:
    """Converts a datetime object to an ISO formatted string."""
    return dt.isoformat()

def sanitize_input(input_string: str) -> str:
    """Sanitizes input strings to remove potentially harmful characters or patterns."""
    # Implement specific sanitization rules as needed
    return input_string.strip()

def fetch_all_pages(fetch_page_function, **params) -> List[Dict[str, Any]]:
    """Utility function to fetch all pages of a paginated API response."""
    all_items = []
    page_token = None
    
    while True:
        response, next_page_token = fetch_page_function(page_token=page_token, **params)
        all_items.extend(response)
        if not next_page_token:
            break
        page_token = next_page_token
    
    return all_items