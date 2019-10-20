import smtplib

smtp = smtplib.SMTP('smtp.gmail.com', 465)
smtp.ehlo()
smtp.starttls()
#Next, log in to the server
smtp.login("sarya9907@gmail.com", "rajuarya9")

#Send the mail
msg = "Hello!" # The /n separates the message from the headersss
smtp.sendmail("sarya9907@gmail.com", "sachin.sachinarya.arya@gmail.com", msg)