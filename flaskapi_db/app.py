from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, CarsModel

# initialize the Flask app
app = Flask(__name__)


# initialise the DB URI
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://username:password@host:port/databasename'
#  Set the Modifications to False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# connect the Db and the app 
db.init_app(app)
# initialize the migration for the app and database
migrate = Migrate(app, db)


# route for Creating and Reading entities
@app.route('/cars', methods=['GET','POST'])
def get_cars():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = CarsModel(name=data['name'],model=data['model'],cylinder=data['cylinder'])
            db.session.add(new_car)
            db.session.commit()
            return jsonify({'message': f'Car {new_car.name} has been created successfully.'}),201
        else:
            return jsonify({'error':'The request payload is not JSON format'}),404

    elif request.method == 'GET':
        cars = CarsModel.query.all()
        car_results = [{
            'name':car.name,
            'model':car.model,
            'cylinder':car.cylinder
        }for car in cars
        ]
        return jsonify({'count':len(car_results),'cars':car_results})


@app.route('/car/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_car(id):
    car = CarsModel.query.get_or_404(id)

    if request.method == 'GET':
        car_response = {
            "name": car.name,
            "model": car.model,
            "cylinder": car.cylinder
        }
        return jsonify({"message": "success", "car": car_response})

    elif request.method == 'PUT':
        data = request.get_json()
        car.name = data['name']
        car.model = data['model']
        car.cylinder = data['cylinder']
        db.session.add(car)
        db.session.commit()
        return jsonify({"message": f"car {car.name} successfully updated"})

    elif request.method == 'DELETE':
        db.session.delete(car)
        db.session.commit()
        return jsonify({"message": f"Car {car.name} successfully deleted."})



if __name__=='__main__':
    app.run(debug=True)
