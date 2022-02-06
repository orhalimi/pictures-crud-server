import os
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

UPLOAD_FOLDER = 'static/upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
engine = create_engine("mysql+pymysql://root:ka*dj#D23Aff2@localhost:3307/prod") #TODO: put in variable
Session = sessionmaker(bind=engine)


@app.route("/images", methods=["POST"])
def get_images():
    files = request.files.getlist('images[]')

    return None


if __name__ == "__main__":
    # app.run(debug=True)
    pass
