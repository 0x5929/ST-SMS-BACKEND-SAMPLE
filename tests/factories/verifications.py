import factory


class VerificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'account.emailaddress'
        django_get_or_create = ('email',)

    # defaults, can be overwritten in __init__
    verified = True
    primary = True
