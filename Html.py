class Html:

    def __init__(self, header="", body=""):
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

    def add_scripts(self, codes, body=True):
        for code in codes:
            self.add_script(code, body)

    def add_scriptlink(self, url, body=True):
        if body:
            self.scripts_of_body += "<script src=" + url + "></script>"
        else:
            self.scripts_of_header += "<script src=\"" + url + "\"></script>"

    def add_scriptlinks(self, urls, body=True):
        for url in urls:
            self.add_scriptlink(url, body)

    def get_document(self):
        return "<!Doctype>\n<html>\n<header>\n" + self.header + "\n" + self.scripts_of_header + "\n</header>\n<body>\n" \
               + self.body + "\n" + self.scripts_of_body + "\n</body>\n</html>"

    def get_html_file(self, path="index.html"):
        file = open(path, "w")
        file.write(self.get_document())
        file.close()

    def sorted_table(self, file_entries):
        self.add_scriptlink("http://jenkinscat.gsslab.pnq.redhat.com/sorttable.js")
        self.body += "<table class='table table-condensed table-hover table-bordered sortable'>\n"
        self.body += "<th>\n"
        #self.body += "<td>" + "repository" + "</td>\n"
        self.body += "<td>" + "adoc" + "</td>\n"
        self.body += "<td>" + "xml" + "</td>\n"
        self.body += "<td>" + "pictures" + "</td>\n"
        self.body += "</th>\n"
        for r in file_entries.Files:
            self.body += "<tr>\n"
            self.body += "<td>" + str(r.name) + "</td>\n"
            self.body += "<td>" + str(r.adoc) + "</td>\n"
            self.body += "<td>" + str(r.xml) + "</td>\n"
            self.body += "<td>" + str(r.pictures) + "</td>\n"
            self.body += "</tr>\n"
        self.body += "</table>\n"
