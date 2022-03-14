import pytest

from cms.models import Client, Note

from .cms_constants import CMS_CLIENT_UUID_TO_TEST, CMS_NOTE_UUID_TO_TEST, CLIENT_STR, NOTE_STR

@pytest.mark.cms
class TestCMSModelAttrRequirement:
    """
    Testing Minimum Attribute Requirements for each CMS models
    
    """

    def test_client_model_attr(self):
        client = Client.objects.get(client_uuid__exact=CMS_CLIENT_UUID_TO_TEST)

        if hasattr(client, 'client_uuid') and \
           hasattr(client, 'first_name') and \
           hasattr(client, 'last_name') and \
           hasattr(client, 'phone_number') and \
           hasattr(client, 'initial_contact') and \
           hasattr(client, 'email') and \
           hasattr(client, 'city') and \
           hasattr(client, 'success') and \
           hasattr(client, 'recruit_emails') and \
           hasattr(client, 'school_name'):

           assert True
        else:
            assert False

    def test_note_model_attr(self):
        note = Note.objects.get(note_uuid__exact=CMS_NOTE_UUID_TO_TEST)

        if hasattr(note, 'note_uuid') and \
           hasattr(note, 'date') and \
           hasattr(note, 'product') and \
           hasattr(note, 'price') and \
           hasattr(note, 'content') and \
           hasattr(note, 'client'):
           
           assert True
        else:
            assert False

@pytest.mark.cms
@pytest.mark.current
class TestCMSModelStr:

    """
    Testing str functions of each model in CMS app

    """

    def test_client_model_str(self):
        client = Client.objects.get(client_uuid__exact=CMS_CLIENT_UUID_TO_TEST)
        client.first_name = 'Test'
        client.last_name = 'A'
        assert str(client) == CLIENT_STR 
    
    def test_client_model_full_name_property(self):
        client = Client.objects.get(client_uuid__exact=CMS_CLIENT_UUID_TO_TEST)
        client.first_name = 'Test'
        client.last_name = 'A'
        assert str(client.full_name) == 'test_a' 

    def test_note_model_str(self):
        note = Note.objects.get(note_uuid__exact=CMS_NOTE_UUID_TO_TEST)

        assert str(note) == CMS_NOTE_UUID_TO_TEST