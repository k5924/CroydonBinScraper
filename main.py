import requests
import json
from bs4 import BeautifulSoup
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Cookie Headers: grab this from the croydon council website by using inspect element > application tab > cookie dropdown
__CJ_AYA = os.environ.get("LOCATION_COOKIE")

payload = {
    '__CJ_AYA': f'{__CJ_AYA}'
}

# this communicates with croydon councils website to generate a SessionID (this is why the application is a little slow every time you run it)
session = requests.Session()


request = session.post(
    'http://maps.croydon.gov.uk/aya/pages/aya/accessible/index.jsp?page=2', cookies=payload)

page = request.text

soup = BeautifulSoup(page, features="html.parser")
soup.prettify()

data = {"bins": []}

for bins in soup.findAll("div", {"class": "widget-content waste-panel"}):

    binCollection = bins.find_all('li')

    if binCollection:
        for bin in binCollection:
            for date in bin.select('small > strong'):
                dict_data = {
                    "CollectionDate": date.get_text(strip=True),
                    "BinType": bin.find("strong").contents[0],
                }

                # this code ensures that there are no duplicate entries into the data["bins"] dictionary
                if bin.find("strong").contents[0] not in data:
                    data["bins"].append(dict_data)

    else:
        # this prints an error message so you know if anything is wrong with the program
        for message in bins.find_all("div", {"class": "error-message"}):
            print(message.contents[0])

# this just structures the json in a pretty format
json_data = json.dumps(data, indent=4, sort_keys=True)

print(json_data)
