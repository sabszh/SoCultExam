import json
from flask import Flask, render_template, jsonify, request, session, app, Markup
import openai
import aiapi
import sys, io, re
import os, base64
from io import StringIO
from datetime import datetime
import time

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
    Age = ''
    Gender = ''
    Nationality = ''
    Occupation = ''
    InterAI = ''
    If_yes = ''
    tell_us_more = ''
    # this is a list so create a string to append into csv file
    recommend_this_to_string = ''


    if request.method == 'POST':

        # check that we have all the required fields to append to file
        opinion_one = request.form['opinion_one']
        recommend_this_to = request.form.getlist('recommend_this_to')
        tell_us_more = request.form['tell_us_more']
        # remove special characters from input for security
        tell_us_more = re.sub(r"[^a-zA-Z0-9]","",tell_us_more)

        gender = request.form['gender']
        Nationality = request.form['Nationality']
        Occupation = request.form['Occupation']
        date_of_birth = request.form['date_of_birth']

        # optional fields
        if date_of_birth=='':
            date_of_birth = 'NA'
        if 'Occupation' in request.form:
            Occupation = request.form['Occupation']
        else:
            Occupation = 'NA'


        # check that essential fields have been filled
        Age = ''
        missing_required_answers_list = []
        if opinion_one == 'Choose one...':
            missing_required_answers_list.append('Opinions')
        if tell_us_more == '':
            missing_required_answers_list.append('Tells us more')
        if gender == '':
            missing_required_answers_list.append('What is your gender=')
        ifNationality == '':
            missing_required_answers_list.append('What is yourNationality?')
        if Occupation == '':
            missing_required_answers_list.append('What is your Occupation identity?')


        if len(missing_required_answers_list) > 0:
            # return back a string with missing fields
            Age = '<div class="w3-row-padding w3-padding-16 w3-center"><H3>You missed the following question(s):</H3><font style="color:red;">'
            for ms in missing_required_answers_list:
                Age += '<BR>' + str(ms)
            Age += '</font></div>'
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

            # return thank-you Age
            Age = '<div class="w3-row-padding w3-padding-16 w3-center"><H2><font style="color:blue;">Thank you for taking the time to complete this survey</font></H2></div>'


    return render_template('survey_1.html')

# A: Human AI interaction interface
@app.route('/humanaiA', methods = ['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        prompt = request.form['prompt']

        res = {}
        res['answer'] = aiapi.generateChatResponse(prompt)
        return jsonify(res), 200

    return render_template('AIA.html', **locals())


# B: Human AI interaction interface
@app.route('/humanaiB', methods = ['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        prompt = request.form['prompt']

        res = {}
        res['answer'] = aiapi.generateChatResponse(prompt)
        return jsonify(res), 200

    return render_template('AIB.html', **locals())



# C: Human AI interaction interface
@app.route('/humanaiC', methods = ['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        prompt = request.form['prompt']

        res = {}
        res['answer'] = aiapi.generateChatResponse(prompt)
        return jsonify(res), 200

    return render_template('AIC.html', **locals())


# defining the route
@app.route("/survey_1",methods=['POST','GET'])
def survey_1():
    Age = ''
    gender = ''
   Nationality = ''
    Occupation = ''
    Occupation = ''
    opinion_one = 'Choose one...'
    tell_us_more = ''
    # this is a list so create a string to append into csv file
    recommend_this_to_string = ''


    if request.method == 'POST':

        # check that we have all the required fields to append to file
        opinion_one = request.form['opinion_one']
        recommend_this_to = request.form.getlist('recommend_this_to')
        tell_us_more = request.form['tell_us_more']
        # remove special characters from input for security
        tell_us_more = re.sub(r"[^a-zA-Z0-9]","",tell_us_more)

        gender = request.form['gender']
       Nationality = request.form['age']
        Occupation = request.form['Occupation']
        date_of_birth = request.form['date_of_birth']

        # optional fields
        if date_of_birth=='':
            date_of_birth = 'NA'
        if 'Occupation' in request.form:
            Occupation = request.form['Occupation']
        else:
            Occupation = 'NA'


        # check that essential fields have been filled
        Age = ''
        missing_required_answers_list = []
        if opinion_one == 'Choose one...':
            missing_required_answers_list.append('Opinions')
        if tell_us_more == '':
            missing_required_answers_list.append('Tells us more')
        if gender == '':
            missing_required_answers_list.append('What is your gender=')
        ifNationality == '':
            missing_required_answers_list.append('What is yourNationality?')
        if Occupation == '':
            missing_required_answers_list.append('What is your Occupation identity?')


        if len(missing_required_answers_list) > 0:
            # return back a string with missing fields
            Age = '<div class="w3-row-padding w3-padding-16 w3-center"><H3>You missed the following question(s):</H3><font style="color:red;">'
            for ms in missing_required_answers_list:
                Age += '<BR>' + str(ms)
            Age += '</font></div>'
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

            # return thank-you Age
            Age = '<div class="w3-row-padding w3-padding-16 w3-center"><H2><font style="color:blue;">Thank you for taking the time to complete this survey</font></H2></div>'


    return render_template('survey_2.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8888', debug=False)
