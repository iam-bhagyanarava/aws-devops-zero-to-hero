#Flask is a class provided by the Flask library.
#When you call Flask(__name__), you are creating an instance of the Flask app. That instance is typically called app.
__name__ is a Python built-in variable.
#If your script is the main program being run, __name__ will be "__main__".
#If your script is imported as a module in another script, __name__ will be the module name.
#3️⃣ Why pass __name__ to Flask?
#Flask uses this argument to know where your application is located. 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()
