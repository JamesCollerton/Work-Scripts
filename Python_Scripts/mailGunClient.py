import requests

# Sends an email using Mail-Gun. Pretty standard set up from the website.
def sendEmail(recipient, message, subject, fromEmail):

    key = 'key-17a8bba64262bd0139ac29b6d77e6f58'
    sandbox = 'sandbox03d7770e45654ce5a58c47f7f8a49647.mailgun.org'

    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
    request = requests.post(request_url, auth=('api', key), data={
        'from': fromEmail,
        'to': recipient,
        'subject': subject,
        'text': message
    })