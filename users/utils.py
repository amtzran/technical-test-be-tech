from django.core.mail import EmailMessage
import requests


class Util:

    @staticmethod
    def send_email(data):
        subject = data['email_subject']
        body = data['email_body']
        to = data['email_to']
        email = EmailMessage(subject, body, to=[to])
        email.send()

    @staticmethod
    def send_whatsapp(data):
        payload = {
            'body': data['message'],
            'phone': data['phone']
        }
        requests.get('https://api.chat-api.com/instance246041/sendMessage?token=2l549rr1zsagpamh', data=payload)
