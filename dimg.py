import bottle
import sys
dimg = application = bottle.Bottle()


@dimg.route("/")
def show_index():
    '''
    The front "index" page
    '''
    return bottle.static_file(filename="index.html", root="./static")

if __name__ == "__main__":
    bottle.run(app=dimg, host="localhost", port=8080)
