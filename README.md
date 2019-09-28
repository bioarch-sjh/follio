# follio
Tools for analysing follicles in parchment



# Installation

*Installation is complicated becuase it depends on a custom version of openCV*



https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/


```
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_PYTHON_EXAMPLES=OFF -D INSTALL_C_EXAMPLES=OFF -D OPENCV_ENABLE_NONFREE=ON -D OPENCV_EXTRA_MODULES_PATH=~/git/opencv_contrib/modules -D PYTHON_EXECUTABLE=~/.virtualenvs/cv_4.1.0/bin/python -D BUILD_EXAMPLES=OFF -D BUILD_opencv_python3=yes ..
```

# Running

## Virtual environment

*To list the virtual environments, do `lsvirtualenv`*




-----
# Simon's original email

Dear all

I've managed to push Laura's images through an 'off the shelf' python/openCV blob detector based on this tutorial: 

https://www.learnopencv.com/blob-detection-using-opencv-python-c/ 

I've tweaked the thresholds a bit to be as inclusive as is reasnoable in order to get the results. I'm sharing these mainly because I want to reach consensus on what is possible, and where we should go 

please find the images in the folder "FollicleAnalysis -> 190423PythonBlobDetector" in the B2C Team Drive (I can't seem to get a shareable link on this folder). The python code that generated these images is also in there - please let me know if you want to use it and I'll try to help - it has some folder paths that are unique to my laptop in there at the moment, and you'll need to install python3 and openCV. 

Some observations: 

The follicles that have been detected are shown as green rings. The size of the circle is proportionate to the size of the blob as measured by the detector
For a first pass, it's doing a pretty good job of picking up most of the follicles
The detection is sufficiently good I think to be able to spot arrangements of follicles in the rings - groups of 3 or four follicles are commonly seen
I don't have any metadata, so I'm not able to say what we should expect to see with confidence in these - in this regard your comments are very welcome!
Note this code works on greyscale images - there may be information in the colour that we can work with
there is a nice range of contrasts in this image library that indicates what's likely to be possible moving forward

next steps are

Getting the shape statistics out of the blob detecter - this will require some more extensive codeing
Attempting to make a 'mesh' from the detected blobs to see if any consistent features can be seen in the clusters of follicles

I hope this is useful! I'll also make a start on running the MALDI data through the bacollite code

Simon

-----
# Mike Sole's original notes

## Mike Sole 2:24 PM

Hi Simon - I have just had a look at the blob detection stuff
If you haven't already found it, the source code the simple blob detector can be found here:
https://github.com/opencv/opencv/blob/master/modules/features2d/src/blobdetector.cpp

As you can see there is about 200 lines of core code for the simple blob detector. The code uses a lot of contour feature functionality which can be found here:
https://docs.opencv.org/4.1.1/dd/d49/tutorial_py_contour_features.html

I can see that you want to access information within sub-blocks of findBlobs e.g. "if (params.filterByArea)", "if (params.filterByCircularity)", "if (params.filterByInertia)", if (params.filterByConvexity). I propose that we extract each block into a function so that you can use them however you want to. (edited) 

https://github.com/opencv/opencv/blob/master/modules/features2d/src/blobdetector.cpp

Here is a link to a zip file. The zip file contains two folders, "opencv" contains the whole source code of opencv with my changes included. opencv_contrib contains the source code for additional opencv libraries. Both folders are git repositories, you can use git status and git diff to see my changes. https://www.dropbox.com/s/t371pcgp4i5igfn/custom_opencv.zip?dl=0

Unzip https://www.dropbox.com/s/t371pcgp4i5igfn/custom_opencv.zip?dl=0 within ~/git/

So that you have ~/git/opencv and ~/git/opencv_contrib
Then create a python virtual environment following the steps shown here ONLY CREATE THE VIRTUAL ENVIRONMENT, DO NOT FOLLOW THE TUTORIAL TO INSTALL OPENCV, I'LL OUTLINE THAT IN THE SUBSEQUENT MESSAGE  https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/. I used the virtual environment name of "cv_4.1.0" (edited) 






















