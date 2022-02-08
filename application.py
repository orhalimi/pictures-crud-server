import os
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
engine = create_engine("mysql+pymysql://root:ka*dj#D23Aff2@localhost:3307/prod") #TODO: put in variable
Session = sessionmaker(bind=engine)


@app.route("/images", methods=["POST"])
def get_images():
    files = request.files.getlist('images[]')

    return None


if __name__ == "__main__":
    # app.run(debug=True)
    pass
