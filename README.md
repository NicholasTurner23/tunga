# This is a flask blog post template integrating a couple of extensions not limited to:
1. Flask
2. Flask-SQLAlchemy
3. Flask-Migrate
4. Flask-RESTful
5. Flask-Login
6. Bootstrap-Flask
7. Flask-WTF
8. email_validator
9. flask-marshmallow
10. marshmallow
11. marshmallow-sqlalchemy
12. Jinja2
13. passlib
14. python-dateutil
15. python-decouple
16. SQLAlchemy
### Ref: requirements.txt

# Make commands
1. make initializedb *create initial database. Change migrations/env.py depending on which database engine you are going to use*
2. make migrate message="Your migrations message" *To create migrations after changing the models"
3. make dbupgrade *To make the migration changes in your database*
4. make run *To run the application*
