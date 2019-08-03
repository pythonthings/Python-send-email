import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

people = ["rajsuthan666@gmail.com","rajsuthan777@gmail.com","shanjairajvlogs@gmail.com"]

add_email = input("Any other email you want to send:")
people.append(add_email)

sender_email= "shanjairaj777@gmail.com"
password = input("Enter your password and then press ENTER:")

for i in range(len(people)):
    receiver_email = people[i]

    message = MIMEMultipart("alternative")
    message["Subject"] = "This is a test"
    message["From"] = sender_email
    message["To"] = receiver_email

    #creating the text and the html version of the message

    text = """\
    This is a python test to send emails
    Hope krishna likes this.
    Haribol
    """
    html = """\
    <html>
    <body>
        <h3 style = "background:blue;text-align:center;color:white;padding:10px 0px;">Welcome to Python Emails Sending Automation</h3>
        <p>Becoming a programmer is a cumulative process that builds up your skills day after day and year after year, and programming can be fun and rewarding (mentally, spiritually and financially). This guide does not promise to give a magically easy way to becoming a programmer, and the ordering of the steps is not sacred, but you'll get a general outline of how to become a programmer in one of the modern programming fields.</p>
        <button style="background:blue;border:none;padding:10px;border-radius:5px;"><a style="text-decoration:none;color:white;" href="youtube.com">Youtube</a></button>
    </body>
    </html>
    """

    #Making the text/html into MIMEText objects
    part1 = MIMEText(text,"plain")
    part2 = MIMEText(html,"html")

    #Attaching the parts to the message
    message.attach(part1)
    message.attach(part2)

    #Creating secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
        server.login(sender_email,password)
        server.sendmail(
            sender_email,receiver_email,message.as_string()
        )
    print(receiver_email)
