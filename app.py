from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask!"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/user/<username>')
def user(username):
    return f"Welcome, {username}!"

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return f"The multiplication of {num1} and {num2} is: {result}"

@app.route('/capitalize/<string:text>')
def capitalize(text):
    capitalized_text = text.upper()
    return f"The capitalized text is: {capitalized_text}"

if __name__ == '__main__':
    app.run()
