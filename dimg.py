import bottle
import sys
dimg = application = bottle.Bottle()


@dimg.route("/")
def show_index():
    '''
    The front "index" page
    '''
    return "Running on Python {}".format(sys.version)
