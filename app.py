from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Make sure folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No file uploaded'
    
    image = request.files['image']
    if image.filename == '':
        return 'No selected file'
    
    filename = secure_filename(image.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(image_path)

    # TODO: AI processing logic here

    return f"Image uploaded and saved to: {image_path}"

if __name__ == '__main__':
    app.run(debug=True)
