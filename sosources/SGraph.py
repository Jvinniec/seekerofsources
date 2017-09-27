# ==========================================================================
# SGraph.py
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
#       network. Allows for combining multiple hidden layers 
#

import tensorflow as tf
import sosources as sos

class SGraph:
    """ Implements a TensorFlow graph for training.
    """

    def __init__(self):
        """ Initializes the graph class
        """
        self._layers = []
        

    def AppendLayer(self, layer):
        """ Append a new layer to the end of this graph

        @param[in] layer                Hidden layer to be added

        """
        self._layers.append(layer)


    def InitGraph(self,x):
        """ InitGraph builds the graph for a deep net classifier of astronomy images.
        Args:
        x: an input tensor with the dimensions (N_examples, 784), where 784 is the
           number of pixels in a standard MNIST image.
        Returns:
            A tuple (y, keep_prob). y is a tensor of shape (N_examples, 10), with values
            equal to the logits of classifying the digit into one of 10 classes (the
            digits 0-9). keep_prob is a scalar placeholder for the probability of
            dropout.
        """
        # Reshape to use within a convolutional neural net.
        # Last dimension is for "features" - there is only one here, since images are
        # grayscale -- it would be 3 for an RGB image, 4 for RGBA, etc.
        x_image = tf.reshape(x, [-1, 112, 112, 1])

        # Loop through the layers and assemble the graph
        tf_layers = []
        for i in range(len(self._layers)):
            # If this is the first layer, skip it
            if i == 0:
                tf_layers.append(self._layers[i].DefineLayer(x_image, 
                                                             [5,5,1], 32))
            else:
                # Set the previous layer as the input to this layer
                tf_layers.append(self._layers[i].DefineLayer(tf_layers[-1],
                                 [5,5,self._layers[i-1]._output_dimensions], i*32))
            
        #with tf.name_scope('full_connect1'):
        # Fully connected layer 1 -- after 2 round of downsampling, our 112x112 image
        # is down to 14x14x124 feature maps -- maps this to 1024 features.
        W_fc1 = sos.var.WeightVariable([14 * 14 * 128, 1024])
        #variable_summaries(W_fc1)
        b_fc1 = sos.var.BiasVariable([1024])
        #variable_summaries(b_fc1)

        h_pool3_flat = tf.reshape(tf_layers[-1], [-1, 14*14*128])
        h_fc1 = tf.nn.relu(tf.matmul(h_pool3_flat, W_fc1) + b_fc1)

        #with tf.name_scope('full_connect2'):
        # Map the 1024 features to 10 classes, one for each digit
        W_fc2 = sos.var.WeightVariable([1024, 3])
        #variable_summaries(W_fc2)
        b_fc2 = sos.var.BiasVariable([3])
        #variable_summaries(b_fc2)

        #with tf.name_scope('droppout'):
        # Dropout - controls the complexity of the model, prevents co-adaptation of
        # features.
        keep_prob = sos.var.PlaceHolder(tf.float32)#tf.placeholder(tf.float32)
        tf.summary.scalar('dropout_keep_probability', keep_prob)
        h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

        y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
        return y_conv, keep_prob
