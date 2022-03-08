import pytest


from gms.permissions import (IsSuperuser, 
                            IsAuthenticatedCNAInstructor,
                            IsAuthenticatedHHAInstructor,
                            IsAuthenticatedAdminInstructor,
                            IsAuthenticatedCNAStaffInstructor,
                            IsAuthenticatedHHAStaffInstructor)


from .gms_constants import (AUTH_REG_HHA_INSTR_MSG,
                            AUTH_REG_CNA_INSTR_MSG,
                            AUTH_STAFF_HHA_INSTR_MSG,
                            AUTH_STAFF_CNA_INSTR_MSG,
                            AUTH_ADMIN_INSTR_MSG,
                            AUTH_SUPERUSER_MSG)



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

class View:
    def __init__(self):
        self.view = None



@pytest.mark.gms
@pytest.mark.current
class TestGMSPermissions:
    @pytest.fixture
    def get_request_obj(self):
        return Request()

    @pytest.fixture
    def get_request_super_obj(self):
        return Request(superuser=True)

    @pytest.fixture
    def get_request_admin_obj(self):
        return Request(admin=True)

    @pytest.fixture
    def get_request_staff_obj(self):
        return Request(staff=True)

    @pytest.fixture
    def get_view_obj(self):
        return View()

    def test_IsAuthenticatedCNAInstructor_message(self):
        assert IsAuthenticatedCNAInstructor.message == AUTH_REG_CNA_INSTR_MSG

    def test_IsAuthenticatedCNAInstructor_has_permission(self, get_request_obj, get_view_obj):
        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_instructor = True
        get_request_obj.user.programs = ['CNA']
        get_request_obj.method = 'GET'
        
        assert IsAuthenticatedCNAInstructor().has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_instructor = True
        get_request_obj.user.programs = ['CNA']
        get_request_obj.method = 'GET'
        
        assert IsAuthenticatedCNAInstructor().has_permission(get_request_obj, get_view_obj) == False
    
        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_instructor = False
        get_request_obj.user.programs = ['CNA']
        get_request_obj.method = 'GET'
        
        assert IsAuthenticatedCNAInstructor().has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_instructor = True
        get_request_obj.user.programs = ['HHA']
        get_request_obj.method = 'GET'
        
        assert IsAuthenticatedCNAInstructor().has_permission(get_request_obj, get_view_obj) == False


    def test_IsAuthenticatedHHAInstructor_message(self):
        assert IsAuthenticatedHHAInstructor.message == AUTH_REG_HHA_INSTR_MSG

    def test_IsAuthenticatedHHAInstructor_has_permission(self, get_request_obj, get_view_obj):
        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_instructor = True
        get_request_obj.user.programs = ['HHA']
        get_request_obj.method = 'GET'
        
        assert IsAuthenticatedHHAInstructor().has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_instructor = True
        get_request_obj.user.programs = ['HHA']
        get_request_obj.method = 'GET'
        
        assert IsAuthenticatedHHAInstructor().has_permission(get_request_obj, get_view_obj) == False
    
        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_instructor = False
        get_request_obj.user.programs = ['HHA']
        get_request_obj.method = 'GET'
        
        assert IsAuthenticatedHHAInstructor().has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_instructor = True
        get_request_obj.user.programs = ['CNA']
        get_request_obj.method = 'GET'
        
        assert IsAuthenticatedHHAInstructor().has_permission(get_request_obj, get_view_obj) == False


    def IsAuthenticatedCNAStaffInstructor_message(self):
        assert IsAuthenticatedCNAStaffInstructor.message == AUTH_STAFF_CNA_INSTR_MSG

    def test_IsAuthenticatedCNAStaffInstructor_has_permission(self, get_request_staff_obj, get_view_obj):
        get_request_staff_obj.user.is_authenticated = True
        get_request_staff_obj.user.is_instructor = True
        get_request_staff_obj.user.programs = ['CNA']
        get_request_staff_obj.method = 'GET'
        
        assert IsAuthenticatedCNAStaffInstructor().has_permission(get_request_staff_obj, get_view_obj) == True

        get_request_staff_obj.user.is_authenticated = False
        get_request_staff_obj.user.is_instructor = True
        get_request_staff_obj.user.programs = ['CNA']
        get_request_staff_obj.method = 'GET'
        
        assert IsAuthenticatedCNAStaffInstructor().has_permission(get_request_staff_obj, get_view_obj) == False
    
        get_request_staff_obj.user.is_authenticated = True
        get_request_staff_obj.user.is_instructor = False
        get_request_staff_obj.user.programs = ['CNA']
        get_request_staff_obj.method = 'GET'
        
        assert IsAuthenticatedCNAStaffInstructor().has_permission(get_request_staff_obj, get_view_obj) == False

        get_request_staff_obj.user.is_authenticated = True
        get_request_staff_obj.user.is_instructor = True
        get_request_staff_obj.user.programs = ['HHA']
        get_request_staff_obj.method = 'GET'
        
        assert IsAuthenticatedCNAStaffInstructor().has_permission(get_request_staff_obj, get_view_obj) == False


    def test_IsAuthenticatedHHAStaffInstructor_message(self):
        assert IsAuthenticatedHHAInstructor.message == AUTH_REG_HHA_INSTR_MSG

    def test_IsAuthenticatedHHAStaffInstructor_has_permission(self, get_request_staff_obj, get_view_obj):
        get_request_staff_obj.user.is_authenticated = True
        get_request_staff_obj.user.is_instructor = True
        get_request_staff_obj.user.programs = ['HHA']
        get_request_staff_obj.method = 'GET'
        
        assert IsAuthenticatedHHAStaffInstructor().has_permission(get_request_staff_obj, get_view_obj) == True

        get_request_staff_obj.user.is_authenticated = False
        get_request_staff_obj.user.is_instructor = True
        get_request_staff_obj.user.programs = ['HHA']
        get_request_staff_obj.method = 'GET'
        
        assert IsAuthenticatedHHAStaffInstructor().has_permission(get_request_staff_obj, get_view_obj) == False
    
        get_request_staff_obj.user.is_authenticated = True
        get_request_staff_obj.user.is_instructor = False
        get_request_staff_obj.user.programs = ['HHA']
        get_request_staff_obj.method = 'GET'
        
        assert IsAuthenticatedHHAStaffInstructor().has_permission(get_request_staff_obj, get_view_obj) == False

        get_request_staff_obj.user.is_authenticated = True
        get_request_staff_obj.user.is_instructor = True
        get_request_staff_obj.user.programs = ['CNA']
        get_request_staff_obj.method = 'GET'
        
        assert IsAuthenticatedHHAStaffInstructor().has_permission(get_request_staff_obj, get_view_obj) == False






    def IsAuthenticatedAdminInstructor_message(self):
        assert IsAuthenticatedAdminInstructor.message == AUTH_ADMIN_INSTR_MSG

    def test_IsAuthenticatedAdminInstructor_has_permission(self, get_request_admin_obj, get_view_obj):
        get_request_admin_obj.user.is_authenticated = True
        get_request_admin_obj.user.is_instructor = True
        get_request_admin_obj.user.programs = ['CNA']
        get_request_admin_obj.method = 'GET'
        
        assert IsAuthenticatedAdminInstructor().has_permission(get_request_admin_obj, get_view_obj) == True

        get_request_admin_obj.user.is_authenticated = False
        get_request_admin_obj.user.is_instructor = True
        get_request_admin_obj.user.programs = ['CNA']
        get_request_admin_obj.method = 'GET'
        
        assert IsAuthenticatedAdminInstructor().has_permission(get_request_admin_obj, get_view_obj) == False
    
        get_request_admin_obj.user.is_authenticated = True
        get_request_admin_obj.user.is_instructor = False
        get_request_admin_obj.user.programs = ['CNA']
        get_request_admin_obj.method = 'GET'
        
        assert IsAuthenticatedAdminInstructor().has_permission(get_request_admin_obj, get_view_obj) == False

        get_request_admin_obj.user.is_authenticated = True
        get_request_admin_obj.user.is_instructor = True
        get_request_admin_obj.user.programs = ['HHA']
        get_request_admin_obj.method = 'GET'
        
        assert IsAuthenticatedAdminInstructor().has_permission(get_request_admin_obj, get_view_obj) == True


    def test_IsSuperuser_message(self):
        assert IsSuperuser.message == AUTH_SUPERUSER_MSG

    def test_IsSuperuser_has_permission(self,get_request_super_obj, get_view_obj):
        get_request_super_obj.user.is_authenticated = True

        assert IsSuperuser(
        ).has_permission(get_request_super_obj, get_view_obj) == True

        get_request_super_obj.user.is_authenticated = False
        get_request_super_obj.user.is_superuser = True

        assert IsSuperuser(
        ).has_permission(get_request_super_obj, get_view_obj) == False

        get_request_super_obj.user.is_authenticated = True
        get_request_super_obj.user.is_superuser = False

        assert IsSuperuser(
        ).has_permission(get_request_super_obj, get_view_obj) == False