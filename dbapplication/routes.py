from flask import render_template, request

from models import Person

#a function to avoid circular imports
def register_routes(app, db):
    @app.route('/', methods=['POST','GET'])
    def index():
        if request.method == "GET":
            people=Person.query.all() #sends query all? i.e. like select * in mysql?
            return render_template("index.html",people=people)
        elif request.method == "POST":
            name= request.form.get('name')
            age=int(request.form.get('age'))
            job=request.form.get('job')

            person=Person(name=name,age=age, job=job)   #this object i.e instance of class we should add it to db in next line

            db.session.add(Person)
            db.session.commit()

            people=Person.query.all()
            return render_template("index.html", people=people)

    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter(Person.pid==pid).delete()
        db.session.commit()
        people=Person.query.all()
        return render_template("index.html", people=people)
        #/delete/1(even if we have 1 entry of people) doesn't work as we are using get method in the browser, i.e. we have to use js function or c# function if blazor is used. we have to send a delete request to the backend

    @app.route('/details/<pid>')
    def details(pid):
        person=Person.query.filter(Person.pid==pid).first()
        return render_template('detail.html', person=person)
