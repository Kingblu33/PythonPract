from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojos_models

class Ninja:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.l_name = db_data['l_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def insertninja(cls,data ):
        query ="INSERT INTO ninjas ( first_name,l_name,age,dojo_id, created_at , updated_at ) VALUES (%(first_name)s,%(l_name)s, %(age)s,%(dojo_id)s ,NOW(),NOW());"
        results=connectToMySQL('dojos_ninjas').query_db(query,data)
        return results

