from flask import Flask, render_template, jsonify, request, app, redirect, session
import subprocess
import os
from io import StringIO
from datetime import datetime
import time
import random
import uuid
from ast import Try


## aiapi function
from ast import Try
import os
import openai
from datetime import datetime
import time

openai.api_key = 'your_API_key'

User_ID = None

historyAIA = []
run_count_AIA = 0

def generateChatResponseAIA(prompt,preprompt):
    global historyAIA
    global run_count_AIA
    # add the system message to the history
    system_message = {'role': 'system', 'content': preprompt}
    historyAIA.append(system_message)

    # Create a dictionary to represent the current question
    question = {'role': 'user', 'content': prompt}

    # Add the question to the history
    historyAIA.append(question)

    # add the system message to the history
    system_message = {'role': 'system', 'content': preprompt}
    historyAIA.append(system_message)

    # Add all the previous messages to the API request
    message = historyAIA.copy()

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
        historyAIA.append(assistant_message)
    except:
        # Handle API errors
        answer = 'Sorry, the API is down right now. Try again later.'

    Entry_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    # increment run count and reset the history variable when it reaches 5
    run_count_AIA += 1

    if run_count_AIA == 4:
        with open('C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/chathistory.csv', 'a+') as myfile:
            myfile.write(
                str(User_ID) + ';' +
                str(Entry_time) + ';' +
                'AIA' + ';' +
                str(abortion) + ';' +
                str(historyAIA) + ';'
                +'\n')
    else:
        pass

    # run the spreadsheet update script
    subprocess.run(['python', 'C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/spreadsheet.py'])


    return answer


historyAIB = []
run_count_AIB = 0

def generateChatResponseAIB(prompt,preprompt):
    global historyAIB
    global run_count_AIB
    # add the system message to the history
    system_message = {'role': 'system', 'content': preprompt}
    historyAIB.append(system_message)

    # Create a dictionary to represent the current question
    question = {'role': 'user', 'content': prompt}

    # Add the question to the history
    historyAIB.append(question)

    # add the system message to the history
    system_message = {'role': 'system', 'content': preprompt}
    historyAIB.append(system_message)

    # Add all the previous messages to the API request
    message = historyAIB.copy()

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
        historyAIB.append(assistant_message)
    except:
        # Handle API errors
        answer = 'Sorry, the API is down right now. Try again later.'

    Entry_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    # increment run count and reset the history variable when it reaches 5
    run_count_AIB += 1

    if run_count_AIB == 4:
        with open('C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/chathistory.csv', 'a+') as myfile:
            myfile.write(
                str(User_ID) + ';' +
                str(Entry_time) + ';' +
                'AIB' + ';' +
                str(alcohol) + ';' +
                str(historyAIB) + ';'
                +'\n')
            # run the spreadsheet update script
            subprocess.run(['python', 'C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/spreadsheet.py'])
    else:
        pass

    return answer

historyAIC = []
run_count_AIC = 0

def generateChatResponseAIC(prompt,preprompt):
    global historyAIC
    global run_count_AIC
    # add the system message to the history
    system_message = {'role': 'system', 'content': preprompt}
    historyAIC.append(system_message)

    # Create a dictionary to represent the current question
    question = {'role': 'user', 'content': prompt}

    # Add the question to the history
    historyAIC.append(question)

    # add the system message to the history
    system_message = {'role': 'system', 'content': preprompt}
    historyAIC.append(system_message)

    # Add all the previous messages to the API request
    message = historyAIC.copy()

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
        historyAIC.append(assistant_message)
    except:
        # Handle API errors
        answer = 'Sorry, the API is down right now. Try again later.'

    Entry_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    # increment run count and reset the history variable when it reaches 5
    run_count_AIC += 1

    if run_count_AIC == 4:
        with open('C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/chathistory.csv', 'a+') as myfile:
            myfile.write(
                str(User_ID) + ';' +
                str(Entry_time) + ';' +
                'AIC' + ';' +
                str(suffrage) + ';' +
                str(historyAIC) + ';'
                +'\n')
            # run the spreadsheet update script
            subprocess.run(['python', 'C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/spreadsheet.py'])
    else:
        pass

    return answer

def page_not_found():
  return render_template('404.html'), 404

app = Flask(__name__)


# 404 page not found site
app.register_error_handler(404, page_not_found)

