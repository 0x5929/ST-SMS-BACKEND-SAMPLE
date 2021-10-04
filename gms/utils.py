import uuid


class DatabaseHandler():

    @staticmethod
    def create_or_update(validated_data, instance, model):
        if model.__name__ == 'CNARotation':
            # no nested relations need to be attached when creating, or updating
            pass
        elif model.__name__ == 'CNAStudent':
            # get school ID from request
            rotation_id = uuid.UUID(str(validated_data.get('rotation')))

            # retrieve said school from the DB using ID
            from .models import CNARotation
            rotation = CNARotation.objects.get(
                rotation_uuid__exact=rotation_id)

            # add school to the program object
            validated_data['rotation'] = rotation

        elif model.__name__ == 'CNATheoryRecord' or \
                model.__name__ == 'CNAClinicalRecord':
            # get program ID from request
            student_id = uuid.UUID(str(validated_data.get('student')))

            # retrieve said program from the DB using ID
            from .models import CNAStudent
            student = CNAStudent.objects.get(student_uuid__exact=student_id)

            # add program to the rotation object
            validated_data['student'] = student

        return (instance, validated_data) if instance else validated_data
