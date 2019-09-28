# Standard imports
import cv2
import numpy as np;

ipath = "D:\\sjh\\B2C\\images\\"
opath = "D:\\sjh\\B2C\\python\\"

import os
for file in os.listdir(ipath):
    if file.endswith(".jpg"):
        print(os.path.join(ipath, file))

        # Read image
        im = cv2.imread(os.path.join(ipath, file), cv2.IMREAD_GRAYSCALE)
         
        # Setup SimpleBlobDetector parameters.
        params = cv2.SimpleBlobDetector_Params()
         
        # Change thresholds
        params.minThreshold = 0;
        params.maxThreshold = 200;
         
        # Filter by Area.
        params.filterByArea = True
        params.minArea = 10
        params.maxArea = 100
         
        # Filter by Circularity
        params.filterByCircularity = True
        params.minCircularity = 0.01
         
        # Filter by Convexity
        params.filterByConvexity = True
        params.minConvexity = 0.087
         
        # Filter by Inertia
        params.filterByInertia = True
        params.minInertiaRatio = 0.01
         
         
        pbig = params
        pbig.minArea = 100
        pbig.maxArea = 1000
         
         
        # Set up the detector with default parameters.
        detector = cv2.SimpleBlobDetector_create(params)
        dbig = cv2.SimpleBlobDetector_create(pbig)
         
        # Detect blobs.
        keypoints = detector.detect(im)
        kbig = dbig.detect(im)
         
        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        im_with_kbig = cv2.drawKeypoints(im_with_keypoints, kbig, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        

        
        # Show keypoints
        #cv2.imshow("Keypoints", im_with_keypoints)
        #cv2.waitKey(0)
        
        #print("Keypoints:")
        #for point in keypoints:
        #    print("point {0} has ")
        
        cv2.imwrite(os.path.join(opath, file),im_with_kbig)

