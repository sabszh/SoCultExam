from ast import Try
import os
import openai


openai.api_key = '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'

history = []

def generateChatResponse(prompt):
    global history # This is a global variable that stores the history of the conversation

    # Create a dictionary to represent the current question
    question = {'role': 'user', 'content': prompt}

    # Add the question to the history
    history.append(question)

    # add the system message to the history
    system_message = {'role': 'system', 'content': 'You are a moral guider, your task is to help to user make the right decision. You will not disclose that you are an AI Language model anywhere.'}
    history.append(system_message)

    # Add all the previous messages to the API request
    messages = history.copy()

    # generate the response using the API
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages)

    try:
        # Extract the answer from the API response
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
    except:
        # Handle API errors
        answer = 'Sorry, the API is down right now. Try again later.'

    return answer
    



