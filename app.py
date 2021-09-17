from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

print('un cambio')


class Tareas(Resource):
    def get(self):
        return {
            'message': 'las tareas son:'
        }

    def post(self):
        return {
            'message': 'Tarea creada exitosamente'
        }


api = Api(app)

api.add_resource(Tareas, '/tareas')

if __name__ == '__main__':
    app.run(debug=True)
