Feature: Student Management System as Superuser
    when super user logs onto sms system
    will have GET/POST/PUT/PATCH/DELETE access to all sms endpoints
    can filter student query by student parameters
    and since super user is not assigned with a particular school location
    he/she can manage all school's resource

    Scenario: superuser requesting to read schools resource
        Given logged on as superuser
        When request GET to /api/sms/schools
        Then will receive JSON response of data

    Scenario: superuser requesting to read programs resource
        Given logged on as superuser
        When request GET to /api/sms/programs
        Then will receive JSON response of data
        And server response status is OK 200



    Scenario: superuser requesting to read rotations resource
        Given logged on as superuser
        When request GET to /api/sms/rotations
        Then will receive JSON response of data



    Scenario: superuser requesting to read students resource
        Given logged on as superuser
        When request GET to /api/sms/students
        Then will receive JSON response of data



    Scenario: superuser requesting to create a student resource of the same school program rotation
        Given logged on as superuser
        When request POST to /api/sms/students of the same school
        Then database will create a student record

    Scenario: superuser requesting to create a student resource of a program rotation from different school
        Given logged on as superuser
        When request POST to /api/sms/students to a program rotation of another school
        Then database will create the student record

    Scenario: superuser requesting to fully edit a student resource
        Given logged on as superuser
        When request PUT to /api/sms/students/student_uuid
        Then database will edit the student record

    Scenario: superuser requesting to partially edit a student resource
        Given logged on as superuser
        When request PATCH to /api/sms/students/student_uuid
        Then database will edit the student record

    Scenario: superuser requesting to delete a student resource
        Given logged on as superuser
        When request DELETE to /api/sms/students/student_uuid
        Then database will delete the student record


    Scenario: superuser requesting to create sms/schools resource
        Given logged on as superuser
        When request POST to /api/sms/schools
        Then database will create the school record

    Scenario: superuser requesting to fully edit sms/schools resource
        Given logged on as superuser
        When request PUT to /api/sms/schools/school_uuid
        Then database will edit the school record

    Scenario: superuser requesting to partially edit sms/schools resource
        Given logged on as superuser
        When request PATCH to /api/sms/schools/school_uuid
        Then database will edit the school record

    Scenario: superuser requesting to delete sms/schools resource
        Given logged on as superuser
        When request DELETE to /api/sms/schools/school_uuid
        Then database will delete the school record

    Scenario: superuser requesting to create sms/programs resource
        Given logged on as superuser
        When request POST to /api/sms/programs
        Then database will create the program record

    Scenario: superuser requesting to fully edit sms/programs resource
        Given logged on as superuser
        When request PUT to /api/sms/programs/program_uuid
        Then database will edit the program record

    Scenario: superuser requesting to partially edit sms/programs resource
        Given logged on as superuser
        When request PATCH to /api/sms/programs/program_uuid
        Then database will edit the program record

    Scenario: superuser requesting to delete sms/programs resource
        Given logged on as superuser
        When request DELETE to /api/sms/programs/program_uuid
        Then database will delete the program record

    Scenario: superuser requesting to create sms/rotations resource
        Given logged on as superuser
        When request POST to /api/sms/rotations
        Then database will create the rotation record

    Scenario: superuser requesting to fully edit sms/rotations resource
        Given logged on as superuser
        When request PUT to /api/sms/rotations/rotation_uuid
        Then database will edit the rotation record

    Scenario: superuser requesting to partially edit sms/rotations resource
        Given logged on as superuser
        When request PATCH to /api/sms/rotations/rotation_uuid
        Then database will edit the rotation record

    Scenario: superuser requesting to delete sms/rotations resource
        Given logged on as superuser
        When request DELETE to /api/sms/rotations/rotation_uuid
        Then database will delete the rotation record


    Scenario: superuser requesting to filter sms/students resource by school
        Given logged on as superuser
        When request GET to /api/sms/students with filters by school name
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by program
        Given logged on as superuser
        When request GET to /api/sms/students with filters by program name
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by rotation
        Given logged on as superuser
        When request GET to /api/sms/students with filters by rotation number
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student first name
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student first name
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student last name
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student last name
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student email
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student email
        Then the specific students data will be returned as JSON response

    Scenario: superuser requesting to filter sms/students resource by student phone
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student phone number
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student ID
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student ID
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student program start date
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student program start date
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student program end date
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student program end date
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student payment completions
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student payment completions
        Then the specific students data will be returned as JSON response



    Scenario: superuser requesting to filter sms/students resource by student program completions
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student program completions
        Then the specific students data will be returned as JSON response



    Scenario: superuser requesting to filter sms/students resource by student employment status
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student employment status
        Then the specific students data will be returned as JSON response


