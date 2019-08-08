# Real-Time Synchronisation of Leap Motion Controller with Wacom Tablet

[![Build Status](https://travis-ci.com/chili-epfl/leap_synchronised.svg?branch=master)](https://travis-ci.com/chili-epfl/leap_synchronised)

<p align="center">
  <img src="https://media.giphy.com/media/UTMEKQJk6hLy9OnHHl/giphy-downsized-large.gif">
</p>

This repository contains the Python code for obtaining data from the Leap Motion sensor **synchronised** with the data from the Wacom tablet. This synchronisation is necessary for integrating LeapMotion and Wacom recordings since the Wacom has a higher frequency than the LeapMotion. The LeapMotion recordings contain the coordinates for the hands, fingers, wrists and elbows. 
The code for obtaining the corresponding data from the Wacom tablet can be found at ```asselbor/tegami``` (```leap-wacom``` branch). This data contains the x-y coordinates for each stroke along with the time and pressure coordinates. The code has been tested and run on a 64-bit system. 

## Requirements
- LeapSDK (can be downloaded [here](https://developer.leapmotion.com/sdk/v2))
- ROS Kinetic
- Standard Python libraries numpy and matplotlib
- asselbor/tegami (leap-wacom branch)

## Getting Started
Copy ```LeapSDK/include/*```, ```LeapSDK/lib/x86/*``` and ```LeapSDK/Leap.py``` into ```LeapSDK/samples/```. Now, replace the file ```LeapSDK/Sample.py``` with ```leap_synchronised/Sample.py```. We are ready to begin!

## Obtaining Synchronised Data
The synchronised data from the Leap Motion sensor and the Wacom tablet can be obtained in two different ways depending on the user's requirements:
- ***Using ROS' ```message_filters.ApproximateTimeSynchronizer```***: This wll print the synchronised data from both the Leap Motion sensor and the Wacom tablet. However, this data will not be sampled at uniform time instants. This may be a requirement for some use cases, for example, if we need to compute the Fourier Transform of the readings. The next method (described in the succeeding point) can be used in such cases. 
*Steps*: Run the code in ```asselbor/tegami``` which will publish the readings from the Wacom tablet to a ROS topic. Open a terminal and run ```Sample.py```, which will publish the data from the Leap Motion sensor to another ROS topic. Now, run the file ```get_data/getDataLeap_ApproximateTimeSynchronizer.py```. 
- ***Using threading to obtain synchronised Leap and Wacom readings***: This will write the Leap and Wacom data to the files ```data/LeapData``` and ```data/WacomData```. These stored readings are synchronised and sampled at ***uniform*** intervals. This overcomes the drawback of the previous method.
*Steps*: Run the code in ```asselbor/tegami``` which will publish the readings from the Wacom tablet to a ROS topic. Open a terminal and run ```Sample.py```, which will publish the data from the Leap Motion sensor to another ROS topic. Now, run the file ```get_data/getDataLeapWacom.py```. 

***[A Side Note] Using threading to obtain data for only the Leap Motion Sensor***: This method is useful if the user wants to obtain the data from Wacom (or any other device like the iPad) separately and carry out the synchronisation process after collecting the data. 
*Steps*: Open a terminal and run ```Sample.py```, which will publish the data from the Leap Motion sensor to a ROS topic. Now, run the file ```get_data/getDataLeap.py```. This will write the Leap data to the file ```data/OnlyLeapData```. 

## Visualisation
The user can visualise the obtained data to verify its correctness. Morever, visualisation will help in getting a better feel and intuitive understanding of the obtained data. The two Jupyter Notebooks, ```visualisation/visualise_leap_data.ipynb``` and ```visualisation/visualise_wacom_data.ipynb```, can be used to visualise the Leap and Wacom data respectively. The former generates a series of images at ```visualisation/visualisation/```, plotting the 3-D coordinates of the hands, fingers, wrists and elbows obtained from the Leap Motion sensor. This can be converted into a video by executing the following command in the terminal: ```avconv -f image2 -i image_%d.png -r 76 -s 800x600 foo.avi```. The latter plots the x-y coordinates of a stroke obtained from the Wacom tablet.

## Other files
The notebook ```utils/check_frequency.ipynb``` can be used to check the frequency of the data obtained from each of the Leap Motion sensor and the Wacom tablet. This is useful since both these devices have different frequencies. It can be used to set the level of approximation in ```message_filters.ApproximateTimeSynchronizer``` (in the first method for obtaining synchronised data) or the threading timer (in the second method for obtaining synchronised data).
The notebooks ```utils/rotate_axes3d.ipynb``` and ```utils/scatter3d.ipynb``` are taken from the matplotlib example notebooks. As the names suggest, they describe how to rotate the axes in 3D and plot a scatter in 3D.