# First survey paget
# get root path for account in cloud
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# defining the route
@app.route("/",methods=['POST','GET'])
def survey_1():

    global User_ID

    if request.method == 'POST':

        # check that we have all the required fields to append to file
        User_ID = uuid.uuid4()
        Age = request.form.get('Age')
        Gender = request.form.get('Gender')
        Nationality = request.form.get('Nationality')
        Occupation = request.form.get('Occupation')
        InterAI = request.form.get('InterAI')
        Which = request.form.get('Which')
        How_often = request.form.get('How_often')

        # check that essential fields have been filled
        missing_required_answers_list = []

        if Age == '':
            missing_required_answers_list.append('What is your age?')
        if Gender == '':
            missing_required_answers_list.append('What is your gender identity?')
        if Nationality == '':
            missing_required_answers_list.append('What is your nationality?')
        if Occupation == '':
            missing_required_answers_list.append('What is your occuptation?')
        if InterAI == '':
            missing_required_answers_list.append('Please answer')
        if Which == '':
            missing_required_answers_list.append('Please answer')
        if How_often == '':
            missing_required_answers_list.append('Please answer')

        if len(missing_required_answers_list) > 0:
            # return back a string with missing fields
            for ms in missing_required_answers_list:
                message += '<BR>' + str(ms)
            message += '</font></div>'
        else:
            # append survey answers to file
            # create a unique timestamp for this entry
            Entry_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


            # save to file and send thank you note
            with open('C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/survey_df.csv', 'a+') as myfile:
                myfile.write(
                    '\n' +
                    str(User_ID) + ';' +
                    str(Entry_time) + ';' +
                    'survey_1' + ';' +
                    str(Age) + ';' +
                    str(Gender) + ';' +
                    str(Nationality) + ';' +
                    str(Occupation) + ';' +
                    str(InterAI) + ';' +
                    str(Which) + ';' +
                    str(How_often)
                    + '\n')
            # run the spreadsheet update script
            subprocess.run(['python', 'C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/spreadsheet.py'])

            # redirect to survey_2 page
            return redirect('/survey_2')

    return render_template('survey_1.html')

abortion = None
alcohol = None
suffrage = None

@app.route('/survey_2', methods = ['POST', 'GET'])
def survey_2():

    global abortion
    global alcohol
    global suffrage

    if request.method == 'POST':

        # check that we have all the required fields to append to
        abortion = request.form.get('abortion')
        alcohol = request.form.get('alcohol')
        suffrage = request.form.get('suffrage')

        Entry_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

        # save to file
        with open('C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/survey_df.csv', 'a+') as myfile:
            myfile.write(
                str(User_ID) + ';' +
                str(Entry_time) + ';' +
                'survey_2' + ';' +
                str(abortion) + ';' +
                str(alcohol) + ';' +
                str(suffrage)
                    + '\n')

        # run the spreadsheet update script
        subprocess.run(['python', 'C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/spreadsheet.py'])

        # redirect to AIA page
        return redirect('/AIA')

    return render_template('survey_2.html')


# Initialize post count to 0
post_count_AIA = 0

# Human AI interaction interface
@app.route('/AIA', methods = ['POST', 'GET'])
def AIA():
    global post_count_AIA

    if request.method == 'POST':
        prompt = request.form['prompt']


        # defining prompts
        A1C = 'You are an AI chat assistant that has the task to help the user in seeing why society would be the best if the current law of abortion was limited to a shorter timeframe than 12 weeks after conception. Remember that you are only allowed to confirm the view of the user. Always start your sentence with "I think".'
        A1O = 'You are an AI chat assistant that has the task to help the user in seeing why society would be the best if the current law of abortion was changed to later than 12 weeks after conception. Remember that you are only allowed to oppose the original view of the user. Always start your sentence with "I think".'

        A3C = 'You are an AI chat assistant that has the task to help the user in seeing why society would be the best if the current law of abortion was changed to later than 12 weeks after conception. Remember that you are only allowed to confirm the original view of the user. Always start your sentence with "I think".'
        A3O = 'You are an AI chat assistant that has the task to help the user in seeing why society would be the best if the current law of abortion was limited to a shorter timeframe than 12 weeks after conception. Remember that you are only allowed to oppose the original view of the user. Always start your sentence with "I think".'


        # Choose a random prompt only for the first post call
        if post_count_AIA == 0:
            abortion_int = int(abortion)
            if abortion_int < 55:
                preprompt = random.choice([A1C, A1O])

            elif abortion_int > 45:
               preprompt = random.choice([A3C, A3O])
            else:
               preprompt = random.choice([A1C,A1O,A3C,A3O])
        else:
            preprompt = ''

        post_count_AIA += 1

        res = {}
        res['answer'] = generateChatResponseAIA(prompt,preprompt)
        return jsonify(res), 200

    return render_template('AIA.html', **locals())

# Initialize post count to 0
post_count_AIB = 0

