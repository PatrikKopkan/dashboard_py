import re


class File:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __str__(self):
        return "Name: " + self.name + " Length: " + str(self.length)

    def dict(self):
        return {'name': self.name, 'length': self.length}


class Repo:
    def __init__(self, name):
        self.name = name
        self.Files = []
        self.adoc = 0
        self.xml = 0
        self.pictures = 0

    def append(self, file):
        self.Files.append(file)

    def parse_from_ls(self, array):
        # temp = []
        # repo = ""
        # for s in array:
        #     match = re.findall(r'\.\/([a-zA-Z_\-0-9]+)', s)
        #     if match:
        #         repo = match[0]
        #     temp = s.split()
        #     if len(temp) == 9:
        #         self.append(File(repo, temp[8], temp[4]))
        pass

    def __str__(self):
        output = ""
        for f in self.Files:
            output += "Repository: " + self.name + " " + f.__str__() + "\n"
        return output

    def count(self):
        for f in self.Files:
            match = re.findall(r'\.[a-z]+$', f.name)
            if match:
                if match[0] == ".adoc":
                    self.adoc += 1

                if match[0] == ".xml":
                    self.xml += 1

            #  if match[0] == ".png" | match[0] == ".jpg" | match[0] == ".jpeg":
            #     self.pictures += 1

                if match[0] == ".png":
                    self.pictures += 1

                if match[0] == ".jpg":
                    self.pictures += 1

                if match[0] == "jpeg":
                    self.pictures += 1




class Repoes:
    Repoes = []

    def __init__(self):
        pass

    def append(self, repo):
        self.Repoes.append(repo)

    def parseFromLs(self, array):
        temp = []
        repo = ""
        for s in array:
            match = re.findall(r'^\.\/([a-zA-Z_\-0-9]+)', s)
            if match:
                repo = match[0]
                self.append(Repo(repo))
                #print(repo + "\n")
            temp = s.split()
            if len(temp) == 9 and len(self.Repoes) > 0:
                #print(temp[8] + " " + temp[4] + "\n")
                self.Repoes[-1].append(File(temp[8], temp[4]))

    def __str__(self):
        output = ""
        for f in self.Repoes:
            output += f.__str__() + "\n"
        return output


# spatne udelane
class FileEntry:
    def __init__(self):
        self.Files = []
        self.adoc = 0
        self.xml = 0
        self.pictures = 0

    def append(self, repo):
        self.Files.append(repo)

    def parse_from_ls(self, array):
        temp = []
        repo = ""
        i = 0
        for s in array:
            match = re.findall(r'\.\/([a-zA-Z_\-0-9]+)', s)
            if match:
                if repo == "":
                    repo = match[0]
                    self.append(Repo(repo))
                elif repo != match[0]:
                    repo = match[0]
                    self.append(Repo(repo))
                    i += 1
            temp = s.split()
            # print(temp)
            # print(len(temp) == 9, 9 & len(self.Files) != 0)
            # print(len(temp) == 9 & len(self.Files) != 0)
            # print(False & True)
            if len(temp) == 9 and len(self.Files) != 0:
                # print(self.Files[i])
                # print(temp[8])
                self.Files[i].append(File(temp[8], temp[4]))

    def __str__(self):
        output = ""
        for f in self.Files:
            output += f.__str__() + "\n"
        return output

    def count(self):
        for f in self.Files:
            f.count()
            self.adoc += f.adoc
            self.xml += f.xml
            self.pictures += f.pictures
