from flask import Flask, render_template, request, redirect, url_for, make_response,jsonify
import os
from dotenv import load_dotenv
import google.generativeai as ai

load_dotenv("D:/Python/Nascom/.env")


app = Flask(__name__)

@app.route('/')
def ope():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)