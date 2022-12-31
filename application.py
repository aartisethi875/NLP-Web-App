from flask import Flask, render_template, request, redirect, session
from db import Database
import api
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

dbo = Database()


@app.route('/')
def index():
    return render_template('Login.html')


@app.route('/Register')
def Register():
    return render_template('register.html')

@app.route('/perform_Registration', methods=['post'])
def perform_Registration():
    name = request.form.get('users_name')
    email = request.form.get('users_email')
    password = request.form.get('users_password')
    response = dbo.insert(name, email, password)
    if response:
        return render_template('Login.html', message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html', message="Email already exists")


@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.search(email, password)

    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('Login.html', message='incorrect email/password')


@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')


@app.route('/Ner')
def Ner():
    if session:
        return render_template('Ner.html')
    else:
        return redirect('/')


@app.route('/perform_Ner', methods=['post'])
def perform_Ner():
    if session:
        text = request.form.get('Ner_text')
        response = api.Ner(text)
        print(response)

        return render_template('Ner.html', response=response)
    else:
        return redirect('/')


app.run(debug = True)