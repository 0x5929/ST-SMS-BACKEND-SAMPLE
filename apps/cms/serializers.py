from rest_framework import serializers

from .validators import CMSValidator
from .models import Client, Note


class NoteSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), allow_null=False)

    class Meta:
        exclude = ('note_uuid',)
        model = Note

    def validate_client(self, value):
        return CMSValidator.note_client_final_validation(value, self)
    # def create(self, validated_data):
    #     return super(NoteSerializer, self).create(Note.objects.create_or_update_note(validated_data=validated_data))

    # def update(self, instance, validated_data):
    #     return super(NoteSerializer, self).update(*Note.objects.create_or_update_note(validated_data=validated_data, instance=instance))


class ClientSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        exclude = ('client_uuid',)
        model = Client

    def validate_first_name(self, value):
        return CMSValidator.no_special_chars_and_captialize_string(value)

    def validate_last_name(self, value):
        return CMSValidator.no_special_chars_and_captialize_string(value)

    def validate_phone_number(self, value):
        return CMSValidator.phone_number_format_checker(value)

    def validate_city(self, value):
        return CMSValidator.no_special_chars_and_captialize_string(value)

    def validate(self, data):
        return CMSValidator.client_final_validation(self, data)
