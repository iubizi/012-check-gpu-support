import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))

'''
gpu supported
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]

nope
[]
'''
