'''
200 성공, 
400 403 권한, 
404 (사용자가 잘못),
500 서버문제

JSON, XML, 
CSV: 콤마, 세퍼레이트 벨류로 나눠진다?

'''
from typing import AsyncGenerator
import requests
import json

oid='001'
aid='0012604850'

params = {
    'suppress_response_codes': True
    #,‘callback’: ‘jQuery1124005705702844427485_1629261815444’
    ,'q': f'''NEWS[ne_{oid}_{aid}]|NEWS_SUMMARY[417_0000726114]|JOURNALIST[76236(period)]|NEWS_MAIN[ne_417_0000726114]'''
    ,'isDuplication': False
    ,'_':1629261815445
}

response = requests.get('https://news.like.naver.com/v1/search/contents',
                        params=params)

data = json.loads(response.text)
print(data['content'][0]['reactions'])
for d in data['contents'][0]['reactions']:
    result.append({
        d['reactionType']:d['count']
    })
    #print(d['reactionType'])
    #print(d['count'])
print(result)


# 네이버 뉴스에서 oid는 언론사 코드?, aid 키값 oid+aid 이렇게 합치면 유일한 값.


# ---------------------------------------------------------------------------------------------------------------------------

import requests
import json
oid = '001'
aid = '0012604850'
params = {
    'suppress_response_codes': True
    #,‘callback’: ‘jQuery1124005705702844427485_1629261815444’
    ,'q': f'''NEWS[ne_{oid}_{aid}]|NEWS_SUMMARY[{oid}_{aid}]|JOURNALIST[76236(period)]|NEWS_MAIN[ne_{oid}_{aid}]'''
    ,'isDuplication': False
    ,'_':1629261815445
}
response = requests.get('https://news.like.naver.com/v1/search/contents',
                        params=params)
data = json.loads(response.text)
result = []
for d in data['contents'][0]['reactions']:
    result.append({
        d['reactionType']:d['count']
    })
print(result)

#-------------------------------------------------------------------------------------

from typing import AsyncGenerator
import requests
params = {
    ‘suppress_response_codes’: True
    ,‘callback’: ‘jQuery1124005705702844427485_1629261815444’
    ,‘q’: ’NEWS[ne_417_0000726114]|NEWS_SUMMARY[417_0000726114]|JOURNALIST[76236(period)]|NEWS_MAIN[ne_417_0000726114]’
    ,‘isDuplication’: False
    ,‘_’:1629261815445
}
response = requests.get(‘https://news.like.naver.com/v1/search/contents’,
                        params=params)
print(response.text)