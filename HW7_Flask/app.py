from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def home():
    if request.method == 'POST':
        user_input = request.form['username']  # Get input from the form
        return render_template('HW6.html', message = f"Welcome to my page {user_input}")  # Pass input to response.html
    return render_template('HW6.html')  # Render the form page

@app.route('/feedback-hw7', methods=['GET','POST'])
def feedback():
    comment = request.form.get('comment')
    if request.method == 'POST':
        comment = request.form['comment']
        return render_template('comment.html', comment=comment)  # Render the greet page with the user's name
    return render_template('feedback-hw7.html')

@app.route('/comment')
def comment(comment):
    return render_template('comment.html', comment=comment)


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
# The debug mode allows you to see detailed error messages and automatically reload the server when you make changes to your code. This is useful for development, but should be turned off in production environments for security reasons.