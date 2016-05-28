import bottle
import sys
dimg = application = bottle.Bottle()


@dimg.route("/")
def show_index():
    '''
    :return The front "index" page
    '''
    return bottle.static_file(filename="index.html", root="./static")


@dimg.post("/validate")
def validate():
    '''
    This page validates the uploaded file
    :return: A page with the return status
    '''
    image = bottle.request.files.get("img")
    filename = image.filename
    image.save(destination="img", overwrite=True)
    return bottle.static_file(filename=filename, root="./img")

if __name__ == "__main__":
    bottle.run(app=dimg, host="localhost", port=8080)
