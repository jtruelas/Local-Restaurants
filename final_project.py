from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    return "This page will display all restaurants"


@app.route('/restaurants/new/')
def newRestaurant():
    return "This page will add a new restaurant"


@app.route('/restaurants/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    return "This page will edit restaurant %d" % restaurant_id


@app.route('/restaurants/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return "This page will delete restaurant %d" % restaurant_id


@app.route('/restaurants/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    return "This page will display menu items for \
    restaurant %d" % restaurant_id


@app.route('/restaurants/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
    return "This page will add menu items to \
    restaurant %d" % restaurant_id


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "This page will edit menu item %d from \
    restaurant %d" % (menu_id, restaurant_id)


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "This page will delete menu item %d from \
    restaurant %d" % (menu_id, restaurant_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
