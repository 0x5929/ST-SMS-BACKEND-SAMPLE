    Scenario: superuser requesting to create a student resource of the same school program rotation
        Given logged on as superuser
        When request POST to /api/sms/students of the same school
        Then database will create a student record

    Scenario: superuser requesting to create a student resource of a program rotation from different school
        Given logged on as superuser
        When request POST to /api/sms/students to a program rotation of another school
        Then database will create the student record
        
    Scenario: admin office user requesting to create a student resource of the same school program rotation
        Given logged on as admin office user
        When request POST to /api/sms/students of the same school
        Then database will create a student record

    Scenario: admin office user requesting to create a student resource of a program rotation from different school
        Given logged on as admin office user
        When request POST to /api/sms/students to a program rotation of another school
        Then database will not create the student record
