#!/usr/bin/python

import tensorflow as tf

# Test labels in sparse mode
# A collection of input:label in order zB
labels = [0,1,2,3,4]

sess = tf.InteractiveSession()

one_hot_ten = tf.one_hot(indices=labels, depth=max(labels), on_value=1., off_value=0.)

tf.Print(one_hot_ten, [one_hot_ten], message="one_hot_ten:").eval()
