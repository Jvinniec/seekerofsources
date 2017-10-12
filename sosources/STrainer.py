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
# ==========================================================================


import tensorflow as tf
import sosources as sos


class STrainer:
    """ Class for training a CNN in Tensorflow
    """

    def __init__(self):
        """ Initilizes the training class
        """
        self._graph = sos.SGraph()
        self._data_manager = sos.SDataBatch()
        self._batch_size = 100

        # Parameters
        self._x = None
        self._y_ = None
        self._verbose = True

        # Parameters for controling the training
        self._train_step = None
        self._accuracy = None
        self._y_conv = None
        self._keep_prob = None
        self._cross_entropy = None
        self._correct_prediction = None


    def DataManager(self, data_manager=None):
        """ Get/set the data manager object

        @param[in] data_manager     SDataManager object

        """
        if data_manager is not None:
            self._data_manager = data_manager

        return self._data_manager


    def Graph(self, graph=None):
        """ Get/set the graph to be trained

        @param[in] graph            SGraph object

        """
        if graph is not None:
            self._graph = graph

        return self._graph


    def InitTrainer(self):
        """ Initialize the trainer, assembling the graph
        """
        # Create the input image tensor variable
        image_bins = 112*112    # <-- This should be easy to get from the input data
        self._x = sos.var.PlaceHolder(tf.float32, [None, image_bins], name='x-input')
    
        # Create the image classifications variable (the 'truth' used for training)
        self._y_ = sos.var.PlaceHolder(tf.float32, [None, self._data_manager.NumClassIds()], name='y-input')

        # Initialize the graph
        # y_conv    = output classification based on current network
        # keep_prob = Probability variable for keeping a node 
        self._y_conv, self._keep_prob = self._graph.InitGraph(self._x)

        # Now initialize the rest of the training variables
        self._cross_entropy = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(labels=self._y_, logits=self._y_conv))
        self._train_step = tf.train.AdamOptimizer(1e-4).minimize(self._cross_entropy)
        self._correct_prediction = tf.equal(tf.argmax(self._y_conv, 1), tf.argmax(self._y_, 1))
        self._accuracy = tf.reduce_mean(tf.cast(self._correct_prediction, tf.float32))

        return


    def SaveModel(self, filename="imagemodel.pb"):
        """ Save the model to a file that can be used in production

        @param[in] filename         Name of output file to produce

        """
        return


    def Train(self, ntimes=100):
        """ Train the model using 'ntimes' steps

        @param[in] ntimes           Number of training steps

        """
        # Now create the session and train the graph
        with tf.Session() as sess:
            # Get the test images and truth classifiers
            test_imgs, test_truth = self._data_manager.LoadTests()

            print('Initial test accuracy %g' % self._accuracy.eval(feed_dict={
                self._x: test_imgs, self._y_: test_truth, self._keep_prob: 1.0}))

            # Run a number of training steps
            for i in range(ntimes):
                # Get the training sample and classifications
                train_sample, truth_sample = self._data_manager.NextBatch(self._batch_size)
            
                # Print information if in verbose mode
                if self._verbose:
                    if i % 10 == 0:
                        train_accuracy = self._accuracy.eval(feed_dict={
                                self._x: train_sample, self._y_: truth_sample, self._keep_prob: 1.0})
                    print('step %d, training accuracy %g' % (i, train_accuracy))
      
                self._train_step.run(feed_dict={self._x: train_sample, self._y_: truth_sample, self._keep_prob: 0.5})
                #writer.add_summary(summ, global_step=i)

            if self._verbose:
                print('Final test accuracy %g' % self._accuracy.eval(feed_dict={
                      self._x: test_imgs, self._y_: test_truth, self._keep_prob: 1.0}))


    def Verbose(self, verbose=None):
        """ Set/get the verbosity of the method
        """
        if verbose is not None:
            self._verbose = verbose

        return self._verbose