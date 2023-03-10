from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = 'destinations'
from flask_app import flash
# from flask_app.models.user import User

class City:
    def __init__(self, data):
        self.id = data['id'] 
        self.name = data['name']
        self.descriptions = data['descriptions']
        self.image = data['image']
        self.destination_id = data['destination_id']
        