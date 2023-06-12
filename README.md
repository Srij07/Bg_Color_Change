# Bg_Color_Change

PixelLib requires python’s version 3.5-3.7.
It requires pip’s version >= 19.0

**Step :1**
pip3 install pip,
pip3 install tensorflow,
pip3 install imgaug,
pip3 install pixellib --upgrade,
pip3 install flask-restful

**Step :2**
Go to Pixellib folder -> semantic -> deeplab.py in your installed location of Pixellib and replace this line. Replace this from tensorflow.python.keras.layers import BatchNormalization with from keras.layers.normalization.batch_normalization import BatchNormalization.

**Step :3**
In C:/Users/{{user_name}}/AppData/Roaming/Python/Python311/site-packages/pixellib/semantic/deeplab.py substitute all imports tensorflow.python.keras with tensorflow.keras exept for from tensorflow.python.keras.utils.layer_utils import get_source_inputs.

**Step :4**
Down load deeplabv3_xception_tf_dim_ordering_tf_kernels.h5 from https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5 and place it in folder.
Run the Rest_API using python **Rest.py**. Then access **http://127.0.0.1:5000/changebg**
