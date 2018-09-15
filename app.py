from twilio.rest import Client
import random, os

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
sourcetn = os.environ['TWILIO_TN']
desttn = os.environ['DEST_TN']

def open_texts():
    texts_file = open('texts.txt','r')
    texts = texts_file.readlines()
    return texts

def get_text(texts):
    return random.choice(texts)

def main():
    texts = open_texts()
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            to=desttn,
            from_=sourcetn,
            body=get_text(texts))

if __name__ == "__main__":
    main()
