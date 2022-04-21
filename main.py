import os
from flask import Flask, request
import requests

app = Flask(__name__)

# # Take note of the two endpoints below. They may look the same but one processes GET requests and one processes POST requests

# If a GET request is made
@app.route("/person", methods=["GET"])
def person():
    print("Getting a random person")

    person_json = requests.get("https://randomuser.me/api").json()

    return person_json


# If a POST request is made
@app.route("/person", methods=["POST"])
def person_of_nationality():
    nationality = request.form.get("nationality")

    print(f"Search for person with nationality {nationality}")

    person_json = requests.get(
        "https://randomuser.me/api", params={"nat": nationality}
    ).json()

    return person_json


# If a GET request is made
@app.route("/people", methods=["GET"])
def people():
    number_of_people = request.args.get("number_of_people")

    print(f"Search for {number_of_people} people")

    person_json = requests.get(
        "https://randomuser.me/api", params={"results": number_of_people}
    ).json()

    return person_json


if __name__ == "__main__":
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
