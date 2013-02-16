import xml.sax

class XmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.request_id = ''
        self.request_id_indent = None
        self.indent = None
        self.root = None

    def startElement(self, name, attrs):
        if self.indent is None:
            self.root = name
            self.indent = 0
            return
        if name.lower() == 'requestid':
            self.request_id = None
            self.request_id_indent = self.indent
            return
        print ' '*self.indent + 'startElement("%s", attrs)' % (name,)
        self.indent = self.indent + 4

    def endElement(self, name):
        if self.indent == 0:
            return
        if self.indent == self.request_id_indent:
            return
        self.indent = self.indent - 4
        print ' '*self.indent + 'endElement("%s")' % (name,)

    def characters(self, content):
        if content.strip() == '':
            return
        if self.request_id is None:
            self.request_id = content.encode('utf-8')
            return
        print ' '*self.indent + 'characters("%s")' % (content,)

class AmazonXML(object):
    @classmethod
    def parse(self, source):
        handler = XmlHandler()
        xml.sax.parse(source, handler)
        return handler
