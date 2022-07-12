from datetime import datetime
from email import message
import imp
from flask_restx import Namespace, Resource
from flask import request
from .model import User, Admin, Student, Teacher, check_password
from flask_jwt_extended import create_access_token, current_user

auth_api = Namespace('auth', description='Authentication related operations')


@auth_api.route('/login')
class login(Resource):
    # post contain request body(username and password)
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            return {'error': 'username or password is missing'}, 400

        # find the user in the database
        user = User.objects(username=username).first_or_404(
            message="User not found")

        if not check_password(password, user.password):
            # authentication failed
            return {'error': 'password is incorrect'}, 401

        jwt_token = create_access_token(
            identity=user.username, expires_delta=datetime.timedelta(days=30))

        # create a response containing the token
        return {"user":user.to_dict(), "token":jwt_token}, 201
