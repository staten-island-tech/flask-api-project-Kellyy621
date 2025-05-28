from flask import Flask, render_template, request, redirect, url_for 
import requests

app = Flask(__name__)

#Random dog facts
def random_dog_facts():
    try:
        url = f"https://dog-api.kinduff.com/api/facts?number=[number]"
        response = requests.get(url)
        data = response.json()
        return data.get('facts')
    except Exception as x:
        print("Error getting random facts: {x}")
        return()

#Random dog image(s)
def random_dog_image(breed=None):
    try:
        if breed:
            url=f"https://dog.ceo/api/breed/{breed.lower()}/images/random"
        else:
            url="https://dog.ceo/api/breed/image/random"
        response = request.get(url)
        data = response.json()
        return data.get('message')
    except Exception as x:
        print(f"Error getting message: {x}")
        return None
    
@app.route ('/')
def home():
    facts = random_dog_facts(d)
    image = random_dog_image()
    return render_template("home.html", facts=facts, image=image)

@app.route('/search', methods=['POST'])
def search():
    breed = request.form.get('breed')
    if not breed:
        return redirect(url_for('home'))
    image = random_dog_image(breed)
    if not image:
        error = f"Breed '{breed}' not found"
        return render_template("home.html", facts=[], image = None, error = error)
    facts = random_dog_facts(d)
    return render_template("home.html", facts = facts, image = image, breed = breed)

@app.route('/facts/<int:number')
def multiple_facts(number):
    facts = random_dog_facts(number)
    return render_template("facts.html", facts = facts, number = number)

if __name__ == '__main__':
    app.run(debug=True)



    

       
