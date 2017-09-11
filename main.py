import os
import re

def git_clone(path):
    """

    :type path: str
    """
    commands = "cd /home/$USER/Documents; mkdir -p repoes; cd repoes"

    file = open(path,"r")
    for line in file:
        commands += "; git -c http.sslVerify=false clone " + line.replace("\n", "")

    #print(commands)
    os.system(commands)


def basic_statistic(path):
    commands = "cd " + path
    os.system(commands)
    os.system("ls")

    return ""


def basic_statistic2(path):

    dictin = {}
    mydir = os.listdir(path)

    for i in mydir:
        match = re.search(r'\.[a-z]*$', i)
    if match:
        if len(array) == 0:
            dictin{match.group()} = "1"
        for j in range(len(array)):
            if j == match.group():
                dictin[j] += 1
            else:
                dictin{match.group()} = 1

    else:
        return basic_statistic2(path + i)

#os.system("ls -l")
path2 = "/home/dellboy/Documents/dashboard/links.txt"
#git_clone(path2)
mypath = "/home/$USER/Documents"
os.system("echo $USER > temp.txt")
file = open("temp.txt", "r")
user = file.readline()
user = user.replace("\n", "")
os.system("rm temp.txt")

#basic_statistic2(mypath.replace("$USER", user))
array = []