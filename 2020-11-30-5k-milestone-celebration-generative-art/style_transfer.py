# https://www.tensorflow.org/tutorials/generative/style_transfer

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
import tensorflow as tf
import tensorflow_hub as hub

mpl.rcParams['figure.figsize'] = (12,12)
mpl.rcParams['axes.grid'] = False

# Load compressed models from tensorflow_hub
os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'


# hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# Use local version of model file (remote version not working for some reason...)
print('make sure to initialize local webserver!')
hub_model = hub.load('http://localhost:8000/magenta_arbitrary-image-stylization-v1-256_2.tar.gz')


def tensor_to_image(tensor):
  tensor = tensor*255
  tensor = np.array(tensor, dtype=np.uint8)
  if np.ndim(tensor)>3:
    assert tensor.shape[0] == 1
    tensor = tensor[0]
  return PIL.Image.fromarray(tensor)


def load_img(path_to_img):
  max_dim = 512 # 1280
  img = tf.io.read_file(path_to_img)
  img = tf.image.decode_image(img, channels=3)
  img = tf.image.convert_image_dtype(img, tf.float32)

  shape = tf.cast(tf.shape(img)[:-1], tf.float32)
  long_dim = max(shape)
  scale = max_dim / long_dim

  new_shape = tf.cast(shape * scale, tf.int32)

  img = tf.image.resize(img, new_shape)
  img = img[tf.newaxis, :]
  return img

def plain_image(image_name, image_url):
  content_path = tf.keras.utils.get_file(image_name, image_url)
  content_image = load_img(content_path)
  return tensor_to_image(content_image)

def stylize_image(content_image_name, content_image_url, style_image_name, style_image_url):
  content_path = tf.keras.utils.get_file(content_image_name, content_image_url)
  style_path = tf.keras.utils.get_file(style_image_name, style_image_url)
  
  content_image = load_img(content_path)
  style_image = load_img(style_path)

  stylized_image_tensor = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
  return tensor_to_image(stylized_image_tensor)



  

