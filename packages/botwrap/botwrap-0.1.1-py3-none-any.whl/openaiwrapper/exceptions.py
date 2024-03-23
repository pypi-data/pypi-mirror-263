##Path C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\exceptions.py

class OpenAIRequestError(Exception):
    """Custom exception for handling OpenAI API request errors."""

    def __init__(self, message=None, status_code=None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message} (Status code: {self.status_code})"
