from flask_app import app, db



#  The app decorator executes the main function every time the user enters this route on a specific domain 
@app.route('/')
def main():
    return 'Hello World!'



    