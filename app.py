from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the value of the 'name' parameter from the URL
    restaurant = request.args.get('restaurant')
    menu_item = request.args.get('menu_item')
    time = request.args.get('time')
     
    # Greet Hello to name provided in the URL Parameter
    return "Your order is placed!\nRestaurant:{}".format(restaurant)
