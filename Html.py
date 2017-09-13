class Html:

    def __init__(self, header, body):
        self.header = header
        self.body = body
        self.scripts_of_body = ""
        self.scripts_of_header = ""


    def add_csslink(self, url):
        self.header += "\n<link rel=\"stylesheet\" type=text/css href\"" + url + "\""

    def add_csslinks(self, urls):
        for url in urls:
            self.add_csslink(url)

    def add_script(self, code, body = True):
        if body:
            self.scripts_of_body += "<script>\n" + code + "</script>\n"
        else:
            self.scripts_of_header += "<script>\n" + code + "</script>\n"

    def add_scripts(self, codes, body = True):
        for code in codes:
            self.add_script(code, body)

    def add_scriptlink(self, url, body = True):
        pass

    def get_document(self):
        return "<!Doctype>\n<html>\n<header\n" + self.header + "\n" + self.scripts_of_header + "\n</header>\n<body>\n" \
               + self.body + "\n" + self.scripts_of_body + "\n</body>\n</html>"

    def get_html_file(self, path):
        file = open(path, "w")
        file.write(self.get_document())
        file.close()
