from flask import Flask, g
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)




class CoVaccine(Resource):
    def get(self,hospital_name):
        return {"hospital_name": hospital_name}

api.add_resource(CoVaccine, "/vaccineregistration/<string:hospital_name>")
if __name__ == '__main__':
    app.run(debug=True)
