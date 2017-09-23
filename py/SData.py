# ==========================================================================
# SData.py
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
#       Defines the data class that can be used to load data from a generic
#       FITS file which uses standard keywords to identify parameters of the
#       image inside the file.
# ===========================================================================

import astropy

class SData:
    """ A simple class for storing data and reading from a general FITS file

    This class is dedicated to storing a single instance of an astronomical
    image. It is designed to work with a file that uses general keywords for
    certain image parameters.
    """

    def __init__(self, 
                 filename="", 
                 nxpix=1, nypix=1, nzpix=0, 
                 classification=""):
        """ Defines the class initialization.

        @param[in] filename
        @param[in] nxpix
        @param[in] nypix
        @param[in] nzpix
        @param[in] classification
        """
        # Initialize some values
        self.Filename(filename)
        self._classification = classification
        self._nxpix = nxpix
        self._nypix = nypix
        self._nzpix = nzpix

        # Define the typical keywords used in FITS images to specify dimensions
        self._keyword_nxpix = "nxpix"
        self._keyword_nypix = "nypix"
        self._keyword_nzpix = "nzpix"


    def GetImage(self):
        """ Method for reading an image from a generic fits file

        @param[in] filename     Fits filename of data
        @return a 1D float vector that holds the image information

        This method should be overwritten if your data files are not formatted
        in a standard FITS file with standard FITS keywords
        """

        # Get the appropriate hooks from the dataset
        return 0
    
    def Filename(self, filename=""):
        """ Get/set the filename to extract the data from

        @param[in] filename         Filename to get data from
        """
        # If 'filename' isn't blank, return it's value
        if filename != "":
            self._filename = filename

        # Return the filename
        return self._filename


    def Classification(self, classification=""):
        """ Sets the image's classification

        @param[in] classification         Object classification
        """
        # Update the classification if needbe
        if classification != "":
            self._classification = classification

        # Return the objects classification
        return self._classification


    def Nxpix(self, xpix=0):
        """ Get/set the number of pixels in the x-axis

        @param[in] xpix           Number of pixels in x-axis
        """
        if (xpix > 0):
            self._nxpix = xpix
        
        return self._nxpix
            

    def Nypix(self, ypix=0):
        """ Get/set the number of pixels in the y-axis

        @param[in] ypix           Number of pixels in y-axis
        """
        if ypix > 0:
            self._nypix = ypix

        return self._nypix


    def Nzpix(self, zpix=-1):
        """ Get/set the number of pixels in the z-axis

        @param[in] zpix           Number of pixels in z-axis
        """
        if zpix > -1:
            self._nzpix = zpix

        return self._nzpix
    