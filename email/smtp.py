import smtplib
from getpass import getpass

def send_emails(emails, schedule, get_joke):
    # Connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    password = getpass("What's your password?")
    from_email = 'hamimphopal50@gmail.com'
    server.login(from_email, password)

    # Send to entire email list
    for to_email, name in emails.items():
        message = 'Subject: Welcome to the Adams emailer!\n'
        message += 'Hi ' + name + '!\n\n'
        message += get_joke + '\n\n'
        message += "Best way to prepare for the software engeering postion:"
        message += schedule + '\n\n'
        message += 'Hope this info helped!'
        server.sendmail(from_email, to_email, message)

    server.quit()
