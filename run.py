import matplotlib.pyplot as plt
from skimage.io import imread

from segmentation.extract_channel import red_channel, green_channel, blue_channel


__author__ = 'prithvin'


def main():
    oimage_path = "D:/New_folder/personal/prithvi/2015/dr/train/train.001/10_left.jpeg"
    original = imread(oimage_path)

    plt.subplot(221)
    plt.imshow(original)

    plt.subplot(222)
    plt.imshow(red_channel(original))

    plt.subplot(223)
    plt.imshow(green_channel(original))

    plt.subplot(224)
    plt.imshow(blue_channel(original))

    plt.show()

if __name__ == '__main__':
    main()
