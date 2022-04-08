import smtplib

From ="radhamaredi1995@gmail.com"
me = From
pwd="yqozteemfxuiurzs"

to=["vibha.rawan@neosoftmail.com"]
cc =["lakshmi73862@gmail.com", "grandheraj68@gmail.com"]
bcc =["arun.nadar@neosoftmial.com","rohan.dhere@neosoftmail.com"]

receiver_mail= cc + to + bcc


text="Hi ! this is Radha Maredi"
sub="Send mail through python code"

email_text = """\
From: %s
To: %s
Subject: %s
cc: %s
%s
""" % (me,",".join(to), sub,", ".join(cc), text)

#hosting services, choose which server to sending mail,port
server =smtplib.SMTP('smtp.gmail.com',587)  
server.starttls() # security purpose

server.login(From, pwd)

server.sendmail(From, receiver_mail, email_text)

server.quit() #quit

print("successfully sent")