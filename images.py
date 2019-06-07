#!/usr/bin/env python3


import os
import random

import numpy as np
import tifffile as tiff

import matplotlib.pyplot as plt


folder = '/media/dstl-kaggle/sixteen_band'

filename = random.choice(os.listdir(folder))

print(filename)

class MImage ():
    def __init__(self, filename):
        self.filename = filename
        self._img = tiff.imread(filename)

    def show(self):
        self.get_calibrated_rgb()

        plt.imshow(self._rgb_img)
        plt.show()

    def get_calibrated_rgb(self):
        resolution = self._img.shape[-2:]
        self._rgb_img = np.zeros(resolution + (3,), dtype='uint8')
        channels = [4,2,1]

        calibrations = [(79, 551), (189, 592), (183, 452)]
        target_min = 0
        target_max = 255
        for i in range(3):
            source_min, source_max = calibrations[i]

            values = target_min + (self._img[channels[i],:,:] - source_min) * (target_max - target_min) / (source_max - source_min)
            values[values<target_min] = target_min
            values[values>target_max] = target_max
            self._rgb_img[:,:,i] = values

    def get_rgb(self):
        resolution = self._img.shape[-2:]
        self._rgb_img = np.zeros(resolution + (3,), dtype='uint8')

        lower_percent=2
        higher_percent=98
        target_min = 0
        target_max = 255
        channels = [4,2,1]
        self.thresholds = []
        for i in range(3):
            source_min = np.percentile(self._img[channels[i],:,:], lower_percent)
            source_max = np.percentile(self._img[channels[i],:,:], higher_percent)        
            values = target_min + (self._img[channels[i],:,:] - source_min) * (target_max - target_min) / (source_max - source_min)
            self.thresholds.append((source_min, source_max))
            values[values<target_min] = target_min
            values[values>target_max] = target_max
            self._rgb_img[:,:,i] = values
        #self._rgb_img[:,:,1] = self._img[2,:,:]

def get_random_m_image():
    while True:
        filename = random.choice(os.listdir(folder))
        a,_ = filename.split('.')
        letter = a.split('_')[-1]
        if letter == 'M':
            return filename

def get_all():
    with open('thresholds', 'w') as f:
        for filename in os.listdir(folder):
            a,_ = filename.split('.')
            letter = a.split('_')[-1]
            if letter != 'M':
                continue
            image = MImage(os.path.join(folder,filename))
            image.get_rgb()
            line = filename + ':' + ';'.join([ ','.join(map(str,map(int,_))) for _ in image.thresholds])
            print(line)
            f.write(line + '\n')
     


if __name__ == '__main__':

    filename = get_random_m_image()

    image = MImage(os.path.join(folder,filename))
    image.show()
