import datetime
from flask_restx import Namespace, Resource
from flask import request
from app import user

from flask_jwt_extended import create_access_token, current_user, jwt_required
from app.user import permission_required
from .model import User, Admin, Student, Teacher, check_password, get_hash_password
from ..campus.model import Campus

auth_api = Namespace('auth', description='Authentication related operations')
#auth_api
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
        return {"user": user.to_dict(), "token": jwt_token}, 201


# user_api
user_api = Namespace('users', description='User related operations')
@user_api.route('/')
class UserList(Resource):
    # @jwt_required()
    @permission_required()
    def get(self):
        return [user.to_dict() for user in User.objects()], 200


student_api = Namespace('students', description='Student related operations')
@student_api.route('/')
class StudentList(Resource):
    def post(self):
        request_data = request.json
        request_data['password'] = get_hash_password(request_data['password'])
        request_data['campus'] = Campus.objects(id=request_data['campus']).first_or_404("Campus not found")
        # from_json() api using to JSON string
        student = Student(**request_data)
        student.save()
        return student.to_dict(), 201



admin_api = Namespace('admins', description='Admin related operations')

teacher_api = Namespace('teachers', description='Teacher related operations')