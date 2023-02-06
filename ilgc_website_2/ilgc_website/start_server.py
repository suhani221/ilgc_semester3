from flask import Flask, request, render_template
from map_generator_pincode import *

app = Flask(__name__)  
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/', methods =["GET", "POST"])
def get_pincode():
    if request.method == "POST":
       pincode = request.form.get("pincode")
       pincode=str(pincode)
       make_map_pincode(pincode)
    return render_template("pincode.html")

@app.route('/generated.html')
def map():
    return render_template('generated.html')

if __name__=='__main__':
   app.run()