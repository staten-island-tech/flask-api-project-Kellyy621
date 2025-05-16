from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get ("")
singer_list = response.json()
print(singer_list)

#data of singers 
singers = [
    {
        "id":1,
        "Name":"Clairo",
        "Birthday":"August 18, 1998",
        "Nationality":"American"

        "id":2
        "Name":"Ethel Cain",
        "Birthday":"March 24, 1998",
        "Nationality":"American"

        "id":3
        "Name":"Phoebe Bridgers",
        "Birthday":"August 17, 1994",
        "Nationality":"American"

        "id":4
        "Name":"Ethel Cain",
        "Birthday":"November 7, 1996",
        "Nationality":"New Zealand"
    }
]
@app.route('/api/singers')
def get_singers():
    return jsonify(singers)

if __name__ == '__main__':
    app.run(debug=True)