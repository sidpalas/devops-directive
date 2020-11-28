import json 

def main():
  with open("subscriber_data.json") as f:
    subscriber_data = json.load(f)

  subscriber_data_array = []

  for channel_id, subscriber in subscriber_data.items():
    subscriber_data_array.append({
      "channelId": channel_id,
      "title": subscriber['title']
    })

  with open("subscriber_data_array.json", "w") as f:
      json.dump(subscriber_data_array, f)

if __name__ == "__main__":
    main()