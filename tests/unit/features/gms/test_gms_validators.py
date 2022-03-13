import py
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




    def test_no_duplicate_students_success(self, get_cnaStudent_serializer, get_cnaStudent_obj,  monkeypatch):
        def does_not_exist(rotation__rotation_uuid__exact, first_name__iexact, last_name__iexact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return False
        
        monkeypatch.setattr(CNAStudent.objects, 'filter', does_not_exist)
        data = {
            'rotation': get_cnaStudent_obj.rotation,
            'first_name': get_cnaStudent_obj.first_name,
            'last_name': get_cnaStudent_obj.last_name}

        assert GMSValidator.no_duplicate_students(get_cnaStudent_serializer, data) == data


    
    def test_no_duplicate_students_success_with_partial(self, get_cnaStudent_serializer, monkeypatch):
        def does_not_exist(rotation__rotation_uuid__exact, first_name__iexact, last_name__iexact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return False
        
        monkeypatch.setattr(CNAStudent.objects, 'filter', does_not_exist)
        get_cnaStudent_serializer.partial = True
        data = {
            'rotation': None,
            'first_name': None,
            'last_name': None}


        assert GMSValidator.no_duplicate_students(get_cnaStudent_serializer, data) == data

    def test_no_duplicate_students_failure(self, get_cnaStudent_serializer, get_cnaStudent_obj, monkeypatch):
        def does_exist(rotation__rotation_uuid__exact, first_name__iexact, last_name__iexact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return True
        
        monkeypatch.setattr(CNAStudent.objects, 'filter', does_exist)
        data = {
            'rotation': get_cnaStudent_obj.rotation,
            'first_name': get_cnaStudent_obj.first_name,
            'last_name': get_cnaStudent_obj.last_name}

        with pytest.raises(ValidationError):
            GMSValidator.no_duplicate_students(get_cnaStudent_serializer, data)


    def test_date_checker_success(self, get_cnaRotation_obj):
        instance = get_cnaRotation_obj
        data = {'start_date': '2021-10-10', 'end_date' : '2021-10-11'}
        
        assert GMSValidator.date_checker(data, instance) == data

    def test_date_checker_success_with_partial_and_start(self, get_cnaRotation_obj):
        instance = get_cnaRotation_obj
        instance.start_date = '2021-10-09'
        data = {'end_date' : '2021-10-11'}
        
        assert GMSValidator.date_checker(data, instance, partial=True) == data

    def test_date_checker_success_with_partial_and_end(self, get_cnaRotation_obj):
        instance = get_cnaRotation_obj
        instance.end_date = '2021-10-12'
        data = {'start_date' : '2021-10-11'}
        
        assert GMSValidator.date_checker(data, instance, partial=True) == data

    def test_date_checker_failure(self, get_cnaRotation_obj):
        instance = get_cnaRotation_obj
        data = {'start_date': '2021-10-10', 'end_date' : '2021-10-09'}
        
        with pytest.raises(ValidationError):
            GMSValidator.date_checker(data, instance)


    def test_ensure_same_school_name_rotation_success(self, get_reg_cna_request_obj):
        data = {'school_name': get_reg_cna_request_obj.user.school_name}

        assert GMSValidator.ensure_same_school_name(data, get_reg_cna_request_obj, 'Rotation', partial=False) == data

    def test_ensure_same_school_name_rotation_success_superuser(self, get_superuser_request_obj):
        data = {'school_name': '__DIFF_SCHOOL_NAME__'}

        assert GMSValidator.ensure_same_school_name(data, get_superuser_request_obj, 'Rotation', partial=False) == data

    def test_ensure_same_school_name_rotation_success_with_partial(self, get_reg_cna_request_obj):
        data = {'school_name': None}

        assert GMSValidator.ensure_same_school_name(data, get_reg_cna_request_obj, 'Rotation', partial=True) == data


    def test_ensure_same_school_name_rotation_failure(self, get_reg_cna_request_obj):
        data = {'school_name': '__DIFF_SCHOOL_NAME__'}

        with pytest.raises(ValidationError):
            GMSValidator.ensure_same_school_name(data, get_reg_cna_request_obj, 'Rotation', partial=False)

    def test_ensure_same_school_name_student_success(self, get_cnaRotation_obj, get_reg_cna_request_obj):
        data = {'rotation': get_cnaRotation_obj}
        rot_obj = data.get('rotation')
        rot_obj.school_name = get_reg_cna_request_obj.user.school_name

        assert GMSValidator.ensure_same_school_name(data, get_reg_cna_request_obj, 'Student', partial=False) == data

    def test_ensure_same_school_name_student_success_superuser(self, get_cnaRotation_obj, get_superuser_request_obj):
        data = {'rotation': get_cnaRotation_obj}
        rot_obj = data.get('rotation')
        rot_obj.school_name = '__DIFF_SCHOOL_NAME__'

        assert GMSValidator.ensure_same_school_name(data, get_superuser_request_obj, 'Student', partial=False) == data


    def test_ensure_same_school_name_student_success_partial(self, get_cnaRotation_obj):
        data = {'rotation': None}

        assert GMSValidator.ensure_same_school_name(data, get_cnaRotation_obj, 'Student', partial=True) == data

        data = {'rotation':get_cnaRotation_obj}
        rot_obj = data.get('rotation')
        rot_obj.school_name = None

        assert GMSValidator.ensure_same_school_name(data, get_cnaRotation_obj, 'Student', partial=True) == data

    def test_ensure_same_school_name_student_failure(self, get_cnaRotation_obj, get_reg_cna_request_obj):
        data = {'rotation': get_cnaRotation_obj}
        rot_obj = data.get('rotation')
        rot_obj.school_name = '__DIFF_SCHOOL_NAME__'

        with pytest.raises(ValidationError):
            GMSValidator.ensure_same_school_name(data, get_reg_cna_request_obj, 'Student', partial=False)


    def test_ensure_same_school_name_record_success(self, get_cnaStudent_obj, get_cnaRotation_obj, get_reg_cna_request_obj):
        data = {'student': get_cnaStudent_obj}
        student_obj = data.get('student')
        student_obj.rotation = get_cnaRotation_obj
        student_obj.rotation.school_name = get_reg_cna_request_obj.user.school_name

        assert GMSValidator.ensure_same_school_name(data, get_reg_cna_request_obj, 'Record', partial=False) == data

    def test_ensure_same_school_name_record_success_superuser(self, get_cnaStudent_obj, get_cnaRotation_obj, get_superuser_request_obj):
        data = {'student': get_cnaStudent_obj}
        student_obj = data.get('student')
        student_obj.rotation = get_cnaRotation_obj
        student_obj.rotation.school_name =  '__DIFF_SCHOOL_NAME__'

        assert GMSValidator.ensure_same_school_name(data, get_superuser_request_obj, 'Record', partial=False) == data


    def test_ensure_same_school_name_record_success_partial(self, get_cnaStudent_obj, get_cnaRotation_obj, get_reg_cna_request_obj):
        data = {'student': None}

        assert GMSValidator.ensure_same_school_name(data, get_reg_cna_request_obj, 'Record', partial=True) == data

        data = {'student': get_cnaStudent_obj}
        student_obj = data.get('student')

        #NOTE this test was taken out because of the data structure, related objects must not be NULL or None, or else DB will complain
        # student_obj.rotation = None
        # assert GMSValidator.ensure_same_school_name(data, get_reg_cna_request_obj, 'Record', partial=True) == data

        
        student_obj.rotation = get_cnaRotation_obj
        student_obj.rotation.school_name =  None

        assert GMSValidator.ensure_same_school_name(data, get_reg_cna_request_obj, 'Record', partial=True) == data


    def test_ensure_same_school_name_record_failure(self, get_cnaStudent_obj, get_cnaRotation_obj, get_reg_cna_request_obj):
        data = {'student': get_cnaStudent_obj}
        student_obj = data.get('student')
        student_obj.rotation = get_cnaRotation_obj
        student_obj.rotation.school_name = '_DIFF_SCHOOL_NAME__'

        with pytest.raises(ValidationError):
            GMSValidator.ensure_same_school_name(data, get_reg_cna_request_obj, 'Record', partial=False)


    def test_ensure_no_dup_rot_success_rot_exists(self, get_cnaRotation_obj, monkeypatch):
        def does_exist(school_name__exact, rotation_num__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return True
        
        monkeypatch.setattr(CNARotation.objects, 'filter', does_exist)

        data = {'rotation_num': get_cnaRotation_obj.rotation_num}
        instance = get_cnaRotation_obj

        assert GMSValidator.ensure_no_dup_rot(data, 'CNARotation', instance, partial=False) == data
        

    def test_ensure_no_dup_rot_success_rot_not_exists(self, get_cnaRotation_obj, monkeypatch):
        def does_not_exist(school_name__exact, rotation_num__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return False
        
        monkeypatch.setattr(CNARotation.objects, 'filter', does_not_exist)

        data = {}
        instance = get_cnaRotation_obj

        assert GMSValidator.ensure_no_dup_rot(data, 'CNARotation', instance, partial=False) == data
        assert GMSValidator.ensure_no_dup_rot(data, 'CNARotation', None, partial=False) == data
        

    def test_ensure_no_rot_success_partial(self):
        data = {}
        assert GMSValidator.ensure_no_dup_rot(data, 'CNARotation', None, partial=True) == data


    def test_ensure_no_dup_rot_failure(self, get_cnaRotation_obj, monkeypatch):
        def does_exist(school_name__exact, rotation_num__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return True
        
        monkeypatch.setattr(CNARotation.objects, 'filter', does_exist)

        data = {'rotation_num': get_cnaRotation_obj.rotation_num}

        # WHAT MAKES IT FAIL? If we are not updating, aka posting, or creating, and there is a rotation with that rot number already
        with pytest.raises(ValidationError):
            GMSValidator.ensure_no_dup_rot(data, 'CNARotation', None, partial=False)

        # ALSO: if we are updating, and the rotation number is changed, which should never happen, but lets include it
        data = {'rotation_num': '__INVALID_ROT_NUM__'}

        with pytest.raises(ValidationError):
            GMSValidator.ensure_no_dup_rot(data, 'CNARotation', get_cnaRotation_obj, partial=False)



    def test_final_rot_validation(self, get_cnaRotation_serializer, mocker):
        mocked_date_checker = mocker.patch('gms.validators.GMSValidator.date_checker')
        mocked_ensure_same_school_name = mocker.patch('gms.validators.GMSValidator.ensure_same_school_name')
        mocked_ensure_no_dup_rot = mocker.patch('gms.validators.GMSValidator.ensure_no_dup_rot')

        get_cnaRotation_serializer.partial = True
        GMSValidator.final_rot_validation(get_cnaRotation_serializer, get_cnaRotation_serializer.data)

        mocked_date_checker.assert_called_once()
        mocked_ensure_same_school_name.assert_called_once()
        mocked_ensure_no_dup_rot.assert_called_once()


    def test_final_student_validation(self, get_cnaStudent_serializer, mocker):
        mocked_ensure_same_school_name = mocker.patch('gms.validators.GMSValidator.ensure_same_school_name')
        mocked_no_duplicate_students = mocker.patch('gms.validators.GMSValidator.no_duplicate_students')

        get_cnaStudent_serializer.partial = True
        GMSValidator.final_student_validation(get_cnaStudent_serializer, get_cnaStudent_serializer.data)

        mocked_ensure_same_school_name.assert_called_once()
        mocked_no_duplicate_students.assert_called_once()

    def test_final_record_validation(self, get_cnaTheoryRecord_serializer, mocker):
        mocked_ensure_same_school_name = mocker.patch('gms.validators.GMSValidator.ensure_same_school_name')
        mocked_no_duplicate_records = mocker.patch('gms.validators.GMSValidator.no_duplicate_records')

        get_cnaTheoryRecord_serializer.partial = True
        GMSValidator.final_record_validation(get_cnaTheoryRecord_serializer, get_cnaTheoryRecord_serializer.data)
        
        mocked_ensure_same_school_name.assert_called_once()
        mocked_no_duplicate_records.assert_called_once()