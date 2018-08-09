

from flask import Flask, render_template, redirect, url_for, request, flash
import FileEntry
import FileEntry
from forms import LoginForm
from config import Config
from flask import session
import sqlite3
from werkzeug import secure_filename
import git
import gitlogparser

app = Flask(__name__)
app.config.from_object(Config)

global _Repositories
_Repositories = FileEntry.Repoes('data/repositories/')
_Repositories.count()


@app.route('/')
def index():
    print(_Repositories)
    return render_template('index.html', _Repositories=_Repositories)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        session['username'] = form.username.data
        session['password'] = form.password.data
        return redirect('/administration')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/administration')
def administration():
    return render_template('administration.html')


@app.route('/add_repoes', methods=['GET', 'POST'])
def add_repoes():
    if request.method == 'POST':
        last_url = ''
        try:
            f = request.files['file']
            for url in f:
                url.strip()
                git.Repo("~/data/repositories").clone(url)
                last_url = url
        except:
            flash('Check file you have uploaded. Urls must be separated by enter. Last used url: {}'.format(last_url))
            return
        return 'file uploaded successfully'


@app.route('/repository/<repository>')
def repository(repository):
    return ''

print(app.config['SECRET_KEY'])

if __name__ == '__main__':
    app.run(debug=True)
