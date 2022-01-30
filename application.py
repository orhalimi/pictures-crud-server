import os
from flask import Flask, request

UPLOAD_FOLDER = 'static/upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/images", methods=["POST"])
def get_images():
    files = request.files.getlist('images[]')
    print(files)
    for file in files:
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
    return None


if __name__ == "__main__":
    app.run(debug=True)
