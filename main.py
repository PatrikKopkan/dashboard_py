import os
import re
import FileEntry

def git_clone(path):
    """

    :type path: str
    """
    commands = "cd /home/$USER/Documents; mkdir -p repoes; cd repoes"

    file = open(path,"r")
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
    commands = "cd " + path + "; ls -R -l > mytemp.txt"
    os.system(commands)
    file = open(path + "/mytemp.txt", "r")
    output = file.readlines()
    file.close()
    os.system("cd " + path + "; rm mytemp.txt")
    return output


def basic_statistic2(path, keys=[], counts=[],):
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

        return basic_statistic2(keys, counts)
    return keys, counts


path2 = "/home/dellboy/Documents/dashboard/links.txt"
#git_clone(path2)
mypath = "/home/$USER/Documents/repoes"

var = basic_statistic(mypath.replace("$USER", get_user()))
files = FileEntry.FileEntry()
files.parse_from_ls(var)
files.count()
print(files)
print(files.xml)



