from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from google_search import process_name  # Import the process_name function
from Resources.res import Home, User, Check

app = Flask(__name__)
api = Api(app, prefix='/api')
CORS(app)

# class Check(Resource):
#     def post(self):
#         data = request.get_json()
#         name = data.get('nm')
#         result = process_name(name)  # Call the process_name function
#         return jsonify(result=result)

api.add_resource(Home, '/')
api.add_resource(Check, '/check')
api.add_resource(User, '/<usr>')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
