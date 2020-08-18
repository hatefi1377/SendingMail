import smtplib
from email.message import EmailMessage



email = EmailMessage()
email['from'] = 'Ali Hatefi'
email['to'] = ''
email['subject'] = 'Subject'

email.set_content('''
Hello this is a test email.
Thanks for reading this.
''')

password = ''
username = ''

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username , password)
    smtp.send_message(email)
    print('done!')
