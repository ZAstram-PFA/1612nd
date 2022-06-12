from flask import Flask, render_template
from data import data
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def abtpage():
    return render_template('about.html')

@app.route('/product/<data_type>')
def product(data_type): 
    data_list = data[data_type]
    return render_template('products.html',product_type_template=data_type, product_template=data_list)

@app.route('/product/<data_type>/<int:data_id>') 
def datas(data_type,data_id):
    data_profile = data[data_type][data_id] 
    return render_template('stuff.html',data_profile=data_profile)

if __name__ == "__main__":
    app.run(debug=True)
