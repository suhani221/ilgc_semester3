from flask import Flask, request
import numpy
import folium

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form method="POST">
            <label>Name:</label>
            <input type="text" name="name"><br>
             <label>age:</label>
            <input type="text" name="age"><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/', methods=['POST'])
def form_data():
    name = request.form['name']
    age = request.form['age']
    latitude =name
    longitude = age
    map = folium.Map(location=[latitude, longitude], zoom_start=12)
    print("jn")
    map.save("mapgen2.html")
    return f'Hello, {latitude}! You are {longitude} years old.'

if __name__ == '__main__':
    app.run()





