import requests
import json
import time

magazineOffset = 0
contestOffset = 0
exhibitOffset = 0
galleryOffset = 0

for i in range(10): # 0~9
    params = {
    #magazineOffset=0&contestOffset=0&exhibitOffset=0&galleryOffset=0
    'magazineOffset':magazineOffset
    ,'contestOffset':contestOffset
    ,'exhibitOffset':exhibitOffset
    ,'galleryOffset':galleryOffset
    }

    response = requests.get("https://www.jungle.co.kr/recent.json", params=params)
    print(response.text)

    magazineOffset = data['magazineOffset'] #0
    contestOffset = data['contestOffset'] #6
    exhibitOffset = data['exhibitOffset'] #0
    galleryOffset = data['galleryOffset'] #0

    time.sleep(1) #너무 빨리 크롤링 하면 보안상 문제가 될 수 있으니 일정한 텀?을 가지고 돌리게하는 것.

    # 리스트나 딕셔너리를 가져오고 바꾸고 개지랄하는 연습이 필요
    # 반복문도 연습할 것.

    for d in data['moreList']:
        print(d['title'])
        print(d['targetCo'])

    #print(data['moreList'])    

# 이렇게 10페이지를 가져올 수 있다.
# 전부 다 가져오고 싶은 경우 existMore이 False가 될 때 까지 돌리면 된다.

# ------------
import requests
import json
import time
magazineOffset = 0
contestOffset = 0
exhibitOffset = 0
galleryOffset = 0
for i in range(10): # 0~9
    params = {
        ‘magazineOffset’: magazineOffset
        ,‘contestOffset’: contestOffset
        ,‘exhibitOffset’: exhibitOffset
        ,‘galleryOffset’: galleryOffset
    }
    response = requests.get(“https://www.jungle.co.kr/recent.json”, params=params)
    data = json.loads(response.text)
    for d in data[‘moreList’]:
        print(d[‘title’])
        print(d[‘targetCode’])
    magazineOffset = data[‘magazineOffset’] #0
    contestOffset = data[‘contestOffset’] #6
    exhibitOffset = data[‘exhibitOffset’] #0
    galleryOffset = data[‘galleryOffset’] #0
    time.sleep(1)
#print(data[‘moreList’])
