from flask import Flask, url_for, jsonify, request, json, flash
import pandas as pd
#import cv2
import numpy as np
#import base64
from art import StyleTransfer
import scipy.misc

app = Flask(__name__)
artist = StyleTransfer()

@app.route('/', methods=['POST']) 
def predict(): 
    results ={}
    try:
        if request.headers['Content-Type'] == 'application/json':
            text=request.json['text']
        path1= request.form['path1'] 
        path2= request.form['path2'] 
        numi=request.form['numi'] 

        best, best_loss = artist.run_style_transfer(path1, path2, numi)
        scipy.misc.toimage(best, cmin=0.0).save('outfile.jpg')
        print("Guarde la imagen")
        results['status'] = 'exito'
        return jsonify(results)
    except Exception as e:
        print(e)
        results['status'] = 'fracaso'
        return jsonify(results)
        

@app.route('/')
def api_root():
    return 'Welcome'


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")

