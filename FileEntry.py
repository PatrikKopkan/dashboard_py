import re


class File:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __str__(self):
        return "Name: " + self.name + " Length: " + str(self.length)


class FileEntry:
    def __init__(self):
        self.Files = []
        self.adoc = 0
        self.xml = 0
        self.pictures = 0

    def append(self, file):
        self.Files.append(file)

    def parse_from_ls(self, array):
        temp = []
        for s in array:
            temp = s.split()
            if len(temp) == 9:
                self.append(File(temp[8], temp[4]))

    def __str__(self):
        output = ""
        for f in self.Files:
            output += f.__str__() + "\n"
        return output

    def count(self):
        for f in self.Files:
            match = re.findall(r'\.[a-z]+', f.name)
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
