import os
import bottle
import logging
import random
import string

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

dimg = application = bottle.Bottle()
dimg.catchall = False

def image_name(n):
    return ''.join(random.choice(string.ascii_lowercasecase + string.digits) for _ in range(n))

@dimg.post("/validate")
def validate():
    """
    This page validates the uploaded file
    returns: A page with uploaded file
    """
    image = bottle.request.files.get("img")
    extension = os.path.splitext(image.filename)
    image.filename = image_name(6) + extension
    logging.debug("Uploaded image {}".format(image.filename))
    image.save(destination="/var/www/dimg/static/img", overwrite=True)

    bottle.redirect("/static/img/" + image.filename)

if __name__ == "__main__":
    bottle.run(app=dimg, host="localhost", port=8080)
