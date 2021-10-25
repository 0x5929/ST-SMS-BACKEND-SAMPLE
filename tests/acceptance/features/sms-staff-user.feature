Feature: Student Management System as Staff User
    when staff office user logs onto sms system
    will have read access to all sms endpoints
    will have POST/PUT/PATCH/DELETE access to sms students, rotations endpoints
    can filter student query by student parameters
    and everything is done only to user's own school

    Scenario: staff office user requesting to read schools resource
        Given logged on as staff office user
        When request GET to /api/sms/schools
        Then will receive JSON response of data



    Scenario: staff office user requesting to read programs resource
        Given logged on as staff office user
        When request GET to /api/sms/programs
        Then will receive JSON response of data
        And server response status is OK 200



    Scenario: staff office user requesting to read rotations resource
        Given logged on as staff office user
        When request GET to /api/sms/rotations
        Then will receive JSON response of data



    Scenario: staff office user requesting to read students resource
        Given logged on as staff office user
        When request GET to /api/sms/students
        Then will receive JSON response of data



    Scenario: staff office user requesting to create a student resource of the same school program rotation
        Given logged on as staff office user
        When request POST to /api/sms/students of the same school
        Then database will create a student record

    Scenario: staff office user requesting to create a student resource of a program rotation from different school
        Given logged on as staff office user
        When request POST to /api/sms/students to a program rotation of another school
        Then database will not create the student record

    Scenario: staff office user requesting to fully edit a student resource
        Given logged on as staff office user
        When request PUT to /api/sms/students/student_uuid
        Then database will edit the student record

    Scenario: staff office user requesting to partially edit a student resource
        Given logged on as staff office user
        When request PATCH to /api/sms/students/student_uuid
        Then database will partially edit the student record

    Scenario: staff office user requesting to delete a student resource
        Given logged on as staff office user
        When request DELETE to /api/sms/students/student_uuid
        Then database will delete the student record


    Scenario: staff office user requesting to create sms/schools resource
        Given logged on as staff office User
        When request POST to /api/sms/schools
        Then database will not create the school record

    Scenario: staff office user requesting to fully edit sms/schools resource
        Given logged on as staff office User
        When request PUT to /api/sms/schools/school_uuid
        Then database will not edit the school record

    Scenario: staff office user requesting to partially edit sms/schools resource
        Given logged on as staff office User
        When request PATCH to /api/sms/schools/school_uuid
        Then database will not edit the school record

    Scenario: staff office user requesting to delete sms/schools resource
        Given logged on as staff office User
        When request DELETE to /api/sms/schools/school_uuid
        Then database will not delete the school record

    Scenario: staff office user requesting to create sms/programs resource
        Given logged on as staff office User
        When request POST to /api/sms/programs
        Then database will not create the program record

    Scenario: staff office user requesting to fully edit sms/programs resource
        Given logged on as staff office User
        When request PUT to /api/sms/programs/program_uuid
        Then database will not edit the program record

    Scenario: staff office user requesting to partially edit sms/programs resource
        Given logged on as staff office User
        When request PATCH to /api/sms/programs/program_uuid
        Then database will not edit the program record

    Scenario: staff office user requesting to delete sms/programs resource
        Given logged on as staff office User
        When request DELETE to /api/sms/programs/program_uuid
        Then database will not delete the program record

    Scenario: staff office user requesting to create sms/rotations resource
        Given logged on as staff office User
        When request POST to /api/sms/rotations
        Then database will create the rotation record

    Scenario: staff office user requesting to fully edit sms/rotations resource
        Given logged on as staff office User
        When request PUT to /api/sms/rotations/rotation_uuid
        Then database will edit the rotation record

    Scenario: staff office user requesting to partially edit sms/rotations resource
        Given logged on as staff office User
        When request PATCH to /api/sms/rotations/rotation_uuid
        Then database will partially edit the rotation record

    Scenario: staff office user requesting to delete sms/rotations resource
        Given logged on as staff office User
        When request DELETE to /api/sms/rotations/rotation_uuid
        Then database will delete the rotation record

    Scenario: staff office user requesting to filter sms/students resource by school
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by school name
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by program
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by program name
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by rotation
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by rotation number
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student first name
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student first name
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student last name
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student last name
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student email
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student email
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student phone
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student phone number
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student ID
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student ID
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student program start date
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student program start date
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student program end date
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student program end date
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student payment completions
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student payment completions
        Then the specific students data will be returned as JSON response



    Scenario: staff office user requesting to filter sms/students resource by student program completions
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student program completions
        Then the specific students data will be returned as JSON response



    Scenario: staff office user requesting to filter sms/students resource by student employment status
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student employment status
        Then the specific students data will be returned as JSON response



    Scenario: staff user requesting to read /api/sms/schools
        Given logged on as staff user with is_office set to false
        When request GET to /api/sms/schools
        Then No data response will be sent from server

    Scenario: staff user requesting to read /api/sms/programs
        Given logged on as staff user with is_office set to false
        When request GET to /api/sms/programs
        Then No data response will be sent from server

    Scenario: staff user requesting to read /api/sms/rotations
        Given logged on as staff user with is_office set to false
        When request GET to /api/sms/rotations
        Then No data response will be sent from server


    Scenario: staff user requesting to read /api/sms/students
        Given logged on as staff user with is_office set to false
        When request GET to /api/sms/students
        Then No data response will be sent from server


    Scenario: staff user requesting to create /api/sms/schools
        Given logged on as staff user with is_office set to false
        When request POST to /api/sms/schools
        Then No data response will be sent from server

    Scenario: staff user requesting to create /api/sms/programs
        Given logged on as staff user with is_office set to false
        When request POST to /api/sms/programs
        Then No data response will be sent from server

    Scenario: staff user requesting to create /api/sms/rotations
        Given logged on as staff user with is_office set to false
        When request POST to /api/sms/rotations
        Then No data response will be sent from server


    Scenario: staff user requesting to create /api/sms/students of same school
        Given logged on as staff user with is_office set to false
        When request POST to /api/sms/students of the same school
        Then No data response will be sent from server

    Scenario: staff user requesting to create /api/sms/students to a program rotation of another school
        Given logged on as staff user with is_office set to false
        When request POST to /api/sms/students to a program rotation of another school
        Then No data response will be sent from server

    Scenario: staff user requesting to fully update /api/sms/schools
        Given logged on as staff user with is_office set to false
        When request PUT to /api/sms/schools/school_uuid
        Then No data response will be sent from server

    Scenario: staff user requesting to fully update  /api/sms/programs
        Given logged on as staff user with is_office set to false
        When request PUT to /api/sms/programs/program_uuid
        Then No data response will be sent from server

    Scenario: staff user requesting to fully update  /api/sms/rotations
        Given logged on as staff user with is_office set to false
        When request PUT to /api/sms/rotations/rotation_uuid
        Then No data response will be sent from server


    Scenario: staff user requesting to fully update  /api/sms/students
        Given logged on as staff user with is_office set to false
        When request PUT to /api/sms/students/student_uuid
        Then No data response will be sent from server


    Scenario: staff user requesting to partially update /api/sms/schools
        Given logged on as staff user with is_office set to false
        When request PATCH to /api/sms/schools/school_uuid
        Then No data response will be sent from server

    Scenario: staff user requesting to partially update  /api/sms/programs
        Given logged on as staff user with is_office set to false
        When request PATCH to /api/sms/programs/program_uuid
        Then No data response will be sent from server

    Scenario: staff user requesting to partially update  /api/sms/rotations
        Given logged on as staff user with is_office set to false
        When request PATCH to /api/sms/rotations/rotation_uuid
        Then No data response will be sent from server


    Scenario: staff user requesting to partially update  /api/sms/students
        Given logged on as staff user with is_office set to false
        When request PATCH to /api/sms/students/student_uuid
        Then No data response will be sent from server


    Scenario: staff user requesting to delete /api/sms/schools
        Given logged on as staff user with is_office set to false
        When request DELETE to /api/sms/schools/school_uuid
        Then No data response will be sent from server

    Scenario: staff user requesting to delete /api/sms/programs
        Given logged on as staff user with is_office set to false
        When request DELETE to /api/sms/programs/program_uuid
        Then No data response will be sent from server

    Scenario: staff user requesting to delete /api/sms/rotations
        Given logged on as staff user with is_office set to false
        When request DELETE to /api/sms/rotations/rotation_uuid
        Then No data response will be sent from server

    Scenario: staff user requesting to delete /api/sms/students
        Given logged on as staff user with is_office set to false
        When request DELETE to /api/sms/students/student_uuid
        Then No data response will be sent from server
