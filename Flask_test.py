#coding:utf-8
'''
Created on 2017��9��22��

@author: lenovo
'''
from flask import Flask
import Json_test
app = Flask(__name__)

@app.route('/')
def index():
    return Json_test.format_json()

if __name__ == '__main__':
    
    app.run(debug=True,port=8000,host='0.0.0.0')