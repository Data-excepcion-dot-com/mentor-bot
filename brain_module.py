#!/usr/bin/env python3

import os
from openai import OpenAI
from dotenv import load_dotenv

class ChatGPT:

    """A class to interact with OpenAI's ChatGPT model."""
    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Retrieve the OPENAI_API_KEY environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")

        # Instantiate Open AI client with OPENAI_API_KEY
        self.client = OpenAI(
            api_key=self.api_key,
        )

        # A constant to describe the role or behavior of the chatbot
        self.MAIN_ROLE = "This is the behavior of chatGPT"

    """
    Make a request to the OpenAI API.

    Args:
    - message (str): The message to be sent to the OpenAI API.
    - role (str, optional): The role associated with the message. Defaults to "system".

    Returns:
    - str: The response content from the OpenAI API.
    """
    def request_openai(self, message, role="system"):

        # Create a chat completion with the provided message and role
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": role, "content": message}],
        )

        # Return the complete API response
        return response