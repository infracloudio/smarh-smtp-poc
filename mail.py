import smtplib

sender = 'from@example.com'
receivers = ['kn.sandeep@gmail.com']
message = """From: From Person <from@example.com>
To: To Person <to@example.com>
Subject: SMTP email example


This is a test message.
"""

try:
    smtpObj = smtplib.SMTP('0.0.0.0')
    smtpObj.sendmail(sender, receivers, message)         
    print("Successfully sent email")
except smtplib.SMTPException:
    print("Failure")
    pass