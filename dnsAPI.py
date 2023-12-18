from flask import Flask, request, jsonify
from const import *

app = Flask(__name__)
registry = {}

@app.route('/register', methods=['PUT'])
def register():
    data = request.json
    name = data.get('serviceName')
    url = data.get('url')

    if name!=None and url!=None:
        registry[name] = url
        return jsonify(), 200
    return jsonify({'Failure': 'Invalid payload'}), 400

@app.route('/unregister', methods=['DELETE'])
def unregister():
    name = request.args.get('serviceName')
    
    if name in registry:
        del registry[name]
        return jsonify(), 204
    return jsonify({'Failure': f'Service not found'}), 404

@app.route('/lookup', methods=['GET'])
def lookup():
    service_name = request.args.get('name')

    if service_name in registry:
        return jsonify({'url': registry[service_name]})
    return jsonify({'error': f'Service {service_name} not found'}), 404


if __name__ == '__main__':
    app.run(host=IP, port=PORT)