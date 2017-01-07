#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
    
msg = MIMEText('hello, send by python...', 'plain', 'utf-8')
from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8')     #廖大文中“Header(...).encode()”对方无法接收文件,去掉encode()后，方可正常接收

msg.attach(MIMEText('<html><body><h1>hello</h1>' +  # h1为标题文字显示样式与正文有区别
'<p>我在图片上面</p>' +   #在图片上面插入文字
'<p><img src="cid:0"></p>' +
'<p>我在图片下面</p>' +     #在图片下面插入文字
'</body></html>', 'html', 'utf-8'))

with open('read\\test2.png', 'rb') as f: #WIN7系统完整路径为(c:\\work\\xxx.xx),当前路径为(xxx\\xxx.xx)
    mime = MIMEBase('image', 'png', filename='test2.png')
    mime.add_header('Content-Disposition', 'attachment', filename='test2.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()