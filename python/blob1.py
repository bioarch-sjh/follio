import cv2

if __name__ == "__main__":

    # Read image
    im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)

    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector_create()

    # the detect function uses a binary image as input for findBlobs 
    # - https://github.com/opencv/opencv/blob/master/modules/features2d/src/blobdetector.cpp
    ret, binary_img = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)

    # we can now call the newly exposed functions so that we can access values used within findBlobs
    # - https://github.com/opencv/opencv/blob/master/modules/features2d/src/blobdetector.cpp
    contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        moments = cv2.moments(contour)
        location = detector.getBlogLocation(moments)

        print("\nArea: ", detector.getArea(moments))
        print("Circularity: ", detector.getCircularity(moments, contour))
        print("Inertia: ", detector.getInertia(moments))
        print("Convexity: ", detector.getConvexity(contour))
        print("Location: ", location)
        print("Radius: ", detector.getBlobRadius(contour, location))

    cv2.imwrite("blob_output.jpg", im)
