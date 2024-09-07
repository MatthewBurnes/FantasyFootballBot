import sendEmail
import datetime

print(datetime.datetime.now())
waitTime = datetime.datetime.now() + datetime.timedelta(minutes= 10)
print(waitTime)
while(datetime.datetime.now() < waitTime):
    continue
sendEmail.sendEmail()
