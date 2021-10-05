from rest_framework import serializers

from ..validators import GMSValidator
from ..models import CNARotation, CNAStudent, CNATheoryRecord, CNAClinicalRecord


class CNATheoryRecordSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=CNAStudent.objects.all(), allow_null=False)

    class Meta:
        exclude = ('cna_theory_record_uuid',)
        model = CNATheoryRecord

    def validate_student(self, value):
        return GMSValidator.reference_does_not_change_on_updates(value, self.instance, 'student')

    def validate(self, data):
        return GMSValidator.no_duplicate_records(data, self.Meta.model.__name__)

    def create(self, validated_data):
        return super(CNATheoryRecordSerializer, self).create(CNATheoryRecord.objects.create_or_update(validated_data=validated_data))

    def update(self, instance, validated_data):
        return super(CNATheoryRecordSerializer, self).update(*CNATheoryRecord.objects.create_or_update(validated_data=validated_data, instance=instance))


class CNAClinicalRecordSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=CNAStudent.objects.all(), allow_null=False)

    class Meta:
        exclude = ('cna_clinical_record_uuid',)
        model = CNAClinicalRecord

    def validate_student(self, value):
        return GMSValidator.reference_does_not_change_on_updates(value, self.instance, 'student')

    def validate(self, data):
        return GMSValidator.no_duplicate_records(data, self.Meta.model.__name__)

    def create(self, validated_data):
        return super(CNAClinicalRecordSerializer, self).create(CNAClinicalRecord.objects.create_or_update(validated_data=validated_data))

    def update(self, instance, validated_data):
        return super(CNAClinicalRecordSerializer, self).update(*CNAClinicalRecord.objects.create_or_update(validated_data=validated_data, instance=instance))


class CNAStudentSerializer(serializers.ModelSerializer):
    rotation = serializers.PrimaryKeyRelatedField(
        queryset=CNARotation.objects.all(), allow_null=False)

    cna_theory_records = CNATheoryRecordSerializer(
        many=True, read_only=True)
    cna_clinical_records = CNAClinicalRecordSerializer(
        many=True, read_only=True)

    class Meta:
        exclude = ('student_uuid',)
        model = CNAStudent

    def validate(self, data):
        return GMSValidator.no_duplicate_students(data, self.Meta.model.__name__)

    def create(self, validated_data):
        return super(CNAStudentSerializer, self).create(CNAStudent.objects.create_or_update(validated_data=validated_data))

    def update(self, instance, validated_data):
        return super(CNAStudentSerializer, self).update(*CNAStudent.objects.create_or_update(validated_data=validated_data, instance=instance))


class CNARotationSerializer(serializers.ModelSerializer):
    cna_students = CNAStudentSerializer(
        many=True, read_only=True)

    class Meta:
        exclude = ('rotation_uuid',)
        model = CNARotation

    def validate(self, data):
        data = GMSValidator.date_checker(data)
        return GMSValidator.ensure_same_school_name(data, self.context.get('request'))

    # NOTE no more nested create/update here since we are at the top level, and thus no create/update methods are overridden here
