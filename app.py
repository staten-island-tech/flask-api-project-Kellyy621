from flask import Flask, render_template, request, redirect, url_for 
import requests

app = Flask(__name__)

#Random dog facts
def random_dog_facts(number=5):
    try:
        url = f"https://dog-api.kinduff.com/api/facts?number={number}"
        response = requests.get(url, verify = True)
        response.raise_for_status()
        data = response.json()
        print(f"API response data: {data}")
        return data.get('facts')
    except Exception as x:
        print(f"Error getting random facts: {x}")
        return[]

#Random dog image(s)
def random_dog_image(breed=None):
    try:
        if breed:
            url=f"https://dog.ceo/api/breed/{breed.lower()}/images/random"
        else:
            url="https://dog.ceo/api/breeds/image/random"
        response = requests.get(url)
        data = response.json()
        return data.get('message')
    except Exception as x:
        print(f"Error getting message: {x}")
        return None
    
@app.route ('/')
def home():
    facts = random_dog_facts(5)
    image = random_dog_image()
    return render_template("home.html", facts=facts, image=image, error=None, breed=None)

@app.route('/search', methods=['GET'])
def search():
    breed = request.args.get('breed')
    if not breed:
        return redirect(url_for('home'))
    image = random_dog_image(breed)
    if not image:
        error = f"Breed '{breed}' not found"
        return render_template("home.html", facts=[], image = None, error = error, breed = breed)
    facts = random_dog_facts(5)
    return render_template("home.html", facts = facts, image = image, breed = breed)

@app.route('/generate-image')
def generate_image():
    image = random_dog_image()
    facts = random_dog_facts(5)
    return render_template('home.html', facts=facts, image=image)

@app.route('/facts/<int:number>')
def multiple_facts(number):
    facts = random_dog_facts(number)
    print(f"Requested number: {number}")
    print(f"Facts returned: {facts}") 
    return render_template("facts.html", facts=facts, number=number)

if __name__ == '__main__':
    app.run(debug=True)



    

       
