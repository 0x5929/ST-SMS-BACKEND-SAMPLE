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
    password = 'ye_rui_hu_xiao'

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""

        manager = cls._get_manager(model_class)
        # The default would use ``manager.create(*args, **kwargs)``
        # also we are ignoreing create_superuser, we can just override create_user settings to make the user a superuser
        return manager.create_user(*args, **kwargs)
