Feature: Student Management DELETE access

    Superuser can delete every resource for all schools
    Admin user can deletet program, rotation, student resource for own school
    Staff user can delete rotation, student resource for own school
    Regular user cannot delete student resource for own school
    
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
        Then database will not delete the school record

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
        Then database will not delete the school record

    Scenario: staff office user requesting to delete sms/programs resource
        Given logged on as staff office User
        When request DELETE to /api/sms/programs/program_uuid
        Then database will not delete the program record

    Scenario: staff office user requesting to delete sms/rotations resource
        Given logged on as staff office User
        When request DELETE to /api/sms/rotations/rotation_uuid
        Then database will delete the rotation record


    Scenario: regular office user requesting to delete a student resource
        Given logged on as regular office user
        When request DELETE to /api/sms/students/student_uuid
        Then database will not delete the student record


    Scenario: regular office user requesting to delete sms/schools resource
        Given logged on as regular office User
        When request DELETE to /api/sms/schools/school_uuid
        Then database will not delete the school record


    Scenario: regular office user requesting to delete sms/programs resource
        Given logged on as regular office User
        When request DELETE to /api/sms/programs/program_uuid
        Then database will not delete the program record


    Scenario: regular office user requesting to delete sms/rotations resource
        Given logged on as regular office User
        When request DELETE to /api/sms/rotations/rotation_uuid
        Then database will not delete the rotation record
