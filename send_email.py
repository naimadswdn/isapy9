import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(topic, content):
    """
    Function that is sending an email.
    :param topic: it is a topic of an email
    :param content: it is a content of the message
    :return:
    """
    mail = MIMEMultipart()
    mail["Subject"] = topic
    mail["To"] = 'naimadswdn@gmail.com'
    mail["From"] = 'isapy@int.pl'

    body = MIMEText(content)
    mail.attach(body)

    server = smtplib.SMTP('poczta.int.pl')
    server.login('isapy@int.pl', 'isapython;')
    server.send_message(mail)
    server.quit()

    print('Email has been send successfully.')