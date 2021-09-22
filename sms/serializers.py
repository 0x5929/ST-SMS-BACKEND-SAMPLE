from rest_framework import serializers
from .models import School, Program, Rotation, Student


class StudentSerializer(serializers.ModelSerializer):
    rotation = serializers.PrimaryKeyRelatedField(
        queryset=Rotation.objects.all(), allow_null=False)

    class Meta:
        fields = '__all__'
        model = Student


class RotationSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    program = serializers.PrimaryKeyRelatedField(
        queryset=Program.objects.all(), allow_null=False)

    class Meta:
        fields = '__all__'
        model = Rotation
        depth = 1


class ProgramSerializer(serializers.ModelSerializer):
    rotations = RotationSerializer(many=True, read_only=True)
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(), allow_null=False)

    class Meta:
        fields = '__all__'
        model = Program
        depth = 2


class SchoolSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = School
        depth = 3
