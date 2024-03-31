from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

users = {
    'user1@example.com': {'lottery_number': 123, 'won': 'yes'},
    'user2@example.com': {'lottery_number': 456, 'won': 'no'}
}


@app.route('/', methods=['GET'])
def about():
    return "hello world"

@app.route('/api/checkin', methods=['POST'])
def checkin():
    # Parse the incoming JSON request to extract the email
    data = request.json
    email = data.get('email')

    # Search for the email in the dictionary
    if email in users:
        user_data = users[email]
        exist = True
        lottery_number = user_data['lottery_number']
        won = user_data['won']
    else:
        exist = False
        lottery_number = -1  # Using -1 to indicate not found or not applicable
        won = 'not applicable'

    # Respond with the data
    return jsonify({
        'exist': exist,
        'lottery_number': lottery_number,
        'won': won
    })


# debug=True to avoid restart the local development server manually after each change to your code.
# host='0.0.0.0' to make the server publicly available.
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=8080)