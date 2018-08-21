import sys

sys.path.append(r'C:\Users\Patrick\PycharmProjects\dashboard_py')
import unittest
import gitlogparser
import git
import os
import datetime
import pytest


class TestGitEntry(unittest.TestCase):
    pass


class TestGitLog(unittest.TestCase):
    def setUp(self):
        self.path_to_repoes = r'C:\Users\Patrick\PycharmProjects\dashboard_py\unittests\repositories'
        self.repo = git.Repo(os.path.join(self.path_to_repoes, 'test1'))

    def test_parse_from_gitlog(self):
        gitlog = gitlogparser.GitLog()
        list = self.repo.git.log(stat=True).split('\n')
        gitlog.parse_from_gitlog(list)
        entries = gitlog.git_entries

        self.assertEqual(len(entries), 5)

        Expected_output = [
            [
                'f769e3ce7429d38af8598fe029b6ab3a238e162d',
                'PatrikKopkan',
                'kopkanpatrik@gmail.com',
                datetime.datetime.strptime('Fri Aug 17 11:34:45 2018', '%c'),
                'Create test.xml',
                2,
                0
            ],

            [
                '84c4133c0e503675f653a9af74ddaa8f7ae029a1',
                'PatrikKopkan',
                'kopkanpatrik@gmail.com',
                datetime.datetime.strptime('Fri Aug 17 11:33:47 2018', '%c'),
                'Create test.adoc',
                1,
                0
            ],
            [
                '1d9a54d96f820e08fd50686494a6aa569d9e8abc',
                'PatrikKopkan',
                'kopkanpatrik@gmail.com',
                datetime.datetime.strptime('Fri Aug 17 11:31:59 2018', '%c'),
                'Create test.png',
                1,
                0
            ],
            [
                '23169af6ae052fcfb4e98ea9c6a3067196ec10d8',
                'PatrikKopkan',
                'kopkanpatrik@gmail.com',
                datetime.datetime.strptime('Fri Aug 17 11:31:18 2018', '%c'),
                'Create test.adoc',
                1,
                0
            ],
            [
                '67ef5f90563bce99a57ba07f3ea4cbda5a6d88d1',
                'PatrikKopkan',
                'kopkanpatrik@gmail.com',
                datetime.datetime.strptime('Sun Sep 3 11:24:13 2017', '%c'),
                'Create README.md',
                1,
                0
            ]
        ]

        for i in range(len(entries)):
            self.assertEqual(entries[i].commit, Expected_output[i][0])
            self.assertEqual(entries[i].author, Expected_output[i][1])
            self.assertEqual(entries[i].email, Expected_output[i][2])
            self.assertEqual(entries[i].date, Expected_output[i][3])
            self.assertEqual(entries[i].message, Expected_output[i][4])
            self.assertEqual(entries[i].insertions, Expected_output[i][5])
            self.assertEqual(entries[i].deletions, Expected_output[i][6])

        for line in list:
            print(line)
