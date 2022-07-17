import datetime
from email import message
from flask_restx import Namespace, Resource
from flask import request, jsonify

from app.user import permission_required
from .model import Course

from flask_jwt_extended import create_access_token, current_user, jwt_required
from ..utils import paginate


course_api = Namespace("courses")

@course_api.route("/")
class CourseListApi(Resource):
    @permission_required()
    def get(self):
        query = {}
        if "campus" in request.args:
            query["campus"] = request.args["campus"]

        page = request.args.get("page", 1, int)

        return paginate(Course.objects(**query), page)

    @permission_required()
    def post(self):
        # convert JSON data to document instance
        course = Course.from_json(request.data)
        course.save()
        return course.to_dict(), 201

@course_api.route("/<course_id>")
class CourseApi(Resource):
    @jwt_required()
    def get(self, course_id):
        course = Course.objects(id=course_id).first_or_404()
        return course.to_dict()