import json
import os

from constants import STYLE_IMAGES
from style_transfer import plain_image, stylize_image

def main():
  with open('./subscriber_data.json') as f:
    subscriber_data = json.load(f)

  count = 0
  for channel_id, subscriber in subscriber_data.items():
    sub_name = ''.join(e for e in subscriber.get("title") if e.isalnum())
    sub_url = subscriber.get("thumbnail_url")
    print(count, channel_id, sub_name, sub_url)
    print('\n')
    channel_path = os.path.join(os.getcwd(), "photos", channel_id)
    os.makedirs(channel_path, exist_ok=True)

    image_path = os.path.join(channel_path, "unstylized.jpg")
    unstylized_image = plain_image(sub_name, sub_url)
    # unstylized_image.show()
    unstylized_image.save(image_path)

    for style_name, style_url in STYLE_IMAGES.items():
      image_path = os.path.join(channel_path,style_name)
      if not os.path.exists(image_path):  
        stylized_image = stylize_image(sub_name, sub_url, style_name, style_url)
        # stylized_image.show()
        stylized_image.save(image_path)
    
    count += 1

    


if __name__ == "__main__":
  main()