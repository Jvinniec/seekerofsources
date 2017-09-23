# ==========================================================================
# STrainer.py
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
#       Implements training of a TensorFlow graph for a simple convolutional 
#       neural network.
#

import SGraph
import tensorflow as tf

class STrainer:
    """ Class for training a CNN in Tensorflow
    """

    def __init__(self):
        """ Initilizes the training class
        """
        self._graph = SGraph


    def Graph(self, graph):
        """ Get/set the graph to be trained

        @param[in] graph            TensorFlow graph object
        """
        self._graph = graph

    def InitTrainer(self):
        """ Initialize the trainer, assembling the graph
        """
        # Create the model variable
        x = tf.placeholder(tf.float32, [None, 112*112], name='x-input')

        # Define loss and optimizer
        y_ = tf.placeholder(tf.float32, [None, 3], name='y-input')
