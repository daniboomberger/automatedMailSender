from getpass import getpass
from string import Template
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import json
import smtplib

'''
 TODO: add error handling
'''

#variables for user credentials
user_email = ''
user_password = ''

#variables for smtp ssl config
smtp_url = ''
smtp_port = ''

#variable for json file
json_path = ''

#variables for email message
mail_template_path = ''
mail_message = MIMEMultipart()
mail_subject = ''
mail_receiver = ''
mail_body = ''


#function to provide connection to mail server and also sending the actual message
def mailServerConnection() :
    mail_server = smtplib.SMTP_SSL(smtp_url, smtp_port)
    mail_server.ehlo()
    mail_server.login(user_email, user_password)
    mail_server.send_message(mail_message)

#function to parse the json file
def jsonParser():
    global mail_subject
    global mail_receiver
    global mail_body

    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)
    for i in range(0, len(json_data)-1):
        current_json_data = json_data[str(i)]
        mail_subject = current_json_data['subject']
        mail_receiver = current_json_data['receiver']
        mail_body = createMailBody(current_json_data)
        mailMessage()
        mailServerConnection()
    pass

#function which creates with an template and json data a mail body
def createMailBody(data):
    mail_template_text = open(mail_template_path).read()
    template = Template(mail_template_text)

    try:
        body = template.substitute(
            name = data['name'], 
            formal = data['formal'],
        )
    except: 
        print('An Error occured with the template')
    return body 

#function to create an mail message with necassary config
def mailMessage():
    mail_message['Subject'] = mail_subject
    mail_message['FROM'] = user_email
    mail_message['To'] = mail_receiver
    mail_message.attach(MIMEText(mail_body, 'plain'))


if __name__ == '__main__':
    user_email = input('Enter your e-mail: ')
    user_password = getpass('Enter your password: ')
    smtp_url = input('Enter the smtp ssl url: ') 
    smtp_port = input('Enter the smtp ssl port: ')
    json_path = input('Enter your json file path: ')
    mail_template_path  = input('Enter your mail template file path: ')
    jsonParser()

