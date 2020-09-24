import keras

from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
from keras_retinanet.utils.gpu import setup_gpu

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import time

def grab_camera_snapshot(camera_id=0, fallback_filename='zdjecie.jpg'):
    camera = cv2.VideoCapture(camera_id)
    try:
        for i in range(15):
            snapshot_ok, image = camera.read()
        if not snapshot_ok:
            print("Ups: could not access camera")
            if fallback_filename:
                image = read_image_bgr(fallback_filename)
    finally:
        camera.release()
    return image

gpu = 0
setup_gpu(gpu)

# wybieramy model
model_path = os.path.join('.', '', 'resnet50_coco_best_v2.1.0.h5')
model = models.load_model(model_path, backbone_name='resnet50')

labels_to_names = {
    0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane',
    5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light',
    10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench',
    14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow',
    20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack',
    25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee',
    30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite',
    34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard',
    37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass',
    41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl',
    46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli',
    51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake',
    56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed',
    60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse',
    65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave',
    69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book',
    74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear',
    78: 'hair drier', 79: 'toothbrush'}

# ładujemy obrazek, moze byc algo konkretny albo z kamery
image = read_image_bgr('003.jpg')
#image = grab_camera_snapshot()

# tworzenie kopii obrazka po której będziemy malować i którą wyświetlimy
draw = image.copy()
draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)

# przygotowanie obrazka
image = preprocess_image(image)
image, scale = resize_image(image)

# przepuszczenie obrazka przez sieć
start = time.time()
boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))
print("processing time: ", time.time() - start)

# przeskalowanie naszych pudełek ktore będziemy rysować na obrazku
boxes /= scale

# jeżeli score byl > 50 to wtedy rysujemy na obrazku
for box, score, label in zip(boxes[0], scores[0], labels[0]):
    # scores są posortowane więc jak trafimy na mniejszy niż 0.5 to mozemy dalej nie sprawdzać
    # chociaż z ciekawości ustawilem na mniejszy
    # wiecej rysuje, ale i więcej sie myli, czego się spodziwałem
    if score < 0.4:
        break
    color = label_color(label)
    b = box.astype(int)
    draw_box(draw, b, color=color)
    caption = "{} {:.3f}".format(labels_to_names[label], score)
    draw_caption(draw, b, caption)

plt.figure(figsize=(15, 15))
plt.axis('off')
plt.imshow(draw)
plt.show()