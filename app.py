from flask import Flask, g
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///vaccine_database.db"
db = SQLAlchemy(app)


# this database for storing informations of patients
class VaccineDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hospital_name = db.Column(db.String(40), nullable=True)
    name_of_patient = db.Column(db.String(30), nullable=True)
    phone_number = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    date = db.Column(db.String(20), nullable=True)


co_vaccine = reqparse.RequestParser()
co_vaccine.add_argument("name_of_patient", type=str, help="name of patient", required=True)
co_vaccine.add_argument("phone_number", type=int, help="phone number of patient", required=True)
co_vaccine.add_argument("age", type=int, help="age of patient", required=True)
co_vaccine.add_argument("date", type=str, help="name of patient", required=True)

get_co_vaccine = reqparse.RequestParser()
get_co_vaccine.add_argument("name_of_patient", type=str, help="name of patient")
get_co_vaccine.add_argument("phone_number", type=int, help="phone number of patient")
get_co_vaccine.add_argument("age", type=int, help="age of patient")
get_co_vaccine.add_argument("date", type=str, help="name of patient")
to_json = {
    "name_of_patient": fields.String,
    "phone_number": fields.Integer,
    "age": fields.Integer,
    "date": fields.String
}


class CoVaccine(Resource):
    # this function for register patients only if available slots
    @marshal_with(to_json)
    def put(self, hospital_name):
        client_input = co_vaccine.parse_args()
        print(client_input['phone_number'])
        results = VaccineDatabase.query.filter_by(date=client_input['date']) and VaccineDatabase.query.filter_by(
            hospital_name=hospital_name).all()
        print(client_input['name_of_patient'])
        if results:
            for result in range(len(results)):
                g.count = +result
            if g.count <= 15:
                datas = VaccineDatabase(hospital_name=hospital_name,
                                        name_of_patient=client_input['name_of_patient'],
                                        phone_number=client_input['phone_number'], age=client_input['age'],
                                        date=client_input['date'])
                db.session.add(datas)
                db.session.commit()
                return datas, 201
            else:
                return abort(404, message="slots are filled,choose different date")
        else:
            datas = VaccineDatabase(hospital_name=hospital_name, name_of_patient=client_input['name_of_patient'],
                                    phone_number=client_input['phone_number'], age=client_input['age'],
                                    date=client_input['date'])
            db.session.add(datas)
            db.session.commit()
            return datas, 201

    # for checking available slots in hospitals
    def get(self, hospital_name):
        client_input = get_co_vaccine.parse_args()
        results = VaccineDatabase.query.filter_by(date=client_input['date']) and VaccineDatabase.query.filter_by(
            hospital_name=hospital_name).all()
        for result in range(len(results)):
            g.counting = +result
        sum = 15 - g.counting
        to_str = str(sum)
        return {"number of available slots in hospital": to_str}, 200


api.add_resource(CoVaccine, "/vaccineregistration/<string:hospital_name>")
if __name__ == '__main__':
    app.run(debug=True)
