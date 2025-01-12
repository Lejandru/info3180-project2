"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
import datetime
from app import app, db, login_manager, csrf
from flask import render_template, request, redirect, url_for, flash, jsonify, g, make_response
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, RegisterForm, NewCarForm
from app.models import Users, Cars, Favs
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from sqlalchemy import or_


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###
@app.route("/api/register", methods=["POST"])
def register():
    form = RegisterForm(request.form)
    photo = request.files["photo"]
    form.photo.data = photo
    if request.method == "POST" and form.validate_on_submit() == True:
        username = form.username.data
        password = form.password.data
        name = form.name.data
        email = form.email.data
        location = form.location.data
        bio = form.biography.data
        photo = form.photo.data
        photo = uploadPhoto(form.photo.data)
        date_joined = form.date_joined.data

        try:
            #create user object and add to database
            user = Users(username, password, name, email, location, bio, photo, date_joined)
            if user is not None:
                db.session.add(user)
                db.session.commit()

                #flash message to indicate the a successful entry
                success = "User sucessfully registered"
                return jsonify(message=success), 201

        except Exception as e:
            print(e)
            db.session.rollback()
            error = "An error occured with the server. Try again!"
            return jsonify(error=error), 401

    #flash message to indicate registration failure
    failure = "Error: Invalid/Missing user information"
    return jsonify(error=failure), 401


@app.route("/api/cars", methods=["POST"])
@login_required

def addNewCar():
    form= NewCarForm(request.form)
    photo = request.files["photo"]
    form.photo.data = photo
    if request.method == "POST" and form.validate_on_submit() == True:
        #Gets the user input from the form
        make = form.make.data
        model = form.model.data
        colour = form.colour.data
        year = form.year.data
        transmission = form.transmission.data
        car_type = form.car_type.data
        price = float(form.price.data)
        description = form.description.data
        photo = form.photo.data
        photo = uploadPhoto(form.photo.data)
        user_id = int(form.user_id.data)

        try:
        #create user object and add to database
            car = Cars(description, make, model, colour, year, transmission, car_type, price, photo, user_id)
            if car is not None:
                db.session.add(car)
                db.session.commit()

                #flash message to indicate the a successful entry
                success = "Car sucessfully added"
                return jsonify(message=success), 201

        except Exception as e:
            print(e)
            db.session.rollback()
            error = "An error occured with the server. Try again!"
            return jsonify(error=error), 401

    #flash message to indicate failure
    failure = "Error: Invalid/Missing information"
    return jsonify(error=failure), 401




@app.route("/api/cars", methods=["GET"])

def allCars():
    try:
        cars = []
        allcars = db.session.query(Cars).order_by(Cars.id.desc()).all()

        for car in allcars:                                      

            c = {"photo": os.path.join(app.config['GET_FILE'], car.photo), "year": car.year, "make": car.make,"price":car.price, "model":car.model}
            cars.append(c)
        return jsonify(cars=cars), 201
    except Exception as e:
        print(e)

        error = "Internal server error"
        return jsonify(error=error), 401



#api route to allow the user to login into their profile on the application
@app.route("/api/auth/login", methods=["POST"])
def login():
    form = LoginForm(request.form)
    print(form.data)
    if request.method == "POST":
        # change this to actually validate the entire form submission
        # and not just one field
        if form.validate_on_submit():
            # Get the username and password values from the form.
            username = form.username.data
            password = form.password.data
           
            user = db.session.query(Users).filter_by(username=username).first()

            if user is not None and check_password_hash(user.password, password):
                # get user id, load into session
                login_user(user)

                #creates bearer token for user
                payload = {'user': user.username}
                jwt_token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm = 'HS256').decode('utf-8')

                #Flash message to indicate a successful login
                success = "User successfully logged in."
                return jsonify(message=success, token=jwt_token, user_id=user.id)

            error = "Incorrect username or password"
            return jsonify(error=error), 401

        #Flash message to indicate a failed login
        failure = "Failed to login user"
        return jsonify(error=failure)


#api route to allow the user to logout
@app.route("/api/auth/logout", methods=["GET"])
@login_required

def logout():
    logout_user()

    #Flash message indicating a successful logout
    success = "User successfully logged out."
    return jsonify(message=success)

#Save the uploaded photo to a folder
def uploadPhoto(upload):
    filename = secure_filename(upload.filename)
    upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return filename


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized_handler():
    #NOT SURE WHY ITS NOT RENDERING PROPERLY FOR EVERYTHING SO I DID THIS INSTEAD FOR THE LOGIN CHECK SO YOU CAN LOGOUT
    failure = "User not logged in"
    return jsonify(error=failure)


# gets the details of a specific car
@app.route('/api/cars/<car_id>',methods=["GET"])
@login_required

def car_details(car_id):
    if request.method=="GET":
        try:
            details= Cars.query.filter_by(id=car_id).first()
            if details is not None:
                return make_response(jsonify(details=details),201)
            else:
                return make_response(jsonify(response="Car not found"))
        except Exception as e:
            print(e)
            error="Internal server error"
            return make_response(jsonify(error=error)),401
    
#add car to favourites for logged in user
@app.route('/api/cars/<car_id>/favourite',methods=["POST"])
@login_required

def add_user_fav_car(username,car_id):
    if request.method=="POST":
        user= Users.query.filter_by(username=username).first()
        fav= Favs.query.filter_by(user_id=user.id,car_id=car_id).first()
        if fav is None:
            try:
                db.session.add(fav)
                db.session.commit()
                return make_response(jsonify(response="Added to Favourites"))
            except: 
                make_response(jsonify(response="Could not be found"))
        else:
            return make_response(jsonify(response="Item is already in Favourites"))

#search for cars by make or model
@app.route('/api/search',methods=["GET"])
@login_required

def search_cars(username):
    if request.method=="GET":
        query= request.args.get('query')
        query="%{}%".format(query)
        cars= Cars.query.filter(or_(Cars.model.like(query), Cars.make.like(query)))
        for car in cars:
                return make_response(jsonify({"cars":[car.to_json]}))
    else:
        return make_response(jsonify(response="Could not be found"))

# gets details of a user
@app.route('/api/users/<user_id>',methods=["GET"])
@login_required

def user_details(user_id):
    if request.method =="GET":
        try:
            details= Users.query.filter_by(id=user_id).first()
            if details is not None:
                return make_response(jsonify(details=details),201)
            else:
                return make_response(jsonify(response="User not found"))
        except Exception as e:
            print(e)
            error="Internal server error"
            return make_response(jsonify(error=error)),401


@app.route('/api/users/<user_id>/favourites',methods=["GET"])
@login_required

#CSRF token to be added 
def user_fav_car(username,user_id):
    if request.method =="GET":
        user= Users.query.filter_by(username=username).first()
        favs=db.session.query(Cars).join(Favs).filter(Favs.user_id==user.id)

        if favs is not None:
            for fav in favs:
                return make_response(jsonify({"favs":[fav.to_json]}))
        else:
            return make_response(jsonify(response="Could not be found"))

    
# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")