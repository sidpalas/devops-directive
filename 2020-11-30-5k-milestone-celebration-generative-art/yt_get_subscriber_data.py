import json 

# from yt_channels import get_channel_title_and_thumbnail_url
from yt_studio import get_subscriber_channel_ids

def main(use_cache = True):
    if use_cache:
        with open("channel_ids.json") as f:
            channel_ids = json.load(f)        
    else:
        channel_ids = get_subscriber_channel_ids()


    # Add custom list
    with open("channel_ids_manual.json") as f:
        channel_ids_manual = json.load(f)

    channel_ids.extend(channel_ids_manual)

    if use_cache:
        with open("subscriber_data.json") as f:
            subscriber_data = json.load(f)
    else:
        subscriber_data = {}

    count = 0
    for channel_id in channel_ids:
        count += 1
        if subscriber_data.get(channel_id):
            print(f'{channel_id} subscriber data already exists')
            continue
        title, thumbnail_url = get_channel_title_and_thumbnail_url(channel_id)
        print(count, channel_id, title, thumbnail_url)
        subscriber_data[channel_id] = {
            "title": title,
            "thumbnail_url": thumbnail_url
        }
        

    with open("subscriber_data.json", "w") as f:
        json.dump(subscriber_data, f)


if __name__ == "__main__":
    main()