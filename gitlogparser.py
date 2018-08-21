import re
import git
import sqlite3
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.dates import date2num
from matplotlib.ticker import Formatter
import os.path


temp = './data/temp'

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
        for line in array:
            print(line)
        for line in array:
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
                if re.search(r"<\w+@\w+\.\w+>", line):
                    email = re.search(r"<(\w+@\w+\.\w+)>", line)[1]

            elif re.search(r"Author: (\w+)", line):
                author = re.search(r"Author: (\w+)", line)[1]
                if re.search(r"<\w+@\w+\.\w+>", line):
                    email = re.search(r"<(\w+@\w+\.\w+)>", line)[1]


            elif re.search(r"Date:\s+(.+) (?:(.)(?:\d(\d)\d\d))", line):
                search = re.search(r"Date:\s+(.+) (?:(.)(?:\d(\d)\d\d))", line)
                date = search[1]
                sign = search[2]
                zone = search[3]
                date = datetime.datetime.strptime(date, '%c')
                zone = datetime.timedelta(hours=int(zone))
                if sign == '-':
                    date = date + zone
                else:
                    date = date - zone

                # timed = datetime.timedelta(
                #     hours=
                # )

            elif re.search(r"    (.+)", line):
                message += re.search(r"    (.+)", line)[1]

            elif re.search(r'(\d+) insertion(?:s)*', line):
                insertions = int(re.search(r'(\d+) insertion(?:s)*\(\+\)', line)[1])
                print(line)
                print(insertions)
                if re.search(r'(\d+) deletion(?:s)*', line):
                    deletions = int(re.search(r'(\d+) deletion(?:s)*', line)[1])

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


# date = datetime.strptime('Wed May 2 07:31:44 2018 -0700', '')
# print(date)
# test = open("gitlog_example", "r")
# test = test.readlines()
# import git

path_to_repoes = './data/repositories/'
repo = 'flask-website'


def setup_ticks(step):
    """Configure ticks so only each n-th tick will be visible."""

    locs, plt_labels = plt.xticks()
    plt.setp(plt_labels, rotation=90)
    for tick in plt_labels:
        tick.set_visible(False)

    for tick in plt_labels[::step]:
        tick.set_visible(True)

def make_graphs(path_to_repoes, repo, temp):
    repo = git.Repo(os.path.join(path_to_repoes, repo))

    assert repo, 'error'

    gitlog = GitLog()
    list = repo.git.log(stat=True).split('\n')
    gitlog.parse_from_gitlog(list)
    charts = DataForCharts()
    charts.parse(gitlog)

    x = []
    y = []
    list_of_graphs = []
    for author, data in charts.authors.items():
        author = 'Unknown' if author is None or author == '' else author
        print(author)
        print(data)
        for d in data:
            # print((d.date))
            # x.append(date2num(d.date))
            # type(d.date)
            x.append(d.date)
            # print(d.insertions - d.deletions)
            y.append(d.insertions - d.deletions)
        print('x: {} y: {}'.format(len(x), len(y)))

        # formatter = MyFormatter(x)
        hfmt = dates.DateFormatter('%Y-%m-%d')

        # fig, ax = plt.subplots()
        # # ax.xaxis.set_major_formatter(hfmt)
        # ax.plot(x, y, 'o-')
        # fig.autofmt_xdate()
        # ax.set_title(author)
        # plt.show()
        # # fig.savefig(os.path.join(temp, author))
        # list_of_graphs.append('temp/' + author + '.png')
        # x = []
        # y = []

        # plt.rcdefaults()
        items = len(x)
        fig = plt.bar(np.arange(items), y)
        plt.xticks(np.arange(items), x)
        step = 1
        if items > 20:
            step = 2
            if items > 40:
                step = 3
        setup_ticks(step)
        # ax.xaxis.set_major_formatter(hfmt)
        # ax.plot(x, y, 'o-')
        # fig.autofmt_xdate()
        # ax.set_title(author)
        plt.show()
        # plt.savefig(os.path.join(temp, author))
        list_of_graphs.append('temp/' + author + '.png')
        x = []
        y = []
        # plt.close(fig)
    return list_of_graphs

# path_to_repoes = './unittests/repositories'
# repo = git.Repo(os.path.join(path_to_repoes, 'test1'))
# gitlog = GitLog()
# list = repo.git.log(stat=True).split('\n')
# gitlog.parse_from_gitlog(list)
# entries = gitlog.git_entries
# print(entries[0].email)




# make_graphs(path_to_repoes, repo, temp)


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
