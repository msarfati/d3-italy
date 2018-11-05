# d3-italy
Michael Sarfati

# Getting started
FLASK_APP=d3italy APP_CONFIG=config/development.py flask db init
FLASK_APP=d3italy APP_CONFIG=config/development.py flask db populate
FLASK_APP=d3italy APP_CONFIG=config/development.py flask run

# Data API Snippets
```bash
curl http://127.0.0.1:5000/api/region/1

curl -G --data-urlencode "name_en=Rome" http://127.0.0.1:5000/api/city

curl -G --data-urlencode "population[gte]=40000&population[lte]=50000" http://127.0.0.1:5000/api/city
```