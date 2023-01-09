import smtplib

my_email = "allinpositive@gmail.com"
password = "sk125874!"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="iamfakertoo@gmail.com", msg="Hello")
connection.close()