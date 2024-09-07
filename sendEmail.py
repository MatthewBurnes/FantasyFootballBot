#send myself an email                       
#send myself an email on event
#host this somewhere (aws??)
#add a readme
#make sure env variables stay hidden

import smtplib
from email.mime.text import MIMEText
def sendEmail():
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('coachgusthagoat@outlook.com', 'Redhotspot!')
    smtpObj.sendmail('coachgusthagoat@outlook.com', 'matthewburnes@berkeley.edu', 'Subject: TestEmail.\n\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
    smtpObj.quit()