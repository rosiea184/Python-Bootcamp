from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#from flask_sqlalchemy_app.venv.ai_utils import categorize

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'   
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/')
def home():
    status = request.args.get('filter','all')
    if status == 'pending':
        tasks = Task.query.filter_by(completed=False).order_by(Task.id).all()
    elif status == 'completed':
        tasks = Task.query.filter_by(completed=True).order_by(Task.id).all()
    else:
        tasks = Task.query.order_by(Task.id).all()
    #tasks = Task.query.all()
    return render_template('index.html', tasks = tasks, active_filter=status)  # Render the home page using the index.html template

@app.route('/add', methods= ['POST'])
def add_task():
    task = request.form.get('task')
    #category = categorize(task)
    new_task = Task(title=task) #category=category)  # Create a new task instance
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get(task_id)
    task.completed = not task.completed  # Toggle the completed status
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:task_id>', methods=['POST','GET'])
def edit(task_id):
    task = Task.query.get(task_id)
    if request.method == 'POST':
        task.title = request.form.get('task')
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', task=task)
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
