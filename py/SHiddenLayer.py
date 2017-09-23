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

import tensorflow as tf

class SHiddenLayer:
    """ Implements a TensorFlow hidden layer
    """

    def __init__(self):
        """ Initialize the class
        """
        self._input = 1


    def Conv2d(self, x, W):
        """conv2d returns a 2d convolution layer with full stride."""
        return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


    def MaxPool_2x2(self, x):
        """max_pool_2x2 downsamples a feature map by 2X."""
        return tf.nn.max_pool(x, 
                              ksize=[1, 2, 2, 1],
                              strides=[1, 2, 2, 1], 
                              padding='SAME')

    def WeightVariable(self, shape):
        """ Generates a weight variable of a given shape.

        @param[in] shape                Input shape
        """
        initial = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(initial)


    def BiasVariable(self, shape):
        """ Generates a bias variable of a given shape.
        
        @param[in] shape                Input shape
        """
        initial = tf.constant(0.1, shape=shape)
        return tf.Variable(initial)


    def DefineLayer(self, input_tensor, 
                    input_dim, output_dim, layer_name, 
                    act=tf.nn.relu):
        """ Define the actual layer for use

        @param[in] input_tensor         Input tensor
        @param[in] input_dim            Input dimension
        @param[in] output_dim           Output dimension
        @param[in] layer_name           Name for this layer
        @param[in] act                  Activation
        """
        with tf.name_scope(layer_name):
            with tf.name_scope('weights'):
                input_dim.append(output_dim)
                # First convolutional layer - maps one grayscale image to x feature maps.
                W = WeightVariable(input_dim)
                variable_summaries(W)
            with tf.name_scope('biases'):
                # Define the bias variable
                b = BiasVariable([output_dim])
                variable_summaries(b)
            with tf.name_scope('Wx_plus_b'):
                preactivate = conv2d(input_tensor, W) + b
                tf.summary.histogram('pre_activations', preactivate)
                activations = act(preactivate, name='activation')
                tf.summary.histogram('activations', activations)

            # Pooling layer - downsamples by 2X.
            h_pool = max_pool_2x2(activations)
            tf.summary.histogram('pool', h_pool)
            return h_pool