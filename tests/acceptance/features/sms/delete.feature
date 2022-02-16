Feature: Student Management DELETE access

    Superuser can delete every resource for all schools
    Admin user can deletet program, rotation, student resource for own school
    Staff user can delete rotation, student resource for own school
    Regular user cannot delete student resource for own school

    Scenario: requesting to auth login
        Given no initial logon
        When request GET to /auth/login/
        Then server will respond with 405

    Scenario: superuser requesting to delete a student resource
        Given logged on as superuser
        When request DELETE to /api/sms/students/student_uuid
        Then database will delete the student record

    Scenario: superuser requesting to delete sms/schools resource
        Given logged on as superuser
        When request DELETE to /api/sms/schools/school_uuid
        Then database will delete the school record


    Scenario: superuser requesting to delete sms/programs resource
        Given logged on as superuser
        When request DELETE to /api/sms/programs/program_uuid
        Then database will delete the program record

    Scenario: superuser requesting to delete sms/rotations resource
        Given logged on as superuser
        When request DELETE to /api/sms/rotations/rotation_uuid
        Then database will delete the rotation record


    Scenario: admin office user requesting to delete a student resource
        Given logged on as admin office user
        When request DELETE to /api/sms/students/student_uuid
        Then database will delete the student record

    Scenario: admin office user requesting to delete sms/schools resource
        Given logged on as admin office User
        When request DELETE to /api/sms/schools/school_uuid
        Then will be permission denied

    Scenario: admin office user requesting to delete sms/programs resource
        Given logged on as admin office User
        When request DELETE to /api/sms/programs/program_uuid
        Then database will delete the program record

    Scenario: admin office user requesting to delete sms/rotations resource
        Given logged on as admin office User
        When request DELETE to /api/sms/rotations/rotation_uuid
        Then database will delete the rotation record

    Scenario: staff office user requesting to delete a student resource
        Given logged on as staff office user
        When request DELETE to /api/sms/students/student_uuid
        Then database will delete the student record


    Scenario: staff office user requesting to delete sms/schools resource
        Given logged on as staff office User
        When request DELETE to /api/sms/schools/school_uuid
        Then will be permission denied

    Scenario: staff office user requesting to delete sms/programs resource
        Given logged on as staff office User
        When request DELETE to /api/sms/programs/program_uuid
        Then will be permission denied

    Scenario: staff office user requesting to delete sms/rotations resource
        Given logged on as staff office User
        When request DELETE to /api/sms/rotations/rotation_uuid
        Then database will delete the rotation record


    Scenario: regular office user requesting to delete a student resource
        Given logged on as regular office user
        When request DELETE to /api/sms/students/student_uuid
        Then will be permission denied


    Scenario: regular office user requesting to delete sms/schools resource
        Given logged on as regular office User
        When request DELETE to /api/sms/schools/school_uuid
        Then will be permission denied


    Scenario: regular office user requesting to delete sms/programs resource
        Given logged on as regular office User
        When request DELETE to /api/sms/programs/program_uuid
        Then will be permission denied


    Scenario: regular office user requesting to delete sms/rotations resource
        Given logged on as regular office User
        When request DELETE to /api/sms/rotations/rotation_uuid
        Then will be permission denied




    @current
    Scenario: superuser requesting to delete ST2 sms/students resource
        Given logged on as superuser
        When request DELETE to ST2 /api/sms/students/student_uuid
        Then database will delete the ST2 student record


    @current
    Scenario: superuser requesting to delete ST2 sms/schools resource
        Given logged on as superuser
        When request DELETE to ST2 /api/sms/schools/school_uuid
        Then database will delete the ST2 school record

    @current
    Scenario: superuser requesting to delete ST2 sms/programs resource
        Given logged on as superuser
        When request DELETE to ST2 /api/sms/programs/program_uuid
        Then database will delete the ST2 program record

    @current
    Scenario: superuser requesting to delete ST2 sms/rotations resource
        Given logged on as superuser
        When request DELETE to ST2 /api/sms/rotations/rotation_uuid
        Then database will delete the ST2 rotation record

    @current
    Scenario: admin office user requesting to delete ST2 sms/students resource
        Given logged on as admin office user
        When request DELETE to ST2 /api/sms/students/student_uuid
        Then server will respond with 404

   
    @current
    Scenario: admin office user requesting to delete ST2 sms/schools resource
        Given logged on as admin office User
        When request DELETE to ST2 /api/sms/schools/school_uuid
        Then will be permission denied

    @current
    Scenario: admin office user requesting to delete ST2 sms/programs resource
        Given logged on as admin office User
        When request DELETE to ST2 /api/sms/programs/program_uuid
        Then server will respond with 404

    @current
    Scenario: admin office user requesting to delete sms/rotations resource
        Given logged on as admin office User
        When request DELETE to ST2 /api/sms/rotations/rotation_uuid
        Then server will respond with 404


    @current
    Scenario: staff office user requesting to delete ST2 sms/students resource
        Given logged on as staff office user
        When request DELETE to ST2 /api/sms/students/student_uuid
        Then server will respond with 404

    @current
    Scenario: staff office user requesting to delete ST2 sms/schools resource
        Given logged on as staff office User
        When request DELETE to ST2 /api/sms/schools/school_uuid
        Then will be permission denied

    @current
    Scenario: staff office user requesting to delete ST2 sms/programs resource
        Given logged on as staff office User
        When request DELETE to ST2 /api/sms/programs/program_uuid
        Then will be permission denied

    @current
    Scenario: staff office user requesting to delete ST2 sms/rotations resource
        Given logged on as staff office User
        When request DELETE to ST2 /api/sms/rotations/rotation_uuid
        Then server will respond with 404

    @current
    Scenario: regular office user requesting to delete ST2 sms/students resource
        Given logged on as regular office user
        When request DELETE to ST2 /api/sms/students/student_uuid
        Then will be permission denied

    @current
    Scenario: regular office user requesting to delete ST2 sms/schools resource
        Given logged on as regular office User
        When request DELETE to ST2 /api/sms/schools/school_uuid
        Then will be permission denied

    @current
    Scenario: regular office user requesting to delete ST2 sms/programs resource
        Given logged on as regular office User
        When request DELETE to ST2 /api/sms/programs/program_uuid
        Then will be permission denied


    @current
    Scenario: regular office user requesting to delete ST2 sms/rotations resource
        Given logged on as regular office User
        When request DELETE to ST2 /api/sms/rotations/rotation_uuid
        Then will be permission denied
