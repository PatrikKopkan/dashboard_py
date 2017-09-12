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


def basic_statistic2(path, keys=[], counts=[]):

    keys = keys
    counts = counts
    mydir = os.listdir(path)
    for i in mydir:
        temp = True
        match = re.findall(r'\.[a-z]+', i)
        if match:

            for j in range(len(keys)):
                if keys[j] == match[0]:
                    counts[j] += 1
                    temp = False
                    break
            if temp:
                keys.append(match[0])
                counts.append(1)
        else:
            return basic_statistic2(path + "/" + i, keys, counts)
    return keys, counts

#os.system("ls -l")
path2 = "/home/dellboy/Documents/dashboard/links.txt"
#git_clone(path2)
mypath = "/home/$USER/Documents/test"
os.system("echo $USER > temp.txt")
file = open("temp.txt", "r")
user = file.readline()
user = user.replace("\n", "")
os.system("rm temp.txt")

print(basic_statistic2(mypath.replace("$USER", user)))
string = "afa.cf afa.txt .png"
#print(re.findall(r'\.[a-z]+', string))
#print(match)
