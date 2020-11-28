# -*- coding: utf-8 -*-

# Sample Python code for youtube.subscriptions.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "google_oauth_client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    next_page_token = ''
    subscriber_dict = {}
    count = 0
    
    while next_page_token != None:
        print("Getting next page:", next_page_token, count)

        request = youtube.subscriptions().list(
            part="subscriberSnippet",
            maxResults=1,
            mySubscribers=True,
            pageToken=next_page_token
        )
        response = request.execute()
        next_page_token = response.get('nextPageToken')

        subscribers = response.get('items')
        for subscriber in subscribers:
            count += 1
            snippet = subscriber.get('subscriberSnippet')
            channel_id = snippet.get('channelId')
            title = snippet.get('title')
            url = snippet['thumbnails']['high']['url']
            subscriber_dict[channel_id] = {
                'title': title,
                'url': url
            }

    print('Total subscribers:', count)

    with open('subscribers.json', 'w') as f:
        json.dump(subscriber_dict, f)


if __name__ == "__main__":
    main()