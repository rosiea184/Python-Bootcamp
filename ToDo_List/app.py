from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.template_filter('format_date')
def format_date(value):
    try:
        date_obj = datetime.strptime(value, "%Y-%m-%d")
        return date_obj.strftime("%m/%d/%Y")
    except (ValueError, TypeError):
        return value

tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks = tasks)  # Render the home page using the index.html template

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    if task_text:
        tasks.append({'text': task_text, 'completed': False, 'date': ''})  # Add the task to the list with a default completed status of False and no date
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

@app.route('/cross_off/<int:task_id>', methods=['POST'])
def cross_off_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed'] # Cross off the task by wrapping it in <s> tags
    return redirect('/')


@app.route('/add_date/<int:task_id>', methods=['POST'])
def add_date(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['date'] = request.form.get('due_date')
    return redirect('/')

@app.route('/clear_all', methods=['POST'])
def clear_all_tasks():
    tasks.clear()  # Clears all tasks from the list
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True) 

