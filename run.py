# file with the task of running the app
# By creating this file and having a seperate packgage we avoid import errors.

from flask_app import create_app  # importing from __init__.py within flask_app package
 

app = create_app()

if __name__ == '__main__': # Python Interpreter automatically assigns '__main__' module to the special variable __name__ when reading the source file, allowing me to control source file's/script's behaviour
    app.run(debug=True)    # Server is reloaded on any code change and provides detailed error messages

