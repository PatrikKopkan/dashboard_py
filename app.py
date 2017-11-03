from flask import Flask, render_template,redirect, url_for
import main

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
    files = main.FileEntry.FileEntry()
    files.parse_from_ls(var)
    return render_template('index.html')


@app.route('/admininstration')
def administration():
    return render_template('administration.html')


if __name__ == '__main__':
    app.run(debug=True)
