import os

def setup():

    if not os.path.exists('models'):
        os.makedirs('models')

    if not os.path.exists('client_repo'):
        os.makedirs('client_repo')

    model_py_content = """
import tensorflow as tf

class MLMODEL:
    def __init__(self):
        self.model = tf.keras.models.Sequential() # write your model code
        self.model.compile() # write your model compile code

    def getModel(self):
        return self.model
"""

    with open('client_repo/MODEL.py', 'w') as f:
        f.write(model_py_content)