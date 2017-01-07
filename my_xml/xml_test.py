#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
#        print('<%s>' % tag)
#        print('%s' % attrs)
        if len(attrs) > 0 and attrs[0][0] == 'href':
            self.useful_data = True
        elif len(attrs) > 0 and attrs[0][1] == 'event-location':
            self.useful_data = True
        elif len(attrs) > 0 and attrs[0][0] == 'datetime':
            self.useful_data = True
        else:
            self.useful_data = False
        
    def handle_endtag(self, tag):
        pass
#        print('</%s>' % tag)
        
    def handle_startendtag(self, tag, attrs):
#        print('<%s/>' % tag)
        pass
    def handle_data(self, data):
        if self.useful_data == True:
            print(data)
        
    def handle_comment(self, data):
#        print('<!--', data, '-->')
        pass
    def handle_entityref(self, name):
#        print('&%s:' % name)
        pass
    def handle_charref(self, name):
#        print('&#%s:' % name)
        pass
parser = MyHTMLParser()
'''
parser.feed(<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"sss\">html</a> HTML&nbsp; tutorial...<br>END</p>
</body></html>)
'''

parser.feed('''<li>
    <h3 class="event-title"><a href="/events/python-events/480/">PyCon Cameroon</a></h3>
    <p>                                                      
        <time datetime="2017-01-12T00:00:00+00:00">12 Jan. &ndash; 15 Jan. <span class="say-no-more"> 2017</span></time>                        
        <span class="event-location">Molyko Buea,Cameroon</span>
    </p>
</li>''')