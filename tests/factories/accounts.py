import factory

from apps.authentication.models import Account
from apps.sms.models import School, Program, Rotation, Student
from apps.cms.models import Client, Note
from apps.gms.models import CNARotation, HHARotation, CNAStudent, HHAStudent, CNATheoryRecord, HHATheoryRecord, CNAClinicalRecord, HHAClinicalRecord


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account
        django_get_or_create = ('email',)

    # defaults, can be overwritten in __init__
    school_name = 'STI'
