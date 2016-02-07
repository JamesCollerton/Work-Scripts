import sys
import json
from flask import Flask

# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# app = Flask(__name__)
 
# @app.route("/")

# def hello():
    # return "Hello World!"

def makeCall(callDetails):

	# Get these credentials from http://twilio.com/user/account
	account_sid = callDetails["SID"]
	auth_token = callDetails["AuthToken"]
	to_number = callDetails["myNum"]
	from_number = callDetails["twilioNum"]
	client = TwilioRestClient(account_sid, auth_token)
	 
	# Make the call
	call = client.calls.create(to=to_number,  # Any phone number
	                           from_=from_number, # Must be a valid Twilio number
	                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

def getCallDetails():

	with open('../Ignore/phoneDetails.json') as data_file:    
		callDetails = json.load(data_file)

	return(callDetails)

def main():

	callDetails = getCallDetails()
	makeCall(callDetails)
	# app.run(debug=True)
 
if __name__ == "__main__":
	main()

# def main():

# 	print("Hello")



# if __name__ == "__main__":
#     main()
