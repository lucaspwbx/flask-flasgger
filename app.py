from flask import Flask, jsonify
from flasgger import Swagger, swag_from

# creates flask app
app = Flask(__name__)

# injects flask app into swagger instance
swagger = Swagger(app)

PEOPLE = [
    {"name": "Foo", "age": 59},
    {"name": "Bar", "age": 20}
]


@app.route('/people')
@swag_from('people.yml')
def people():
    return jsonify(PEOPLE)


app.run(debug=True)
