import bottle
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

logger.basicConfig(filename='debug.log', level=logging.DEBUG)

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
    print("Does uwsgi logging work?")
    image = bottle.request.files.get("img")
    filename = image.filename
    logger.debug("Uploaded image filename: {}".format(filename))
    image.save(destination="img", overwrite=True)

    bottle.redirect("/static/img/" + filename)

if __name__ == "__main__":
    bottle.run(app=dimg, host="localhost", port=8080)
