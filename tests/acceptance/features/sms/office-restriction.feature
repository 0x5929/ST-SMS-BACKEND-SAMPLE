Feature: Student Management office users only

    admin, staff, regular users must be labeled as an office worker to access sms resources
    superuser not tested in this feature, can access all, but is tested in respective get/post/put/patch/del features

    Scenario: admin user requesting to read /api/sms/schools
        Given logged on as admin user with is_office set to false
        When request GET to /api/sms/schools
        Then will be permission denied

    Scenario: admin user requesting to read /api/sms/programs
        Given logged on as admin user with is_office set to false
        When request GET to /api/sms/programs
        Then will be permission denied

    Scenario: admin user requesting to read /api/sms/rotations
        Given logged on as admin user with is_office set to false
        When request GET to /api/sms/rotations
        Then will be permission denied

    Scenario: admin user requesting to create /api/sms/schools
        Given logged on as admin user with is_office set to false
        When request POST to /api/sms/schools
        Then will be permission denied

    Scenario: admin user requesting to create /api/sms/programs
        Given logged on as admin user with is_office set to false
        When request POST to /api/sms/programs
        Then will be permission denied

    Scenario: admin user requesting to create /api/sms/rotations
        Given logged on as admin user with is_office set to false
        When request POST to /api/sms/rotations
        Then will be permission denied


    Scenario: admin user requesting to create /api/sms/students of the same school
        Given logged on as admin user with is_office set to false
        When request POST to /api/sms/students of the same school
        Then will be permission denied


    Scenario: admin user requesting to create /api/sms/students to a program rotation of another school
        Given logged on as admin user with is_office set to false
        When request POST to /api/sms/students to a program rotation of another school
        Then will be permission denied


    Scenario: admin user requesting to fully update /api/sms/schools
        Given logged on as admin user with is_office set to false
        When request PUT to /api/sms/schools/school_uuid
        Then will be permission denied

    Scenario: admin user requesting to fully update  /api/sms/programs
        Given logged on as admin user with is_office set to false
        When request PUT to /api/sms/programs/program_uuid
        Then will be permission denied

    Scenario: admin user requesting to fully update  /api/sms/rotations
        Given logged on as admin user with is_office set to false
        When request PUT to /api/sms/rotations/rotation_uuid
        Then will be permission denied


    Scenario: admin user requesting to fully update  /api/sms/students
        Given logged on as admin user with is_office set to false
        When request PUT to /api/sms/students/student_uuid
        Then will be permission denied


    Scenario: admin user requesting to partially update /api/sms/schools
        Given logged on as admin user with is_office set to false
        When request PATCH to /api/sms/schools/school_uuid
        Then will be permission denied

    Scenario: admin user requesting to partially update  /api/sms/programs
        Given logged on as admin user with is_office set to false
        When request PATCH to /api/sms/programs/program_uuid
        Then will be permission denied

    Scenario: admin user requesting to partially update  /api/sms/rotations
        Given logged on as admin user with is_office set to false
        When request PATCH to /api/sms/rotations/rotation_uuid
        Then will be permission denied


    Scenario: admin user requesting to partially update  /api/sms/students
        Given logged on as admin user with is_office set to false
        When request PATCH to /api/sms/students/student_uuid
        Then will be permission denied


    Scenario: admin user requesting to delete /api/sms/schools
        Given logged on as admin user with is_office set to false
        When request DELETE to /api/sms/schools/school_uuid
        Then will be permission denied

    Scenario: admin user requesting to delete /api/sms/programs
        Given logged on as admin user with is_office set to false
        When request DELETE to /api/sms/programs/program_uuid
        Then will be permission denied

    Scenario: admin user requesting to delete /api/sms/rotations
        Given logged on as admin user with is_office set to false
        When request DELETE to /api/sms/rotations/rotation_uuid
        Then will be permission denied

    Scenario: admin user requesting to delete /api/sms/students
        Given logged on as admin user with is_office set to false
        When request DELETE to /api/sms/students/student_uuid
        Then will be permission denied

    Scenario: staff user requesting to read /api/sms/schools
        Given logged on as staff user with is_office set to false
        When request GET to /api/sms/schools
        Then will be permission denied

    Scenario: staff user requesting to read /api/sms/programs
        Given logged on as staff user with is_office set to false
        When request GET to /api/sms/programs
        Then will be permission denied

    Scenario: staff user requesting to read /api/sms/rotations
        Given logged on as staff user with is_office set to false
        When request GET to /api/sms/rotations
        Then will be permission denied


    Scenario: staff user requesting to read /api/sms/students
        Given logged on as staff user with is_office set to false
        When request GET to /api/sms/students
        Then will be permission denied


    Scenario: staff user requesting to create /api/sms/schools
        Given logged on as staff user with is_office set to false
        When request POST to /api/sms/schools
        Then will be permission denied

    Scenario: staff user requesting to create /api/sms/programs
        Given logged on as staff user with is_office set to false
        When request POST to /api/sms/programs
        Then will be permission denied

    Scenario: staff user requesting to create /api/sms/rotations
        Given logged on as staff user with is_office set to false
        When request POST to /api/sms/rotations
        Then will be permission denied


    Scenario: staff user requesting to create /api/sms/students of same school
        Given logged on as staff user with is_office set to false
        When request POST to /api/sms/students of the same school
        Then will be permission denied

    Scenario: staff user requesting to create /api/sms/students to a program rotation of another school
        Given logged on as staff user with is_office set to false
        When request POST to /api/sms/students to a program rotation of another school
        Then will be permission denied

    Scenario: staff user requesting to fully update /api/sms/schools
        Given logged on as staff user with is_office set to false
        When request PUT to /api/sms/schools/school_uuid
        Then will be permission denied

    Scenario: staff user requesting to fully update  /api/sms/programs
        Given logged on as staff user with is_office set to false
        When request PUT to /api/sms/programs/program_uuid
        Then will be permission denied

    Scenario: staff user requesting to fully update  /api/sms/rotations
        Given logged on as staff user with is_office set to false
        When request PUT to /api/sms/rotations/rotation_uuid
        Then will be permission denied


    Scenario: staff user requesting to fully update  /api/sms/students
        Given logged on as staff user with is_office set to false
        When request PUT to /api/sms/students/student_uuid
        Then will be permission denied


    Scenario: staff user requesting to partially update /api/sms/schools
        Given logged on as staff user with is_office set to false
        When request PATCH to /api/sms/schools/school_uuid
        Then will be permission denied

    Scenario: staff user requesting to partially update  /api/sms/programs
        Given logged on as staff user with is_office set to false
        When request PATCH to /api/sms/programs/program_uuid
        Then will be permission denied

    Scenario: staff user requesting to partially update  /api/sms/rotations
        Given logged on as staff user with is_office set to false
        When request PATCH to /api/sms/rotations/rotation_uuid
        Then will be permission denied


    Scenario: staff user requesting to partially update  /api/sms/students
        Given logged on as staff user with is_office set to false
        When request PATCH to /api/sms/students/student_uuid
        Then will be permission denied


    Scenario: staff user requesting to delete /api/sms/schools
        Given logged on as staff user with is_office set to false
        When request DELETE to /api/sms/schools/school_uuid
        Then will be permission denied

    Scenario: staff user requesting to delete /api/sms/programs
        Given logged on as staff user with is_office set to false
        When request DELETE to /api/sms/programs/program_uuid
        Then will be permission denied

    Scenario: staff user requesting to delete /api/sms/rotations
        Given logged on as staff user with is_office set to false
        When request DELETE to /api/sms/rotations/rotation_uuid
        Then will be permission denied

    Scenario: staff user requesting to delete /api/sms/students
        Given logged on as staff user with is_office set to false
        When request DELETE to /api/sms/students/student_uuid
        Then will be permission denied

    Scenario: regular user requesting to read /api/sms/schools
        Given logged on as regular user with is_office set to false
        When request GET to /api/sms/schools
        Then will be permission denied


    Scenario: regular user requesting to read /api/sms/programs
        Given logged on as regular user with is_office set to false
        When request GET to /api/sms/programs
        Then will be permission denied


    Scenario: regular user requesting to read /api/sms/rotations
        Given logged on as regular user with is_office set to false
        When request GET to /api/sms/rotations
        Then will be permission denied



    Scenario: regular user requesting to read /api/sms/students
        Given logged on as regular user with is_office set to false
        When request GET to /api/sms/students
        Then will be permission denied


    Scenario: regular user requesting to create /api/sms/schools
        Given logged on as regular user with is_office set to false
        When request POST to /api/sms/schools
        Then will be permission denied


    Scenario: regular user requesting to create /api/sms/programs
        Given logged on as regular user with is_office set to false
        When request POST to /api/sms/programs
        Then will be permission denied


    Scenario: regular user requesting to create /api/sms/rotations
        Given logged on as regular user with is_office set to false
        When request POST to /api/sms/rotations
        Then will be permission denied



    Scenario: regular user requesting to create /api/sms/students of same school
        Given logged on as regular user with is_office set to false
        When request POST to /api/sms/students of the same school
        Then will be permission denied


    Scenario: regular user requesting to create /api/sms/students to a program rotation of another school
        Given logged on as regular user with is_office set to false
        When request POST to /api/sms/students to a program rotation of another school
        Then will be permission denied


    Scenario: regular user requesting to fully update /api/sms/schools
        Given logged on as regular user with is_office set to false
        When request PUT to /api/sms/schools/school_uuid
        Then will be permission denied

    Scenario: regular user requesting to fully update  /api/sms/programs
        Given logged on as regular user with is_office set to false
        When request PUT to /api/sms/programs/program_uuid
        Then will be permission denied


    Scenario: regular user requesting to fully update  /api/sms/rotations
        Given logged on as regular user with is_office set to false
        When request PUT to /api/sms/rotations/rotation_uuid
        Then will be permission denied



    Scenario: regular user requesting to fully update  /api/sms/students
        Given logged on as regular user with is_office set to false
        When request PUT to /api/sms/students/student_uuid
        Then will be permission denied



    Scenario: regular user requesting to partially update /api/sms/schools
        Given logged on as regular user with is_office set to false
        When request PATCH to /api/sms/schools/school_uuid
        Then will be permission denied


    Scenario: regular user requesting to partially update  /api/sms/programs
        Given logged on as regular user with is_office set to false
        When request PATCH to /api/sms/programs/program_uuid
        Then will be permission denied


    Scenario: regular user requesting to partially update  /api/sms/rotations
        Given logged on as regular user with is_office set to false
        When request PATCH to /api/sms/rotations/rotation_uuid
        Then will be permission denied



    Scenario: regular user requesting to partially update  /api/sms/students
        Given logged on as regular user with is_office set to false
        When request PATCH to /api/sms/students/student_uuid
        Then will be permission denied



    Scenario: regular user requesting to delete /api/sms/schools
        Given logged on as regular user with is_office set to false
        When request DELETE to /api/sms/schools/school_uuid
        Then will be permission denied


    Scenario: regular user requesting to delete /api/sms/programs
        Given logged on as regular user with is_office set to false
        When request DELETE to /api/sms/programs/program_uuid
        Then will be permission denied


    Scenario: regular user requesting to delete /api/sms/rotations
        Given logged on as regular user with is_office set to false
        When request DELETE to /api/sms/rotations/rotation_uuid
        Then will be permission denied

    Scenario: regular user requesting to delete /api/sms/students
        Given logged on as regular user with is_office set to false
        When request DELETE to /api/sms/students/student_uuid
        Then will be permission denied


