import re


class GitEntry:

    def __init__(self, commit, author, email, date):
        self.commit = commit
        self.author = author
        self.email = email
        self.date = date
        self.message = ""

    def __str__(self):
        return "commit: " + self.commit + "author: " + self.author


class Gitlog:

    def __init__(self):
        self.git_entries = []

    def parse_from_gitlog(self, array):
        commit = ""
        author = ""
        for s in array:
            commitm = re.findall(s, r"commit\s(\w+)")
            authorm = re.findall(s, r"Author:\s(\w+\s\w+)")
            email = re.findall(s, r"<\w+@\w+\.\w+>")
            datem = re.findall(s, r"Date:\s+(.+)")

            if commitm:
                commit = commitm[0]
            if authorm:
                author = authorm[0]
            if email:
                email = email[0]
            if datem:
                self.git_entries.append(GitEntry(commit, author, email, datem[0]))
