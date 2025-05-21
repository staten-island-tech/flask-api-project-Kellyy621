from flask import Flask, render_template, jsonify

app = Flask(__name__)

#data of singers 
singers = [
    {
        "id":1,
        "Name":"Clairo",
        "Birthday":"August 18, 1998",
        "Nationality":"American",
        "Songs":"Sofia, Bags, Juna",
        "Image":"https://wp.dailybruin.com/images/2024/07/Clairo-Charm-album-cover.jpeg"
    },
    {   "id":2,
        "Name":"Ethel Cain",
        "Birthday":"March 24, 1998",
        "Nationality":"American",
        "Songs":"Strangers, Televangelism, American Teenager",
        "Image":"https://a2.cdn.hhv.de/items/images/generated/970x970/01208/1208222/3-ethel-cain-preacher-s-daughter.webp"
    },
    {   "id":3,
        "Name":"Phoebe Bridgers",
        "Birthday":"August 17, 1994",
        "Nationality":"American",
        "Songs":"Waiting Room, Funeral, I Kmow The End, Scott Street",
        "Image":"https://cdn-images.dzcdn.net/images/cover/1dc007dfa7ce8eb17289a7722b98d5e9/1900x1900-000000-80-0-0.jpg"
    },
    { "id":4,
        "Name":"Billie Eilish",
        "Birthday":"December 18, 2001",
        "Nationality":"American",
        "Songs":"Wildflower, Birds of a Feather, What Was I Made For",
        "Image":"https://www.jambase.com/wp-content/uploads/2024/04/billie-eilish-new-album-hit-me-hard-and-soft-v2-1480x832.jpg"
    }
]
@app.route('/api/singers')
def get_singers():
    return jsonify(singers)

@app.route('/api/singers/<int:singer_id>')
def get_singer(singer_id):
    singer = next((s for s in singers if s["id"] == singer_id), None)
    if singer:
        return jsonify(singer)
    return jsonify({"error": "Singer not found"}), 404

@app.route('/')
def index():
     return render_template('index.html', singers=singers)

if __name__ == '__main__':
    app.run(debug=True)