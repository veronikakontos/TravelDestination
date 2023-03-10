from flask_app import app, session, redirect, render_template, request
from flask_app.models.destination import Destination
import requests

@app.route('/destinations')
def destinations():
    if 'user_id' not in session:
        return redirect('/logout')
    # return "welcome to destinations {session['first_name]}"
    return render_template('destinations.html',destinations= Destination.get_all())

@app.route('/destinations/new')
def new_destination():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('new.html')

@app.route('/destination/popdest')
def popdest():
    print(request.form)
    return render_template('popdest.html')

@app.route('/destination/popdest/contact')
def contact_info():
    print(request.form)
    return render_template('contact.html')

#CREATE============================================================
@app.route('/destination/create', methods=['POST'])
def create_destination():
    print(request.form)
    if not Destination.validate_destination(request.form):
        return redirect('/destinations/new')
    Destination.save(request.form)
    return redirect('/destinations')
#SHOW================================================================
@app.route('/destination/<int:id>')
def show_destination(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : id
    }
    return render_template("show_destination.html", destination = Destination.get_one(data)) 

#EDIT====================================================================
@app.route('/destination/edit/<int:id>')
def edit_destination(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id
    }
    return render_template("edit_destination.html", destination = Destination.get_one(data)) 
    
#UPDATE=====================================================================
@app.route('/destinations/update/', methods = ['POST'])
def update_destination():
    if not Destination.validate_destination(request.form):
        return redirect(f'/destination/edit/{request.form["id"]}')
    Destination.update(request.form)
    return redirect ('/destinations')


@app.route('/weather/<city>')
def weather(city):
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=14d2b133467ff7fb5cda8f6d98e34ad5&units=imperial").json()
    print(data)
    session["weather"] = data
    return render_template('weather.html', data=data)


# DELETE=====================================================================
@app.route('/destination/delete/<int:id>')
def delete_destination(id):
    data ={'id': id}
    Destination.delete(data)
    return redirect('/destinations')