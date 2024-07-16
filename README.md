
## Overview

This project demonstrates a test flow developed during my internship, illustrating a client-server architecture with a PUF-based authentication mechanism. The codebase includes a Flask server (`cityServer.py`) and a client (`client.py`) that interact with a MongoDB database to fetch challenges and verify responses. This test setup is also hosted on Docker on a Raspberry Pi, incorporating the logic developed in a research paper on securing IoT devices using PUF-driven lightweight challenge-response authentication protocols.

Note - This code doesn't contain the exact logic with which the client would react because of privacy concerns. This Script in all just demonstrates the basic flow of our Architecture.

## Prerequisites

- Python 3.x
- Flask
- pymongo
- requests
- MongoDB

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-repo/test-flow.git
   cd test-flow
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Start MongoDB:**

   Ensure MongoDB is running locally on `127.0.0.1:27017`. Create the required database and collection:

   ```sh
   mongo
   use PUF
   db.createCollection("CRPs")
   ```

   Populate the `CRPs` collection with your challenge-response pairs.

## Running the Server

1. **Start the Flask server:**

   ```sh
   python cityServer.py
   ```

   This will start the server on `http://127.0.0.1:5000`.

## Running the Client

1. **Start the client:**

   ```sh
   python client.py
   ```

   The client will continuously request challenges from the server, compute responses, and send them back for verification.

## Code Explanation

### cityServer.py

The server-side script, `cityServer.py`, handles fetching challenges from the MongoDB database and verifying client responses.

- **Dependencies:**

  ```python
  from flask import Flask, request, jsonify
  from pymongo import MongoClient
  import random
  ```

- **Database Setup:**

  ```python
  client = MongoClient('mongodb://127.0.0.1:27017/')
  db = client['PUF']
  challenges_collection = db['CRPs']
  ```

- **Endpoints:**

  - `/send_challenge`: Sends a random challenge from the database.
  - `/receive_response`: Verifies the response received from the client.

### client.py

The client-side script, `client.py`, fetches challenges from the server, computes a response using a test logic (response = challenge * 2 + 1), and sends the response back to the server for verification.

- **Dependencies:**

  ```python
  import requests
  import time
  ```

- **Functions:**

  - `receive_challenge()`: Fetches a challenge from the server.
  - `send_response(challenge, response)`: Sends the computed response to the server.

## Docker Setup

This project is also hosted on Docker on a Raspberry Pi, where the logic is adapted according to the research paper developed during the internship. To set up the project on Docker:

1. **Build Docker Images:**

   ```sh
   docker build -t city_server ./city_server
   docker build -t client ./client
   ```

2. **Run Docker Containers:**

   ```sh
   docker-compose up
   ```

This setup includes a Docker Compose configuration to orchestrate the Flask server, client, and MongoDB containers.

## Conclusion

This project summarizes the client-server architecture and response logic used to test the PUF-based authentication mechanism. The current setup is hosted on Docker on a Raspberry Pi, aligning with the developed research paper's logic.

## Additional Information

- The logic for response calculation and challenge handling can be modified as per the requirements of the research paper.
- Ensure MongoDB is populated with appropriate challenge-response pairs for accurate testing.
