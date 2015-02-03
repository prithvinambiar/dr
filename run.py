import glob

from skimage.io import imread
from matplotlib import pyplot
from segmentation.preprocess import *


__author__ = 'prithvin'


def main():
    directory_names = glob.glob('D:/New folder/personal/prithvi/2015/plankton/train/train/*')
    images = glob.glob(directory_names[0] + '/*')
    interested_image = images[0]
    img = imread(interested_image, as_grey=True)

    pyplot.figure(1)
    pyplot.subplot(321)
    pyplot.imshow(img, cmap=pyplot.cm.get_cmap('gray'))

    binary_image = binary(img)
    pyplot.subplot(322)
    pyplot.imshow(binary_image, cmap=pyplot.cm.get_cmap('gray'))

    dilated_image = dilate(binary_image)
    pyplot.subplot(323)
    pyplot.imshow(dilated_image, cmap=pyplot.cm.get_cmap('gray'))

    labeled_image = label(dilated_image)
    pyplot.subplot(324)
    labeled_image = labeled_image * binary_image
    pyplot.imshow(labeled_image)

    big_image = largest_region(labeled_image)
    pyplot.subplot(325)
    pyplot.imshow(big_image[0], cmap= pyplot.cm.get_cmap('gray'))
    pyplot.show()

if __name__ == '__main__':
    main()
