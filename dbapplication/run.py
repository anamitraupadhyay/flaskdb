from app import create_app

flask_app= create_app()

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=True) #instead of running app.py file we run run.py file
#running this file flask db init->flask db migrate command in terminal will result in an  error
#detected added table 'people'
#now to create a migration(upgrade it) run flask db upgrade
#init only once and migrate & upgrade everytime we make change in scheme(add a new class, change a field)
#sqlite3 testdb.db...for accessing testdb shell in sqlite