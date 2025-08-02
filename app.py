from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
      return "Welcome to MRECW"
if __name__=="main":
      app.run(host='0.0.0.0',port=10000)