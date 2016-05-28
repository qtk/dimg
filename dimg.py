import bottle
import logging
import random
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

dimg = application = bottle.Bottle()
dimg.catchall = False

def image_name(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

@dimg.post("/validate")
def validate():
    """
    This page validates the uploaded file
    returns: A page with uploaded file
    """
    image = bottle.request.files.get("img")
    image.filename = image_name(6)
    logging.debug("Uploaded image filename: {}".format(filename))
    image.save(destination="/var/www/dimg/static/img", overwrite=True)

    bottle.redirect("/static/img/" + filename)

if __name__ == "__main__":
    bottle.run(app=dimg, host="localhost", port=8080)
