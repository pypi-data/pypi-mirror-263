##Path C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\assistants.py

import logging

class AssistantManager:
    def __init__(self, api_client):
        self.api_client = api_client
        self.logger = logging.getLogger(__name__)

    def _validate_tools_config(self, tools):
        if tools is not None and not all(isinstance(tool, dict) for tool in tools):
            raise ValueError("Tools configuration must be a list of dictionaries.")

    def create(self, name, instructions, model, tools=None, **kwargs):
        """Creates a new Assistant."""
        self._validate_tools_config(tools)
        data = {
            "name": name,
            "instructions": instructions,
            "model": model,
            "tools": tools or [],
            **kwargs
        }
        self.logger.info(f"Creating new assistant with name: {name}")
        return self.api_client.make_api_call("assistants", method="POST", data=data)

    def retrieve(self, assistant_id):
        """Retrieves a specific Assistant."""
        self.logger.info(f"Retrieving assistant with ID: {assistant_id}")
        return self.api_client.make_api_call(f"assistants/{assistant_id}", method="GET")

    def update(self, assistant_id, **kwargs):
        """Updates an existing Assistant."""
        if 'tools' in kwargs:
            self._validate_tools_config(kwargs['tools'])
        self.logger.info(f"Updating assistant with ID: {assistant_id}")
        return self.api_client.make_api_call(f"assistants/{assistant_id}", method="PATCH", data=kwargs)

    def delete(self, assistant_id):
        """Deletes a specific Assistant."""
        self.logger.info(f"Deleting assistant with ID: {assistant_id}")
        return self.api_client.make_api_call(f"assistants/{assistant_id}", method="DELETE")

    def list(self, **kwargs):
        """Lists all Assistants using query parameters for pagination or filtering."""
        self.logger.info("Listing assistants")
        return self.api_client.make_api_call("assistants", method="GET", params=kwargs)