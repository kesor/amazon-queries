import xml.sax


class AmazonXmlHandler(xml.sax.handler.ContentHandler):

    def startDocument(self):
        self.stack = []

    def startElement(self, name, attrs):
        self.stack.append(name)
        self.text_content = ''

    def characters(self, content):
        self.text_content += content

    def endElement(self, name):
        tail = self.stack.pop()
        if isinstance(tail, tuple):
            print "its a tuple!"
        self.stack.append( (tail, self.text_content) )

    def result(self):
        return self.stack


def parse(source, parse_func=xml.sax.parse, handler_class=AmazonXmlHandler):
    handler = handler_class()
    parse_func(source, handler)
    return handler.result()
