import pytest

from gms.models import CNARotation, HHARotation, CNAStudent, HHAStudent, CNATheoryRecord, CNAClinicalRecord, HHAClinicalRecord, HHATheoryRecord
from gms.serializers import CNARotationSerializer, HHARotationSerializer, CNAStudentSerializer, HHAStudentSerializer, CNATheoryRecordSerializer, CNAClinicalRecordSerializer, HHATheoryRecordSerializer, HHAClinicalRecordSerializer
from gms.validators import GMSValidator

class User:
    def __init__(self, superuser=False, admin=False, staff=False):
        self.school_name = 'STI'
        self.is_superuser = superuser
        self.is_admin = admin
        self.is_staff = staff
        self.is_authenticated = None
        self.programs = None

class Request:
    def __init__(self, superuser=False, admin=False, staff=False):
        self.user = User(superuser=superuser, admin=admin, staff=staff)
        self.method = None


@pytest.mark.gms
@pytest.mark.current
class TestGMSValidator:

    @pytest.fixture
    def get_reg_cna_request_obj(self):
        ro = Request()
        ro.programs = ['CNA']

        return ro

    @pytest.fixture
    def get_reg_hha_request_obj(self):
        ro = Request()
        ro.programs = ['HHA']

        return ro

    @pytest.fixture
    def get_staff_cna_request_obj(self):
        ro = Request(staff=True)
        ro.programs = ['CNA']

        return ro

    @pytest.fixture
    def get_staff_hha_request_obj(self):
        ro = Request(staff=True)
        ro.programs = ['HHA']

        return ro

    @pytest.fixture
    def get_admin_request_obj(self):
        return Request(admin=True)

    @pytest.fixture
    def get_superuser_request_obj(self):
        return Request(superuser=True)

    @pytest.fixture
    def get_cnaRotation_obj(self):
        return CNARotation.objects.all().first()

    @pytest.fixture
    def get_hhaRotation_obj(self):
        return HHARotation.objects.all().first()

    @pytest.fixture
    def get_cnaStudent_obj(self):
        return CNAStudent.objects.all().first()

    @pytest.fixture
    def get_hhaStudent_obj(self):
        return HHAStudent.objects.all().first()

    @pytest.fixture
    def get_cnaTheoryRecord_obj(self):
        return CNATheoryRecord.objects.all().first()

    @pytest.fixture
    def get_cnaClinicalRecord_obj(self):
        return CNAClinicalRecord.objects.all().first()

    @pytest.fixture
    def get_hhaTheoryRecord_obj(self):
        return HHATheoryRecord.objects.all().first()

    @pytest.fixture
    def get_hhaClinicalRecord_obj(self):
        return HHAClinicalRecord.objects.all().first()

    @pytest.fixture
    def get_cnaRotation_serializer(self):
        return CNARotationSerializer()

    @pytest.fixture
    def get_hhaRotation_serializer(self):
        return HHARotationSerializer()

    @pytest.fixture
    def get_cnaStudent_serializer(self):
        return CNAStudentSerializer()

    @pytest.fixture
    def get_hhaStudent_serializer(self):
        return HHAStudentSerializer()

    @pytest.fixture
    def get_cnaTheoryRecord_serializer(self):
        return CNATheoryRecordSerializer()

    @pytest.fixture
    def get_cnaClinicalRecord_serializer(self):
        return CNAClinicalRecordSerializer()

    @pytest.fixture
    def get_hhaTheoryRecord_serializer(self):
        return HHATheoryRecordSerializer()

    @pytest.fixture
    def get_hhaClinicalRecord_serializer(self):
        return HHAClinicalRecordSerializer()
    