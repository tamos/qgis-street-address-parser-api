from flask import Flask, request
from flask_restful import Resource, Api
from deepparse.parser import AddressParser

app = Flask(__name__)
api = Api(app)
PARSER = AddressParser(model_type = 'lightest')

todos = {}


def parse_addresses(addr):
    # to do: write exceptions to log or somewhere I can inspect
    rv = {}
    try:
        rv['parsed_address'] = PARSER(addr).to_dict()
        print("Inside parse, result is", rv['parsed_address'])
        rv['status'] = 'Success'
    except:
        rv['parsed_address'] = 'Parsing Error'
        rv['status'] = 'Failure'
    return rv

class Parse(Resource):
    # to do: add proper error codes

    def get(self):
        try:
            addr = request.form['address']
        except:
            return dict(status='Failure', details='Error reading request data.')
        try:
            rv = parse_addresses(addr)
        except:
            return dict(status='Failure', details='Error parsing addresses.')
        return dict(status='Success', parsed=rv)

api.add_resource(Parse, '/parse')

if __name__ == '__main__':
    app.run(debug=True)
