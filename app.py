from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

#data of singers 
singers = [
    {
        "id":1,
        "Name":"Clairo",
        "Birthday":"August 18, 1998",
        "Nationality":"American",
        "Image":"clairo.jpg"
    },
    {   "id":2,
        "Name":"Ethel Cain",
        "Birthday":"March 24, 1998",
        "Nationality":"American",
        "Image":"ethel_cain.jpg"
    },
    {   "id":3,
        "Name":"Phoebe Bridgers",
        "Birthday":"August 17, 1994",
        "Nationality":"American",
        "Image":"phoebe_bridgers.jpg"
    },
    { "id":4,
        "Name":"Billie Ellish",
        "Birthday":"December 18, 2001",
        "Nationality":"American",
        "Image":"billie_ellish.jpg"
    }
]
@app.route('/api/singers')
def get_singers():
    return jsonify(singers)

@app.route('/')
def index():
     return render_template('index.html', singers=singers)

if __name__ == '__main__':
    app.run(debug=True)