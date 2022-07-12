from flask_jwt_extended import jwt_required
from .model import User
import functools

from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user


def permission_required(permission=None):
    def wrapper(func):
        @jwt_required()
        @functools.wraps(func)
        def decorator(*args, **kwargs):

            if current_user._cls == "User.Admin":
                if permission is None or permission in current_user.permissions:
                    return func(*args, **kwargs)
                else:
                    return {'message': f"Permission '{permission}' is required"}

            return {'message': "Permission denied"}, 403



# taking the jwt manager from app instance

def register_user_lookup(jwt):

    def user_lookup_callback(jwt_header, jwt_payload):
        identity = jwt_payload['sub']
        return User.objects(username=identity).first_or_404(message="User not found")

    # use jwt user_lookup_loader function to activate the callback function
    jwt.user_lookup_loader(user_lookup_callback)
