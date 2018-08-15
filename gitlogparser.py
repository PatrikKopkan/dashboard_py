import re
import git
import sqlite3
import datetime as datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from matplotlib.ticker import Formatter

0

class GitEntry:

    def __init__(self, commit, author, email, date, message, insertions, deletions):
        self.commit = commit
        self.author = author
        self.email = email
        self.date = date
        self.message = message
        self.insertions = 0 if insertions is None else insertions
        self.deletions = 0 if deletions is None else deletions

    def __str__(self):
        return "commit: {}, author {}, insertions: {}, del: {}".format(self.commit, self.author, self.insertions,
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

            elif re.search(r"Date:\s+(.+) (?:(.)(?:\d(\d)\d\d))", line):
                search = re.search(r"Date:\s+(.+) (?:(.)(?:\d(\d)\d\d))", line)
                date = search[1]
                sign = search[2]
                zone = search[3]
                date = datetime.datetime.strptime(date, '%c')
                zone = datetime.timedelta(hours=int(zone))
                if sign == '-':
                    date = date - zone
                else:
                    date = date + zone

                # timed = datetime.timedelta(
                #     hours=
                # )

            elif re.search(r"    (.+)", line):
                message += re.search(r"    (.+)", line)[1]

            if re.search(r'(\d+) insertions', line):
                insertions = int(re.search(r'(\d+) insertions\(\+\)', line)[1])
            if re.search(r'(\d+) deletions', line):
                deletions = int(re.search(r'(\d+) deletions', line)[1])

        self.git_entries.append(GitEntry(commit, author, email, date, message, insertions, deletions))


class DataEntry:
    def __init__(self, date, insertions, deletions):
        self.date = date
        self.insertions = insertions
        self.deletions = deletions

    def __str__(self):
        return 'date: {} insertions: {} deletions: {}'.format(self.date, self.insertions, self.deletions)

    def __repr__(self):
        return 'self.date: {} self.insertions: {} self.deletions: {}'.format(self.date, self.insertions, self.deletions)


class DataForCharts:
    def __init__(self):
        self.authors = {}

    def parse(self, gitlog_instance):
        for entry in gitlog_instance.git_entries:
            data = DataEntry(entry.date, entry.insertions, entry.deletions)
            if not entry.author in self.authors:
                self.authors[entry.author] = [data]
            else:
                self.authors[entry.author].append(data)

    def __str__(self):
        return self.authors.__str__()


# date = datetime.strptime('Wed May 2 07:31:44 2018 -0700', '')
# print(date)
# test = open("gitlog_example", "r")
# test = test.readlines()
# import git
repo = git.Repo('./')

assert repo, 'error'

gitlog = GitLog()
list = repo.git.log(stat=True).split('\n')
gitlog.parse_from_gitlog(list)
charts = DataForCharts()
charts.parse(gitlog)


class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%Y-%m-%d'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(np.round(x))
        if ind >= len(self.dates) or ind < 0:
            return ''

        return self.dates[ind]


x = []
y = []
for author, data in charts.authors.items():
    print(author)
    print(data)
    for d in data:
        # print((d.date))
        # x.append(date2num(d.date))
        x.append(d.date)
        # print(d.insertions - d.deletions)
        y.append(d.insertions - d.deletions)
    print('x: {} y: {}'.format(len(x), len(y)))

    # plt.plot_date(x, y, 'o-', label='Lines')
    #
    # plt.xlabel('Date')
    # plt.ylabel('lines')
    # plt.title(author)
    # plt.legend()
    # plt.show()
    # x = []
    # y = []

    formatter = MyFormatter(x)

    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(formatter)
    ax.plot(np.arange(len(x)), y, 'o-')
    fig.autofmt_xdate()
    plt.title(author)
    plt.show()



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
