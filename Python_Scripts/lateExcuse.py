import requests
import sys
# import json

# Imports the sendEmail function from the mailGunClient.py file
from mailGunClient import *
from emailDictionary import *

# ------------------------------------------------------------------------------ 
# Global Variables

# Email string for the body of the email. Name, tube and status will all be dynamically
# replaced.
EMAIL_SUBJECT = "Sorry, running late!"
EMAIL_FROM = "jc1175@my.bristol.ac.uk"
EMAIL_CONTENTS = "Hi <NAME>,\n\nI'm really sorry, but the <TUBE> line has a <STATUS>. " + \
				 "I will be running a few minutes late, but hopefully not too long!" + \
				 "\n\nBest,\n\nJames"

# Printed if there aren't any tubes delayed.
NO_DELAYED_TUBES = "\n\nNo tubes are delayed! You need a different excuse!\n\n"

# Printed if no recipient has been specified.
ERROR_NO_COMMAND_LINE_ARGUMENTS = "\n\nInsufficient command line arguments.\n\n"
ERROR_INVALID_RECIPIENT = "\n\nInvalid recipient name.\n\n"

# Error code for printing on system exit.
ERROR_CODE = 1

# ------------------------------------------------------------------------------ 
# Functions

# Gets the command line arguments (i.e. recipient name)
def getCommandLineArg(commandLineArgs):

	try:
		recipientName = commandLineArgs[1]
	except:
		print(ERROR_NO_COMMAND_LINE_ARGUMENTS)
		sys.exit(ERROR_CODE)

	return(recipientName)

# Gets the dictionary of email addresses for use in sendMail
# def getEmailDictionary():

# 	with open('../Ignore/emailDetails.json') as data_file:    
# 	    emailJson = json.load(data_file)

# 	return(emailJson)

def getRecipientEmail(emailDictionary, recipientName):

	recipientEmail = ""

	try:
		recipientEmail = emailDictionary[recipientName]
	except:
		print(ERROR_INVALID_RECIPIENT)
		sys.exit(1)

	if recipientEmail == "":
		print(ERROR_INVALID_RECIPIENT)
		sys.exit(1)

	return(recipientEmail)

# This gets the tube statuses using a request to the TFL API.
def getTubeStatusJson():

	try:
		tubeRequest = requests.get('https://api.tfl.gov.uk/line/mode/tube/status')
	except requests.exceptions.RequestException as e:
		print e
		sys.exit(ERROR_CODE)

	return(tubeRequest.json())

# This strips down the tube results from the API into just the tube name and status.
def getTubeInfo(tubeStatusJson):

	tubeStatusArray = []

	for tubeStatus in tubeStatusJson:
		tubeInfoDict = {}
		tubeInfoDict['name'] = tubeStatus['name']
		tubeInfoDict['lineStatus'] = tubeStatus['lineStatuses'][0]['statusSeverityDescription']
		tubeStatusArray.append(tubeInfoDict)

	return(tubeStatusArray)

# This returns the first tube that doesn't have good service.
def getDelayedTube(tubeStatusArray):

	for tubeStatus in tubeStatusArray:
		if tubeStatus['lineStatus'] != 'Good Service':
			return(tubeStatus)			

	return({'name': 'Victoria', 'lineStatus': 'Closed'})

	print(NO_DELAYED_TUBES)
	sys.exit(ERROR_CODE)

# This replaces the parts of the email string (tube, status and name) with the 
# values from the command line and the API.
def createEmailString(tubeStatus, recipientName):

	emailString = EMAIL_CONTENTS.replace('<TUBE>', tubeStatus['name'])
	emailString = emailString.replace('<STATUS>', tubeStatus['lineStatus'].lower())
	emailString = emailString.replace('<NAME>', recipientName)

	return(emailString)

# ------------------------------------------------------------------------------ 
# MAIN

# Gets the command line arguments, tube statuses, strips them, finds the first
# delayed tube and then dynamically creates an email string and sends it.
def main():

	recipientName = getCommandLineArg(sys.argv)
	emailDictionary = getEmailDictionary()
	recipientEmail = getRecipientEmail(emailDictionary, recipientName)
	tubeStatusJson = getTubeStatusJson()
	tubeStatusArray = getTubeInfo(tubeStatusJson)
	tubeStatus = getDelayedTube(tubeStatusArray)
	emailString = createEmailString(tubeStatus, recipientName)
	sendEmail(recipientEmail, emailString, EMAIL_SUBJECT, EMAIL_FROM)

if __name__ == "__main__":
    main()