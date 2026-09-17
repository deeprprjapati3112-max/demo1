from flask import Flask 

app =Flask (__name__)

@app.route("/")
def hello_world():
    return "<p>hello,world!</p>"

app.run()

# to create the link for project 
