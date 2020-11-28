import json
import requests


SUBS_PER_QUERY = 1000


def get_subscribers(auth_hash, cookie_string, page_token):
    headers = {
        "authorization": f"SAPISIDHASH {auth_hash}",
        "content-type": "application/json",
        "origin": "https://studio.youtube.com",
        "referer": "https://studio.youtube.com/channel/UC4MdpjzjPuop_qWNAvR23JA",
        "cookie": cookie_string,
    }

    params = (
        ("alt", "json"),
        ("key", "AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo"),
    )

    data = (
        '{"query":{"externalChannelId":"UC4MdpjzjPuop_qWNAvR23JA","order":"SUBSCRIBER_ORDER_SUBSCRIBER_COUNT_DESC","subscribedAfter":{"seconds":"0"},"numSubscriptionsRequested":"'
        + str(SUBS_PER_QUERY)
        + '"},"pageToken":"'
        + page_token
        + '","mask":{"channelId":true,"thumbnailDetails":{"all":true},"title":true,"metric":{"all":true},"permissions":{"all":true}},"context":{"client":{"clientName":62,"clientVersion":"1.20201118.04.00","hl":"en","gl":"US","experimentsToken":"","utcOffsetMinutes":-300},"request":{"returnLogEntry":true,"internalExperimentFlags":[{"key":"force_route_delete_playlist_to_outertube","value":"false"},{"key":"force_live_chat_merchandise_upsell","value":"false"}]},"user":{"onBehalfOfUser":"103601053026800248569","delegationContext":{"roleType":{"channelRoleType":"CREATOR_CHANNEL_ROLE_TYPE_OWNER"},"externalChannelId":"UC4MdpjzjPuop_qWNAvR23JA"},"serializedDelegationContext":"EhhVQzRNZHBqempQdW9wX3FXTkF2UjIzSkEqAggI"},"clientScreenNonce":"MC4zODQ3NDA5OTk2NzA1NzU5Ng.."}}'
    )

    response = requests.post(
        "https://studio.youtube.com/youtubei/v1/creator/list_creator_public_subscribers",
        headers=headers,
        params=params,
        data=data,
    )

    return response.json()


def get_subscriber_channel_ids():
    auth_hash = "1606073822_7532238984badf6ac0d42443b914ae0b4f9a7fbb"
    cookie_string = "VISITOR_INFO1_LIVE=PNuwI5zZ3DI; _ga=GA1.2.1587387558.1581554964; NID=204=XbStKwc0B-HShVS9nVneX8sJQYjWvH8mqBCi5xpXcvT0Kjm7nbsx5O3nixMY3DjRqioegXESC5qqP32KOETkO5pnLUCoB2UzhhgcsJKdqdqhRAPn8sD2wJqVQmXgM55RiFL9NOgIPRFKXT39DHeaNioHUFGJKlvcOsgrU2QZDXl6O6P07oGF6kwutRSnquJVmWgbdrGHvwO9NsMo2ESI; PREF=cvdm=grid&f5=30030&al=en&f6=40000000&f4=4000000; LOGIN_INFO=AFmmF2swRAIgQWhXw1tnwdkfE5knKYiu3BtdZYs2trUbs7dhAYVUMVsCIF4YjvPcUN7_o9Zlnm8uzoT3ZGh1j3E9ZdO6LoliLkxI:QUQ3MjNmeUpNTXpZcVpROTBlVlVaMGtLVENSODhZQTRCY0huQjItWi1vNEpKUWpTaE8wakJGUC1zYUlnNU42aVZFQ215MzI3UWFIUnU0YURDZ3R6R1N5RlJBZk9GVUJMc05JQU5rN1kycDRhempCbXNGTXYyMkJOcmdGTGVCVi1CRG1SOVA3YnRTNm9rOE45RHp5NU0wSnJYT2ZnNGN3WGhSb2FmY2ljLURHWGhZY050SjdiX2NkNkwtU3dpODNndDRpc3Z6ZmFWQlBDS3lGRWhsR1ZCN1EzbzFGczAwbE8zLWNaM1UwRkVlank3TGxtQUlQOW5vTHJQbTBZdmlDTVhpMTBGZEJyYTVVSQ==; SID=3gcu7z3tB22JClt_h7RVw6dClerpAuj8zwrhs7F9jcuQSRlbzRbs1aUuuUMmXzvuz7zKzg.; __Secure-3PSID=3gcu7z3tB22JClt_h7RVw6dClerpAuj8zwrhs7F9jcuQSRlbXV0m6uVS6O4imDpbZmfT7w.; HSID=Ab3NESEb40Lfvg7_K; SSID=AdS0sFiaaqIwK-3lc; APISID=GkhkPEsHGW0YpjJm/AB2VsILdygTNA1Iyy; SAPISID=Mp0Ie6ilqJYXsrZW/A_Pj_XfbcU1iJ7Y7a; __Secure-3PAPISID=Mp0Ie6ilqJYXsrZW/A_Pj_XfbcU1iJ7Y7a; YSC=lo6erDAu-mc; wide=1; tb-quick-edit-toolbar-dataUC4MdpjzjPuop_qWNAvR23JA=%7B%22url%22%3A%22https%3A//studio.youtube.com/channel/UC4MdpjzjPuop_qWNAvR23JA/videos/upload%3Ffilter%3D%255B%255D%26sort%3D%257B%2522columnType%2522%253A%2522date%2522%252C%2522sortOrder%2522%253A%2522DESCENDING%2522%257D%22%2C%22page%22%3A1%2C%22videos%22%3A%5B%5D%2C%22description%22%3A%22This%20list%20currently%20shows%20videos%20that%20were%20last%20displayed%20on%20your%20%3Ca%20href%3D%5C%22https%3A//studio.youtube.com/channel/UC4MdpjzjPuop_qWNAvR23JA/videos/upload%3Ffilter%3D%255B%255D%26sort%3D%257B%2522columnType%2522%253A%2522date%2522%252C%2522sortOrder%2522%253A%2522DESCENDING%2522%257D%5C%22%3EMy%20Videos%3C/a%3E%20page.%22%7D; YTC=rel|1606074376; SIDCC=AJi4QfHRmSzXiyAgwOpZqY61SsQMUY5vP_xkfstPRJYbrPto_ncMpLw-bV2TmSRm6ePJtVmyGQI; __Secure-3PSIDCC=AJi4QfE9LKYwkQHNIgNlev1Z0Uz1__CHqG0_9vhzLl9ljxALIudg7GgDfGfUGHjtbFGN809edok"
    next_page_token = ""

    count = 0
    channel_ids = []

    while next_page_token != None:
        subscriber_api_response = get_subscribers(
            auth_hash, cookie_string, next_page_token
        )

        next_page_token = subscriber_api_response.get("nextPageToken")
        subscribers = subscriber_api_response.get("creatorChannelData")
        for subscriber in subscribers:
            channel_ids.append(subscriber["channelId"])

        print(next_page_token, count)
        count += SUBS_PER_QUERY


    with open("channel_ids.json", "w") as f:
        json.dump(channel_ids, f)

    return channel_ids


if __name__ == "__main__":
    get_subscriber_channel_ids()
