#!/usr/bin/env python3

import json

from brain_module import ChatGPT

"""
Retrieve the main word from the question.

Args:
- client_ref (str): The client reference to the OpenAI API.

Returns:
- str: The word identified from the OpenAI API.
"""
def get_main_word(client_ref):
    question = input("Ask me a question about something you want to learn about: ")
    detail_question = "Can you give the main word of the following question: " + question + "?"
    response = client_ref.request_openai(detail_question)
    return response.choices[0].message.content

"""
Retrieve the categorization of a given word.

Args:
- client_ref (str): The client reference to the OpenAI API.
- word (str): The main word to look up.

Returns:
- dict: The Dict structure of the categorization for the given word.
"""
def get_category(client_ref, word):
    question = "Can you give a categorization for the word {}?".format(word)
    detail_question = question + "Please give the response in a proper JSON format as follows: { topic: $, subtopic: $}"
    response = client_ref.request_openai(detail_question)
    return json.loads(response.choices[0].message.content)


"""
Make the initial configuration of the Bot.

Args:
- ref (str): The client reference to the OpenAI API.

Returns:
- str: The response content from the OpenAI API.
"""
def welcome_configuration(ref):
    print("Let's start...")
    # Retrieve main word from given question.
    word = get_main_word(ref)
    # Retrieve category from the given word.
    category = get_category(ref, word)
    # With the category

if  __name__ == "__main__":
    # Instantiate ChatGPT Class
    client_gpt = ChatGPT()

    # Configure Bot
    welcome_configuration(client_gpt)