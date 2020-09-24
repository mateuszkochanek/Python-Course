import keras
import tensorflow as tf
from tensorflow.keras import optimizers

import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import time



def myMobileNet(alpha):
    num_classes = 10
    inputs = tf.keras.layers.Input(shape=(32, 32, 3))

    x = Conv(inputs, filters=32, kernel_size=3, strides=2, alpha=alpha)
    x = ConvDw(x, filters=32, strides=1, alpha=alpha)
    x = Conv(x, filters=64, kernel_size=1, alpha=alpha)
    x = ConvDw(x, filters=64, strides=2, alpha=alpha)
    x = Conv(x, filters=128, kernel_size=1, alpha=alpha)
    x = ConvDw(x, filters=128, strides=1, alpha=alpha)
    x = Conv(x, filters=128, kernel_size=1, alpha=alpha)
    x = ConvDw(x, filters=128, strides=2, alpha=alpha)
    x = Conv(x, filters=256, kernel_size=1, alpha=alpha)
    x = ConvDw(x, filters=256, strides=1, alpha=alpha)
    x = Conv(x, filters=256, kernel_size=1, alpha=alpha)
    x = ConvDw(x, filters=256, strides=2, alpha=alpha)
    x = Conv(x, filters=512, kernel_size=1, alpha=alpha)
    for i in range( 5 ):
        x = ConvDw(x, filters=512 , strides=1 , alpha=alpha)
        x = Conv(x, filters=512 , kernel_size=1 , alpha=alpha)
    x = ConvDw(x, filters=512, strides=2, alpha=alpha)
    x = Conv(x, filters=1024, kernel_size=1, alpha=alpha)
    x = tf.keras.layers.AveragePooling2D(pool_size=(1, 1))(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(num_classes)(x)
    outputs = tf.keras.layers.Activation('softmax')(x)

    model = tf.keras.models.Model(inputs, outputs)
    return model

def ConvDw( x , filters , strides , alpha=1.0 ):
    x = tf.keras.layers.DepthwiseConv2D( kernel_size=3 , padding='same' )( x )
    x = tf.keras.layers.BatchNormalization(momentum=0.999)( x )
    x = tf.keras.layers.Activation( 'relu' )( x )
    x = tf.keras.layers.Conv2D( np.floor( filters * alpha ) , kernel_size=( 1 , 1 ) , strides=strides , use_bias=False , padding='same' )( x )
    x = tf.keras.layers.BatchNormalization(momentum=0.999)(x)
    x = tf.keras.layers.Activation('relu')(x)
    return x

def Conv( x , filters , kernel_size , strides=1 , alpha=1.0 ):
    x = tf.keras.layers.Conv2D( np.floor( filters * alpha ) , kernel_size=kernel_size , strides=strides , use_bias=False , padding='same' )( x )
    x = tf.keras.layers.BatchNormalization( momentum=0.999 )(x)
    x = tf.keras.layers.Activation('relu')(x)
    return x



(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

x_train = np.array( x_train ) / 255
y_train = np.array( y_train )
x_test = np.array( x_test ) / 255
y_test = np.array( y_test )
model = myMobileNet(1.0)
model.summary()
n_epochs = 5

model.compile(
    optimizer=optimizers.SGD(lr=0.1),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    x=x_train, y=y_train,
    epochs=n_epochs,
)
model.evaluate(x=x_test, y=y_test, verbose=1)