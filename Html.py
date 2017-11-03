class Html:

    def __init__(self, head="", body=""):
        self.head = head
        self.body = body
        self.scripts_of_body = ""
        self.scripts_of_head = ""

    def add_csslink(self, url):
        self.head += "\n<link rel=\"stylesheet\" type=text/css href=\"" + url + "\""

    def add_csslinks(self, urls):
        for url in urls:
            self.add_csslink(url)

    def add_script(self, code, body=True):
        if body:
            self.scripts_of_body += "<script>\n" + code + "</script>\n"
        else:
            self.scripts_of_head += "<script>\n" + code + "</script>\n"

    def add_scripts(self, codes, body=True):
        for code in codes:
            self.add_script(code, body)

    def add_scriptlink(self, url, body=True):
        if body:
            self.scripts_of_body += "<script src=\"" + url + "\"></script>"
        else:
            self.scripts_of_head += "<script src=\"" + url + "\"></script>"

    def add_scriptlinks(self, urls, body=True):
        for url in urls:
            self.add_scriptlink(url, body)

    def get_document(self):
        return "<!Doctype>\n<html>\n<head>\n" + self.head + "\n" + self.scripts_of_head \
               + "\n</head>\n<body>\n" \
               + self.body + "\n" + self.scripts_of_body + "\n</body>\n</html>"

    def get_html_file(self, path="index.html"):
        file = open(path, "w")
        file.write(self.get_document())
        file.flush()
        file.close()

    def sorted_table(self, file_entries):
        self.add_scriptlink("http://jenkinscat.gsslab.pnq.redhat.com/sorttable.js")
        self.body += "<table class='table table-condensed table-hover table-bordered sortable'>\n"
        self.body += "<tr>\n"
        self.body += "<th>" + "repository" + "</th>\n"
        self.body += "<th>" + "adoc" + "</th>\n"
        self.body += "<th>" + "xml" + "</th>\n"
        self.body += "<th>" + "pictures" + "</th>\n"
        self.body += "</tr>\n"
        for r in file_entries.Files:
            self.body += "<tr>\n"
            self.body += "<td>" + str(r.name) + "</td>\n"
            self.body += "<td>" + str(r.adoc) + "</td>\n"
            self.body += "<td>" + str(r.xml) + "</td>\n"
            self.body += "<td>" + str(r.pictures) + "</td>\n"
            self.body += "</tr>\n"
        self.body += "</table>\n"
