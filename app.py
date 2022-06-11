from flask import Flask
from data import products #takes the products dictionary from the data.py
app = Flask(__name__)

@app.route('/')
def index(): #homepage HTML code
    return """<h1>Children's Corner!</h1>
            <p>We offer a great selection of products for kids</p>
            <p>Click on the links below!</p>
            <ul>
                <li><a href='/products/books'>Books for kids!</a></li>
                <li><a href='/products/toys'>Educational toys!</a></li>
                <li><a href='/products/school supplies'>School supplies!</a></li>
            </ul>
            <footer><a href='/about'>About us!</a></footer>
            """

@app.route('/about') #About Us page HTML code, maybe use part of the documentation?
def abtpage():
    return "<h1>About Us!</h1>" #use """ """ for multiple lines in one quote string

@app.route('/products/<pro_duct>') 
def product(pro_duct): #This is like the animals function in the adopt-a-pet code
    html = "<h1>List of {}</h1>".format(pro_duct)
    html += "<ul>"
    
    for count, product in enumerate(products[pro_duct]): #I followed Step 16 in the project
        html+="<li><a href='/products/"+pro_duct+"/"+str(count)+"'>"+product['name']+"</a></li>" #I formatted it like this because other formats wouldn't work lol

    
    html+= "</ul>"
    return html
    
@app.route('/products/<prod_type>/<int:x>') #prod_type is either books, toys or school supplies; x is the index of the specific item
def prod(prod_type,x): #this is the pet function described in step 13
    prod = products[prod_type][x] 
    html = "<h1>{}</h1>".format(prod['name'])
    
    html += "<p>Creator/Manufacturer: {}</p>".format(prod['creator'])
    html += "<p>Description: {}</p>".format(prod['description'])
    html += "<p>Price: {}</p>".format(prod['price'])

    
    
    
    return html

if __name__ == "__main__":
    app.run(debug=True)