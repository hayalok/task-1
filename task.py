# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:19:56 2020

@author: Alok
"""

#importing required modules
import numpy as np
import pandas as pd
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

#creating global variables
fileExist = False
dataset = pd.DataFrame()
numeric_col = []
cat_col = []

# this function uploades a file
@app.route('/uploader', methods = ['POST'])
def upload_file():    
    global fileExist
    global dataset
    global numeric_col
    global cat_col
    if request.method == 'POST':
        
        f = request.files['file']
        #f.save("datacsvfile.xlsx")
        fileExist = True
        dataset = pd.read_csv(f)
        all_col = dataset.columns
        desc_ds = dataset.describe()
        numeric_col = [i for i in desc_ds.columns]
        cat_col = list(set(all_col)- set(numeric_col))
        result = {
                "message":"File uploaded successfully",
                "Numeric_Columns": numeric_col,
                "Categorical Columns or Non-numerical Columns": cat_col
                }
        return result
     
# this function gives details about uploaded file   
@app.route('/getfileinfo', methods = ['GET', 'POST'])
def get_file_info():
    
    if request.method == 'GET':
        
        if fileExist:
            result = {
                "message":"File exist",
                "Numeric Columns": numeric_col,
                "Categorical Columns or Non-numerical Columns": cat_col
                }
            return result
            
        else:
            return "No File exist on server"

# this function returns the category that holds the maximum groupby sum for the passed numeric column  
@app.route('/check', methods = ['GET'])
def check():
    error = False
    cat_error_text = ""
    num_error_text = ""
    if request.method == 'GET':
        
        if fileExist:
            cat  = request.args.get('cat', None)
            num  = request.args.get('num', None)
            #dataset = pd.read_excel('datacsvfile.xlsx')
            if cat not in cat_col:
                error = True
                cat_error_text  = "Category column '{}' passed does not exist".format(cat)
            if num not in numeric_col:
                error = True
                num_error_text  = " Numeric column '{}' passed does not exist".format(num)
            
            if error:
                text = cat_error_text + num_error_text
                return text
            else:
                new_col = dataset.groupby(cat)[num].transform('sum')
                result = dataset[cat][new_col.idxmax()]
                text = "Category - '{}' of column '{}' has maximum groupby sum for '{}'".format(result,cat,num)
            #text = "Category - '" + result + "' of column '"+ cat + "' has maximum groupby sum for '" + num + "'"
                return text
        else:
            return "No File exist on server"


if __name__ == '__main__':
     app.run(port='5002')