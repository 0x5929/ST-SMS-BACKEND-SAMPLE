from rest_framework import serializers
from .validators import ReferenceObjDoesNotChangeOnUpdates, NoSpecialCharactersAndCapitalizeString, StudentIDFormat
from .models import School, Program, Rotation, Student


class StudentSerializer(serializers.ModelSerializer):
    rotation = serializers.PrimaryKeyRelatedField(
        queryset=Rotation.objects.all(), allow_null=False)

    class Meta:
        fields = '__all__'
        model = Student

    def create(self, validated_data):
        return super(StudentSerializer, self).create(Student.objects.create_or_update_student(validated_data=validated_data))

    def update(self, instance, validated_data):
        return super(StudentSerializer, self).update(*Student.objects.create_or_update_student(validated_data=validated_data, instance=instance))


class RotationSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    program = serializers.PrimaryKeyRelatedField(
        queryset=Program.objects.all(), allow_null=False,
        validators=[ReferenceObjDoesNotChangeOnUpdates(reference="program_uuid")])

    class Meta:
        fields = '__all__'
        model = Rotation
        depth = 1

    def create(self, validated_data):
        return super(RotationSerializer, self).create(Rotation.objects.create_or_update_rotation(validated_data=validated_data))

    def update(self, instance, validated_data):
        return super(RotationSerializer, self).update(*Rotation.objects.create_or_update_rotation(validated_data=validated_data, instance=instance))


class ProgramSerializer(serializers.ModelSerializer):
    rotations = RotationSerializer(many=True, read_only=True)
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(), allow_null=False,
        validators=[ReferenceObjDoesNotChangeOnUpdates(reference="school_uuid")])

    class Meta:
        fields = '__all__'
        model = Program
        depth = 2

    def create(self, validated_data):
        return super(ProgramSerializer, self).create(Program.objects.create_or_update_program(validated_data=validated_data))

    def update(self, instance, validated_data):
        return super(ProgramSerializer, self).update(*Program.objects.create_or_update_program(validated_data=validated_data, instance=instance))


class SchoolSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = School
        depth = 3
        validators = [
            NoSpecialCharactersAndCapitalizeString(
                fields=['school_name', 'school_code', 'school_address'])

        ]

    def create(self, validated_data):
        return super(SchoolSerializer, self).create(School.objects.create_or_update_school(validated_data=validated_data))

    def update(self, instance, validated_data):
        return super(SchoolSerializer, self).update(*School.objects.create_or_update_school(validated_data=validated_data, instance=instance))


# from rest_framework.validators import UniqueForYearValidator

# class ExampleSerializer(serializers.Serializer):
#     # ...
#     class Meta:
#         # Blog posts should have a slug that is unique for the current year.
#         validators = [
#             UniqueForYearValidator(
#                 queryset=BlogPostItem.objects.all(),
#                 field='slug',
#                 date_field='published'
#             )
#         ]
