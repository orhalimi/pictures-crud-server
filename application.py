from flask import Flask, request
import utils.db
from models.image import Image

app = Flask(__name__)
# TODO: put in variable


@app.route("/images", methods=["POST"])
def get_images():
    files = request.files.getlist('images[]')

    return None


if __name__ == "__main__":
    # app.run(debug=True)
    utils.db.insert(Image(owner="orhalimi", image_blob=bytes("heyhey", encoding='utf8')))
    pass
