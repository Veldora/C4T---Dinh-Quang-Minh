
from skimage.feature import hog
from skimage.io import imread
from sklearn.externals import joblib
import glob
import os
import Last_session.config as lsc
import cv2

    
def extract_features():
    des_type = 'HOG'

    # If feature directories don't exist, create them
    if not os.path.isdir(lsc.pos_feat_ph):
        os.makedirs(lsc.pos_feat_ph)

    # If feature directories don't exist, create them
    if not os.path.isdir(lsc.neg_feat_ph):
        os.makedirs(lsc.neg_feat_ph)

    print( "Calculating the descriptors for the positive samples and saving them")
    for im_path in glob.glob(os.path.join(lsc.pos_im_path, "*")):
        #print im_path

        im = imread(im_path, as_grey=True)
        #cv2.imshow("im",im)
        #cv2.waitKey()
        if des_type == "HOG":
            #print(orientations,pixels_per_cell,cells_per_block,visualize,normalize)
            fd = hog(im, lsc.orientations, lsc.pixels_per_cell, lsc.cells_per_block, None, lsc.visualize, lsc.normalize)
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(lsc.pos_feat_ph, fd_name)
        joblib.dump(fd, fd_path)
    print ("Positive features saved in {}".format(lsc.pos_feat_ph))

    print ("Calculating the descriptors for the negative samples and saving them")
    for im_path in glob.glob(os.path.join(lsc.neg_im_path, "*")):
        im = imread(im_path, as_grey=True)
        if des_type == "HOG":
            fd = hog(im, lsc.orientations, lsc.pixels_per_cell, lsc.cells_per_block, None, lsc.visualize, lsc.normalize)
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(lsc.neg_feat_ph, fd_name)
    
        joblib.dump(fd, fd_path)
    print ("Negative features saved in {}".format(lsc.neg_feat_ph))

    print ("Completed calculating features from training images")

if __name__=='__main__':
    extract_features()
