import requests
import json


def getTweet(query):

    headers = {
        'accept': '*/*'
        #,'accept-encoding': 'gzip, deflate, br'
        #,'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
        ,'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
        #,'content-type': 'application/json'
        #,'cookie': '_ga=GA1.2.443444804.1615563358; _gid=GA1.2.457209665.1629116764; G_ENABLED_IDPS=google; kdt=Lp98UdnEy0tpxDqvVwU2t9lH6l5zA9HyNnOFHZsA; mbox=session#984bf879573b4efea62ffc86ea0d61bf#1629121941|PC#984bf879573b4efea62ffc86ea0d61bf.32_0#1692366092; dnt=1; lang=en; _sl=1; personalization_id="v1_Q3SpJaz6SfmfYvkjjRLRJA=="; guest_id=v1%3A162934951370851813; undefined; G_AUTHUSER_H=0; gt=1428221493305962497; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D'
        #,'referer': 'https://twitter.com/metaversekorea_'
        #,'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"'
        #,'sec-ch-ua-mobile': '?0'
        #,'sec-fetch-dest': 'empty'
        #,'sec-fetch-mode': 'cors'
        #,'sec-fetch-site': 'same-origin'
        ,'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        #,'x-csrf-token': '0834ca21b9f4b7389da8dbe07b299062'
        ,'x-guest-token': '1428221493305962497'
        #,'x-twitter-active-user': 'yes'
        #,'x-twitter-client-language': 'ko'
    }

    variables = {
        "screen_name": query
        ,"withSafetyModeUserFields": True
        ,"withSuperFollowsUserFields": False
    }

    # Dict -> JSON(text)
    # json.dumps(dict)
    # JSON(text) -> Dict
    # json.loads("")

    params = {
        'variables': json.dumps(variables)
    }

    response = requests.get("https://twitter.com/i/api/graphql/LPilCJ5f-bs3MjJJNcuuOw/UserByScreenName", headers=headers, params=params)
    data = json.loads(response.text)
    rest_id = data['data']['user']['result']['rest_id']


    # variables = {
    #     "userId": rest_id,
    #     "count": 20,
    #     "withTweetQuoteCount": True,
    #     "includePromotedContent": True,
    #     "withSuperFollowsUserFields": False,
    #     "withUserResults":True,
    #     "withBirdwatchPivots": False,
    #     "withReactionsMetadata": False,
    #     "withReactionsPerspective": False,
    #     "withSuperFollowsTweetFields": False,
    #     "withVoice": True
    # }

    # params = {
    #     'variables': json.dumps(variables)
    # }


    # response2 = requests.get("https://twitter.com/i/api/graphql/PIt4K9PnUM5DP9KW_rAr0Q/UserTweets", params=params, headers=headers)
    # tweet_data = json.loads(response2.text)

    # # get tweeet
    # for tweet in tweet_data['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries']:

    #     try:
    #         print(tweet['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
    #     except:
    #         pass

    # cursor = tweet_data['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries'][-1]['content']['value']

    cursor = ''

    for i in range(5):
        #두번째
        variables = {
            "userId": rest_id,
            "count": 20,
            "withTweetQuoteCount": True,
            "includePromotedContent":True,
            "withSuperFollowsUserFields": False,
            "withUserResults":True,
            "withBirdwatchPivots":False,
            "withReactionsMetadata":False,
            "withReactionsPerspective":False,
            "withSuperFollowsTweetFields":False,
            "withVoice":True
        }

        if cursor != '':
            variables["cursor"] = cursor

        params = {
            'variables': json.dumps(variables)
        }


        response2 = requests.get("https://twitter.com/i/api/graphql/PIt4K9PnUM5DP9KW_rAr0Q/UserTweets", params=params, headers=headers)
        tweet_data = json.loads(response2.text)

        # get tweeet
        for tweet in tweet_data['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries']:

            try:
                print(tweet['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
            except:
                pass

        cursor = tweet_data['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries'][-1]['content']['value']
        # print(cursor)


getTweet("dondaeji")

# ====================================================================================================================================================
import requests
import json


def getTweet(query):

    headers = {
        'accept': '*/*'
        ,'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
        ,'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        ,'x-guest-token': '1428221493305962497'
    }

    variables = {
        "screen_name": query
        ,"withSafetyModeUserFields": True
        ,"withSuperFollowsUserFields": False
    }

    params = {
        'variables': json.dumps(variables)
    }

    response = requests.get("https://twitter.com/i/api/graphql/LPilCJ5f-bs3MjJJNcuuOw/UserByScreenName", headers=headers, params=params)
    data = json.loads(response.text)
    rest_id = data['data']['user']['result']['rest_id']

    cursor = ''

    for i in range(5):

        variables = {
            "userId": rest_id,
            "count": 20,
            "withTweetQuoteCount": True,
            "includePromotedContent":True,
            "withSuperFollowsUserFields": False,
            "withUserResults":True,
            "withBirdwatchPivots":False,
            "withReactionsMetadata":False,
            "withReactionsPerspective":False,
            "withSuperFollowsTweetFields":False,
            "withVoice":True
        }

        if cursor != '':
            variables["cursor"] = cursor

        params = {
            'variables': json.dumps(variables)
        }


        response2 = requests.get("https://twitter.com/i/api/graphql/PIt4K9PnUM5DP9KW_rAr0Q/UserTweets", params=params, headers=headers)
        tweet_data = json.loads(response2.text)

        # get tweeet
        for tweet in tweet_data['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries']:

            try:
                print(tweet['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
            except:
                pass

        cursor = tweet_data['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries'][-1]['content']['value']


getTweet("dondaeji")

'''
import requests
import json
headers = {
     ‘accept’: ‘*/*’
    ,‘accept-encoding’: ‘gzip, deflate, br’
    ,‘accept-language’: ‘ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7’
    ,‘authorization’: ‘Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA’
    ,‘content-type’: ‘application/json’
    ,‘cookie’: ‘_ga=GA1.2.443444804.1615563358; _gid=GA1.2.457209665.1629116764; G_ENABLED_IDPS=google; kdt=Lp98UdnEy0tpxDqvVwU2t9lH6l5zA9HyNnOFHZsA; mbox=session#984bf879573b4efea62ffc86ea0d61bf#1629121941|PC#984bf879573b4efea62ffc86ea0d61bf.32_0#1692366092; dnt=1; lang=en; _sl=1; personalization_id=“v1_Q3SpJaz6SfmfYvkjjRLRJA==“; guest_id=v1%3A162934951370851813; undefined; G_AUTHUSER_H=0; gt=1428221493305962497; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D’
    ,‘referer’: ‘https://twitter.com/metaversekorea_’
    ,‘sec-ch-ua’: ‘“Chromium”;v=“92", ” Not A;Brand”;v=“99”, “Google Chrome”;v=“92”’
    ,‘sec-ch-ua-mobile’: ‘?0’
    ,‘sec-fetch-dest’: ‘empty’
    ,‘sec-fetch-mode’: ‘cors’
    ,‘sec-fetch-site’: ‘same-origin’
    ,‘user-agent’: ‘Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36’
    ,‘x-csrf-token’: ‘0834ca21b9f4b7389da8dbe07b299062’
    ,‘x-guest-token’: ‘1428221493305962497’
    ,‘x-twitter-active-user’: ‘yes’
    ,‘x-twitter-client-language’: ‘ko’
}
response = requests.get(“https://twitter.com/i/api/graphql/LPilCJ5f-bs3MjJJNcuuOw/UserByScreenName?variables=%7B%22screen_name%22%3A%22metaversekorea_%22%2C%22withSafetyModeUserFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Afalse%7D”, headers=headers)
print(response)

# =====================================================================================================================================

import requests
import json
headers = {
     ‘accept’: ‘*/*’
    #,‘accept-encoding’: ‘gzip, deflate, br’
    #,‘accept-language’: ‘ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7’
    ,‘authorization’: ‘Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA’
    #,‘content-type’: ‘application/json’
    #,‘cookie’: ‘_ga=GA1.2.443444804.1615563358; _gid=GA1.2.457209665.1629116764; G_ENABLED_IDPS=google; kdt=Lp98UdnEy0tpxDqvVwU2t9lH6l5zA9HyNnOFHZsA; mbox=session#984bf879573b4efea62ffc86ea0d61bf#1629121941|PC#984bf879573b4efea62ffc86ea0d61bf.32_0#1692366092; dnt=1; lang=en; _sl=1; personalization_id=“v1_Q3SpJaz6SfmfYvkjjRLRJA==“; guest_id=v1%3A162934951370851813; undefined; G_AUTHUSER_H=0; gt=1428221493305962497; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D’
    #,‘referer’: ‘https://twitter.com/metaversekorea_’
    #,‘sec-ch-ua’: ‘“Chromium”;v=“92", ” Not A;Brand”;v=“99”, “Google Chrome”;v=“92”’
    #,‘sec-ch-ua-mobile’: ‘?0’
    #,‘sec-fetch-dest’: ‘empty’
    #,‘sec-fetch-mode’: ‘cors’
    #,‘sec-fetch-site’: ‘same-origin’
    ,‘user-agent’: ‘Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36’
    #,‘x-csrf-token’: ‘0834ca21b9f4b7389da8dbe07b299062’
    ,‘x-guest-token’: ‘1428221493305962497’
    #,‘x-twitter-active-user’: ‘yes’
    #,‘x-twitter-client-language’: ‘ko’
}
variables = {
    “screen_name”: “metaversekorea_”
    ,“withSafetyModeUserFields”: True
    ,“withSuperFollowsUserFields”: False
}
# Dict -> JSON(text)
# json.dumps(dict)
# JSON(text) -> Dict
# json.loads(“”)
params = {
    ‘variables’: json.dumps(variables)
}
response = requests.get(“https://twitter.com/i/api/graphql/LPilCJ5f-bs3MjJJNcuuOw/UserByScreenName”, headers=headers, params=params)
data = json.loads(response.text)
rest_id = data[‘data’][‘user’][‘result’][‘rest_id’]

#=====================================================================================================================================================
import requests
import json

headers = {
     'accept': '*/*'
    #,'accept-encoding': 'gzip, deflate, br'
    #,'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
    ,'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
    #,'content-type': 'application/json'
    #,'cookie': '_ga=GA1.2.443444804.1615563358; _gid=GA1.2.457209665.1629116764; G_ENABLED_IDPS=google; kdt=Lp98UdnEy0tpxDqvVwU2t9lH6l5zA9HyNnOFHZsA; mbox=session#984bf879573b4efea62ffc86ea0d61bf#1629121941|PC#984bf879573b4efea62ffc86ea0d61bf.32_0#1692366092; dnt=1; lang=en; _sl=1; personalization_id="v1_Q3SpJaz6SfmfYvkjjRLRJA=="; guest_id=v1%3A162934951370851813; undefined; G_AUTHUSER_H=0; gt=1428221493305962497; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D'
    #,'referer': 'https://twitter.com/metaversekorea_'
    #,'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"'
    #,'sec-ch-ua-mobile': '?0'
    #,'sec-fetch-dest': 'empty'
    #,'sec-fetch-mode': 'cors'
    #,'sec-fetch-site': 'same-origin'
    ,'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    #,'x-csrf-token': '0834ca21b9f4b7389da8dbe07b299062'
    ,'x-guest-token': '1428221493305962497'
    #,'x-twitter-active-user': 'yes'
    #,'x-twitter-client-language': 'ko'
}

variables = {
    "screen_name": "metaversekorea_"
    ,"withSafetyModeUserFields": True
    ,"withSuperFollowsUserFields": False
}

# Dict -> JSON(text)
# json.dumps(dict)
# JSON(text) -> Dict
# json.loads("")

params = {
    'variables': json.dumps(variables)
}

response = requests.get("https://twitter.com/i/api/graphql/LPilCJ5f-bs3MjJJNcuuOw/UserByScreenName", headers=headers, params=params)
data = json.loads(response.text)
rest_id = data['data']['user']['result']['rest_id']

'''

