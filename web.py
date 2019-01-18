from flask import Flask
app = Flask (__name__)

@app.rounte('/')
def index():
 return 'hello, world'
 

