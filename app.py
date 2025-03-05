from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the value of the 'name' parameter from the URL
    restaurant = request.args.get('restaurant')
    menu_item = request.args.get('menu_item')
    time = request.args.get('time')
    
    respond = "Your order is placed! \n Restaurant: " + restaurant
    return respond
