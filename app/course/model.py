from mongoengine import (
    StringField,
    ReferenceField,
    ListField,
    CASCADE,
    DateTimeField,
    FloatField,
    EmbeddedDocument,
    EmbeddedDocumentField,
)
from flask_mongoengine import Document
from datetime import datetime


class Course(Document):
    name = StringField(required=True, max_length=200)
    uni_course_code = StringField(required=True, max_length=200)
    description = StringField(required=True, max_length=200)
    teacher = ReferenceField("Teacher", reverse_delete_rule=CASCADE)
    campus = ReferenceField("Campus", reverse_delete_rule=CASCADE)
    created_time = DateTimeField(default=datetime.now)
    publish_time = DateTimeField(default=datetime.now)
    original_price = FloatField()
    cover_image = StringField()
    enrolled_students = ListField(ReferenceField("User"))

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "uni_course_code": self.uni_course_code,
            "description": self.description,
            "teacher": {
                "id": str(self.teacher.id),
                "display_name": self.teacher.display_name,
            },
            "campus": self.campus.to_dict(),
            "created_time": self.created_time.isoformat(),
            "publish_time": self.publish_time.isoformat(),
            "original_price": self.original_price,
            "cover_image": self.cover_image,
        }
