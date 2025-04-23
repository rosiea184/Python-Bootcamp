from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
#Flask is a micro web framework for Python. It is lightweight and easy to use, making it a popular choice for building web applications. Flask is designed to be simple and flexible, allowing developers to create web applications quickly and easily. It provides a simple way to handle HTTP requests and responses, manage sessions, and render templates. Flask also has a large ecosystem of extensions that can be used to add functionality to your application, such as database integration, authentication, and more.
# The Flask framework is built on top of the Werkzeug WSGI toolkit and the Jinja2 template engine. It is designed to be easy to use and understand, making it a great choice for beginners and experienced developers alike. Flask is also highly customizable, allowing developers to create applications that meet their specific needs.  
@app.route('/')
def home():
    return render_template('index.html')  # Render the home page using the index.html template

@app.route('/about')
def about():
    return render_template('about.html', name="Alex", passion="Coding")    


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
# The debug mode allows you to see detailed error messages and automatically reload the server when you make changes to your code. This is useful for development, but should be turned off in production environments for security reasons.