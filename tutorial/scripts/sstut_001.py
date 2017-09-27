# ==========================================================================
# sstut_001.py
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
#       This script outlines the basics for creating a very generic 
#       TensorFlow graph using SoS and training the model on a set of data.
# ==========================================================================

# Generic imports
import argparse
import sys

# SoS imports
import tensorflow as tf
import sosources as sos

FLAGS = None

def LoadDataManager(filenames):
    """ Loads the data manager for this tutorial """
    # Initialize the data batch object
    databatch = sos.SDataBatch()

    # Split the data files by the delimiter
    list_names = filenames.split(',')

    # Loop through the supplied data files and load them into the data manager
    for batch in list_names:
        # Split the filename from the classification
        filename, classifier = batch.split(':')

        # Load the image files and associate them with the classification
        databatch.AppendData(filename, classifier)

    return databatch


def CreateGraph(x):
    """ Creates a generic TensorFlow graph with two hidden layers 
    
    @param[in] x            Input tensor representing a 1D representation of image
    """
    # Create a graph object
    graph = sos.SGraph()

    # Create the 3 hidden layers. By default, each layer reduces the size of
    # the tensor input to the next layer by a factor of 2 in each dimension.
    # This is known as 'pooling'
    hidden1 = sos.SHiddenLayer('layer1')
    hidden2 = sos.SHiddenLayer('layer2')
    hidden3 = sos.SHiddenLayer('layer3')

    # Now add all of the hidden layers to the graph
    graph.AppendLayer( hidden1 )
    graph.AppendLayer( hidden2 )
    graph.AppendLayer( hidden3 )

    # Return the initialized TensorFlow graph objects
    return graph.InitGraph(x)


def GetOpts():
    """ Load the command line options """
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_lists', type=str,
                        help='List of files containing lists of images in format \'list1:category1,list2:category2\'.')
    return parser.parse_known_args()


def main(_):
    """ Main method for running the TensorFlow convolutional neural network.
    This is where things actually happen.
    """
    # Load the data
    data = LoadDataManager(FLAGS.image_lists)

    # Create the input image tensor variable
    image_bins = 112*112    # <-- This should be easy to get from the input data
    x = sos.var.PlaceHolder(tf.float32, [None, image_bins], name='x-input')
    
    # Create the image classifications variable (the 'truth' used for training)
    y_ = sos.var.PlaceHolder(tf.float32, [None, data._class_ids], name='y-input')

    # Initialize the graph
    # y_conv    = output classification based on current network
    # keep_prob = Probability variable for keeping a node 
    y_conv, keep_prob = CreateGraph(x)

    # Now initialize the rest of the training variables
    cross_entropy = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
    correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # Now create the session and train the graph
    with tf.Session() as sess:
        # Get the test images and truth classifiers
        test_imgs, test_truth = data.LoadTests()

        print('Initial test accuracy %g' % accuracy.eval(feed_dict={
              x: test_imgs, y_: test_truth, keep_prob: 1.0}))

        # Run a number of training steps
        for i in range(100):
            #randnums = gen_random(50, 0, len(obj_list))
            train_sample, truth_sample = data.NextBatch(10)
            
            if i % 10 == 0:
                train_accuracy = accuracy.eval(feed_dict={
                        x: train_sample, y_: truth_sample, keep_prob: 1.0})
                print('step %d, training accuracy %g' % (i, train_accuracy))
      
            train_step.run(feed_dict={x: train_sample, y_: truth_sample, keep_prob: 0.5})
            #writer.add_summary(summ, global_step=i)

        print('Final test accuracy %g' % accuracy.eval(feed_dict={
              x: test_imgs, y_: test_truth, keep_prob: 1.0}))


if __name__ == '__main__':
    """ Main method """
    # Extract the command line arguments
    FLAGS, unparsed = GetOpts()

    # Run a TensorFlow application
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)

