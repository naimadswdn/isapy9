import smtplib

from email.mime.text import MIMEText

text_file = 'python7.py'
me = 'isapy@o2.pl'
to = 'damianseredyn@gmail.com'

fp = open(text_file, 'r')
msg = MIMEText(fp.read())

fp.close()

msg['Subject'] = f'Content of {text_file}'
msg['From'] = me
msg['To'] = to

s = smtplib.SMTP_SSL('poczta.02.pl:465')
s.login(me, 'isapython')
s.sendmail(me, to, msg.as_string())
s.quit()
print('done')
