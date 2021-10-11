from rest_framework.test import APITestCase
from apps.sms.models import School, Program, Rotation, Student


class TestSMSModelStr(APITestCase):
    def test_school_model_str(self):
        pass

    def test_program_model_str(self):
        pass

    def test_rotation_model_str(self):
        pass

    def test_student_model_str(self):
        pass


class TestSMSModelAttrRequirement(APITestCase):
    def test_school_model_attr(self):
        pass

    def test_program_model_attr(self):
        pass

    def test_rotation_model_attr(self):
        pass

    def test_student_model_attr(self):
        pass


class TestSMSModelAttrExtraLogic(APITestCase):
    def test_rotation_size(self):
        pass

    def test_student_school_name(self):
        pass

    def test_student_pre_hook(self):
        pass

    def test_student_save_update_delete_settings_false(self):
        # test that right Google Module wont be called
        pass

    def test_student_save_update_delete_settings_true(self):
        # test that right Google Module will be called
        pass
