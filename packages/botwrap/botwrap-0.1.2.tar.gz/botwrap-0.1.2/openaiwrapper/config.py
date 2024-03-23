##Path C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\config.py

import os

# OpenAI API Key
# IMPORTANT: Never hard-code your API keys in your code. Instead, use environment variables
# or other methods to keep them secure.
API_KEY = os.getenv("OPENAI_API_KEY")


# Base URL for the OpenAI API
BASE_URL = "https://api.openai.com/v1"

# Configuration for tools (if any specific configurations are needed)
TOOLS = {
    # Example tool configuration (adjust or remove according to your actual tools and needs)
    "code_interpreter": {
        "enabled": True,
        "config_key": "example_value"
    }
}

# Any other global configuration variables can be added here
