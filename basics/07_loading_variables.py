import tensorflow as tf
sess = tf.InteractiveSession()

spikes = tf.Variable([False] * 8, name="spikes")
saver = tf.train.Saver()

try:
    saver.restore(sess, 'spikes.ckpt.index')
    print (spikes.eval())
except:
    print "File not found"
