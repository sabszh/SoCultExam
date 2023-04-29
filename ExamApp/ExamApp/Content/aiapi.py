from ast import Try
import os
import openai
from datetime import datetime
import time



openai.api_key = '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'

history = []

def generateChatResponse(prompt,preprompt):
    global history
    # add the system message to the history
    system_message = {'role': 'system', 'content': preprompt}
    history.append(system_message)

    # Create a dictionary to represent the current question
    question = {'role': 'user', 'content': prompt}

    # Add the question to the history
    history.append(question)

    # add the system message to the history
    system_message = {'role': 'system', 'content': preprompt}
    history.append(system_message)

    # Add all the previous messages to the API request
    message = history.copy()

    # generate the response using the API
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message,
        max_tokens = 100)

    try:
        # Extract the answer from the API response
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')

        # add the system message with the answer to the history
        assistant_message = {'role': 'assistant', 'content': answer}
        history.append(assistant_message)
    except:
        # Handle API errors
        answer = 'Sorry, the API is down right now. Try again later.'

    Entry_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    with open('C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/chathistory.csv', 'a+') as myfile:
        myfile.write(
            str(User_ID) + ';' +
            str(Entry_time) + ';' +
            'AIA' + ';' + 
            str(abortion) + ';' +
            str(history) + ';'
            + '\n')
    # run the spreadsheet update script
    subprocess.run(['python', 'C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/spreadsheet.py'])

    return answer