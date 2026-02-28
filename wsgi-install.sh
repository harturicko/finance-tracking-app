#!/bin/sh

echo "executing wsgi-install.sh"
apk add gcc musl-dev apache2 apache2-dev
pip install mod_wsgi
adduser -D -H wsgi
mod_wsgi-express start-server wsgi --user wsgi --group wsgi --port 5000 --host 0.0.0.0 --application-type module