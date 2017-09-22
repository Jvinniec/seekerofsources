# seekerofsources
SoS implements a convolutional neural network (CNN) for finding/classifying 
objects in astronomy data. I would really like this to have a C++ interface,
but at the moment it looks like the TensorFlow C++ API is insufficient to
easily make this doable. So, in the meantime the approach will be to code in
Python (3.6+!!!) and possibly make an interface to the Python code in C++.

# TODO before initial release
* Flesh out codebase
* Define README sections

# Dependencies
TensorFlow (described [here](https://www.tensorflow.org/)) is the primary 
external dependency. This is the code base that implements the actual machine
learning components.

cfitsio ([here](https://heasarc.gsfc.nasa.gov/fitsio/fitsio.html)) is also 
required in order to create/update FITS files.

# Downloading


# Installing


# A quick example
To see an example of how to use the SoS library, please check out the tutorial
directory. You should start with `tutorial/Guide.md` for a walk-through of the
tutorial.

# For Developers
Please see the included guidelines in `Developers.md` file.