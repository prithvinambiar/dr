import numpy

__author__ = 'prithvin'

def red_channel(rgb_image):
    img = numpy.copy(rgb_image)
    img[:, :, 1] = 0
    img[:, :, 2] = 0
    return img

def green_channel(rgb_image):
    img = numpy.copy(rgb_image)
    img[:, :, 0] = 0
    img[:, :, 2] = 0
    return img

def blue_channel(rgb_image):
    img = numpy.copy(rgb_image)
    img[:, :, 0] = 0
    img[:, :, 1] = 0
    return img
