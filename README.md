# Satellite Image Segmentation

A TensorFlow / keras implementation of a machine learning algorithm for finding features in satellite imagery.
This uses the DSTL data set as a starting point for training an image segmentation net (https://www.kaggle.com/c/dstl-satellite-imagery-feature-detection).

The neural net used is the UNET for detecting features from an annotated dataset. The layers are set up as outlined in the original paper by Ronneberger, Fischer and Brox (arXiv:1505.04597). The number of channels is set to 10 for the different bands of satellite imaging data and the largest convolutional layer of the net is 512x512x3.

The viewer tool can be used to create annotated data for use in the training and classifying.
