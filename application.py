import json

from flask import Flask, request
from flask_cors import CORS
from utils.decorators import authentication

from utils.db import session_scope
from models.image import Image
from models.image_tag import ImageTag


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})



@app.route("/images", methods=["POST"])
@authentication
def save_images(user):
    files = request.files.getlist('images[]')
    images_meta = json.loads(request.form['json'])['meta']
    if( len(files) != len(images_meta)):
        return {"message": "Invalid input"}, 500
    with session_scope() as session:
        for meta, file in zip(images_meta, files):
            image = Image(owner_id=user['id'], image_blob=file.read(), name=meta['name'])
            session.add(image)
            session.commit()
            print (meta)
            for tag in meta['tags']:
                image_tag = ImageTag(tag=tag, image_id=image.id)
                session.add(image_tag)
                session.commit()
    return {"message": "Saved!"}, 200

if __name__ == "__main__":
    app.run(debug=True)

    # with session_scope() as session:
    #     session.add(user)
    #     session.commit()
    #     print(user)
