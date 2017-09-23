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

import SData

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


    def NextBatch(self, batchsize=10):
        """ Return a batch of data and it's associated classification

        @param[in] batchsize            Number of images to load
        """
        # Get the vectors to be returned
        data = []
        classes = []

        # Loop through the data and get the next batch of images
        

    def AppendData(self, file="", classification=""):
        """ Load a single file with a given classification

        @param[in] file                 Filename to be loaded
        @param[in] classification       Image classification
        """
        image = SData
        image.Filename(file)
        image.Classification(classification)
        self._data.append(image)

        # Check if classification is known
        if classification not in self._class_ids:
            self._class_ids.append(classification)


    def AppendDataList(self, list_file="", classification=""):
        """ Load a list of images with a specific classification

        @param[in] list_file            Text file containing a list of objects
        @param[in] classification       Classification for all files in list
        """
        # Load the runlist text file

        # Loop through each line in the file


        return 0

