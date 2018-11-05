# d3-italy
Michael Sarfati

# Getting started
FLASK_APP=d3italy APP_CONFIG=config/development.py flask db init
FLASK_APP=d3italy APP_CONFIG=config/development.py flask db populate
FLASK_APP=d3italy APP_CONFIG=config/development.py flask run

# Data API Snippets
curl -G --data-urlencode "id=1" http://127.0.0.1:5000/api/region