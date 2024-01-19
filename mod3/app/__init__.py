from flask import Flask
from flask_migrate import Migrate
from config import Config


UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['csv', 'jpg', 'jpeg','png', 'pdf'])



app = Flask(__name__)
app.config.from_object(Config)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


from app import routes