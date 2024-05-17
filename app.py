from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return f'''
  <h1> Adopt a Pet!</h1>
  <p> Browse through the links below to find your new furry friend: </p>
  <li><a href='/animals/dogs'>Dogs</a><li>
  <li><a href='/animals/cats'>Cats</a><li>
  <li><a href='/animals/rabbits'>Rabbits</a><li>
  '''
@app.route('/animals/<pet_type>')
def animals(pet_type):
  pet_list_html = ""
  for idx, pet in enumerate(pets[pet_type]):
    pet_list_html += f'''<li><a href = '/animals/{pet_type}/{idx}'>{pet['name']}</a></li>'''
  html = f'''
    <h1>List of {pet_type}</h1>
    <ul>
      {pet_list_html}
    </ul>
  '''
  return html

@app.route('/pet/<pet_type>/<pet_id>')
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  html = f'''
    <h1>{pet["name"]}</h1>
    <img src="{pet["url"]}" />
    <p>{pet["description"]}</p>
    <ul>
      <li>{pet["breed"]}</li>
      <li>{pet["age"]}</li>
    </ul>
    <ul>'''
  return html