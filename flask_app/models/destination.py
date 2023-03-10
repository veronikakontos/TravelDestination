from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = 'destinations'
from flask_app import flash
from flask_app.models.city import City

# from flask_app.models.user import User

class Destination:
    def __init__(self, data):
        self.id = data['id'] 
        self.name = data['name']
        self.descriptions = data['descriptions']
        self.date_made = data['date_made']
        self.price = data['price']
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.cities = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO destinations (name, descriptions, date_made, price ,user_id) VALUES (%(name)s, %(descriptions)s, %(date_made)s, %(price)s, %(user_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM destinations JOIN users ON users.id = destinations.user_id"
        results = connectToMySQL(DATABASE).query_db(query)
        destinations = []
        for destination in results:
            destinations.append(cls(destination))
        return destinations


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM destinations Join users ON users.id = destinations.user_id LEFT JOIN cities on destinations.id = cities.destination_id WHERE destinations.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        destination = Destination(result[0])
        for city in result:
            temp_city = {
                "id" : city['id'],
                "name" : city['cities.name'],
                "descriptions" : city['cities.descriptions'],
                "image" : city['image'],
                "destination_id" : city['destination_id']
            }
            destination.cities.append(City(temp_city))

            

            
        return destination


    @classmethod
    def update(cls, data):
        query = "UPDATE destinations SET name = %(name)s, descriptions = %(descriptions)s, date_made = %(date_made)s, price = %(price)s WHERE destinations.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_destination(destination):
        is_valid = True
        if len(destination['name']) < 1:
            flash("Name is to short")
            is_valid = False
        if len(destination['descriptions']) < 4:
            flash("Descriptions shoulb be longer")
            is_valid = False
        if len(destination['date_made']) == "":
            flash("Enter a date")
            is_valid = False
        if not 'price'in destination:
            flash("Price is incorrect")
            is_valid = False

        # if int(destination['number_served']) <= 0:
        #     flash("Destination has to have at least 1 person")
        #     is_valid = False
        return is_valid
    
    # DELETE DESTINATION
    @classmethod
    def delete(cls,data):
            query  = "DELETE FROM destinations WHERE id = %(id)s;"
            return connectToMySQL(DATABASE).query_db(query,data)   
