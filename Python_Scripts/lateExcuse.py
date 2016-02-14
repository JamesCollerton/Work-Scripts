import requests

def getTubeStatusJson():

	try:
		tubeRequest = requests.get('https://api.tfl.gov.uk/line/mode/tube/status')
	except requests.exceptions.RequestException as e:
		print e
		sys.exit(1)

	return(tubeRequest.json())

def getTubeInfo(tubeStatusJson):

	delayedTubes = []

	for tubeStatus in tubeStatusJson:
		delayedTubeInfo = {}
		delayedTubeInfo['name'] = tubeStatus['name']
		delayedTubeInfo['lineStatus'] = tubeStatus['lineStatuses'][0]['statusSeverityDescription']
		delayedTubes.append(delayedTubeInfo)
		
	print(delayedTubes)

def main():

	tubeStatusJson = getTubeStatusJson()
	getTubeInfo(tubeStatusJson)

if __name__ == "__main__":
    main()