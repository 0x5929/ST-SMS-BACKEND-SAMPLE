import pytest
from rest_framework.exceptions import ValidationError

from gms.models import (CNARotation, 
                        HHARotation, 
                        CNAStudent, 
                        HHAStudent, 
                        CNATheoryRecord, 
                        CNAClinicalRecord, 
                        HHAClinicalRecord, 
                        HHATheoryRecord)

from gms.serializers import (CNARotationSerializer, 
                            HHARotationSerializer, 
                            CNAStudentSerializer, 
                            HHAStudentSerializer, 
                            CNATheoryRecordSerializer, 
                            CNAClinicalRecordSerializer, 
                            HHATheoryRecordSerializer, 
                            HHAClinicalRecordSerializer)

from sms.serializers import RotationSerializer as IncorrectSerializer

from gms.validators import GMSValidator

from .gms_constants import TEST_STUDENT_UUID, TEST_RECORD_TOPIC


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
    
    @pytest.fixture
    def get_incorrect_sms_serializer(self):
        return IncorrectSerializer()

    def test_reference_does_not_change_on_updates_cna_theory_success(self, get_cnaTheoryRecord_obj):
        instance = get_cnaTheoryRecord_obj
        reference = 'student'
        value = instance.student

        assert GMSValidator.reference_does_not_change_on_updates(
            value, instance, reference).student_uuid == get_cnaTheoryRecord_obj.student.student_uuid

    def test_reference_does_not_change_on_updates_cna_clinical_success(self, get_cnaClinicalRecord_obj):
        instance = get_cnaClinicalRecord_obj
        reference = 'student'
        value = instance.student

        assert GMSValidator.reference_does_not_change_on_updates(
            value, instance, reference).student_uuid == get_cnaClinicalRecord_obj.student.student_uuid


    def test_reference_does_not_change_on_updates_hha_theory_success(self, get_hhaTheoryRecord_obj):
        instance = get_hhaTheoryRecord_obj
        reference = 'student'
        value = instance.student

        assert GMSValidator.reference_does_not_change_on_updates(
            value, instance, reference).student_uuid == get_hhaTheoryRecord_obj.student.student_uuid

    def test_reference_does_not_change_on_updates_hha_clinical_success(self, get_hhaClinicalRecord_obj):
        instance = get_hhaClinicalRecord_obj
        reference = 'student'
        value = instance.student

        assert GMSValidator.reference_does_not_change_on_updates(
            value, instance, reference).student_uuid == get_hhaClinicalRecord_obj.student.student_uuid


    def test_reference_does_not_change_on_updates_cna_theory_failure(self, get_cnaTheoryRecord_obj):
        instance = get_cnaTheoryRecord_obj
        reference = 'student'
        value = TEST_STUDENT_UUID

        with pytest.raises(ValidationError):
            GMSValidator.reference_does_not_change_on_updates(value, instance, reference)

    def test_reference_does_not_change_on_updates_cna_clinical_failure(self, get_cnaClinicalRecord_obj):
        instance = get_cnaClinicalRecord_obj
        reference = 'student'
        value = TEST_STUDENT_UUID

        with pytest.raises(ValidationError):
            GMSValidator.reference_does_not_change_on_updates(value, instance, reference)

    def test_reference_does_not_change_on_updates_hha_theory_failure(self, get_hhaTheoryRecord_obj):
        instance = get_hhaTheoryRecord_obj
        reference = 'student'
        value = TEST_STUDENT_UUID

        with pytest.raises(ValidationError):
            GMSValidator.reference_does_not_change_on_updates(value, instance, reference)

    def test_reference_does_not_change_on_updates_hha_clinical_failure(self, get_hhaClinicalRecord_obj):
        instance = get_hhaClinicalRecord_obj
        reference = 'student'
        value = TEST_STUDENT_UUID

        with pytest.raises(ValidationError):
            GMSValidator.reference_does_not_change_on_updates(value, instance, reference)


    def test_get_current_rot_id_cna_success(self, get_cnaTheoryRecord_serializer, get_cnaStudent_obj):
        data = {'student': get_cnaStudent_obj}

        assert GMSValidator.get_current_rot_id(
            get_cnaTheoryRecord_serializer, data) == get_cnaStudent_obj.rotation.rotation_uuid

    def test_get_current_id_cna_failure(self, get_incorrect_sms_serializer, get_cnaStudent_obj):
        data = {'student': get_cnaStudent_obj}

        with pytest.raises(ValidationError):
            GMSValidator.get_current_rot_id(get_incorrect_sms_serializer, data)


    def test_get_current_rot_id_hha_success(self, get_hhaTheoryRecord_serializer, get_hhaStudent_obj):
        data = {'student': get_hhaStudent_obj}

        assert GMSValidator.get_current_rot_id(
            get_hhaTheoryRecord_serializer, data) == get_hhaStudent_obj.rotation.rotation_uuid

    def test_get_current_id_hha_failure(self, get_incorrect_sms_serializer, get_hhaStudent_obj):
        data = {'student': get_hhaStudent_obj}

        with pytest.raises(ValidationError):
            GMSValidator.get_current_rot_id(get_incorrect_sms_serializer, data)


    def test_no_duplicate_records_success(self, get_cnaTheoryRecord_serializer, get_cnaTheoryRecord_obj, monkeypatch):
        def does_not_exist(student__rotation__rotation_uuid__exact, topic__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return False

        def get_rot_id(serializer, data):
            return get_cnaTheoryRecord_obj.student.rotation.rotation_uuid

        monkeypatch.setattr(CNATheoryRecord.objects, 'filter', does_not_exist)
        monkeypatch.setattr(GMSValidator, 'get_current_rot_id', get_rot_id)
        data = {'topic': get_cnaTheoryRecord_obj.topic}

        assert GMSValidator.no_duplicate_records(get_cnaTheoryRecord_serializer, data) == data

    
    def test_no_duplicate_records_with_partial_success(self, get_cnaTheoryRecord_serializer, get_cnaTheoryRecord_obj, monkeypatch):
        def does_not_exist(student__rotation__rotation_uuid__exact, topic__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return False

        def get_rot_id(serializer, data):
            return get_cnaTheoryRecord_obj.student.rotation.rotation_uuid

        monkeypatch.setattr(CNATheoryRecord.objects, 'filter', does_not_exist)
        monkeypatch.setattr(GMSValidator, 'get_current_rot_id', get_rot_id)

        data = {'topic': get_cnaTheoryRecord_obj.topic}
        get_cnaTheoryRecord_serializer.partial = True

        assert GMSValidator.no_duplicate_records(get_cnaTheoryRecord_serializer, data) == data



    def test_no_duplicate_records_POST_failure(self, get_cnaTheoryRecord_serializer, get_cnaTheoryRecord_obj, monkeypatch):
        def does_exist(student__rotation__rotation_uuid__exact, topic__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return True

        def get_rot_id(serializer, data):
            return get_cnaTheoryRecord_obj.student.rotation.rotation_uuid

        monkeypatch.setattr(CNATheoryRecord.objects, 'filter', does_exist)
        monkeypatch.setattr(GMSValidator, 'get_current_rot_id', get_rot_id)
        data = {'topic': get_cnaTheoryRecord_obj.topic}

        with pytest.raises(ValidationError):
            GMSValidator.no_duplicate_records(get_cnaTheoryRecord_serializer, data)



    def test_no_duplicate_records_UPDATE_failure(self, get_cnaTheoryRecord_serializer, get_cnaTheoryRecord_obj, monkeypatch):
        def does_exist(student__rotation__rotation_uuid__exact, topic__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return True

        def get_rot_id(serializer, data):
            return get_cnaTheoryRecord_obj.student.rotation.rotation_uuid

        monkeypatch.setattr(CNATheoryRecord.objects, 'filter', does_exist)
        monkeypatch.setattr(GMSValidator, 'get_current_rot_id', get_rot_id)

        data = {'topic': get_cnaTheoryRecord_obj.topic}
        get_cnaTheoryRecord_serializer.instance = get_cnaTheoryRecord_obj
        get_cnaTheoryRecord_serializer.instance.topic = TEST_RECORD_TOPIC


        with pytest.raises(ValidationError):
            GMSValidator.no_duplicate_records(get_cnaTheoryRecord_serializer, data)




