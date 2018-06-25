from os import rename

from flask import Flask, render_template, redirect, url_for, request, flash
#import main
import FileEntry
from forms import LoginForm
from config import Config
from flask import session
import sqlite3

app = Flask(__name__)
app.config.from_object(Config)

#@app.route('/')
#def index():
    # path2 = "/home/dellboy/Documents/dashboard/links.txt"
    # # git_clone(path2)
    # mypath = "/home/$USER/Documents/repoes"
    #
    # var = main.basic_statistic(mypath.replace("$USER", main.get_user()))
    # # output = ""
    # # for item in var:
    # #     output += item + "\n"
    # # print(output)
    #
    # files = FileEntry.Repoes()
    # files.parseFromLs(var)
    # files.count()
    # print(files)
    #return render_template('index.html', files=files)




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


@app.route('/repository/<repository>')
def repository(repository):
    pass
print(app.config['SECRET_KEY'])


if __name__ == '__main__':
    app.run(debug=True)


