from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/add_mantenimiento', methods=['POST'])
def add_mantenimiento():
    # Obtener los datos del cuerpo de la solicitud
    data = request.json
    
    # Validar que se proporcionaron los campos necesarios
    if 'Id' not in data or 'nombre' not in data or 'fecha' not in data or 'ip' not in data or 'mantenimiento' not in data:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    # URL del servicio del catálogo
    catalogo_url = f"http://34.207.108.141:8080/Cloud/catalogo/{data['Id']}"

    # Obtener el recurso existente del catálogo
    response = requests.get(catalogo_url)
    
    if response.status_code != 200:
        return jsonify({"error": "No se pudo obtener el recurso del catálogo"}), response.status_code

    # Obtener el recurso existente
    existing_data = response.json()

    # Agregar el campo de mantenimiento
    existing_data['mantenimiento'] = data['mantenimiento']

    # Aquí podrías enviar el recurso actualizado a otro servicio o almacenarlo
    # Por ejemplo, podrías hacer un POST a otro endpoint o guardar en una base de datos

    return jsonify(existing_data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)