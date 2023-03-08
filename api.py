from flask_restful import Resource
from flask import jsonify
from orm import db_session
from orm.models import *


class UserResource(Resource):
    def get(self, user_id):
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict()})


class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'user': [user.to_dict() for user in users]})