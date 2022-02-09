
Feature: Student Management READ access
    
    All office users have read access to all sms resources


    Scenario: superuser requesting to read sms/schools resource
        Given logged on as superuser
        When request GET to /api/sms/schools
        Then will receive JSON response of data

    Scenario: superuser requesting to read sms/programs resource
        Given logged on as superuser
        When request GET to /api/sms/programs
        Then will receive JSON response of data

    Scenario: superuser requesting to read sms/rotations resource
        Given logged on as superuser
        When request GET to /api/sms/rotations
        Then will receive JSON response of data

    Scenario: superuser requesting to read sms/students resource
        Given logged on as superuser
        When request GET to /api/sms/students
        Then will receive JSON response of data

    Scenario: admin office user requesting to read sms/schools resource
        Given logged on as admin office user
        When request GET to /api/sms/schools
        Then will receive JSON response of data

    Scenario: admin office user requesting to read sms/programs resource
        Given logged on as admin office user
        When request GET to /api/sms/programs
        Then will receive JSON response of data

    Scenario: admin office user requesting to read sms/rotations resource
        Given logged on as admin office user
        When request GET to /api/sms/rotations
        Then will receive JSON response of data

    Scenario: admin office user requesting to read sms/students resource
        Given logged on as admin office user
        When request GET to /api/sms/students
        Then will receive JSON response of data
 
   Scenario: staff office user requesting to read sms/schools resource
        Given logged on as staff office user
        When request GET to /api/sms/schools
        Then will receive JSON response of data


    Scenario: staff office user requesting to read sms/programs resource
        Given logged on as staff office user
        When request GET to /api/sms/programs
        Then will receive JSON response of data
        And server response status is OK 200


    Scenario: staff office user requesting to read sms/rotations resource
        Given logged on as staff office user
        When request GET to /api/sms/rotations
        Then will receive JSON response of data


    Scenario: staff office user requesting to read sms/students resource
        Given logged on as staff office user
        When request GET to /api/sms/students
        Then will receive JSON response of data

    Scenario: regular office user requesting to read sms/schools resource
        Given logged on as regular office user
        When request GET to /api/sms/schools
        Then will receive JSON response of data


    Scenario: regular office user requesting to read sms/programs resource
        Given logged on as regular office user
        When request GET to /api/sms/programs
        Then will receive JSON response of data


    Scenario: regular office user requesting to read sms/rotations resource
        Given logged on as regular office user
        When request GET to /api/sms/rotations
        Then will receive JSON response of data


    Scenario: regular office user requesting to read sms/students resource
        Given logged on as regular office user
        When request GET to /api/sms/students
        Then will receive JSON response of data






    
    Scenario: superuser requesting to read ST2 sms/students resource
        Given logged on as superuser
        When request GET to ST2 /api/sms/students/student_uuid
        Then will receive JSON response of data

    
    Scenario: superuser requesting to read ST2 sms/schools resource
        Given logged on as superuser
        When request GET to ST2 /api/sms/schools/school_uuid
        Then will receive JSON response of data

    
    Scenario: superuser requesting to read ST2 sms/programs resource
        Given logged on as superuser
        When request GET to ST2 /api/sms/programs/program_uuid
        Then will receive JSON response of data

    
    Scenario: superuser requesting to read ST2 sms/rotations resource
        Given logged on as superuser
        When request GET to ST2 /api/sms/rotations/rotation_uuid
        Then will receive JSON response of data

    
    Scenario: admin office user requesting to read ST2 sms/students resource
        Given logged on as admin office user
        When request GET to ST2 /api/sms/students/student_uuid
        Then server will respond with 404
   
   
    
    Scenario: admin office user requesting to read ST2 sms/schools resource
        Given logged on as admin office User
        When request GET to ST2 /api/sms/schools/school_uuid
        Then server will respond with 404

    
    Scenario: admin office user requesting to read ST2 sms/programs resource
        Given logged on as admin office User
        When request GET to ST2 /api/sms/programs/program_uuid
        Then server will respond with 404

    
    Scenario: admin office user requesting to read sms/rotations resource
        Given logged on as admin office User
        When request GET to ST2 /api/sms/rotations/rotation_uuid
        Then server will respond with 404

    
    Scenario: staff office user requesting to read ST2 sms/students resource
        Given logged on as staff office user
        When request GET to ST2 /api/sms/students/student_uuid
        Then server will respond with 404

    
    Scenario: staff office user requesting to read ST2 sms/schools resource
        Given logged on as staff office User
        When request GET to ST2 /api/sms/schools/school_uuid
        Then server will respond with 404

    
    Scenario: staff office user requesting to read ST2 sms/programs resource
        Given logged on as staff office User
        When request GET to ST2 /api/sms/programs/program_uuid
        Then server will respond with 404

    
    Scenario: staff office user requesting to read ST2 sms/rotations resource
        Given logged on as staff office User
        When request GET to ST2 /api/sms/rotations/rotation_uuid
        Then server will respond with 404

    
    Scenario: regular office user requesting to read ST2 sms/students resource
        Given logged on as regular office user
        When request GET to ST2 /api/sms/students/student_uuid
        Then server will respond with 404

    
    Scenario: regular office user requesting to read ST2 sms/schools resource
        Given logged on as regular office User
        When request GET to ST2 /api/sms/schools/school_uuid
        Then server will respond with 404

    
    Scenario: regular office user requesting to read ST2 sms/programs resource
        Given logged on as regular office User
        When request GET to ST2 /api/sms/programs/program_uuid
        Then server will respond with 404


    
    Scenario: regular office user requesting to read ST2 sms/rotations resource
        Given logged on as regular office User
        When request GET to ST2 /api/sms/rotations/rotation_uuid
        Then server will respond with 404
