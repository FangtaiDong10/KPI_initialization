from flask_mongoengine import Document
from mongoengine import StringField, ReferenceField, ListField


class User(Document):
    username = StringField(required=True, unique=True, max_length=36)
    password = StringField(required=True)
    display_name = StringField()
    telephone = StringField()
    campus = ReferenceField('Campus', reverse_delete_rule='CASCADE')

    # allow to derive from this class
    meta = {"allow_inheritance": True}

    def to_dict(self):
        return {
            'id': str(self.id),
            'username': self.username,
            'display_name': self.display_name,
            'campus': self.campus.name,
            'telephone': self.telephone,

            # print class name
            'user_type': str(self._cls)
        }


class Student(User):
    wx = StringField()
    uni = StringField()

    def to_dict(self):
        return super().to_dict() | {"wx": self.wx, "uni": self.uni}


class Admin(User):
    permissions = ListField(StringField(), required=True, default=[])

    def to_dict(self):
        return super().to_dict() | {"permissions": self.permissions}


class Teacher(User):
    abn = StringField(max_length=20)
    
    def to_dict(self):
        return super().to_dict() | {"abn": self.abn}

