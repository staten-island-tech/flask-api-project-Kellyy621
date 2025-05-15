from flask import Flask, render_template
import requests

app = Flask(__name__)

#data of singers 

singers = [
    {
        "id":1,
        "Name":"Clairo",
        "Birthday":"August 18, 1998",
        "Nationality":"American"

        

    }
]