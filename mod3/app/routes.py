from flask import render_template, redirect, url_for, flash, request, send_from_directory
from app import app, ALLOWED_EXTENSIONS
import boto3
import logging
import uuid
import random
import time



import os
import sys
from werkzeug.utils import secure_filename

root = logging.getLogger()
root.setLevel("DEBUG")

session = boto3.session.Session(
    aws_access_key_id=app.config.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=app.config.get('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=app.config.get('AWS_SESSION_TOKEN')
)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

root.addHandler(handler)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == "POST":
        flash("Processing File")
        logging.info('file' not in request.files)
        if 'file' not in request.files:
            logging.info("No file attached")
            flash("No file attached")
            return redirect(request.url)
        bucket = session.resource('s3').Bucket('submissionbucket2')

        file = request.files['file']

        if file.filename == "":
            logging.info("No file attached")
            flash("No file attached")
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            logging.info("Successfully uploaded")
            flash("Successfully uploaded!")
            flash(file.filename)
            
            ## Consider saving the file
            fname, ext = os.path.splitext(file.filename)
            fname_rand = fname + str(uuid.uuid4()) + ext
            filename = "293837210"#secure_filename(fname_rand)
            file.save(os.path.join(os.getcwd(), filename))
            bucket.upload_file(filename, os.path.join(os.getcwd(), filename))
            logging.info(f"{filename} has been uploaded to s3")
            rand = random.randint(1,3)
            time.sleep(rand)
            return send_from_directory(f"C:\\Users\\Middl\\OneDrive\\Documents\\mod3\\example_docs", f"example{rand}.json", as_attachment=True, download_name="Submission Result.json")

    if request.method == "GET":
        flash("Please select file")
    return render_template('upload.html', title="Upload Form Example")