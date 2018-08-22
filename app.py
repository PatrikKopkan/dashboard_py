from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import FileEntry
from forms import LoginForm
from config import Config
from flask import session
import sqlite3
from werkzeug import secure_filename
import git
import gitlogparser
import os, re
from flask import g

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)

    def __repr__(self):
        return '<User {}, password: {}>'.format(self.username, self.password)



global _Path_To_Repoes
_Path_To_Repoes = './data/repositories/'
global _Repositories
global _Temp
_Temp = './static/temp/'
_Repositories = FileEntry.Repoes(_Path_To_Repoes)
_Repositories.count()


#
# def get_db():
#     if 'db' not in g:
#         g.db = SQLAlchemy(app)
#
#     return g.db
#
# @app.teardown_appcontext
# def teardown_db():
#     db = g.pop('db', None)
#
#     if db is not None:
#         db.close()

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
def administration():  # todo: hash password
    page = ''
    try:
        query = User.query.filter_by(username=session['username'], password=session['password']).first()
        if query is not None:
            print('in if')
            page = render_template('administration.html', _Repositories=_Repositories)
        else:
            page = redirect(url_for('login'))
            flash('wrong password or username')
    except KeyError:
        flash('not logged in')
        page = redirect(url_for('login'))
    finally:
        return page

@app.route('/add_repoes', methods=['GET', 'POST'])
def add_repoes():
    if request.method == 'POST':
        added_repoes = []
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
                added_repoes.append(str)
            # last_url = url
        _Repositories.count(added_repoes)
        return redirect('administration')


@app.route('/delete_repo/<repository>')
def delete_repo(repository):
    path_to_del_repo = os.path.join(_Repositories.path, repository)
    print(path_to_del_repo)
    for root, dirs, files in os.walk(path_to_del_repo, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    _Repositories.delete(repository)


@app.route('/repository/<repository>')
def repository(repository):
    list_of_graphs = gitlogparser.make_graphs(_Path_To_Repoes, repository, _Temp)
    return render_template('repository.html', list_of_graphs=list_of_graphs)



if __name__ == '__main__':
    app.run(debug=True)
