import requests
import json
from bs4 import BeautifulSoup

results = []

response = requests.get('')
data = json.loads(response.text)
bs = BeautifulSoup(data['data']['template'], "html.parser")
#bs.find()
#print(data['data']['template'])

for company in bs.select(".company.item"):
    
    result = {
         'name' : company.select_one(".company-name strong").text
        ,'description' : company.select_one(".description").text
        ,'job' : []
    }   
    
    #print(company.select(".company-name strong")[0].text
    #name = company.select_one(".company-name strong").text
    #description = company.select_one(".description").text
    #company.select(".job_detail > div > a.job-title")

    for job in company.select(".job-detail > div > a.job-title"):
        result['jobs'].append(job.text)
        #print(job) 
        #print(job.attrs) #안에 있는 옵션을 가져올 수 있다.
        #print(job.text) #텍스트만 가져온다.

    results.append(result)

    print(results)

#------------------------------------------------------------------------------------------------------------------------------------

#while문으로 해보자
#True경우만 반복하다가 False가 나오면 중단하는 형식

import requests
import json
from bs4 import BeautifulSoup

results = []
page = 0

while page < 3:

    response = requests.get('https://www.rocketpunch.com/api/jobs/template?page=' + str(page) + '&q=')
    data = json.loads(response.text)
    bs = BeautifulSoup(data['data']['template'], "html.parser")
    #bs.find()
    #print(data['data']['template'])

    for company in bs.select(".company.item"):
        
        result = {
            'name' : company.select_one(".company-name strong").text
            ,'description' : company.select_one(".description").text
            ,'job' : []
        }   
        
        #print(company.select(".company-name strong")[0].text
        #name = company.select_one(".company-name strong").text
        #description = company.select_one(".description").text
        #company.select(".job_detail > div > a.job-title")

        for job in company.select(".job-detail > div > a.job-title"):
            result['jobs'].append(job.text)
            #print(job) 
            #print(job.attrs) #안에 있는 옵션을 가져올 수 있다.
            #print(job.text) #텍스트만 가져온다.

        results.append(result)

        print(results)
        page += 1

#------------------------------------------------------------------------------------------------------------------------------------

import requests
import json
from bs4 import BeautifulSoup
results = []
page = 1
while page < 3:
    response = requests.get(‘https://www.rocketpunch.com/api/jobs/template?page=’ + str(page) + ‘&q=’)
    data = json.loads(response.text)
    bs = BeautifulSoup(data[‘data’][‘template’], “html.parser”)
    for company in bs.select(“.company.item”):
        result = {
            ‘name’: company.select_one(“.company-name strong”).text
            ,‘description’: company.select_one(“.description”).text
            ,‘jobs’: []
        }
        #name = company.select_one(“.company-name strong”).text
        #description = company.select_one(“.description”).text
        for job in company.select(“.job-detail > div > a.job-title”):
            result[‘jobs’].append(job.text)
        results.append(result)
    print(results)
    page += 1