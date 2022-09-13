from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas_models

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas=[]


    @classmethod
    def alldojos(cls):
        query="SELECT * FROM dojos"

        results=connectToMySQL('dojos_ninjas').query_db(query)
        dojos=[]

        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def savedojo(cls,data):
        query = "Insert INTO dojos (name,created_at,updated_at) VALUES(%(name)s,NOW(),NOW());"
        results = connectToMySQL('dojos_ninjas').query_db(query,data)
        return results
    
    @classmethod
    def get_ninjas_with_dojos( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN  ninjas ON dojos.id = ninjas.dojo_id WHERE dojo_id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
        dojo = cls( results[0] )
        for data in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_info= {
                "id" : data["ninjas.id"],
                "first_name" : data["first_name"],
                "l_name" : data["l_name"],
                "age" : data["age"],
                "created_at" : data["ninjas.created_at"],
                "updated_at" : data["ninjas.updated_at"]
            }
            ninja_instance=ninjas_models.Ninja(ninja_info)
            dojo.ninjas.append(ninja_instance)

        return dojo

