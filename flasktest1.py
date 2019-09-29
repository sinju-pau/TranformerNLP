#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:53:33 2019

@author: nidhinabraham
"""

# HELLO WORLD!

from flask import Flask, request


# Declare a flask app

app = Flask(__name__)

@app.route('/')
def add():
    a= request.args.get("a")
    b= request.args.get("b")
    return str(int(a)+int(b))

if __name__ =='__main__':
    app.run(port = 7000)


print(add(10,20))

from flasgger import Swagger