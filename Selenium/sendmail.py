import smtplib


from_mail = "ranaruhan123@gmail.com",
to_mail = "bisma.tariq98@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_mail, 'rufkorocpiakwbrs')

message = "Hey there is only one thing that compare"

server.sendmail(from_mail,to_mail,message)


server.quit()

