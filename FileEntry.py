import os


class File:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __str__(self):
        return "Name: " + self.name + " Length: " + str(self.length)

    def dict(self):
        return {'name': self.name, 'length': self.length}

    def toList(self):
        return []


class Repo:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.Files = []
        self.adoc = 0
        self.xml = 0
        self.pictures = 0

    def append(self, file):
        self.Files.append(file)

    # def __str__(self):
    #     output = ""
    #     for f in self.Files:
    #         output += "Repository: " + self.name + " " + f.__str__() + "\n"
    #     return output

    def __str__(self):
        return "name: {} adoc: {} pictures: {} xml: {}".format(self.name, self.adoc, self.pictures, self.xml)

    def count(self):
        for root, dirs, files in os.walk(self.path):
            for filename in files:
                extension = os.path.splitext(filename)[1][1:].strip()
                if extension == "adoc":
                    self.adoc += 1

                elif extension == "xml":
                    self.xml += 1

                elif extension == "png":
                    self.pictures += 1

                elif extension == "jpg":
                    self.pictures += 1

                elif extension == "jpeg":
                    self.pictures += 1


class Repoes:
    def __init__(self, path):
        self.path = path
        self.Repoes = []

    def append(self, repo):
        self.Repoes.append(repo)

    def delete(self, del_repo):
        self.Repoes = [repo for repo in self.Repoes if repo.name != del_repo]


    def __str__(self):
        output = ""
        for f in self.Repoes:
            output += f.__str__() + "\n"
        return output

    def count(self, added_repoes=[]):
        if len(added_repoes) == 0:
            self.Repoes = []
            for repo in os.listdir(self.path):
                r = Repo(repo, os.path.join(self.path, repo))
                r.count()
                self.append(r)
        else:
            for added_repo in added_repoes:  # deal with error
                r = Repo(repo, os.path.join(self.path, repo))
                r.count()
                self.append(r)
# global repositories
# repositories = Repoes('data/repositories/')
# repositories.count()
# print(repoes)
