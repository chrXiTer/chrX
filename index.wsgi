import sae
sae.add_vendor_dir('vendor')
import sys

from myapp import app
application = sae.create_wsgi_app(app)

#"""

#run(app, host='localhost', port=8080, debug='true', reloader=True)
#"""