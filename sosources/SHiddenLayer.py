# ==========================================================================
# SHiddenLayer.py
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
#       Implements a TensorFlow graph for a simple convolutional neural
#       network. Allows for defining several hidden layers.
#

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import sosources as sos

class SHiddenLayer:
    """ Implements a TensorFlow hidden layer
    """


    def __init__(self, layer_name):
        """ Initialize the class 
        
        @param[in] layer_name           Name ltimately used by TensorBoard
        
        """
        # Initialize the data members
        self._name = layer_name
        self._pool = 2
        self._output_dimensions = 1


    def Conv2d(self, x, W):
        """conv2d returns a 2d convolution layer with full stride."""
        return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


    def DefineLayer(self, input_tensor, 
                    input_dim, output_dim, 
                    act=tf.nn.relu):
        """ Define the actual layer for use

        @param[in] input_tensor         Input tensor
        @param[in] input_dim            Input dimension
        @param[in] output_dim           Output dimension
        @param[in] layer_name           Name for this layer
        @param[in] act                  Activation

        """
        self._output_dimensions = output_dim

        #with tf.name_scope(self._name):
        #with tf.name_scope('weights'):
        input_dim.append(output_dim)
        # First convolutional layer - maps one grayscale image to x feature maps.
        W = sos.var.WeightVariable(input_dim)
        #variable_summaries(W)
        
        # Define the bias variable
        #with tf.name_scope('biases'):
        b = sos.var.BiasVariable([output_dim])
        #variable_summaries(b)
   
        #with tf.name_scope('Wx_plus_b'):
        preactivate = self.Conv2d(input_tensor, W) + b
        tf.summary.histogram('pre_activations', preactivate)
        activations = act(preactivate, name='activation')
        tf.summary.histogram('activations', activations)

        # Pooling layer - downsamples by 2X.
        h_pool = self.MaxPool(activations)
        tf.summary.histogram('pool', h_pool)
        return h_pool


    def MaxPool(self, in_tensor):
        """ MaxPool downsamples a feature map by self._pool times 
        
        @param[in] in_tensor            Input tensor

        """
        return tf.nn.max_pool(in_tensor, 
                              ksize=[1, self._pool, self._pool, 1],
                              strides=[1, self._pool, self._pool, 1], 
                              padding='SAME')


    def Name(self, name=""):
        """ Define the name of the object

        @paramp[in] name            Name of this layer

        """
        # If the name is not empty, set the value
        if len(name) > 0:
            self._name = name

        # Return current value of name
        return self._name


    def Pool(self, pool=0):
        """ Set the level of pooling at the end of this layer 

        @param[in] pool         Pooling level
        
        """
        # Update the pooling value if provided value is greater than 0
        if (pool > 0):
            self._pool = pool
        
        # Return the current value of pool
        return self._pool
