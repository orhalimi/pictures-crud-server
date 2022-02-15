from flask import Flask, request
from utils.db import session_scope
from models.image import Image
from models.user import User
import binascii
import os
import hashlib

app = Flask(__name__)
# TODO: put in variable


@app.route("/images", methods=["POST"])
def get_images():
    files = request.files.getlist('images[]')
    # db_session = utils.db.create_session()
    # with db_session as session:

    return None


if __name__ == "__main__":
    # app.run(debug=True)
    salt = binascii.hexlify(os.urandom(4)).decode()
    password = "myPassword"
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt), 100000)
    hashed_password = dk.hex()
    print(hashed_password)
    print(salt)
    user = User(username="orhalimi", password=hashed_password, salt=salt)

    with session_scope() as session:
        session.add(user)
        session.commit()
        print(user)


    # image = Image(owner=1, image_blob=bytes("heyhey", encoding='utf8'))

    pass
