Feature: Student Management partially EDIT access

    Superuser can partially edit every resource for all schools
    Admin user can partially edit program, rotation, student resource for own school
    Staff user can partially edit rotation, student resource for own school
    Regular user can partially edit student resource for own school
    
    Scenario: superuser requesting to partially edit a student resource
        Given logged on as superuser
        When request PATCH to /api/sms/students/student_uuid
        Then database will partially edit the student record

    Scenario: superuser requesting to partially edit sms/schools resource
        Given logged on as superuser
        When request PATCH to /api/sms/schools/school_uuid
        Then database will partially edit the school record

    Scenario: superuser requesting to partially edit sms/programs resource
        Given logged on as superuser
        When request PATCH to /api/sms/programs/program_uuid
        Then database will partially edit the program record

    Scenario: superuser requesting to partially edit sms/rotations resource
        Given logged on as superuser
        When request PATCH to /api/sms/rotations/rotation_uuid
        Then database will partially edit the rotation record

    Scenario: admin office user requesting to partially edit a student resource
        Given logged on as admin office user
        When request PATCH to /api/sms/students/student_uuid
        Then database will partially edit the student record

    Scenario: admin office user requesting to partially edit sms/schools resource
        Given logged on as admin office User
        When request PATCH to /api/sms/schools/school_uuid
        Then database will not edit the school record

    Scenario: admin office user requesting to partially edit sms/programs resource
        Given logged on as admin office User
        When request PATCH to /api/sms/programs/program_uuid
        Then database will partially edit the program record

    Scenario: admin office user requesting to partially edit sms/rotations resource
        Given logged on as admin office User
        When request PATCH to /api/sms/rotations/rotation_uuid
        Then database will partially edit the rotation record

    Scenario: staff office user requesting to partially edit a student resource
        Given logged on as staff office user
        When request PATCH to /api/sms/students/student_uuid
        Then database will partially edit the student record

    Scenario: staff office user requesting to partially edit sms/schools resource
        Given logged on as staff office User
        When request PATCH to /api/sms/schools/school_uuid
        Then database will not edit the school record

    Scenario: staff office user requesting to partially edit sms/programs resource
        Given logged on as staff office User
        When request PATCH to /api/sms/programs/program_uuid
        Then database will not edit the program record

    Scenario: staff office user requesting to partially edit sms/rotations resource
        Given logged on as staff office User
        When request PATCH to /api/sms/rotations/rotation_uuid
        Then database will partially edit the rotation record

    Scenario: regular office user requesting to partially edit a student resource
        Given logged on as regular office user
        When request PATCH to /api/sms/students/student_uuid
        Then database will partially edit the student record

    Scenario: regular office user requesting to partially edit sms/schools resource
        Given logged on as regular office User
        When request PATCH to /api/sms/schools/school_uuid
        Then database will not edit the school record

    Scenario: regular office user requesting to partially edit sms/programs resource
        Given logged on as regular office User
        When request PATCH to /api/sms/programs/program_uuid
        Then database will not edit the program record


    Scenario: regular office user requesting to partially edit sms/rotations resource
        Given logged on as regular office User
        When request PATCH to /api/sms/rotations/rotation_uuid
        Then database will not edit the rotation record


