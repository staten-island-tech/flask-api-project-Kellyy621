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
    
def random_dog_image(breed=None):
    try:
        if breed:
            url=f"https://dog.ceo/api/breed/{breed.lower()}/images/random"
        else:
            url="https://dog.ceo/api/breed/image/random"
        response = request.get(url)
        data = response.json()
        return data.get('message')
    

# New route: When a user clicks a Pokémon card, this page shows more details and a stats chart
@app.route("/pokemon/<int:id>")
def pokemon_detail(id):
    # Get detailed info for the Pokémon using its id
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    
    # Extract extra details like types, height, and weight
    types = [t['type']['name'] for t in data['types']]
    height = data.get('height')
    weight = data.get('weight')
    name = data.get('name').capitalize()
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
    
    # Extract base stats for the chart (e.g., hp, attack, defense, etc.)
    stat_names = [stat['stat']['name'] for stat in data['stats']]
    stat_values = [stat['base_stat'] for stat in data['stats']]
    
    # Send all details to the pokemon.html template
    return render_template("pokemon.html", pokemon={
        'name': name,
        'id': id,
        'image': image_url,
        'types': types,
        'height': height,
        'weight': weight,
        'stat_names': stat_names,
        'stat_values': stat_values
    })

if __name__ == '__main__':
    app.run(debug=True)

    
