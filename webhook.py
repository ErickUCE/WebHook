from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def home():
    return "Hi, I am Erick. WebHook with Python"

# WebHook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Recibe datos de un WebHook
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            event:
              type: string
            data:
              type: string
    responses:
      200:
        description: Datos recibidos con éxito
    """
    data = request.get_json()
    if data:
        return jsonify({"message": "Received data", "data": data}), 200
    else:
        return jsonify({"message": "No data received"}), 400

if __name__ == "__main__":
    app.run(debug=True)
