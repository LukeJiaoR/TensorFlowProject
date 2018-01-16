import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

sess = tf.Session()
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + 提供tf.add(a, b)的一个快捷方式

print(sess.run(adder_node, {a: 3, b: 4.5}))
print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))