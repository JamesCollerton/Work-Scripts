import requests

EMAIL_CONTENTS = "Hi <NAME>,\n\nI'm really sorry, but the <TUBE> line has a <STATUS>" + \
				 "I will be running a few minutes late, but hopefully not too long!" + \
				 "\n\nBest,\n\nJames"

NO_DELAYED_TUBES = "\n\nNo tubes are delayed! You need a different excuse!"

ERROR_CODE = 1

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

	delayedTubeStatus = ""
	delayedTubeName = ""

	for tubeStatus in tubeStatusArray:
		if tubeStatus['lineStatus'] != 'Good Service':
			return(tubeStatus)			

	print(NO_DELAYED_TUBES)
	sys.exit(ERROR_CODE)

def main():

	tubeStatusJson = getTubeStatusJson()
	tubeStatusArray = getTubeInfo(tubeStatusJson)
	tubeStatus = getDelayedTube(tubeStatusArray)
	print(tubeStatus)

if __name__ == "__main__":
    main()