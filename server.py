#Import Libraries
import socket
import datetime
import yagmail
import os
from twilio.rest import Client

#Build a infinite looping script that checks the servers every hour and sends email or text if it reports to be dowmn
yag = yagmail.SMTP('email', 'password')

def is_running(site):
    """This function attempts to connect to the given server using a socket.
        Returns: Whether or not it was able to connect to the server."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((site, 80))
        return True
    except:
        return False

def save_log(state):
    f = open("server_log.txt", "a")
    f.write(state)
    f.close()

def send_email(site):
    contents = [
    f'There is a problem with {site} as of {date_time}\n'
    ]
    yag.send('sender@gmail.com', 'Server Status', contents)

def send_text(site):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body='There is a problem with {site} as of {date_time}',
            from_='+15555555555',
            to='+15555555555'
        )

if __name__ == "__main__":
    while True:
        site = input('Website to check: ')
        date_time = datetime.datetime.now()
        if is_running(f'{site}'):
            print(f"{site} is running as of {date_time}")
            state = str(f"{site} is running as of {date_time}\n")
            save_log(state)
        else:
            print(f'There is a problem with {site} as of {date_time}')
            state = str(f'There is a problem with {site} as of {date_time}\n')
            save_log(state)
            send_email(site)
        if input("Would You like to check another website(Y/N)? ") in {'n', 'N'}:
            break