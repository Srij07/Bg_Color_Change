import pixellib
import base64
from flask import Flask, jsonify, request
from pixellib.tune_bg import alter_bg

app = Flask(__name__)


@app.route('/changebg', methods = ['GET'])
def changebg():
  
    converted_string = ""
    change_bg = alter_bg()
    change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
    output = change_bg.color_bg("photo.jpg", colors = (255,255,255), output_image_name = "two.jpg")
    with open("two.jpg", "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
        
    #print(converted_string)
    return converted_string
  
  
# driver function
if __name__  == '__main__':
  
    app.run(debug = False)

