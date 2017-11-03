import os
import re
import FileEntry
import subprocess
import Html


JS_LINK = "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"
CSS_LINK = "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"


def git_clone(path):
    """

    :type path: str
    """
    commands = "cd /home/$USER/Documents; mkdir -p repoes; cd repoes"

    file = open(path, "r")
    for line in file:
        commands += "; git -c http.sslVerify=false clone " + line.replace("\n", "")
    os.system(commands)
    file.close()


def get_user():
    os.system("echo $USER > temp.txt")
    file = open("temp.txt", "r")
    user = file.readline()
    file.close()
    user = user.replace("\n", "")
    os.system("rm temp.txt")
    return user


def basic_statistic(path):
    commands = "cd " + path + "; ls -R -l> mytemp.txt"
    os.system(commands)
    file = open(path + "/mytemp.txt", "r")
    output = file.readlines()
    file.close()
    os.system("cd " + path + "; rm mytemp.txt")
    return output


def basic_statistic2(path):
    # commands = "cd " + path + "; ls -R -l > mytemp.txt"
    # p = subprocess.Popen(commands, stdout=subprocess.PIPE, shell=True)
    # for line in p.stdout:
    #     print(line)
    commands = "cd " + path + "; ls -R -l> mytemp.txt"
    os.system(commands)
    file = open(path + "/mytemp.txt", "r")
    output = ""
    for line in file:
        output += line
    file.close()
    os.system("cd " + path + "; rm mytemp.txt")
    print(output)


path2 = "/home/dellboy/Documents/dashboard/links.txt"
# git_clone(path2)
mypath = "/home/$USER/Documents/repoes"

#var = basic_statistic(mypath.replace("$USER", get_user()))
# output = ""
# for item in var:
#     output += item + "\n"
# print(output)
#files = FileEntry.FileEntry()
#files.parse_from_ls(var)
#files.count()
#doc = Html.Html()
#doc.add_csslink(CSS_LINK)
#doc.add_scriptlink(JS_LINK)
#doc.sorted_table(files)
#print(doc.get_document())
#doc.get_html_file("/home/dellboy/Documents/index.html")
# print(files.xml)
