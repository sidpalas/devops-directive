import cv2
import os

from constants import STYLE_IMAGES
from style_transfer import plain_image, stylize_image

# ### extract frames

video_capture = cv2.VideoCapture('video/test.mp4')
success,image = video_capture.read()
count = 0
while success:
  cv2.imwrite(f"video/frames/frame{count}.jpg", image)     # save frame as JPEG file      
  success,image = video_capture.read()
  print('Read a new frame: ', success)
  count += 1

## stylize frames
count = 0
style_name = 'picasso.jpg'
style_url = 'https://i.pinimg.com/474x/8b/13/56/8b1356ddb41dc38cc2c21275eedb874b.jpg'
while True:
  try:
    frame_url = f"http://localhost:8000/frames/frame{count}.jpg"
    frame_name = f"picasso-frame{count}.jpg"
    stylized_path = f"video/stylized_frames/frame{count}.jpg"
    stylized_image = stylize_image(frame_name, frame_url, style_name, style_url)
    stylized_image.save(stylized_path)
    count += 1
    print(count)
  except:
    break



### reconstruct video
path = "video/stylized_frames/frame0.jpg"
frame = cv2.imread(path)
fps = 30
height,width,_ = frame.shape
video_out = cv2.VideoWriter('video/picasso-out.mp4',cv2.VideoWriter_fourcc(*"mp4v"),fps,(width,height))

count = 0
frame_exists = True
while frame_exists:
  frame = cv2.imread(path)
  video_out.write(frame)
  print("frame written")

  count += 1
  print(count)
  path = f"video/stylized_frames/frame{count}.jpg" 
  frame_exists = os.path.exists(path)


video_out.release()
cv2.destroyAllWindows() 