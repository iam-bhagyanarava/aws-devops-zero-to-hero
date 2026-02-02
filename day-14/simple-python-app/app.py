#Flask is a class provided by the Flask library.
#When you call Flask(__name__), you are creating an instance of the Flask app. That instance is typically called app.
#__name__ is a Python built-in variable.
#If your script is the main program being run, __name__ will be "__main__".
#If your script is imported as a module in another script, __name__ will be the module name.
#Why pass __name__ to Flask? Flask uses this argument to know where your application is located. Flask(__name__), Flask sets self.root_path to the directory containing the module 
#@app.route('/') is a decorator
#In Python, the @something syntax is called a decorator. A decorator modifies a function or adds extra behavior to it.
#In Flask, @app.route('/') tells the Flask app: “Hey Flask, when someone goes to the URL '/' (the root of the website), run this function (hello) and return its result.”
#app.route() registers a URL path with a function. The function underneath the decorator is called a view function.
#Flask keeps an internal mapping, something like this:
#URL Path	Function
#/         	hello()


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()
