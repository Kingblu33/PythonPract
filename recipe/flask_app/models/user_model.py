from flask_app.config.mysqlconnections import MySQLConnection, connectToMySQL
from flask_app.models import recipe_model

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

from flask import flash

class User: 
    db = "recipes"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['updated_at']
        self.updated_at = data['created_at']

        self.recipe = []


    @staticmethod
    def validate_info(form_data):
        is_valid=True
        if len(form_data["first_name"]) < 3 :
            flash("First Name needs to be more than three(3) characters")
            is_valid=False

        if len(form_data["last_name"]) < 3 :
            flash("last Name needs to be more than three(3) characters")
            is_valid=False
        if len(form_data["password"]) < 3 :
            flash("Password needs to be more than three(3) characters")
            is_valid=False
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(form_data["password"]) < 5:
            flash("password needs to be longer than 5 characters")
            is_valid=False

        if form_data["password"] != form_data["confirm_password"]:
            flash("passwords dont match")
            is_valid=False

        return is_valid
    @classmethod
    def save_new_user(cls,data):
        query="INSERT INTO users (first_name,last_name,email,password,updated_at,created_at) VALUES ( %(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());"
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    @classmethod
    def login(cls,data):
        query="SELECT * FROM users WHERE email=%(email)s;"
        results=connectToMySQL(cls.db).query_db(query,data)

        if len(results) < 1:
            return False

        return cls(results[0])
    
    @classmethod 
    def idek(cls,data):
        query="SELECT * FROM users WHERE id=%(id)s"
        results=connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def join(cls,data):
        query = "SELECT * FROM users left JOIN recipes ON users.id=recipes.user_id WHERE users.id=%(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)

        user= cls(results[0])

        for data in results:

            recipe_data = {
                "id" : data["recipes.id"], 
                
                "name" : data["name"],
                "description" : data["description"],
                "instructions" : data["instructions"],
                "under_30" : data["under_30"],
                "date_made" : data["date_made"],
                "user_id" : data["user_id"],

                "created_at" : data["recipes.created_at"],
                "updated_at" : data["recipes.updated_at"],
            }

            recipe_instance = recipe_model.Recipe(recipe_data)

            user.recipe.append(recipe_instance)
            print(recipe_instance)

        return user

    @classmethod
    def getoneu(cls,data):
        query="SELECT * FROM users WHERE id= %(id)s"
        results=connectToMySQL(cls.db).query_db(query,data)
        
        return  cls(results[0])