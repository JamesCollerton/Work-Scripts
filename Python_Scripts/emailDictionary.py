import json

# ------------------------------------------------------------------------------

# emailDictionary.py

# This script is used to scan in the email addresses as a .json for use across
# the various scripts.

# ------------------------------------------------------------------------------

# Gets the dictionary of email addresses for use in sendMail
def getEmailDictionary():

	with open('../Ignore/emailDetails.json') as data_file:    
	    emailJson = json.load(data_file)

	return(emailJson)