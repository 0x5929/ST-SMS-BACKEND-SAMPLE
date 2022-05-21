Feature: Student Management Student Statistics

    All office users have read access to all sms resources



    Scenario: superuser requesting to read sms/student_statistics resource
        Given logged on as superuser
        When request GET to /api/sms/students/student_statistics
        Then will receive statistics JSON response


    Scenario: admin office user requesting to read sms/student_statistics resource
        Given logged on as admin office user
        When request GET to /api/sms/students/student_statistics
        Then will receive statistics JSON response


    Scenario: staff office user requesting to read sms/student_statistics resource
        Given logged on as staff office user
        When request GET to /api/sms/students/student_statistics
        Then will receive statistics JSON response


    Scenario: regular office user requesting to read sms/student_statistics resource
        Given logged on as regular office user
        When request GET to /api/sms/students/student_statistics
        Then will receive statistics JSON response

