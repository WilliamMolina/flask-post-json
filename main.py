from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

## Resource class
class Post(Resource):
    def post(self):
        print(request.json)        
        return request.json, 201

##
## Actually setup the Api resource routing here
##
api.add_resource(Post, '/dummy')

if __name__ == '__main__':
    app.run(debug=True)