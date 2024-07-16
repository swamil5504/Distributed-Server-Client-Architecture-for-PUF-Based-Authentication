from flask import Flask, request, jsonify
from pymongo import MongoClient
import random

app = Flask(__name__)
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['PUF']
challenges_collection = db['CRPs']

def fetch_challenge():
    challenges_records = list(challenges_collection.find())
    if challenges_records:
        return random.choice(challenges_records)
    else:
        return None

@app.route('/send_challenge', methods=['GET'])
def send_challenge():
    challenge_record = fetch_challenge()
    if challenge_record:
        return jsonify({'challenge': challenge_record['Challenge']})
    else:
        return jsonify({'error': 'No challenges found in the database'})

@app.route('/receive_response', methods=['POST'])
def receive_response():
    data = request.json
    response = data.get('response')
    challenge = data.get('challenge')
    if response is not None and challenge is not None:
        stored_record = challenges_collection.find_one({'Challenge': challenge})
        if stored_record and stored_record['Response'] == response:
            return jsonify({'flag': True})  # Successful authentication
        else:
            return jsonify({'flag': False})
    else:
        return jsonify({'error': 'Invalid data received'})

if __name__ == '__main__':
    app.run(debug=True)
