# cell-segmentation
In this work, cell segmentation was carried out through U-net. Segmented microscopic images were introduced to the neural network model with an annotation tool using OpenCV. 

This is a supervised algorithm to predict the segmentation of raw microscopic images using U-net architecture. The following process has been done to carry out cell segmentation process:

1- Because this is a supervised method we need annotated images from original raw microscopic images. To have annotated pictures, the cell_annot.py code was utilised. 

2- Once annotated images created, then unet_segment.py code was implemented to train the U-net neural network with raw and annotated images. 

3- Finally we are ready to predict any microscopic images to do cell segmentation process at the end!

Hope this can help there in computer vision projects!

