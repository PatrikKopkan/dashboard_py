from flask import Flask, render_template, redirect, url_for, request
import main
import FileEntry
app = Flask(__name__)


@app.route('/')
def index():
    path2 = "/home/dellboy/Documents/dashboard/links.txt"
    # git_clone(path2)
    mypath = "/home/$USER/Documents/repoes"

    var = main.basic_statistic(mypath.replace("$USER", main.get_user()))
    # output = ""
    # for item in var:
    #     output += item + "\n"
    # print(output)

    files = FileEntry.Repoes()
    files.parseFromLs(var)
    files.count()
    print(files)
    return render_template('index.html', files=files)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return request.form['username']
    else:
        return render_template('login.html')


@app.route('/admininstration')
def administration():

    return render_template('administration.html')


if __name__ == '__main__':
    app.run(debug=True)
