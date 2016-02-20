import requests
import json

# ------------------------------------------------------------------------------

# mailGunClient.py

# This script is used with the MailGun client to ping off emails using my
# MailGun client. It reads in the key and sandbox from an untracked file.

# ------------------------------------------------------------------------------

# Gets the mail gun details from an untracked file.
def getMailGunDetails():

	with open('../Ignore/mailGunDetails.json') as data_file:    
	    emailJson = json.load(data_file)

	return(emailJson)

# Sends an email using Mail-Gun. Pretty standard set up from the website.
def sendEmail(recipient, message, subject, fromEmail):

	mailGunDetails = getMailGunDetails()

	key = mailGunDetails['key']
	sandbox = mailGunDetails['sandbox']

	request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
	request = requests.post(request_url, auth=('api', key), data={
	    'from': fromEmail,
	    'to': recipient,
	    'subject': subject,
	    'text': message
    })