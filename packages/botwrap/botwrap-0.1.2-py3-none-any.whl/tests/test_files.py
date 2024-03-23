##Path of module being tested C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\files.py
##Path of test C:\Users\jamig\OneDrive\Desktop\botwrap\tests\test_files.py

import os
import requests
import logging
from openaiwrapper.api_client import OpenAIAPIClient, OpenAIRequestError


class FileOperationError(Exception):
    """Custom exception for file operation errors."""
    pass

class FileManager:
    def __init__(self, api_client: OpenAIAPIClient):
        self.api_client = api_client
        self.logger = logging.getLogger(__name__)

    def upload_file(self, file_path: str):
        """Uploads a file to the OpenAI API.

        Args:
            file_path: Path to the file to be uploaded.

        Returns:
            The API response for the file upload.

        Raises:
            FileOperationError: If the file cannot be uploaded.
        """
        self.validate_file_for_upload(file_path)
        url = f"{self.api_client.base_url}/files"
        headers = {"Authorization": f"Bearer {self.api_client.api_key}"}
        files = {"file": open(file_path, "rb")}
        try:
            response = requests.post(url, headers=headers, files=files)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            self.logger.error(f"HTTPError during file upload: {e}")
            raise FileOperationError(f"HTTPError during file upload: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error during file upload: {e}")
            raise FileOperationError(f"Unexpected error during file upload: {e}")

    def delete_file(self, file_id: str):
        """Deletes a specific file by ID.

        Args:
            file_id: ID of the file to delete.

        Returns:
            The API response for the file deletion.
        """
        try:
            return self.api_client.make_api_call(f"files/{file_id}", method="DELETE")
        except OpenAIRequestError as e:
            raise FileOperationError(f"Failed to delete file {file_id}: {e}")

    def get_file_content(self, file_id: str):
        """Fetches and returns the content of a specified file.

        Args:
            file_id: ID of the file whose content is to be fetched.

        Returns:
            The content of the file.
        """
        try:
            response = self.api_client.make_api_call(f"files/{file_id}/content", method="GET", stream=True)
            return response.content
        except OpenAIRequestError as e:
            raise FileOperationError(f"Failed to fetch content for file {file_id}: {e}")

    def list_files(self, **kwargs):
        """Lists files with optional filtering and sorting.

        Args:
            **kwargs: Optional arguments that `list_files` function accepts.

        Returns:
            The API response for listing files.
        """
        params = {key: value for key, value in kwargs.items() if value is not None}
        try:
            return self.api_client.make_api_call("files", method="GET", params=params)
        except OpenAIRequestError as e:
            raise FileOperationError(f"Failed to list files: {e}")

    def validate_file_for_upload(self, file_path: str):
        """Validates the file against OpenAI's upload constraints before uploading.

        Args:
            file_path: Path to the file to be validated.

        Raises:
            ValueError: If the file does not meet the criteria for upload.
        """
        max_file_size = 52428800  # 50 MB for example
        file_size = os.path.getsize(file_path)
        if file_size > max_file_size:
            raise ValueError("File exceeds the maximum allowed size.")
        # Additional validations can be added here.