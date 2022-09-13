from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import user_model
from flask import flash

class Recipe: 
    db = "recipes"
    def __init__(self,data):

        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user={}
    @staticmethod
    def validate_recipe(form_data):
        is_valid = True
        if len(form_data["name"]) < 3:
            flash("recipe name needs to be atleast 3 characters")
            is_valid = False
        if len(form_data["description"]) < 10:
            flash("descritpion needs to be atleast 10 characters")
            is_valid = False
        if len(form_data["instructions"]) < 10:
            flash("instructions  needs to be atleast 10 characters")
            is_valid=False
        if len(form_data["description"]) < 10:
            flash("descritpion needs to be atleast 10 characters")
            is_valid= False

        
        return is_valid

    @classmethod
    def save(cls,data):
        query="INSERT INTO recipes (name,description,instructions,under_30,date_made,user_id) VALUES( %(name)s ,%(description)s , %(instructions)s,%(under_30)s,%(date_made)s,%(user_id)s)"
        results=connectToMySQL(cls.db).query_db(query,data)

        return results
    
    @classmethod
    def get_one(cls,data):
        query="SELECT * FROM recipes WHERE id= %(id)s"
        results=connectToMySQL(cls.db).query_db(query,data)

        return cls(results[0])
    
    @classmethod
    def update_recipe(cls,data):
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,under_30=%(under_30)s,date_made=%(date_made)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)