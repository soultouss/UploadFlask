from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

img_extenison = set(['jpg', 'jpg'])

def check_extension(extension):
    return extension in img_extension

@app.route('/upload', methods = ['GET', 'POST'])
def upload_fiile():
    try:
        extension = request.files['file'].filename.rsplit('.', 1)[1].lower()
    except:
        return "invalide extension"
    if extension and check_extension(extension): 
        if request.method == 'POST':
            f = request.files['file']
            f.save('/var/www/html/images/' + secure_filename(f.filename))
            return 'file uploaded successfully'
        else:
            return "Invalid method POST"

@app.route('/display')
def display():
    return render_template('display.php')
