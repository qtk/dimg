import bottle
import logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

dimg = application = bottle.Bottle()


@dimg.route("/")
def show_index():
    """
    :return The front "index" page
    """
    return bottle.static_file(filename="index.html", root="/var/www/dimg")


@dimg.post("/validate")
def validate():
    """
    This page validates the uploaded file
    :return: A page with uploaded file
    """
    image = bottle.request.files.get("img")
    filename = image.filename
    logging.info("Uploaded image filename: {}".format(filename))
    image.save(destination="img", overwrite=True)

    bottle.redirect("/static/img/" + filename)

if __name__ == "__main__":
    bottle.run(app=dimg, host="localhost", port=8080)
