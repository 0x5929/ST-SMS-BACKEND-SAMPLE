from rest_framework import serializers

from ..validators import GMSValidator
from ..models import HHARotation, HHAStudent, HHATheoryRecord, HHAClinicalRecord


class HHATheoryRecordSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=HHAStudent.objects.all(), allow_null=False)

    class Meta:
        exclude = ('hha_theory_record_uuid',)
        model = HHATheoryRecord

    def validate_student(self, value):
        return GMSValidator.reference_does_not_change_on_updates(value, self.instance, 'student')

    def validate(self, data):
        return GMSValidator.no_duplicate_records(self, data)

    # def create(self, validated_data):
    #     return super(HHATheoryRecordSerializer, self).create(HHATheoryRecord.objects.create_or_update(validated_data=validated_data))

    # def update(self, instance, validated_data):
    #     return super(HHATheoryRecordSerializer, self).update(*HHATheoryRecord.objects.create_or_update(validated_data=validated_data, instance=instance))


class HHAClinicalRecordSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=HHAStudent.objects.all(), allow_null=False)

    class Meta:
        exclude = ('hha_clinical_record_uuid',)
        model = HHAClinicalRecord

    def validate_student(self, value):
        return GMSValidator.reference_does_not_change_on_updates(value, self.instance, 'student')

    def validate(self, data):
        return GMSValidator.no_duplicate_records(self, data)

    # def create(self, validated_data):
    #     return super(HHAClinicalRecordSerializer, self).create(HHAClinicalRecord.objects.create_or_update(validated_data=validated_data))

    # def update(self, instance, validated_data):
    #     return super(HHAClinicalRecordSerializer, self).update(*HHAClinicalRecord.objects.create_or_update(validated_data=validated_data, instance=instance))


class HHAStudentSerializer(serializers.ModelSerializer):
    rotation = serializers.PrimaryKeyRelatedField(
        queryset=HHARotation.objects.all(), allow_null=False)

    hha_theory_records = HHATheoryRecordSerializer(
        many=True, read_only=True)
    hha_clinical_records = HHAClinicalRecordSerializer(
        many=True, read_only=True)

    class Meta:
        exclude = ('student_uuid',)
        model = HHAStudent

    def validate(self, data):
        return GMSValidator.no_duplicate_students(self, data)

    # def create(self, validated_data):
    #     return super(HHAStudentSerializer, self).create(HHAStudent.objects.create_or_update(validated_data=validated_data))

    # def update(self, instance, validated_data):
    #     return super(HHAStudentSerializer, self).update(*HHAStudent.objects.create_or_update(validated_data=validated_data, instance=instance))


class HHARotationSerializer(serializers.ModelSerializer):
    hha_students = HHAStudentSerializer(
        many=True, read_only=True)

    class Meta:
        exclude = ('rotation_uuid',)
        model = HHARotation

    def validate(self, data):
        return GMSValidator.final_rot_validation(self, data)
