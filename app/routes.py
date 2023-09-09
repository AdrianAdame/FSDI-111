from flask import Flask

app = Flask(__name__)

@app.get("/")
def about_me():
    me = {
        "first_name" : "Adrian",
        "last_name" : "Adame",
        "hobbies" : "Coding",
        "is_active" : True
    }

    return me