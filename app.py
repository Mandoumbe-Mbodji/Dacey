from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    number = data.get('number')
    message = data.get('message')

    # Ajoutez le code pour envoyer le message à WhatsApp (par exemple, en utilisant Selenium)

    return jsonify({"success": True, "message": "Message sent successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
