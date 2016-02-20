import json

# Gets the dictionary of email addresses for use in sendMail
def getEmailDictionary():

	with open('../Ignore/emailDetails.json') as data_file:    
	    emailJson = json.load(data_file)

	return(emailJson)