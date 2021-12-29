Feature: Student Management CREATE access

    Superuser can create every resource for all schools
    Admin user can create program, rotation, student resource for own school
    Staff user can create rotation, student resource for own school
    Regular user can create student resource for own school

    Scenario: requesting to auth login
        Given no initial logon
        When request GET to /auth/login/
        Then server will respond with 405
        
    Scenario: superuser requesting to create a student resource of the same school program rotation
        Given logged on as superuser
        When request POST to /api/sms/students of the same school
        Then database will create the student record

    Scenario: superuser requesting to create a student resource of a program rotation from different school
        Given logged on as superuser
        When request POST to /api/sms/students to a program rotation of another school
        Then database will create the student record of another school


    Scenario: superuser requesting to create sms/schools resource
        Given logged on as superuser
        When request POST to /api/sms/schools
        Then database will create the school record

    Scenario: superuser requesting to create sms/programs resource
        Given logged on as superuser
        When request POST to /api/sms/programs
        Then database will create the program record

    Scenario: superuser requesting to create sms/rotations resource
        Given logged on as superuser
        When request POST to /api/sms/rotations
        Then database will create the rotation record

    Scenario: admin office user requesting to create a student resource of the same school program rotation
        Given logged on as admin office user
        When request POST to /api/sms/students of the same school
        Then database will create the student record

    Scenario: admin office user requesting to create a student resource of a program rotation from different school
        Given logged on as admin office user
        When request POST to /api/sms/students to a program rotation of another school
        Then database will not create the student record

    Scenario: admin office user requesting to create sms/schools resource
        Given logged on as admin office User
        When request POST to /api/sms/schools
        Then database will not create the school record

    Scenario: admin office user requesting to create sms/programs resource
        Given logged on as admin office User
        When request POST to /api/sms/programs
        Then database will create the program record

    Scenario: admin office user requesting to create sms/rotations resource
        Given logged on as admin office User
        When request POST to /api/sms/rotations
        Then database will create the rotation record

    Scenario: staff office user requesting to create a student resource of the same school program rotation
        Given logged on as staff office user
        When request POST to /api/sms/students of the same school
        Then database will create the student record

    Scenario: staff office user requesting to create a student resource of a program rotation from different school
        Given logged on as staff office user
        When request POST to /api/sms/students to a program rotation of another school
        Then database will not create the student record

    Scenario: staff office user requesting to create sms/schools resource
        Given logged on as staff office User
        When request POST to /api/sms/schools
        Then database will not create the school record

    Scenario: staff office user requesting to create sms/programs resource
        Given logged on as staff office User
        When request POST to /api/sms/programs
        Then database will not create the program record

    Scenario: staff office user requesting to create sms/rotations resource
        Given logged on as staff office User
        When request POST to /api/sms/rotations
        Then database will create the rotation record

    Scenario: regular office user requesting to create a student resource of the same school program rotation
        Given logged on as regular office user
        When request POST to /api/sms/students of the same school
        Then database will create the student record

    Scenario: regular office user requesting to create a student resource of a program rotation from different school
        Given logged on as regular office user
        When request POST to /api/sms/students to a program rotation of another school
        Then database will not create the student record

    Scenario: regular office user requesting to create sms/schools resource
        Given logged on as regular office User
        When request POST to /api/sms/schools
        Then database will not create the school record

    Scenario: regular office user requesting to create sms/programs resource
        Given logged on as regular office User
        When request POST to /api/sms/programs
        Then database will not create the program record

    Scenario: regular office user requesting to create sms/rotations resource
        Given logged on as regular office User
        When request POST to /api/sms/rotations
        Then database will not create the rotation record