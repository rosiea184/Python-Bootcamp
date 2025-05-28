import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import boto3
import json
import logging
#from flask_sqlalchemy_app.venv.ai_utils import categorize
logging.basicConfig(level=logging.INFO, filename='app.log')

app = Flask(__name__)
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')

def get_db_secret(secret_name, region_name='us-east-1'):
    client = boto3.client('secretsmanager', region_name=region_name)
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    secret = get_secret_value_response['SecretString']
    return json.loads(secret)

# fetch credentials from AWS Secrets Manager
secret = get_db_secret('prod/rds/mydb')


basedir = os.path.abspath(os.path.dirname(__name__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{db_user}:{db_password}@{db_host}'\
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{secret['username']}:{secret['password']}@{secret['host']}/{secret['dbname']}"  # Use environment variables for database credentials
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
BUCKET_NAME = 'flask-todo-bucket'  # Replace with your S3 bucket name

def upload_to_s3(file_path, s3_key):
    s3 = boto3.client('s3')
    file_name = os.path.basename(file_path)
    try:
        s3.upload_file(file_path, BUCKET_NAME, file_name)
        logging.info(f"Uploaded {file_name} to S3 bucket {BUCKET_NAME} with key {s3_key}.")
        return f"https://{BUCKET_NAME}.s3.amazonaws.com/{s3_key}"  # Return the S3 URL of the uploaded file
    except Exception as e:
        logging.error(f"Error uploading file to S3: {e}")
        return None
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
    try:
        file = request.files.get('file')
    except Exception as e:
        logging.error(f"Error retrieving file: {e}")
        file = None
    if file:
        # Save the file locally and upload to S3
        file_path = os.path.join(basedir, file.filename)  # Save the file locally
        file.save(file_path)
        s3_url = upload_to_s3(file_path, file.filename)  # Upload to S3
        os.remove(file_path)  # Remove the local file after uploading
        new_task.s3_url = s3_url
        logging.info(f"File uploaded to S3: {s3_url}")
    else:
        logging.info("No file received.")
        
    new_task = Task(title=task)  # Create a new task instance
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
    app.run(host='0.0.0.0',debug=True)
