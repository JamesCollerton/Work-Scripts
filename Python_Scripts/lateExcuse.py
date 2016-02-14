import requests



def main():
	r = requests.get('https://api.tfl.gov.uk/line/mode/tube/status')
	print(r.json()[1])

if __name__ == "__main__":
    main()