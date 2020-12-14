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
        ("key", "AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo")
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
    print("Get auth_hash and cookie from network request in YT studio!")
    auth_hash = ""
    cookie_string = ""
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
