import requests
import sys

from mailGunClient import *

EMAIL_CONTENTS = "Hi <NAME>,\n\nI'm really sorry, but the <TUBE> line has a <STATUS>. " + \
				 "I will be running a few minutes late, but hopefully not too long!" + \
				 "\n\nBest,\n\nJames"

NO_DELAYED_TUBES = "\n\nNo tubes are delayed! You need a different excuse!\n\n"

ERROR_NO_COMMAND_LINE_ARGUMENTS = "\n\nInsufficient command line arguments.\n\n"

ERROR_CODE = 1

def getCommandLineArg(commandLineArgs):

	try:
		recipientName = commandLineArgs[1]
	except:
		print(ERROR_NO_COMMAND_LINE_ARGUMENTS)
		sys.exit(ERROR_CODE)

	return(recipientName)

def getTubeStatusJson():

	try:
		tubeRequest = requests.get('https://api.tfl.gov.uk/line/mode/tube/status')
	except requests.exceptions.RequestException as e:
		print e
		sys.exit(ERROR_CODE)

	return(tubeRequest.json())

def getTubeInfo(tubeStatusJson):

	tubeStatusArray = []

	for tubeStatus in tubeStatusJson:
		tubeInfoDict = {}
		tubeInfoDict['name'] = tubeStatus['name']
		tubeInfoDict['lineStatus'] = tubeStatus['lineStatuses'][0]['statusSeverityDescription']
		tubeStatusArray.append(tubeInfoDict)

	return(tubeStatusArray)

def getDelayedTube(tubeStatusArray):

	for tubeStatus in tubeStatusArray:
		if tubeStatus['lineStatus'] != 'Good Service':
			return(tubeStatus)			

	return({'name': 'Victoria', 'lineStatus': 'Closed'})

	print(NO_DELAYED_TUBES)
	sys.exit(ERROR_CODE)

def createEmailString(tubeStatus, recipientName):

	emailString = EMAIL_CONTENTS.replace('<TUBE>', tubeStatus['name'])
	emailString = emailString.replace('<STATUS>', tubeStatus['lineStatus'].lower())
	emailString = emailString.replace('<NAME>', recipientName)

	return(emailString)

def main():

	recipientName = getCommandLineArg(sys.argv)
	tubeStatusJson = getTubeStatusJson()
	tubeStatusArray = getTubeInfo(tubeStatusJson)
	tubeStatus = getDelayedTube(tubeStatusArray)
	emailString = createEmailString(tubeStatus, recipientName)
	sendEmail('jc1175@my.bristol.ac.uk', emailString, "Testing", 'jc1175@my.bristol.ac.uk')

if __name__ == "__main__":
    main()