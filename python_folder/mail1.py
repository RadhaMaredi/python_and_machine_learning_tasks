import smtplib  #import smtplib

#store from details in variables
from_address ="radhamaredi1995@gmail.com"
me = from_address
pwd="yqozteemfxuiurzs"

#store the sending address in variables
to=["vibha.rawan@neosoftmail.com"]
cc =["lakshmi73862@gmail.com", "grandheraj68@gmail.com"]
bcc =["arun.nadar@neosoftmial.com","rohan.dhere@neosoftmail.com"]

#concatinate all sending address
receiver_mail= cc + to + bcc

#store subject and body of our mail in variables
text="Hi ! this is Radha Maredi"
sub="Send mail through python code"

#join the from, sending address and subject, body 
email_text = """\
From: %s
To: %s
Subject: %s
cc: %s
%s
""" % (me,",".join(to), sub,", ".join(cc), text)

#hosting services, choose which server to sending mail,port
server =smtplib.SMTP('smtp.gmail.com',587)  
server.starttls()       #used this for security purpose
server.login(from_address, pwd)  #login to the mail
#sending the mail
server.sendmail(from_address, receiver_mail, email_text)
server.quit() #quit from the mail

#print the text to know weather our text was successfullly sent or not.
print("successfully sent")