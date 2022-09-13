from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    db="login_schema"
    def __init__(self,data):
        self.id = data['id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate(form_data):
        is_valid = True

        if len(form_data["first_name"]) < 2:
            flash("firt name needs to be more than 2 characters")
            is_valid=False

        if len(form_data["last_name"]) < 2:
            flash("last name needs to be more than 2 characters")
            is_valid=False

        if len(form_data["password"]) < 5:
            flash("password needs to be longer than 5 characters")
            is_valid=False
        
        if form_data["password"] != form_data["conf_pass"]:
            flash("passwords dont match")
            is_valid=False
        
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!")
            is_valid = False


        return is_valid   

    @classmethod
    def save(cls, data):
        query= "INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());"
        results= connectToMySQL(cls.db).query_db(query, data)

        return results
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])
