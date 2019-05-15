from django.db import models
from django.contrib.auth.models import User
from . import CommonProps

class Instructor(CommonProps):
    """Represents any lead instructor or junior instructor at NSS"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO: default doesn't seem to work in sqlite. Maybe in another SQL dialect?
    is_awesome = models.BooleanField(default=True)
    students = models.ManyToManyField("Student", through="InstructorStudent", related_name="instr_student")

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    # @property
    # def current_students(self):
    #     return self.students
