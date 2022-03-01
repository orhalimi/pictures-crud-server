import json

from flask import Flask, request
from flask_cors import CORS
from utils.db import session_scope
from models.image import Image
from models.user import User


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route("/images", methods=["POST"])
def get_images():
    files = request.files.getlist('images[]')
    images_meta = json.loads(request.form['json'])['meta']
    if( len(files) != len(images_meta)):
        return {"message": "Invalid input"}, 500
    with session_scope() as session:
        # image = Image()
        # session.add(user)
        # session.commit()
        print(request)
    return {"message": "Saved!"}, 200

if __name__ == "__main__":
    app.run(debug=True)
    # salt = binascii.hexlify(os.urandom(4)).decode()
    # password = "myPassword"
    # dk = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt), 100000)
    # hashed_password = dk.hex()
    # print(hashed_password)
    # print(salt)
    # user = User(username="orhalimi", password=hashed_password, salt=salt)

    # with session_scope() as session:
    #     session.add(user)
    #     session.commit()
    #     print(user)


    # image = Image(owner=1, image_blob=bytes("heyhey", encoding='utf8'))

    pass
