#Import Libraries
#Import Libraries
import socket
import datetime
import yagmail
import os
from twilio.rest import Client

#Yagmail SMTP
yag = yagmail.SMTP('email', 'password')

#Function to connect socket
def is_running(site):
    """This function attempts to connect to the given server using a socket.
        Returns: Whether or not it was able to connect to the server."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((site, 80))
        return True
    except:
        return False

#Function to log into a txt file
def save_log(state):
    f = open("server_log.txt", "a")
    f.write(state)
    f.close()

#Function to send email log
def send_email(site):
    contents = [
    f'There is a problem with {site} as of {date_time}\n'
    ]
    yag.send('sender@gmail.com', 'Server Status', contents)

#Function to send text log
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

#Main Function
if __name__ == "__main__":
    #Array holding what servers you want to check to see if they respond
    servers_to_check=["server.com"]
    #Loop over every server
    for x in servers_to_check:
        site = (x)
        date_time = datetime.datetime.now()
        if is_running(f'{site}'):
            #If it does respond, log successful connection
            state = str(f"{site} is running as of {date_time}\n")
            #Log
            save_log(state)
        else:
            #If it doesn't respond, log the time and date of issue and send email and text notification
            state = str(f'There is a problem with {site} as of {date_time}\n')
            #Log
            save_log(state)
            # Send Email
            send_email(site)
            send_text(site)