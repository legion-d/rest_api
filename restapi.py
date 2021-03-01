from flask import Flask
from flask_restful import Api
from resources.api_db import ItemsList

app = Flask(__name__)
app.secret_key = 'dosh'
api = Api(app)


api.add_resource(ItemsList, '/items')

if __name__ == '__main__':
    app.run(port=5000, debug=True)