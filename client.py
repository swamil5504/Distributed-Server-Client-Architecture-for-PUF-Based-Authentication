import requests
import time

def receive_challenge():
    url = 'http://127.0.0.1:5000/send_challenge'  # Adjust URL if necessary
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('challenge')
        else:
            print(f"Failed to receive challenge. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching challenge: {e}")

    return None

def send_response(challenge, response):
    url = 'http://127.0.0.1:5000/receive_response'  # Adjust URL if necessary
    try:
        response = requests.post(url, json={'challenge': challenge, 'response': response})
        if response.status_code == 200:
            result = response.json()
            print(f"Response status: {result.get('flag')}")
        else:
            print(f"Failed to send response. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending response: {e}")

if __name__ == '__main__':
    while True:
        challenge = receive_challenge()
        if challenge is not None:
            # Calculate response using the logic challenge * 2 + 1
            response = challenge * 2 + 1
            send_response(challenge, response)
        else:
            print("No challenge received.")
            break  # Exit loop if no challenge is received

        time.sleep(1)  # Adjust sleep duration as needed
