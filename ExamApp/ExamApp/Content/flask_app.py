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
import uuid

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
                    str(User_ID) + ',' +
                    str(Entry_time) + ',' +
                    str(Age) + ',' +
                    str(Gender) + ',' +
                    str(Nationality) + ',' +
                    str(Occupation) + ',' +
                    str(InterAI) + ',' +
                    str(Which) + ',' +
                    str(How_often) + ','
                    + '\n')

    return render_template('survey_1.html')



@app.route('/survey_2', methods = ['POST', 'GET'])
def survey_2():

    return render_template('survey_2.html')





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