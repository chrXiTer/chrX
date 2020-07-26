from bottle import Bottle, run
from bottle import static_file

import sae
from routes import app

application = sae.create_wsgi_app(app)

#"""

#run(app, host='localhost', port=8080, debug='true', reloader=True)
#"""