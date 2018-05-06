import re


class GitEntry:

    def __init__(self, commit, author, email, date, message):
        self.commit = commit
        self.author = author
        self.email = email
        self.date = date
        self.message = message

    def __str__(self):
        return "commit: " + self.commit + "author: " + self.author


class Gitlog:

    def __init__(self):
        self.git_entries = []

    def parse_from_gitlog(self, array):
        commit = ""
        author = ""
        email = ""
        date = ""
        message = ""
        for line in array:

                if line == "" or line == "\n":
                    continue

                elif bool(re.match(line, r"commit\s(\w+)")):
                    if commit != "":
                        self.git_entries.append(GitEntry(commit, author, email, date, message))
                        commit = ""
                        author = ""
                        email = ""
                        date = ""
                        message = ""
                    commit = re.match(line, r"commit\s(\w+)").group(1)

                elif bool(re.match(line, r"Author:\s(\w+\s\w+)")):
                    author = re.match(line, r"Author:\s(\w+\s\w+)").group(1)

                elif bool(re.match(line, r"<\w+@\w+\.\w+>")):
                    email = re.match(line, r"<\w+@\w+\.\w+>")

                elif bool(re.match(line, r"Date:\s+(.+)")):
                    date = re.match(line, r"Date:\s+(.+)")

                elif bool(re.match(line,r"    (.+)")):
                    message = re.match(line,r"    (.+)").group(1)

        self.git_entries.append(GitEntry(commit, author, email, date, message))