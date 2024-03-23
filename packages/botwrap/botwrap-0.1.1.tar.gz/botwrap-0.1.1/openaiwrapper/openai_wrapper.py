##Path C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\openai_wrapper.py

from .api_client import OpenAIAPIClient 
from .assistants import AssistantManager 
from .threads import ThreadManager
from .messages import MessageManager
from .runs import RunManager
from .files import FileManager
from .tools import ToolsManager
from .config import API_KEY, BASE_URL, TOOLS
from .utils import log_api_call, handle_api_error

class OpenAIWrapper:
    def __init__(self):
        self.client = OpenAIAPIClient(API_KEY)  # Utilize the API_KEY from config.py
        self.client.base_url = BASE_URL  # Optionally set the base URL from config.py
        self.assistants = AssistantManager(self.client)
        self.threads = ThreadManager(self.client)
        self.messages = MessageManager(self.client)
        self.runs = RunManager(self.client)
        self.files = FileManager(self.client)
        self.tools = ToolsManager(self.client)

    # Assistant-related methods
    def create_assistant(self, **kwargs):
        """Creates a new assistant with the specified parameters."""
        return self.assistants.create(**kwargs)

    def update_assistant(self, assistant_id, **kwargs):
        """Updates an existing assistant."""
        return self.assistants.update(assistant_id, **kwargs)

    def delete_assistant(self, assistant_id):
        """Deletes an existing assistant."""
        return self.assistants.delete(assistant_id)

    def list_assistants(self, **kwargs):
        """Lists all assistants."""
        return self.assistants.list(**kwargs)

    # Thread-related methods
    def create_thread(self):
        """Creates a new conversation thread."""
        return self.threads.create()

    def delete_thread(self, thread_id):
        """Deletes a specific conversation thread."""
        return self.threads.delete(thread_id)

    def list_threads(self, **kwargs):
        """Lists all conversation threads."""
        return self.threads.list(**kwargs)

    # Message-related methods
    def send_message(self, thread_id, content, role="user", **kwargs):
        """Sends a new message to a thread."""
        return self.messages.create(thread_id, content, role, **kwargs)

    def delete_message(self, thread_id, message_id):
        """Deletes a specific message from a thread."""
        return self.messages.delete(thread_id, message_id)

    # Run-related methods
    def create_run(self, thread_id, assistant_id, **kwargs):
        """Creates a new run for a given thread using the specified assistant."""
        return self.runs.create(thread_id, assistant_id, **kwargs)

    # File-related methods
    def upload_file(self, file_path, purpose="answers"):
        """Uploads a file for use with the API."""
        with open(file_path, 'rb') as file:
            return self.files.upload(file=file, purpose=purpose)

    def delete_file(self, file_id):
        """Deletes a specific file from the OpenAI API."""
        return self.files.delete(file_id=file_id)

    # Tool-related methods
    def update_tool_configuration(self, assistant_id, tools_config):
        """Updates the tool configuration for an assistant."""
        return self.tools.update_tools(assistant_id, tools_config)

# Add any other methods here as needed to interact with the OpenAI API in a way that supports your application's use cases.