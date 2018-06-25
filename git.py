import re
import sqlite3


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
        for line in array:
                # print(line)
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
                    commit = re.match(line, r"commit (\w+)").group(1)
                    print(commit)

                elif bool(re.match(line, r"Author: (\w+ \w+)")):
                    author = re.match(line, r"Author: (\w+ \w+)").group(1)
                    print(author)

                elif bool(re.match(line, r"<\w+@\w+\.\w+>")):
                    email = re.match(line, r"<\w+@\w+\.\w+>")
                    print(email)

                elif bool(re.match(line, r"Date:\s+(.+)")):
                    date = re.match(line, r"Date:\s+(.+)")
                    print(date)

                elif bool(re.match(line,r"    (.+)")):
                    message += re.match(line, r"    (.+)").group(1)
                    print(message)

        self.git_entries.append(GitEntry(commit, author, email, date, message))


test = open("gitlog_example", "r")
test = test.readlines()

gitlog = Gitlog()
text = r"commit\s(\w+)"
print(bool(re.match(text, r'commit eee467b7111b9db7900c49a48b90355fc33fdc84 (HEAD -> master, origin/master, origin/HEAD)\n')))
# gitlog.parse_from_gitlog(test)
# print(gitlog.git_entries[0])

db = sqlite3.connect('data/mydb')
cursor = db.cursor()

# cursor.execute('''SELECT name, email, phone FROM users''')
# all_rows = cursor.fetchall()
#  for row in all_rows:
#      print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
#
#  db.close()