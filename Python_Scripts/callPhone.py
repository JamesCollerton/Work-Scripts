import sys
import json
from flask import Flask
from twilio.rest import TwilioRestClient

# Super short script for making calls to my phone using Twilio.

# Makes a call using the details given in an untracked .json file
def makeCall(callDetails):

	account_sid = callDetails["SID"]
	auth_token = callDetails["AuthToken"]
	to_number = callDetails["myNum"]
	from_number = callDetails["twilioNum"]
	client = TwilioRestClient(account_sid, auth_token)
	 
	call = client.calls.create(to=to_number,  
	                           from_=from_number, 
	                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

# Gets the call details from the untracked .json file
def getCallDetails():

	with open('../Ignore/phoneDetails.json') as data_file:    
		callDetails = json.load(data_file)

	return(callDetails)

# Short main, gets details from .json then uses them to make the call.
def main():

	callDetails = getCallDetails()
	makeCall(callDetails)
 
if __name__ == "__main__":
	main()