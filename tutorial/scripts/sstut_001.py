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


def CreateGraph():
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
    return graph


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

    # Create the graph
    graph = CreateGraph()

    # Create the training algorithm
    trainer = sos.STrainer()
    trainer.DataManager( data )
    trainer.Graph( graph )

    # Set a small batch size since we have a small data set
    trainer._batch_size = 10

    # Initialize and run the graph trainer
    trainer.InitTrainer()
    trainer.Train(100)


if __name__ == '__main__':
    """ Main method """
    # Extract the command line arguments
    FLAGS, unparsed = GetOpts()

    # Run a TensorFlow application
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)

