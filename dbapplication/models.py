#in our flask app we don't have db tables we have class tables
#defining a person class, a person can have id, name, age etc.
#when connecting to a db we are connecting to db tables
#orm(sqlalchemy) is it converts classes into db tables
#model is going to be whatever we want to have in a db

from app import db
class Person(db.Model): #this person class inherit from db.Model(defining a db model now)
    __tablename__="people" #name of the table in db

    #defining fields
    pid=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text, nullable=False)
    age=db.Column(db.Integer)
    job=db.Column(db.Text)

    def __representation__(self):
        return f'person with {self.name} and age {self.age}'
    #a model's been made in my application, now we create a db but to do that we have to use this model in my app...creating 4th file routes.py
