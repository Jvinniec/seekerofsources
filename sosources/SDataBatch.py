# ==========================================================================
# SDataBatch.py
# ==========================================================================
# Copyright (C) 2017 J. V. Cardenzana
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ==========================================================================
# Description:
#       This class is responsible for storing batches of SData (or inherited)
#       objects. It also handles obtaining batches of data used in training.
# ===========================================================================

import sosources as sos
import numpy as np

class SDataBatch:
    """ Class responsible for storing batches of data and using it in training
    """

    def __init__(self):
        """ Class initializer
        """
        # Data members
        self._data = []             # Array of data objects
        self._class_ids = []        # Classification IDs
        self._load_random = True    # Specifies whether or not images are
                                    # loaded at random or sequentially
        self._batch_position = 0
        self._test_fraction = 0.1   # Fraction of images reseved for testing


    def AppendData(self, file="", classification=""):
        """ Load a single file with a given classification

        @param[in] file                 Filename to be loaded
        @param[in] classification       Image classification
        """
        # Create a new image object
        image = sos.SData

        # Set the image properties (filename and classification)
        image.Filename(file)
        image.Classification(classification)

        # Append this object to the list of images
        self._data.append(image)

        # Check if the image's classification is known
        if classification not in self._class_ids:
            # Classification is unknown, so add it to the list
            self._class_ids.append(classification)

        return


    def AppendDataList(self, list_file="", classification=""):
        """ Load a list of images with a specific classification

        @param[in] list_file            Text file containing a list of objects
        @param[in] classification       Classification for all files in list
        """
        # Load the runlist text file
        filelist = open(list_file,'r')
        #print('Reading file:',list_file)
        
        # Loop through each file in the list
        file_end = False
        while not file_end:
            # Load the next filename
            filename = filelist.readline()
            
            # If filename is empty, consider it the end of the file
            if len(filename) is 0:
                file_end = True
                continue
            # Otherwise check that the filename doesnt end with a newline
            elif filename.endswith("\n"): 
                # Trim the newline character
                filename = filename[:-1]
            
            # Load this data file into the list of files
            self.AppendData(filename, classification)

        # Loop through each line in the file

        return 0


    def Batch(self, batchsize):
        """ Return the next batch of data in the lists

        @param[in] batchsize            Number of images to load

        """
        # Define empty data and classifier objects
        images = []
        classifiers = []

        # Now load the images
        while len(images) < batchsize:
            # Get the current position
            pos = self._batch_position

            # Load the image and classification vector
            images.append( self._data[pos].GetImage() )
            classifiers.append( self.ClassifierArray(pos) )

            # Increment the classification vector
            self._batch_position += 1
            if self._batch_position == len(self._data):
                # We've passed the end of the images vector, so start over
                self._batch_position = 0

        return images, classifiers


    def BatchRandom(self, batchsize):
        """ Return a random number of images 
        """
        images = []
        classifiers = []
        return (images, classifiers)


    def ClassifierArray(self, pos):
        """ Get a vector of zeros with a 1 at the appropriate classification index
        """
        classifiers = np.zeros(self._class_ids)
        classifiers[self._class_ids.index(self._data[pos].Classification())] = 1

        return classifiers


    def LoadTests(self, test_frac=None):
        """ Returns the images and classifiers to be used in the testing

        @param[in] test_frac            New test fraction value

        Test images are taken from the end of the image list.
        """
        test_imgs = []
        test_classifiers = []

        return (test_imgs, test_classifiers)


    def NextBatch(self, batchsize=10):
        """ Return a batch of data and it's associated classification

        @param[in] batchsize            Number of images to load
        """
        # Return the 
        if self._load_random:
            # Return a random batch of data & classifiers
            return self.BatchRandom(batchsize)
        else:
            # Return the next batch of data & classifiers
            return self.Batch(batchsize)

    def TestFraction(self, test_frac=None):
        """ Set/get the fraction of images to reserve for testing
        """
        if (test_frac is not None):
            self._test_fraction = test_frac
        return self._test_fraction