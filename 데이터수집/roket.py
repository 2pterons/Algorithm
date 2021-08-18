import requests
import json
from bs4 import BeautifulSoup

response = requests.get('')
data = json.loads(response.text)
bs = BeautifulSoup(data['data']['template'], "html.parser")
#print(data['data']['template'])

#bs.find()
#bs.select("")