import pytest
import unittest
import sys

sys.path.append(r'C:\Users\Patrick\PycharmProjects\dashboard_py')
import FileEntry


class TestRepo(unittest.TestCase):

    def setUp(self):
        self.repo1 = FileEntry.Repo('test1',
                                    r'C:\Users\Patrick\PycharmProjects\dashboard_py\unittests\repositories\test1')
        self.repo2 = FileEntry.Repo('test2',
                                    r'C:\Users\Patrick\PycharmProjects\dashboard_py\unittests\repositories\test2')

    def test_count(self):
        self.repo1.count()
        self.repo2.count()

        self.assertEqual(self.repo1.xml, 1)
        self.assertEqual(self.repo1.adoc, 2)
        self.assertEqual(self.repo1.pictures, 1)

        self.assertEqual(self.repo2.pictures, 2)
        self.assertEqual(self.repo2.xml, 0)
        self.assertEqual(self.repo2.adoc, 1)


class TestRepoes(unittest.TestCase):

    def setUp(self):
        self.repoes1 = FileEntry.Repoes(r'C:\Users\Patrick\PycharmProjects\dashboard_py\unittests\repositories')

    def test_count(self):
        self.repoes1.count()

        self.assertEqual(len(self.repoes1.Repoes), 2)
        self.assertEqual(self.repoes1.Repoes[0].xml, 1)
        self.assertEqual(self.repoes1.Repoes[0].adoc, 2)
        self.assertEqual(self.repoes1.Repoes[0].pictures, 1)

        self.assertEqual(self.repoes1.Repoes[1].xml, 0)
        self.assertEqual(self.repoes1.Repoes[1].adoc, 1)
        self.assertEqual(self.repoes1.Repoes[1].pictures, 2)


if __name__ == '__main__':
    unittest.main()
