# ==========================================================================
# SVariableTypes.py
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
#       Defines the different types of variables used in constructing a graph.
#       Note that this module only serves to abstract away the interface with
#       TensorFlow variables.
# ==========================================================================


import tensorflow as tf


def BiasVariable(shape):
    """ Generates a bias variable of a given shape.

    @param[in] shape                Input shape

    """
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def PlaceHolder(dtype=tf.float32, shape=None, name=None):
    """ Define a placeholder variable

    @param[in] dtype               Data type

    """
    return tf.placeholder(dtype=dtype, shape=shape, name=name)


def WeightVariable(shape):
    """ Generates a weight variable of a given shape.

    @param[in] shape                Input shape

    """
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)