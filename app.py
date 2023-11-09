# app.py
from flask import Flask, render_template, request
import io
import zipfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and file.filename.endswith('.zip'):
        filestream = io.BytesIO(file.read())
        with zipfile.ZipFile(filestream) as z:
            list_of_files = z.namelist()
        return render_template('filelist.html', filenames=list_of_files)
    return 'Invalid file type'

if __name__ == '__main__':
    app.run(debug=True)
