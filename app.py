

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
import os, re

app = Flask(__name__)
app.config.from_object(Config)

global _Path_To_Repoes
_Path_To_Repoes = './data/repositories/'
global _Repositories
global _Temp
_Temp = './static/temp/'
_Repositories = FileEntry.Repoes(_Path_To_Repoes)
_Repositories.count()


@app.route('/')
def index():
    # print(_Repositories)
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
        # f = request.files['file']
        # for url in f:
        #     print(url)
        f = request.files['file']
        for url in f:
            str = url.decode('utf-8')
            # print(str)
            str = str.strip()
            # print(str)
            repeated = False
            for dir in os.listdir(_Path_To_Repoes):
                dir_from_url = str.split('/' or '//')[-1].replace('.git', '')
                if dir == dir_from_url:
                    flash('this repository: {} already has been cloned'.format(dir))
                    repeated = True
            if not repeated:
                git.Git("./data/repositories").clone(str)
            # last_url = url

        return redirect('administration')


@app.route('/repository/<repository>')
def repository(repository):
    list_of_graphs = gitlogparser.make_graphs(_Path_To_Repoes, repository, _Temp)
    return render_template('repository.html', list_of_graphs=list_of_graphs)

print(app.config['SECRET_KEY'])

if __name__ == '__main__':
    app.run(debug=True)
