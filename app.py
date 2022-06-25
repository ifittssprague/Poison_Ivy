from webbrowser import get
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

# allows us to repond with a 404 page
from werkzeug.exceptions import abort



app = Flask(__name__)


@app.route('/')
def home():

    return render_template('home.html')


@app.route('/about')
def about():

    return render_template('about.html')


@app.route('/get_started')
def get_started():

    return render_template('get_started.html')


@app.route('/q<int:question_number>')
def question(question_number):
    

    return render_template('question.html')

