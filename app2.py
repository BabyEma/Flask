from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "nombre": "Proyecto Capstone API",
        "version": "1.0",
        "descripcion": "Servidor Flask para el proyecto Capstone"
    })

@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.get_json()

    if not data or "mensaje" not in data:
        return jsonify({
            "error": "Debes enviar un JSON con el campo 'mensaje'"
        }), 400

    return jsonify({
        "respuesta": f"Mensaje recibido: {data['mensaje']}"
    })

if __name__ == "__main__":
    app.run(debug=True)