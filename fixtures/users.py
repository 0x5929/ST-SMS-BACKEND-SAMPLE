from tests.factories.accounts import AccountFactory
from tests.factories.verifications import VerificationFactory


class UserTestHelper:

    TEST_SUPERUSER = 'testsuper'

    TEST_ADMIN_USER = 'testadmin'
    TEST_ADMIN_OFF_USER = 'testofficeadmin'
    TEST_ADMIN_REC_USER = 'testrecruitadmin'
    TEST_ADMIN_INST_USER = 'testinstructoradmin'

    TEST_STAFF_USER = 'teststaff'
    TEST_STAFF_OFF_USER = 'testofficestaff'
    TEST_STAFF_REC_USER = 'testrecruitstaff'
    TEST_STAFF_INST_USER = 'testinstructorstaff'

    TEST_REG_USER = 'testuser'
    TEST_REG_OFF_USER = 'testofficeuser'
    TEST_REG_REC_USER = 'testrecruituser'
    TEST_REG_INST_USER = 'testinstructoruser'

    @classmethod
    def create_user_fixtures(cls):
        #  superuser

        superuser = AccountFactory(
            username=cls.TEST_SUPERUSER,
            email=f'{cls.TEST_SUPERUSER}@locahost',
            first_name=cls.TEST_SUPERUSER,
            last_name=cls.TEST_SUPERUSER,
            is_office=True, is_recruit=True, is_instructor=True,
            is_staff=True, is_admin=True, is_superuser=True)

        VerificationFactory(
            pk=superuser.pk,
            email=superuser.email
        )

        # admin user
        admin_user = AccountFactory(
            username=cls.TEST_ADMIN_USER,
            email=f'{cls.TEST_ADMIN_USER}@locahost',
            first_name=cls.TEST_ADMIN_USER,
            last_name=cls.TEST_ADMIN_USER,
            is_office=False, is_recruit=False, is_instructor=False,
            is_staff=False, is_admin=True)

        VerificationFactory(
            pk=admin_user.pk,
            email=admin_user.email
        )

        # office admin user
        admin_office_user = AccountFactory(
            username=cls.TEST_ADMIN_OFF_USER,
            email=f'{cls.TEST_ADMIN_OFF_USER}@locahost',
            first_name=cls.TEST_ADMIN_OFF_USER,
            last_name=cls.TEST_ADMIN_OFF_USER,
            is_office=True, is_recruit=False, is_instructor=False,
            is_staff=False, is_admin=True)

        VerificationFactory(
            pk=admin_office_user.pk,
            email=admin_office_user.email
        )

        # recruit admin user
        admin_recruit_user = AccountFactory(
            username=cls.TEST_ADMIN_REC_USER,
            email=f'{cls.TEST_ADMIN_REC_USER}@locahost',
            first_name=cls.TEST_ADMIN_REC_USER,
            last_name=cls.TEST_ADMIN_REC_USER,
            is_office=False, is_recruit=True, is_instructor=False,
            is_staff=False, is_admin=True)

        VerificationFactory(
            pk=admin_recruit_user.pk,
            email=admin_recruit_user.email
        )

        # instructor admin user
        admin_instructor_user = AccountFactory(
            username=cls.TEST_ADMIN_INST_USER,
            email=f'{cls.TEST_ADMIN_INST_USER}@locahost',
            first_name=cls.TEST_ADMIN_INST_USER,
            last_name=cls.TEST_ADMIN_INST_USER,
            is_office=False, is_recruit=False, is_instructor=True,
            is_staff=False, is_admin=True)

        VerificationFactory(
            pk=admin_instructor_user.pk,
            email=admin_instructor_user.email
        )

    # staff user
        AccountFactory(
            username=cls.TEST_STAFF_USER,
            email=f'{cls.TEST_STAFF_USER}@locahost',
            first_name=cls.TEST_STAFF_USER,
            last_name=cls.TEST_STAFF_USER,
            is_office=False, is_recruit=False, is_instructor=False,
            is_staff=True, is_admin=False)

        # office staff user
        AccountFactory(
            username=cls.TEST_STAFF_OFF_USER,
            email=f'{cls.TEST_STAFF_OFF_USER}@locahost',
            first_name=cls.TEST_STAFF_OFF_USER,
            last_name=cls.TEST_STAFF_OFF_USER,
            is_office=True, is_recruit=False, is_instructor=False,
            is_staff=True, is_admin=False)

        # recruit staff user
        AccountFactory(
            username=cls.TEST_STAFF_REC_USER,
            email=f'{cls.TEST_STAFF_REC_USER}@locahost',
            first_name=cls.TEST_STAFF_REC_USER,
            last_name=cls.TEST_STAFF_REC_USER,
            is_office=False, is_recruit=True, is_instructor=False,
            is_staff=True, is_admin=False)

        # instructor staff user
        AccountFactory(
            username=cls.TEST_STAFF_INST_USER,
            email=f'{cls.TEST_STAFF_INST_USER}@locahost',
            first_name=cls.TEST_STAFF_INST_USER,
            last_name=cls.TEST_STAFF_INST_USER,
            is_office=False, is_recruit=False, is_instructor=True,
            is_staff=True, is_admin=False)

        # regular user
        AccountFactory(
            username=cls.TEST_REG_USER,
            email=f'{cls.TEST_REG_USER}@locahost',
            first_name=cls.TEST_REG_USER,
            last_name=cls.TEST_REG_USER,
            is_office=False, is_recruit=False, is_instructor=False,
            is_staff=False, is_admin=False)

        # office regular user
        AccountFactory(
            username=cls.TEST_REG_OFF_USER,
            email=f'{cls.TEST_REG_OFF_USER}@locahost',
            first_name=cls.TEST_REG_OFF_USER,
            last_name=cls.TEST_REG_OFF_USER,
            is_office=True, is_recruit=False, is_instructor=False,
            is_staff=False, is_admin=False)

        # recruit regular user
        AccountFactory(
            username=cls.TEST_REG_REC_USER,
            email=f'{cls.TEST_REG_REC_USER}@locahost',
            first_name=cls.TEST_REG_REC_USER,
            last_name=cls.TEST_REG_REC_USER,
            is_office=False, is_recruit=True, is_instructor=False,
            is_staff=False, is_admin=False)

        # instructor regular user
        AccountFactory(
            username=cls.TEST_REG_INST_USER,
            email=f'{cls.TEST_REG_INST_USER}@locahost',
            first_name=cls.TEST_REG_INST_USER,
            last_name=cls.TEST_REG_INST_USER,
            is_office=False, is_recruit=False, is_instructor=True,
            is_staff=False, is_admin=False)