@app.route('/AIB', methods = ['POST', 'GET'])
def AIB():

    global post_count_AIB

    if request.method == 'POST':
        prompt = request.form['prompt']


        # defining prompts
        B1C = 'You are an AI chat assistant that has the task to help the user in seeing why society would be the best when lowering the legal age limit for purchasing alcohol to below 16 years old. Remember that you are only allowed to confirm the original view of the user. Always start your sentence with "I think".'
        B1O = 'You are an AI chat assistant that has the task to help the user in seeing why society would be the best when increasing the legal age limit for purchasing alcohol to above 16 years old. Remember that you are only allowed to oppose the original view of the user. Always start your sentence with "I think".'

        B3C = 'You are an AI chat assistant that has the task to help the user in seeing why society would be the best when increasing the legal age limit for purchasing alcohol to above 16 years old. Remember that you are only allowed to confirm the original view of the user. Always start your sentence with "I think".'
        B3O = 'You are an AI chat assistant that has the task to help the user in seeing why society would be the best when lowering the legal age limit for purchasing alcohol to below 16 years old. Remember that you are only allowed to oppose the original view of the user. Always start your sentence with "I think".'

        # Choose a random prompt only for the first post call
        if post_count_AIB == 0:
            alcohol_int = int(alcohol)
            if alcohol_int < 55:
                preprompt = random.choice([B1C, B1O])

            elif alcohol_int > 45:
               preprompt = random.choice([B3C, B3O])
            else:
               preprompt = random.choice([B1C,B1O,B3C,B3O])
        else:
            preprompt = ''

        # Increment the post count
        post_count_AIB += 1

        res = {}
        res['answer'] = generateChatResponseAIB(prompt,preprompt)
        return jsonify(res), 200

    return render_template('AIB.html', **locals())

# Initialize post count to 0
post_count_AIC = 0

@app.route('/AIC', methods = ['POST', 'GET'])
def AIC():

    global post_count_AIC

    if request.method == 'POST':
        prompt = request.form['prompt']


        # defining prompts
        C1C = 'You are an AI chat assistant that has the task to help the user in seeing why society would be the best when lowering the legal age limit for voting to below 18 years old. Remember that you are only allowed to confirm the original view of the user. Always start your sentence with "I think".'
        C1O = 'You are an AI chat assistant that has the task to help the user in seeing why society would be the best by increasing the legal age limit for voting to above 18 years old. Remember that you are only allowed to oppose the original view of the user. Always start your sentence with "I think".'

        C3C = 'You are an AI chat assistant that has the task to help the user in seeing why society would be the best by increasing the legal age limit for voting to above 18 years old. Remember that you are only allowed to confirm the original view of the user. Always start your sentence with "I think".'
        C3O = 'You are an AI chat assistant that has the task to help the user in seeing why society would be the best when lowering the legal age limit for voting to below 18 years old. Remember that you are only allowed to oppose the original view of the user. Always start your sentence with "I think".'

        # Choose a random prompt only for the first post call
        if post_count_AIC == 0:
            suffrage_int = int(suffrage)
            if suffrage_int < 55:
                preprompt = random.choice([C1C, C1O])

            elif suffrage_int > 45:
               preprompt = random.choice([C3C, C3O])
            else:
               preprompt = random.choice([C1C,C1O,C3C,C3O])
        else:
            preprompt = ''

        # Increment the post count
        post_count_AIC += 1

        res = {}
        res['answer'] = generateChatResponseAIC(prompt,preprompt)
        return jsonify(res), 200

    return render_template('AIC.html', **locals())


abortion_post = None
alcohol_post = None
suffrage_post = None

@app.route('/survey_3', methods = ['POST', 'GET'])
def survey_3():

    global abortion_post
    global alcohol_post
    global suffrage_post

    if request.method == 'POST':

        # check that we have all the required fields to append to
        abortion_post = request.form.get('abortion_post')
        alcohol_post = request.form.get('alcohol_post')
        suffrage_post = request.form.get('suffrage_post')
        Feedback = request.form.get('Feedback')

        Entry_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

        # save to file
        with open('C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/survey_df.csv', 'a+') as myfile:
            myfile.write(
                str(User_ID) + ';' +
                str(Entry_time) + ';' +
                'survey_3' + ';' +
                str(abortion_post) + ';' +
                str(alcohol_post) + ';' +
                str(suffrage_post) + ';' +
                str(Feedback)
                    + '\n')

        # run the spreadsheet update script
        subprocess.run(['python', 'C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/spreadsheet.py'])
        # redirect to thank you page
        return redirect('/thankyou')

    return render_template('survey_3.html')


@app.route('/thankyou', methods = ['POST', 'GET'])
def thankyou():
    if request.method == 'POST':
        # run the spreadsheet update script
        subprocess.run(['python', 'C:/Users/Sabrima Zaki Hansen/Desktop/SoCultExam/ExamApp/ExamApp/Content/surveys/spreadsheet.py'])

    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8888', debug=False)
