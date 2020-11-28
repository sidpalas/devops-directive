import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "google_oauth_client_secret.json"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes
)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials
)


def get_channel_title_and_thumbnail_url(channel_id):
    request = youtube.channels().list(part="snippet", id=channel_id)
    response = request.execute()
    snippet = response["items"][0]["snippet"]
    title = snippet["title"]
    thumbnail_url = snippet["thumbnails"]["high"]["url"]
    return title, thumbnail_url


def main():
    channel_ids = ["UC4MdpjzjPuop_qWNAvR23JA"]
    for channel_id in channel_ids:
        title, thumbnail_url = get_channel_title_and_thumbnail_url(
            channel_id
        )
        print(title, thumbnail_url)

if __name__ == "__main__":
    main()
