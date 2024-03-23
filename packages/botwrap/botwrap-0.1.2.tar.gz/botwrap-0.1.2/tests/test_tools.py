##Path of module being tested C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\tools.py
##Path of test C:\Users\jamig\OneDrive\Desktop\botwrap\tests\test_tools.py

import logging

class ToolsManager:
    def __init__(self, api_client):
        """Initializes the ToolsManager with an API client.

        Args:
            api_client: An instance of OpenAIAPIClient that handles making API calls.
        """
        self.api_client = api_client
        self.logger = logging.getLogger(__name__)

    def update_tools(self, assistant_id, tools_config):
        """Updates the tools configuration for a specific Assistant.

        Args:
            assistant_id: The ID of the Assistant to update tools for.
            tools_config: A list of dictionaries representing the tools configuration.

        Returns:
            A dictionary containing the API response.

        Raises:
            ValueError: If the tools_config is not valid.
            Exception: If an error occurs while making the API request.
        """
        if not isinstance(tools_config, list) or not all(isinstance(tool, dict) for tool in tools_config):
            raise ValueError("tools_config must be a list of dictionaries.")

        data = {"tools": tools_config}
        try:
            return self.api_client.make_api_call(f"assistants/{assistant_id}", method="PATCH", data=data)
        except Exception as e:
            self.logger.error(f"Failed to update tools for assistant {assistant_id}: {e}")
            raise

    def retrieve_tool_configuration(self, assistant_id):
        """Retrieves the current tool configuration for a specific assistant.

        Args:
            assistant_id: The unique identifier for the assistant.

        Returns:
            A dictionary containing the current tool configuration.
        """
        try:
            response = self.api_client.make_api_call(f"assistants/{assistant_id}", method="GET")
            return response.get('tools', [])
        except Exception as e:
            self.logger.error(f"Failed to retrieve tool configuration for assistant {assistant_id}: {e}")
            raise

    def remove_tool(self, assistant_id, tool_type):
        """Removes a specific tool based on tool type from an assistant's configuration.

        Args:
            assistant_id: The unique identifier for the assistant.
            tool_type: The type of the tool to be removed.

        Returns:
            A dictionary containing the updated tool configuration.
        """
        current_tools = self.retrieve_tool_configuration(assistant_id)
        updated_tools = [tool for tool in current_tools if tool.get('type') != tool_type]

        return self.update_tools(assistant_id, updated_tools)

    def submit_tool_outputs(self, thread_id, run_id, tool_outputs):
        """Submits tool outputs for a specific run to continue processing.

        Args:
            thread_id: The unique identifier for the thread related to the run.
            run_id: The unique identifier for the run to submit tool outputs for.
            tool_outputs: Outputs for each tool call.

        Returns:
            A dictionary with the updated run object after submitting tool outputs.
        """
        data = {"tool_outputs": tool_outputs}
        try:
            return self.api_client.make_api_call(f"threads/{thread_id}/runs/{run_id}/submit_tool_outputs", method="POST", data=data)
        except Exception as e:
            self.logger.error(f"Failed to submit tool outputs for run {run_id} in thread {thread_id}: {e}")
            raise