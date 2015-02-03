"""
Provides all sorts of methods to pre-process image
"""
from skimage import morphology, measure
import numpy
from scipy import ndimage
from skimage.measure import regionprops

__author__ = 'prithvin'

# Takes in a gray scale image numpy array and converts it into binary
def binary(img):
    mean = img.mean()
    binary_image = (numpy.uint8)(img < mean)
    return binary_image


# Takes in a binary image and dilates
def dilate(binary_img):
    # assert isinstance(binary_img.dtype, numpy.ndarray)
    # dilated_image = ndimage.binary_dilation(binary_img, ndimage.generate_binary_structure(2, 1)).astype(
    # binary_img.dtype)
    str = ndimage.generate_binary_structure(2, 2)
    dilated_image = morphology.dilation(binary_img, str)
    return dilated_image


def label(dilated_img):
    labeled_img = measure.label(dilated_img)
    return labeled_img


def largest_region(labeled_img):
    regions = regionprops(labeled_img, 'PixelIdxList')
    # print regions[0].coords
    # largest_region = labeled_img(regions[:, 0], regions[:, 1])
    return (regions[0].image, regions[0].moments_hu)
    # for r in regions:
    #     print str(r.label) + ' => ' + str(r.area)
    # return