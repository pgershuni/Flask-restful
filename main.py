from orm import db_session
from flask import Flask
from flask_restful import Api
from api import *


db_session.global_init('db.sqlite')

#session = db_session.create_session()
#user1 = User(name='1', surname='a')
#user2 = User(name='2', surname='b')
#user3 = User(name='3', surname='c')
#session.add(user1)
#session.add(user2)
#session.add(user3)
#session.commit()


app = Flask('my web app')
api = Api(app)


api.add_resource(UserListResource, '/api/v2/users')
api.add_resource(UserResource, '/api/v2/users/<int:user_id>')


app.run()