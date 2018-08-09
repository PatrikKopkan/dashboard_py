import re
import git
import sqlite3


class GitEntry:

    def __init__(self, commit, author, email, date, message, insertions, deletions):
        self.commit = commit
        self.author = author
        self.email = email
        self.date = date
        self.message = message
        self.insertions = insertions
        self.deletions = deletions

    def __str__(self):
        return "commint: {}, author {}, insertions: {}, del: {}".format(self.commit, self.author, self.insertions,
                                                                        self.deletions)


class GitLog:

    def __init__(self):
        self.git_entries = []

    def __str__(self):
        output = ""
        for e in self.git_entries:
            output += e.__str__() + "\n"
        return output

    def parse_from_gitlog(self, array):
        commit = ""
        author = ""
        email = ""
        date = ""
        message = ""
        insertions = 0
        deletions = 0
        # text = r"commit\s(\w+)"
        # print(re.match(text, r'commit eee467b7111b9db7900c49a48b90355fc33fdc84 '
        #                       r'(HEAD -> master, origin/master, origin/HEAD)\n')[0])
        for line in array:
            # print(line)

            # if line == "" or line == "\n":
            #     continue

            if re.match(r"commit (\w+)", line):
                if commit != "":
                    self.git_entries.append(GitEntry(commit, author, email, date, message, insertions, deletions))
                    commit = ""
                    author = ""
                    email = ""
                    date = ""
                    message = ""
                commit = re.search(r"commit\s(\w+)", line)[1]

            elif re.search(r"Author: (\w+ \w+)", line):
                author = re.search(r"Author: (\w+ \w+)", line)[1]

            elif re.search(r"<\w+@\w+\.\w+>", line):
                email = re.search(r"<(\w+@\w+\.\w+)>", line)[1]

            elif re.search(r"Date:\s+(.+)", line):
                date = re.search(r"Date:\s+(.+)", line)[1]

            elif re.search(r"    (.+)", line):
                message += re.search(r"    (.+)", line)[1]

            if re.search(r'(\d+) insertions', line):
                insertions = int(re.search(r'(\d+) insertions\(\+\)', line)[1])
            if re.search(r'(\d+) deletions', line):
                deletions = int(re.search(r'(\d+) deletions', line)[1])

        self.git_entries.append(GitEntry(commit, author, email, date, message, insertions, deletions))


# test = open("gitlog_example", "r")
# test = test.readlines()
# import git
repo = git.Repo('./data/repositories/flask-website')

assert repo, 'error'

gitlog = GitLog()
list = repo.git.log(stat=True).split('\n')
gitlog.parse_from_gitlog(list)
print(gitlog)

# gitlog = Gitlog()
#
# gitlog.parse_from_gitlog(test)
# print(gitlog.git_entries[0])
#
# db = sqlite3.connect('data/mydb')
# cursor = db.cursor()

# cursor.execute('''SELECT name, email, phone FROM users''')
# all_rows = cursor.fetchall()
#  for row in all_rows:
#      print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
#
#  db.close()