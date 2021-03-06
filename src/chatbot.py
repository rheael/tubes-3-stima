from flask import Flask, render_template, flash, request, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#from kmpstringmatching import kmpstringmatching
from Features import *
from werkzeug.utils import secure_filename
import os
#from flask_bootstrap import Bootstrap

global listOfChatAll

listOfChatAll = []

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def open():
    return render_template('open.html')


@app.route('/', methods=['GET', 'POST'])
def upload_all():
    if request.method == 'POST':
        name = request.form['name']
        listOfChat = {}
        global listOfChatAll
        listOfChat[0]=name
        x = getChatBotResponse(name)
        listOfChat[1]=x
        listOfChatAll.append(listOfChat)
        saveDeadlinesComponent()
        return render_template('showmessage.html',listOfChatAll=listOfChatAll,listOfChat=listOfChat)

def getChatBotResponse(name):
    return pilihanInput(name)

@app.route('/aboutuschatbot')
def chatbot():
    return render_template('aboutuschatbot.html')

if __name__ == "__main__":
    app.run(threaded=True)