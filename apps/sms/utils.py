import uuid

from rest_framework.exceptions import ValidationError


class DatabaseHandler():

    @staticmethod
    def create_or_update(validated_data, instance, model):
        if model.__name__ == 'School':
            # no nested relations need to be attached when creating, or updating
            pass
        elif model.__name__ == 'Program':
            # get school ID from request
            school_id = uuid.UUID(str(validated_data.get('school')))

            # retrieve said school from the DB using ID
            from .models import School
            school = School.objects.get(school_uuid__exact=school_id)

            # add school to the program object
            validated_data['school'] = school

        elif model.__name__ == 'Rotation':
            # get program ID from request
            program_id = uuid.UUID(str(validated_data.get('program')))

            # retrieve said program from the DB using ID
            from .models import Program
            program = Program.objects.get(program_uuid__exact=program_id)

            # add program to the rotation object
            validated_data['program'] = program

        elif model.__name__ == 'Student':
            # get rotation ID from request
            rotation_id = uuid.UUID(str(validated_data.get('rotation')))

            # retrieve said rotation from the DB using ID
            from .models import Rotation
            rotation = Rotation.objects.get(rotation_uuid__exact=rotation_id)

            # add rotation to the student object
            validated_data['rotation'] = rotation

        return (instance, validated_data) if instance else validated_data


class ExceptionHandler():

    @staticmethod
    def raise_verror(self, msg):
        raise ValidationError(msg)
