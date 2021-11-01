from rest_framework import serializers

from .validators import SMSValidator
from .models import School, Program, Rotation, Student


class StudentSerializer(serializers.ModelSerializer):
    rotation = serializers.PrimaryKeyRelatedField(
        queryset=Rotation.objects.all(), allow_null=False)

    class Meta:
        fields = '__all__'
        model = Student

    def validate_student_id(self, value):
        return SMSValidator.student_id_format_checker(value)

    def validate_first_name(self, value):
        return SMSValidator.no_special_chars_and_captialize_string(value)

    def validate_last_name(self, value):
        return SMSValidator.no_special_chars_and_captialize_string(value)

    def validate_phone_number(self, value):
        return SMSValidator.phone_number_format_checker(value)

    def validate_mailing_address(self, value):
        return SMSValidator.no_special_chars_and_captialize_string(value)

    def validate_third_party_payer_info(self, value):
        return SMSValidator.no_special_chars_and_captialize_string(value)

    def validate_place_of_employment(self, value):
        return SMSValidator.no_special_chars_and_captialize_string(value)

    def validate_employment_address(self, value):
        return SMSValidator.no_special_chars_and_captialize_string(value)

    def validate_position(self, value):
        return SMSValidator.no_special_chars_and_captialize_string(value)

    def validate_description_of_attempts_to_contact_student(self, value):
        return SMSValidator.no_special_chars_and_captialize_string(value)

    def validate(self, data):
        return SMSValidator.student_final_validation(self, data)


class RotationSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    program = serializers.PrimaryKeyRelatedField(
        queryset=Program.objects.all(), allow_null=False)

    class Meta:
        fields = '__all__'
        model = Rotation
        depth = 1

    def validate_program(self, value):
        return value if not self.instance else SMSValidator.reference_does_not_change_on_updates(value, self.instance, 'program')

    def validate(self, data):
        return SMSValidator.rotation_final_validation(self, data)


class ProgramSerializer(serializers.ModelSerializer):
    rotations = RotationSerializer(many=True, read_only=True)
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(), allow_null=False)

    class Meta:
        fields = '__all__'
        model = Program
        depth = 2

    def validate_school(self, value):
        return value if not self.instance else SMSValidator.reference_does_not_change_on_updates(value, self.instance, 'school')

    def validate(self, data):
        return SMSValidator.program_final_validation(self, data)


class SchoolSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = School
        depth = 3

    def validate_school_name(self, value):
        return SMSValidator.no_special_chars_and_captialize_string(value)

    def validate_school_code(self, value):
        return SMSValidator.no_special_chars_and_captialize_string(value)

    def validate_school_address(self, value):
        return SMSValidator.no_special_chars_and_captialize_string(value)
