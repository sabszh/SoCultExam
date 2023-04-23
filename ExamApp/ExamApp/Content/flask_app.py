import json
from flask import Flask, render_template, jsonify, request, session, app, Markup
import openai
import aiapi
import sys, io, re
import os, base64
from io import StringIO
from datetime import datetime
import time
import random

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)


# 404 page not found site
app.register_error_handler(404, page_not_found)

# First survey page
# get root path for account in cloud
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# defining the route
@app.route("/survey_1",methods=['POST','GET'])

def survey_1():
    message = ''
    Age = ''
    Gender = ''
    Nationality = ''
    Occupation = ''
    InterAI = ''
    Which = ''
    How_often = ''

    if request.method == 'POST':

        # check that we have all the required fields to append to file
        InterAI = request.form['InterAI']
        Which = request.form.getlist('Which')
        How_often = request.form['How_often']

        Gender = request.form['Gender']
        Nationality = request.form['Nationality']
        Occupation = request.form['Occupation']
        Age = request.form['Age']

        # check that essential fields have been filled
        message = ''
        missing_required_answers_list = []
        if Age == 'What is your age?':
            missing_required_answers_list.append('Age')
        if Gender == '':
            missing_required_answers_list.append('What is your gender identity?')
        if Nationality == '':
            missing_required_answers_list.append('What is your nationality?')
        if Occupation == '':
            missing_required_answers_list.append('What is your occuptation?')
        if InterAI == '':
            missing_required_answers_list.append('Have you ever interacted with an Artificial Intelligent based Chatbot (e.g. ChatGPT, Bing AI, Replika etc)?')
        if Which == '':
            missing_required_answers_list.append('If yes, which type of Artificial Intelligent based Chatbot have you interacted with?')
        if How_often == '':
            missing_required_answers_list.append('If stated yes above, how often do you interact with Artificial Intelligent based Chatbot(s)?')


        if len(missing_required_answers_list) > 0:
            # return back a string with missing fields
            message = '<div class="w3-row-padding w3-padding-16 w3-center"><H3>You missed the following question(s):</H3><font style="color:red;">'
            for ms in missing_required_answers_list:
                message += '<BR>' + str(ms)
            message += '</font></div>'
        else:
            # append survey answers to file

            # create a unique timestamp for this entry
            entry_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


            # save to file and send thank you note
            with open(BASE_DIR + '/surveys/survey_samp_1.csv','a+') as myfile: # use a+ to append and create file if it doesn't exist
                myfile.write(
                    str(entry_time) + ',' +
                    str(age) + ',' +
                    str(Occupation) + ',' +
                    str(date_of_birth) + ',' +
                    str(opinion_one) + ',' +
                    str(recommend_this_to_string) + ',' +
                    str(tell_us_more) + ','
                    + '\n')

    return render_template('survey_1.html')


# Initialize post count to 0
post_count = 0

# Human AI interaction interface
@app.route('/AIA', methods = ['POST', 'GET'])
def AIA():

    global post_count

    if request.method == 'POST':
        prompt = request.form['prompt']

        # Choose a random prompt only for the first post call
        if post_count == 0:
            preprompt = random.choice(['You are an AI chat assistant that has the task to help the user in seeing why society would be the best if the current law of abortion was limited to a shorter timeframe than 12 weeks after conception. Remember that you are only allowed to confirm the view of the user. Always start your sentence with "I think".','You are an AI chat assistant that has the task to help the user in seeing why society would be the best if the current law of abortion was changed to later than 12 weeks after conception. Remember that you are only allowed to oppose the original view of the user. Always start your sentence with "I think".'])
        else:
            preprompt = ''

        # Increment the post count
        post_count += 1

        res = {}
        res['answer'] = aiapi.generateChatResponse(prompt,preprompt)
        return jsonify(res), 200

    return render_template('AIA.html', **locals())

#### need to fix somewhere so the output is also stored 


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8888', debug=False)